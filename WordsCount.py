name = input('Enter file:')
handle = open(name, 'r')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        print("word: "+ word)
        print(counts)

#print("counts: "+ len(list(counts.items())))

bigcount = None
bigword = None
for word, count in list(counts.items()):
    print("B4 word, count : " + word, count)
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        print("Inside: " + bigword, bigcount)

print(bigword, bigcount)