'''
.remove(x)
This operation removes element x from the set.
If element x does not exist, it raises a KeyError.
The .remove(x) operation returns None.

.discard(x)
This operation also removes element x from the set.
If element x does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

.pop()
This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError.
'''

n = int(input())
n_set = set(map(int, input().split()))
n_set = set(n_set)
#print(n_set,type(n_set))
c = int(input())
for i in range(c):
    cammand1 = (input()).split(" ")
    cammand = cammand1[0]
    if cammand.lower() == 'pop':
        n_set.pop()
    elif cammand.lower() == 'discard':
        try:
            value = int(cammand1[1])
            n_set.discard(value)
        except:
            continue
    elif cammand.lower() == 'remove':
        try:
            value = int(cammand1[1])
            n_set.remove(value)
        except KeyError:
            continue
print(sum(n_set))