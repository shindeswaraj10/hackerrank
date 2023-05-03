'''
Input Format

The first line consists of an integer, K , the size of each group.
The second line contains the unordered elements of the room number list.

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

Sample Output

8

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
K_list = list(map(int,input().split()))
#print(type(K_list))
print((list(x for x in K_list if K_list.count(x)==1))[0])

#Time complexity of above solution is huge
#for below code space complexity might be more but time complexity is less so prfere below code using dict insteed of list comprehentions
K = int(input())
if 1 < K and K < 1000:
    K_list = list(map(int,input().split()))
    data = {}
    for i in K_list:
        if (i in data): data[i] += 1
        else: data[i] = 1
        
    for i in data:
        if (data[i] != K): print(i)

