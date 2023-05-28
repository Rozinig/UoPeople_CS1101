

def invert_dict(d):
     inverse = dict()
     for key in d:
          val = d[key]
          for i in val:
               if i not in inverse:
                    inverse[i] = [key]
               else:
                    inverse[i].append(key)
     return inverse  
 

fin=open('classes.txt')
classes={}
for line in fin:
	line=line.strip()
	temp=line.split(':')
	print(temp)
	classes[temp[0]]=temp[1].split(',')

fin.close()

sessalc=invert_dict(classes)
print(classes)
print(sessalc)


fout=open('output.txt','w')
for key in sessalc:
	temp=''
	for item in sessalc[key]:
		if temp=='':
			temp=item
		else:
			temp=temp + ',' + item
	temp= key + ':' + temp+'\n'
	print(temp)
	fout.write(temp)
fout.close()



