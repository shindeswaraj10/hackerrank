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