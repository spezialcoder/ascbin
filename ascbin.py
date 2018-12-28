#Developer: developermind405@gmail.com
import sys
if len(sys.argv) > 1:
	do = sys.argv[1]
else:
	print "Missing Parameter"
	sys.exit(0)
if do == "-e":
	print "Press Ctrl+D to finish"
	print "                   Enter Message"
	print "#########################################################"
	while True:
		try:
			text = raw_input("")
		except EOFError:
			break
	
		
	print
	print "                      OUTPUT    "
	print "#########################################################\n"
	binary = []
	for binary_letter in text:
		binary.append(str(bin(ord(binary_letter))).split("0b")[1])
	#count = 3
	for letter in enumerate(binary):
		sys.stdout.write(letter[1]+" ")	
		#if letter[0] == count:
		#		count += 4
		#		print 

	print "\n\n#########################################################"
elif do == "-d":
	print "Press Ctrl+D to finish"
	print "                   Enter Binary"
	print "#########################################################"
	while True:
		try:
			text = raw_input("")
		except EOFError:
			break
	print
	print "                      OUTPUT    "
	print "#########################################################\n"
	binary = text.split()
	message = [] 
	for binary_letter in binary:
		message.append(chr(eval("0b"+binary_letter)))
	count = 3
	for letter in message:
		sys.stdout.write(letter)

	print "\n\n#########################################################"
else:
	print "Parameter                   Description"
	print "---------------------------------------"
	print "-e                    Encode to binary"
	print "-d                    Decode to ascii"
	
