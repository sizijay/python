words=raw_input("Enter the word(s)...")
words=words+" "
s=[]
x=0
word=""
sdrow=""
for i in words:
	if (i==" "):
		x=words.index(i)+1
		s.append(word)
		word=""
	else:
		word=word+i
for i in s[::-1]:
	print (i),
