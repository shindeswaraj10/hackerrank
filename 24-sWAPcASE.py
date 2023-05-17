'''
Sample Input 0

HackerRank.com presents "Pythonist 2".

Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''

def swap_case(s):
    tempString = ""
    for i in s:
        if str.isalpha(i):
            check = lambda x : i.lower() if x <= "Z" else i.upper()
            i = check(i)
        tempString = tempString  + i
        
    return tempString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''
Sample Input

this is a string   

Sample Output

this-is-a-string



In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 

'''
def split_and_join(line):
    # write your code here
    line = line.replace(" ", "-")
    return line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)





    '''
    >>> string = "abracadabra"
    >>> l = list(string)
    >>> l[5] = 'k'
    >>> string = ''.join(l)
    >>> print string
    abrackdabra
    
    '''