#!/usr/bin/python
#read the file and get the count of the each word

def main():
	# read  sample file
	file =open("sample.txt","r")
	#read each line from sample file
	lines=file.readlines()
	#close the file 
	file.close()
	
	#look for patterns
	countYes=0
	countNo=0
	#use loop to read each instance of line from lines variable
	for line in lines:
	
	#strip will use remove "\n"
		line=line.strip()
		#print( line )
		if line == "YES":
			countYes=countYes+1
		else:
			countNo=countNo+1
			
	print("Total no of Yes is:-->",countYes)
	print("Total no of No is :-->",countNo)
		
		
main() 

#file data as mentioned below
"""
Sample.txt
YES
NO
YES
NO"""
#Output of the programme
"""
Total no of Yes is:--> 2
Total no of No is :--> 2
"""

