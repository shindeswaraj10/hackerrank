'''
Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps 
in her collection. She asked for your help. 
You pick the stamps one by one from a stack of N country stamps.

Input Format

The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.

Sample Output

5
'''
# n,m=map(int, input().split(' '))
# print(n,m)

N = int(input())
stamps = set()
for i in range(0,N):
    stamps.add(input())