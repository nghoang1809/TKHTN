#include <Wire.h>              // Thư viện hỗ trợ I2C
#include <LiquidCrystal_I2C.h> // Thư viện cho LCD I2C
#include <TinyGPS++.h>         // Thư viện cho GPS

LiquidCrystal_I2C lcd(0x27, 16, 2); // Địa chỉ LCD I2C
TinyGPSPlus gps;                    // Đối tượng GPS

void setup() {
  Serial1.begin(9600);         // Khởi tạo UART cho GPS
  lcd.init();                  // Khởi tạo LCD I2C
  lcd.backlight();             // Bật đèn nền LCD
  lcd.print("Circuit Digest");
  lcd.setCursor(0, 1);
  lcd.print("STM32 with GPS");
  delay(4000);
  lcd.clear();
}

void loop() {
  GPSDelay(1000);
  double lat_val = gps.location.lat(); // Lấy vĩ độ
  double lng_val = gps.location.lng(); // Lấy kinh độ
  bool loc_valid = gps.location.isValid();

  if (!loc_valid) {
    lcd.clear();
    lcd.print("Waiting");
    delay(4000);
  } else {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("LAT:");
    lcd.print(lat_val, 6);

    lcd.setCursor(0, 1);
    lcd.print("LONG:");
    lcd.print(lng_val, 6);

    delay(4000);
  }
}

static void GPSDelay(unsigned long ms) {
  unsigned long start = millis();
  do {
    while (Serial1.available()) 
      gps.encode(Serial1.read());
  } while (millis() - start < ms);
}