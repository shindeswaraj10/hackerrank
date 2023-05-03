'''
Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0

False

'''
A = set(map(int,input().split()))
n = int(input())
for i in range(n):
    B = set(map(int,input().split()))
    if len(A.union(B)) == len(A):
        pass
    else:
        print("False")
        exit()
print("True")