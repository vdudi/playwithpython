lt = ['a','b','c','d','e','f']
print(lt)

print(lt[1:3])

print(lt[:])

print(lt[:8])

print(lt[-1:])

print(lt[-3:])

lt[1:3]=['B','C']

print(lt)

lt.sort()

print(lt)


l1 = ['p','q','r']
l2 = ['x','y','z']
print(l1)
print(l1.append('s'))

l1.append('s')
print(l1)


l1.extend(l2)
print(l1)

var = l2.pop(2)
print(var)
print(l2)

del l2[1]
#del l2[3]
print(l2)

nums = [3,5,6,8,9]
print(nums)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums)/len(nums))

s='usa'
t1=list(s)
print(t1)

s1 = 'this is great and working!!!'
t2 = s1.split()
print(s1)
print(t2)