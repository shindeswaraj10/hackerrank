'''
Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College.
 One day, she asked her student Mickey to compute the average
  of all the plants with distinct heights in her greenhouse.

  Sample Input

  STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

Sample Output

169.375

'''

def average(array):
    # your code goes here
    set_= set(array)
    return round((sum(set_)/len(set_)),3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)