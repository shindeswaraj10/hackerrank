if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    varOut = list(sorted(set(arr)))
    print(varOut[len(varOut)-2])


'''
    n= 5
    arr = 2 3 6 6 5
    output = 5
'''
