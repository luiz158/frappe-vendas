# -*- coding: utf-8 -*-
import datetime
import urllib.request as urllib2
from lxml import etree

url = 'http://www.sat.gob.mx/informacion_fiscal/tablas_indicadores/Paginas/tipo_cambio.aspx'
day = datetime.date.today().day


def conectar(url):
    return urllib2.urlopen(url).read()


def valor(day):
    data = etree.HTML(conectar(url))
    s = data.xpath("//*/text()[contains(.,'{}/')]".format(day))[0]
    s = float(s.replace('{}/'.format(day), ''))
    return s


def test(got, expected):
    # Simple provided test() function used in main() to print what each
    # function returns vs. what it's supposed to return.
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('valor')
    test(valor(24), float(17.1953))
    test(valor(28), float(17.2760))
    test(valor(29), float(17.2710))


if __name__ == '__main__':
    main()
