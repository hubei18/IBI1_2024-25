# import necessary library
import xml.dom.minidom
import xml.sax
from datetime import datetime
import xml.sax.handler

# process the file by dom
# get all elements that record the terms
start_time=datetime.now()
domtree=xml.dom.minidom.parse('go_obo.xml')
collection=domtree.documentElement
terms=collection.getElementsByTagName('term')

# traverse the terms and record their id, name, is_a number.
# get their namespace, use the variable tick to categorize them
# compare the current highest and decide whether the highest remain unchanged or the current is higher
elementcount=[0,0,0]
max=[[],[],[]]
for term in terms:
    current_elementcount=term.getElementsByTagName('is_a').length
    id=term.getElementsByTagName('id')[0].firstChild.nodeValue
    name=term.getElementsByTagName('name')[0].firstChild.nodeValue
    if term.getElementsByTagName('namespace')[0].firstChild.nodeValue=='molecular_function':
        tick=0
    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue=='biological_process':
        tick=1
    else:
        tick=2
    if current_elementcount>elementcount[tick]:
        elementcount[tick]=current_elementcount
        max[tick]=[{'id':id,"name":name,'is_a':current_elementcount}]
    elif current_elementcount==elementcount[tick]:
        max[tick].append({'id':id,"name":name,'is_a':current_elementcount})

# record the time uasge
end_time=datetime.now()
domtime=end_time-start_time

# print the result
print('---molecular function---')    
for i in max[0]:
    for j in i:
        print(j+':',i[j])
print('---biological process---')
for i in max[1]:
    for j in i:
        print(j+':',i[j])
print('---cellular component---')
for i in max[2]:
    for j in i:
        print(j+':',i[j])
print('time usage:',domtime)
print('--------------above is dom, below is sax------------------')

# define the contenthandler to be used in parser
# read the id, name, is_a number.
# get their namespace, use the variable tick to categorize them
# compare the current highest and decide whether the highest remain unchanged or the current is higher
class oboHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.type=''
        self.ontology=''
        self.id=''
        self.name=''
        self.is_a=0
        self.number=[0,0,0]
        self.max=[[],[],[]]
        self.is_term=False
    def startElement(self, tag, attrs):
        self.type=tag
        if tag=='term':
            self.is_term=True
            self.ontology=''
            self.id=''
            self.name=''
            self.is_a=0
    def characters(self, content):
        if self.is_term:
            if self.type=='id':
                self.id+=content
            elif self.type=='name':
                self.name+=content
            elif self.type=='namespace':
                self.ontology+=content
            elif self.type=='is_a':
                self.is_a+=1
    def endElement(self, tag):
        if tag=='term':
            if self.ontology=='molecular_function':
                tick=0
            elif self.ontology=='biological_process':
                tick=1
            else:
                tick=2
            if self.is_a>self.number[tick]:
                self.max[tick]=[{'id':self.id,'name':self.name,'is_a':self.is_a}]
                self.number[tick]=self.is_a
            elif self.is_a==self.number[tick]:
                self.max[tick].append({'id':self.id,'name':self.name,'is_a':self.is_a})
            self.is_term=False
        self.type=''
            
# set the parser and read the file
start_time=datetime.now()
parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler=oboHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')

# record the time usage
end_time=datetime.now()
saxtime=end_time-start_time

# print the result
print('---molecular function---') 
for i in Handler.max[0]:
    for j in i:
        print(j+':',i[j])
print('---biological process---')
for i in Handler.max[1]:
    for j in i:
        print(j+':',i[j])
print('---cellular component---')
for i in Handler.max[2]:
    for j in i:
        print(j+':',i[j])
print('time usage:',saxtime)

# compare the time usage
if domtime>saxtime:
    print('SAX is faster.')
elif domtime<saxtime:
    print('DOM is faster.')
else:
    print('The same fast.')

# It turned out that SAX need about 1.2 seconds while DOM need about 7.1 seconds.
# SAX is faster