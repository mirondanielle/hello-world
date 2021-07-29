def printAll(seq):
	
	if seq:
		print(seq[0])
		printAll(seq[1:])


printAll("Hello World!")
printAll((20,40,60,80))
printAll([10,30,50,70,90])
