'''
3. Make all character come in the front and 0's at the end:
input = "000sw000r000aj000sh000in000de"
'''

s = "000sw000r000aj000sh000in000de"
s1 = ''
s2 = ''

for i in s:
    if i=='0':
        s1 = s1 + "0"
    else:
        s2 = s2 + i

result = s2+s1
print(result)