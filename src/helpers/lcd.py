import time
import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

def running_text(text):
  for i in range(len(text) - 16 + 1):
    lcd.write_string(text[i:i+16])

    time.sleep(0.2)

def lcd_write(first_line, second_line):
  lcd.clear()
  len(first_line) > 16 if running_text(first_line) else lcd.write_string(first_line)
  lcd.cursor_pos=(1,0)
  len(second_line) > 16 if running_text(second_line) else lcd.write_string(second_line)
