from RPLCD.i2c import CharLCD
import time

# lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
#               cols=20, rows=4, dotsize=8,
#               charmap='A02',
#               auto_linebreaks=True,
#               backlight_enabled=True)

lcd = CharLCD('PCF8574', 0x27)

while(True):
  lcd.clear()
  lcd.write_string("First_line")
  lcd.cursor_pos=(1,0)
  lcd.write_string("Second_line")
  lcd.cursor_pos=(2,0)
  lcd.write_string("Third_line")
  lcd.cursor_pos=(3,0)
  lcd.write_string("Fourth_line")
  time.sleep(1)
  print("printing")


