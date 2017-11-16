from lxml import html
import requests
import xlwt
from tempfile import TemporaryFile

page = requests.get('https://dlibatique.github.io/tufts.html')
tree = html.fromstring(page.content)
events = tree.xpath('//td[@class="h5b"]/text()')

book = xlwt.Workbook()
sheet1 = book.add_sheet('tufts')

for i,e in enumerate(events):
	sheet1.write(i,1,e)

name = "tufts.xls"
book.save(name)
book.save(TemporaryFile())