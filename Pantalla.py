#include <ArduinoJson.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <LovyanGFX.hpp>
#include <Wire.h>
#include <math.h>

#define WIFI_SSID       "UTNG_GUEST"
#define WIFI_PASS       "R3d1nv1t4d0s#UT"
#define MQTT_SERVER     "10.31.5.115"
#define MQTT_PORT       1883
#define MQTT_CLIENT_ID  "ESP32_Display"
#define MQTT_TOPIC_SUB  "esp32/sensores"
#define MQTT_TOPIC_RELE1 "esp32/rele/1"
#define MQTT_TOPIC_RELE2 "esp32/rele/2"
#define MQTT_TOPIC_RELE3 "esp32/rele/3"

#define RELAY1_PIN 21
#define RELAY2_PIN 22
#define RELAY3_PIN 23

class LGFX : public lgfx::LGFX_Device {
  lgfx::Panel_ST7789  _panel;
  lgfx::Bus_Parallel8 _bus;

public:
  LGFX() {
    auto cfg = _bus.config();
    cfg.freq_write = 20000000;
    cfg.pin_wr = 4;
    cfg.pin_rd = 2;
    cfg.pin_rs = 16;
    cfg.pin_d0 = 15;
    cfg.pin_d1 = 13;
    cfg.pin_d2 = 12;
    cfg.pin_d3 = 14;
    cfg.pin_d4 = 27;
    cfg.pin_d5 = 25;
    cfg.pin_d6 = 33;
    cfg.pin_d7 = 32;
    _bus.config(cfg);
    _panel.setBus(&_bus);

    auto pcfg = _panel.config();
    pcfg.pin_cs = 17;
    pcfg.pin_rst = -1;
    pcfg.pin_busy = -1;
    pcfg.memory_width = 240;
    pcfg.memory_height = 320;
    pcfg.panel_width  = 240;
    pcfg.panel_height = 320;
    pcfg.offset_rotation = 0;
    pcfg.invert = true;
    _panel.config(pcfg);

    setPanel(&_panel);
  }
};

LGFX tft;
WiFiClient espClient;
PubSubClient client(espClient);

float temperatura = 0.0;
float humedad = 0.0;
int calidad_aire = 0;

const int MAX_POINTS = 60;
float temp_history[MAX_POINTS];
float air_history[MAX_POINTS];
int temp_index = 0;

void drawTemperatureGraph() {
  int x0 = 10, y0 = 10, w = 220, h = 80;
  tft.drawRect(x0, y0, w, h, TFT_WHITE);
  if (temp_index < 2) return;
  for (int i = 1; i < temp_index; i++) {
    int x1 = x0 + ((i - 1) * w) / MAX_POINTS;
    int y1 = y0 + h - (temp_history[i - 1] * h) / 50;
    int x2 = x0 + (i * w) / MAX_POINTS;
    int y2 = y0 + h - (temp_history[i] * h) / 50;
    tft.drawLine(x1, y1, x2, y2, TFT_RED);

    int aq_y1 = y0 + h - (air_history[i - 1] * h) / 3000;
    int aq_y2 = y0 + h - (air_history[i] * h) / 3000;
    tft.drawLine(x1, aq_y1, x2, aq_y2, TFT_GREEN);
  }
  tft.setCursor(x0, y0 + h + 4);
  tft.setTextColor(TFT_WHITE);
  tft.setTextSize(1);
  tft.printf("Temp: %.1f C", temperatura);
  tft.setCursor(x0 + 120, y0 + h + 4);
  tft.printf("AQ: %d", calidad_aire);
}

void drawHumidityPieChart() {
  int cx = 120, cy = 140, r = 30;
  tft.fillCircle(cx, cy, r, TFT_WHITE);
  int filledAngle = map(humedad, 0, 100, 0, 360);
  for (int angle = 0; angle <= filledAngle; angle++) {
    float theta = angle * DEG_TO_RAD;
    int x = cx + r * cos(theta);
    int y = cy + r * sin(theta);
    tft.drawLine(cx, cy, x, y, TFT_BLUE);
  }
  tft.setCursor(cx - 30, cy + r + 6);
  tft.setTextColor(TFT_WHITE);
  tft.setTextSize(1);
  tft.printf("Humedad: %.1f %%", humedad);
}

void updateDisplay() {
  tft.startWrite();
  tft.fillScreen(TFT_BLACK);
  drawTemperatureGraph();
  drawHumidityPieChart();
  tft.endWrite();
}

void callback(char* topic, byte* payload, unsigned int length) {
  payload[length] = '\0';
  String jsonStr = String((char*)payload);
  DynamicJsonDocument doc(256);
  auto err = deserializeJson(doc, jsonStr);
  if (err) return;

  temperatura = doc["temperatura"].as<float>();
  humedad = doc["humedad"].as<float>();
  calidad_aire = doc["calidad_aire"].as<int>();

  if (temp_index < MAX_POINTS) {
    temp_history[temp_index] = temperatura;
    air_history[temp_index] = calidad_aire;
    temp_index++;
  } else {
    for (int i = 1; i < MAX_POINTS; i++) {
      temp_history[i - 1] = temp_history[i];
      air_history[i - 1] = air_history[i];
    }
    temp_history[MAX_POINTS - 1] = temperatura;
    air_history[MAX_POINTS - 1] = calidad_aire;
  }
  updateDisplay();
}

void setup_wifi() {
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) delay(500);
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect(MQTT_CLIENT_ID)) {
      client.subscribe(MQTT_TOPIC_SUB);
      client.subscribe(MQTT_TOPIC_RELE1);
      client.subscribe(MQTT_TOPIC_RELE2);
      client.subscribe(MQTT_TOPIC_RELE3);
    } else delay(2000);
  }
}

void setup() {
  Serial.begin(115200);
  tft.init();
  tft.setRotation(1);
  pinMode(RELAY1_PIN, OUTPUT);
  pinMode(RELAY2_PIN, OUTPUT);
  pinMode(RELAY3_PIN, OUTPUT);
  digitalWrite(RELAY1_PIN, HIGH);
  digitalWrite(RELAY2_PIN, HIGH);
  digitalWrite(RELAY3_PIN, HIGH);
  for (int i = 0; i < MAX_POINTS; i++) temp_history[i] = air_history[i] = 0;
  temp_index = 0;
  updateDisplay();
  setup_wifi();
  client.setServer(MQTT_SERVER, MQTT_PORT);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();
}
