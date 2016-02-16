import urllib.request as urllib2
from bs4 import BeautifulSoup

url = 'http://www.sat.gob.mx/informacion_fiscal/tablas_indicadores/Paginas/tipo_cambio.aspx'

response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')
# t = soup.body.find_all(text='22')
if len(tables):
    table = tables[0]
    print(table)
