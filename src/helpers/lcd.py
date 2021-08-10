import time
import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

song_symbol = (
  0b00001,
  0b00011,
  0b00101,
  0b01001,
  0b01001,
  0b01011,
  0b11011,
  0b11000
)

lcd.create_char(0, song_symbol)

def running_text(text):
  for i in range(len(text) - 16 + 1):
    lcd.write_string(text[i:i+16])
    time.sleep(0.2)

def lcd_write_running(first_line, second_line):
  lcd.clear()
  running_text(first_line)
  lcd.cursor_pos=(1,0)
  running_text(f"\x00 {second_line}")

def lcd_write(first_line, second_line):
  lcd.clear()
  lcd.write_string(first_line)
  lcd.cursor_pos=(1,0)
  lcd.write_string(second_line)
