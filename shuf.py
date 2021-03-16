import argparse
import random, sys

"""
Pseudo-randomizes a given input or file

"""

def printLinesFromList(output, count, repeatBool, inputRange):	
	if int(count) == 0 and repeatBool == False and inputRange == []:
		for x in output:
			print(x.strip('\n'))
	elif int(count) != 0 and repeatBool == False and inputRange == []:
		if int(count) > len(output):
			for x in output:
				print(x.strip('\n'))
		else:
			i = 0
			while i < int(count):
				print(output[i].strip('\n'))
				i+=1
	elif int(count) != 0 and repeatBool == True and inputRange == []:
		if int(count) > len(output):
			for x in output:
				print(x.strip('\n'))
		else:
			i = 0
			while i < int(count):
				print(output[i].strip('\n'))
				i+=1	
	elif int(count) == 0 and repeatBool == False and inputRange != []:
		for x in output:
			print(x)
	elif int(count) != 0 and repeatBool == False and inputRange != []:
		for x in output:
			print(x)
	elif int(count) == 0 and repeatBool == True and inputRange != []:
		while(repeatBool):
			random.shuffle(output)
			for x in output:
				print(x)
	elif int(count) != 0 and repeatBool == True and inputRange != []:
		if int(count) > len(output):
			for x in output:
				print(s.strip('\n'))
		else:
			i = 0
			while i < int(count):
				print(output[i].strip('\n'))
				i+=1				
	elif int(count) == 0 and repeatBool == True and inputRange == []:
		while(repeatBool):
			random.shuffle(output)
			for x in output:
				print(x.strip('\n'))

def main():		
	parser = argparse.ArgumentParser(description='Return random permutations of lines within a file.')	
	parser.add_argument('-', action='store_true', dest='extraArgs', help='gives random permutation from stdin')
	parser.add_argument('--input-range', '-i', action='store', dest='inputRange', help='gives random permutation of line numbers in range from [LO-HI]')
	parser.add_argument('--head-count', '-n' , action='store', dest='count',  help='only prints out COUNT number of pseudo-randomly chosen lines')
	parser.add_argument('--repeat', '-r', action='store_true', dest='isRepeated', help='prints out a random amount of lines repeatedly')
	parser.add_argument('filename', action='store', nargs='?', const='False', default='', help='prints out a random amount of lines from the file')
	args = parser.parse_args()
	if args.extraArgs==True and (args.inputRange!=None or args.filename!=''):
		parser.error("Error, cannot use '-' with an input range")
	elif  (args.filename=='' or args.extraArgs==True) and args.count==None and args.inputRange==None and args.isRepeated==False: 
		lines=sys.stdin.readlines()		
		random.shuffle(lines)
		printLinesFromList(lines, 0, False, [])
	elif args.filename!='' and args.inputRange==None and args.count==None and args.isRepeated==False and args.extraArgs==False:
		input_file=open(args.filename,'r')
		lines = input_file.readlines()
		input_file.close()
		random.shuffle(lines)
		printLinesFromList(lines, 0, False, [])			 
	elif args.filename!='' and args.inputRange!=None:
		parser.error("Error, cannot use a filename with the input range")
		sys.exit(1)
	elif (args.filename!='' or args.filename=='' or args.extraArgs==True) and args.inputRange==None and args.count!=None and args.isRepeated==False:
		if int(args.count) < 0:
			parser.error("Error, cannot use count with a negative number.")
			sys.exit(1)
		elif int(args.count) == 0:
			sys.exit(1)
		else:
			if args.filename!='':
				input_file=open(args.filename,'r')
				lines = input_file.readlines()
				input_file.close()
				random.shuffle(lines)
				printLinesFromList(lines, int(args.count), False, [])
			elif args.filename=='' or args.extraArgs==True:
				lines = sys.stdin.readlines()
				random.shuffle(lines)
				printLinesFromList(lines, args.count, False, [])		
	elif (args.filename!='' or args.filename=='' or args.extraArgs==True) and args.inputRange==None and args.count!=None and args.isRepeated==True:
		if int(args.count) < 0:
			parser.error("Error, cannot use count with a negative number.")
			sys.exit(1)
		elif int(args.count) == 0:
			sys.exit(1)
		else:
			if args.filename!='':
				input_file=open(args.filename, 'r')
				lines=input_file.readlines()
				input_file.close()
				newLines = []
			else:
				lines = sys.stdin.readlines()
				random.shuffle(lines)
				newLines = []
			if int(args.count) > len(lines):
				for x in range(args.count):
					newLines.append(random.choice(lines))
			else:
				i = 0
				while(i < int(args.count)):
					newLines.append(random.choice(lines))
					i+=1
			printLinesFromList(newLines, int(args.count), True, [])
	elif args.filename=='' and args.inputRange!=None and args.count==None and args.isRepeated==False:
		listForRange = args.inputRange.split("-")
		if int(listForRange[0]) < 0 or int(listForRange[0]) > int(listForRange[1]) or len(listForRange) > 2:
			parser.error("Error, range inputted is invalid")
			sys.exit(1)
		else:
			lines = []
			for x in range(int(listForRange[0]), int(listForRange[1])+1):
				lines.append(x)
			random.shuffle(lines)
			printLinesFromList(lines, 0, False, listForRange)
	elif args.filename=='' and args.inputRange!=None and args.count!=None and args.isRepeated==False:
		listForRange = args.inputRange.split("-")
		if int(listForRange[0]) < 0 or int(listForRange[0]) > int(listForRange[1]) or len(listForRange) > 2 or int(args.count) < 0:	
			parser.error("Error, range inputted/count is invalid.")
			sys.exit(1)
		elif int(args.count) == 0:
			sys.exit(1)	
		else:
			lines = []
			for x in range(int(listForRange[0]), int(listForRange[1])+1):
				lines.append(x)
			newLines = []
			if int(args.count) > len(lines):
				for x in range(len(lines)):
					randLine = random.choice(lines)
					newLines.append(randLine)
					lines.remove(randLine)
			else:
				i = 0
				while(i < int(args.count)):
					randLine = random.choice(lines)
					newLines.append(randLine)
					lines.remove(randLine)
					i+=1
			printLinesFromList(newLines, int(args.count), False, listForRange)
	elif args.filename=='' and args.inputRange!=None and args.count==None and args.isRepeated==True:
		listForRange = args.inputRange.split("-")
		if int(listForRange[0]) < 0 or int(listForRange[1]) > int(listForRange[1]) or len(listForRange) > 2:
			parser.error("Error, range inputted is invalid")
			sys.exit(1)
		else:
			lines = []
		for x in range(int(listForRange[0]), int(listForRange[1])+1):
			lines.append(x)
		printLinesFromList(lines, 0, True, listForRange)
	elif args.filename=='' and args.inputRange!=None and args.count!=None and args.isRepeated==True:
		listForRange = args.inputRange.split("-")
		if int(listForRange[0]) < 0 or int(listForRange[0]) > int(listForRange[1]) or len(listForRange) > 2or int(args.count) < 0:
			parser.error("Error, range inputted/count is invalid.")
			sys.exit(1)
		elif int(args.count) == 0:
			sys.exit(1)
		else:
			lines = []
			for x in range(int(listForRange[0]), int(listForRange[1])+1):
				lines.append(x)
			newLines = []
			if int(args.count) > len(lines):
				for x in range(len(lines)):
					randLine = random.choice(lines)
					newLines.append(randLine)
			else:
				i = 0
				while(i < int(args.count)):
					randLine = random.choice(lines)
					newLines.append(randLine)
					i+=1
			printLinesFromList(newLines, int(args.count), False, listForRange)
	elif (args.filename!='' or args.filename=='' or args.extraArgs==True) and args.inputRange==None and args.count==None and args.isRepeated==True:
		if args.filename!='':
			input_file=open(args.filename, 'r')
			lines=input_file.readlines()
			input_file.close()
			printLinesFromList(lines, 0, True, [])
		else:
			lines = sys.stdin.readlines()
			printLinesFromList(lines, 0, True, [])
	else:
		parser.error("Invalid input.")
		sys.exit(1)
							
if __name__=="__main__":
	main()

