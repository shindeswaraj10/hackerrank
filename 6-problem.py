'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__== '__main__':
    M = int(input())
    a = set(input().split())
    A = {int(item) for item in a}
    N = int(input())
    b = set(input().split())
    B = {int(item) for item in b}
    
    AA = (A-B)
    BB = (B-A)
    for i in sorted(AA.union(BB)):
        print(i)
    


