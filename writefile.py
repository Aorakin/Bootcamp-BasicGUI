from datetime import datetime
from encodings import utf_8

quantity = 10
cal= quantity*100


def writetext(quantity,total):
    stamp = datetime.now()
    stamp = stamp.replace(year=stamp.year+543)#บวกเป็นพศ
    stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    filename = 'dataa.txt'
    with open (filename,'a',encoding='utf-8') as file:
        file.write (('\n'+'วัน-เวลา:{}ทุเรียน :{}กก. ราคาทั้งหมด{:,.2f}บาท'.format(stamp,quantity,total)))


writetext(91,9100)
writetext(92,9200)
writetext(93,9300)
writetext(94,9400)