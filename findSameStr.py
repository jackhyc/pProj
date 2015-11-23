#!/user/bin/env python

handle = open('./test.txt','r')
count=0
name=range(39)
namedic={}
for line in handle:
    line=line.strip()
    if line.find('=')>0:
        substr= line[:line.find('=')]
        nstr=substr[6:substr.find('[')]
        name[count:]=[nstr]
        count = count +1
handle.close()


for i in range(len(name)):
    nstr=name[i]
    namedic[name[i]]=name.count(name[i])

for item,value in namedic.items():
    print '%s,%s' %(item,value)

#print len(name)
