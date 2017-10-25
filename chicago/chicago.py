from lxml import html
import requests
import xlwt
from tempfile import TemporaryFile

page = requests.get('https://dlibatique.github.io/chicago.html')
tree = html.fromstring(page.content)
events = tree.xpath('//td[@class="h5b"]/text()')

book = xlwt.Workbook()
sheet1 = book.add_sheet('Chicago')

for i,e in enumerate(events):
	sheet1.write(i,1,e)

name = "chicago.xls"
book.save(name)
book.save(TemporaryFile())