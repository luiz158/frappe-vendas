import urllib.request as urllib2
import datetime
from StringIO import StringIO
from xml.etree import ElementTree as ET
# from xml.etree import ElementTree as cElementTree
# from cStringIO import StringIO

url = 'http://www.sat.gob.mx/informacion_fiscal/tablas_indicadores/Paginas/tipo_cambio.aspx'


def conectar(url):
    page = urllib2.urlopen(url).read()
    it = ET.iterparse(StringIO(page))
    for _, el in it:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
    return it.root()


def conectar2(url):
    page = urllib2.urlopen(url).read()
    it = ET.parse(StringIO(page))
    for elem in it.getiterator():
        print(elem.tag, elem.attib)


def valor():
    day = datetime.date.today().day
    data = conectar2(url)
    s = data.xpath("//*/text()[contains(.,'{}/')]".format(day))[0]
    s = float(s.replace('{}/'.format(day), ''))
    return s

print(valor())

'''
class iterparse(object):
    root = None

    def __init__(self, file, events=None, namespace_separator="}"):
        if not hasattr(file, 'read'):
            file = open(file, 'rb')
        self._file = file
        self._events = events
        self._namespace_separator = namespace_separator

    def __iter__(self):
        events = []
        b = cElementTree.TreeBuilder()
        p = cElementTree.XMLParser(
            b, namespace_separator=self._namespace_separator)
        p._setevents(events, self._events)
        while 1:
            data = self._file.read(16384)
            if not data:
                break
            p.feed(data)
            for event in events:
                yield event
            del events[:]
        root = p.close()
        for event in events:
            yield event
        self.root = root

page = urllib2.urlopen(url).read()
context = iterparse(StringIO(page), events=("start", "end", "start-ns"))
for event, elem in context:
    print event, elem
'''
