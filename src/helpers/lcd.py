from RPLCD.i2c import CharLCD
from helpers.lcd_characters import song_symbol


lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

lcd.create_char(0, song_symbol)

def lcd_write(lines):
  lcd.clear()
  for line in lines:
    lcd.write_string(line)
    lcd.crlf()
