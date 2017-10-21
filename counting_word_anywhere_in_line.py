#!/usr/bin/python
#read the file and get the count of the each word

def main():
	# read  sample file
	file =open("sampl1.txt","r")
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
		line=line.strip().upper()
		#print( line )
		if line.find("YES")!=-1:
			countYes=countYes+1
		if line.find("NO")!=-1:
			countNo=countNo+1
			
	print("Total no of Yes is:-->",countYes)
	print("Total no of No is :-->",countNo)
		
		
main() 

#file data as mentioned below
"""
Sampl1.txt
YES
NO  YES 
YES
no  YES
YES YES
NO NO"""
#Output of the programme 
"""
Total no of Yes is:--> 5
Total no of No is :--> 2
"""

