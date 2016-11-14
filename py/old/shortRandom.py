import random,sys
l=sys.argv
for i in range(1,len(l)):
	j=random.randint(i,len(l)-1)
	l[i],l[j]=l[j],l[i]
	print(l[i])
