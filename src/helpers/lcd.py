import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)


def lcd_write(first_line, second_line):
  lcd.clear()
  lcd.write_string(first_line)
  lcd.cursor_pos=(1,0)
  lcd.write_string(second_line)