# Enter your code here. Read input from STDIN. Print output to STDOUT
happniness = 0
input_ = input().split()
n = int(input_[0])
m = int(input_[1])
n_input = input().split()
A_input = set(input().split())
B_input = set(input().split())

for i in n_input:
    if i in A_input:
        happniness = happniness + 1
    elif i in B_input:
        happniness = happniness - 1
print(happniness)