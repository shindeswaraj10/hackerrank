'''
Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output
AB
CA
AD
'''

def merge_the_tools(string, k):
    # your code goes here
    varTemp = [string[i:i+k] for i in range(0,len(string),k)]
    for subString in varTemp:
        tempString = ''
        tempSet = list()
        for varSub in subString:
            if varSub not in tempSet:
                tempSet.append(varSub)
                tempString = tempString + varSub
        print(tempString)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)