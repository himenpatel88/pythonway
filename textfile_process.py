#!/usr/bin/python

text=""" Hi This is ABC.
I am currently working as application development analyst in ABC solutions.
I have started my career as ASE and succesfully completed in ABC Solutions.
I am keenly interested in  ASE Python development project.
"""
 
def main():
	
	countASE = 0
	
	lines = text.splitlines()
	for line in lines:
		if  line.find( "ASE" )!= -1 :
			countASE = countASE + 1
			#print ( line )
	
	print("count ASe is ",countASE)
	
	
main()