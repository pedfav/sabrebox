import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

bola = (
  0b01110,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b01110
)

caule_sup = (
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111,
  0b11111
)

caule_inf = (
  0b11111,
  0b11111,
  0b11111,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000
)

chapeleta_sup = (
  0b00000,
  0b00000,
  0b00000,
  0b01100,
  0b01110,
  0b01111,
  0b01111,
  0b01111
)

chapeleta_inf = (
  0b01111,
  0b01111,
  0b01111,
  0b01110,
  0b01100,
  0b00000,
  0b00000,
  0b00000
)

lcd.create_char(0, bola)
lcd.create_char(1, caule_sup)
lcd.create_char(2, caule_inf)
lcd.create_char(3, chapeleta_sup)
lcd.create_char(4, chapeleta_inf)

lcd.write_string('\x03 \x13 \x23 \x33 \x43 \x53')
