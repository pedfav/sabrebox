from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              backlight_enabled=True)

i=0

while(True):
  i=i+1
  lcd.write_string(f"First_line {i}")
  lcd.cursor_pos=(1,0)
  lcd.write_string(f"Second_line {i}")
  lcd.cursor_pos=(2,0)
  lcd.write_string(f"Third_line {i}")
  lcd.cursor_pos=(3,0)
  lcd.write_string(f"Fourth_line {i}")
  time.sleep(0.5)
  print("printing")


