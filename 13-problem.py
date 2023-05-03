'''
Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output

True 
False
False
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
Result = []
for i in range(T):
    N_of_A = int(input())
    A = set(map(int,input().split()))
    N_of_B = int(input())    
    B = set(map(int,input().split()))
    if len(A.union(B)) == len(B):
        Result.append('True')
    else:
        Result.append('False')

for x in Result:
    print(x)