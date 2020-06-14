file = input("Enter File Name, like email-short.txt: ")
try:
    #fhand = open('mbox-short.txt')
    fhand = open(file)
except:
    print("Exception, file not found")

#inp = fhand.read()
#print((len(inp)))
#print("111 "+ inp[:20])

for line in fhand:
    if line.startswith('From:'):
        line = line.rstrip()
        line = line.upper()
        print("Line: "+ line)

