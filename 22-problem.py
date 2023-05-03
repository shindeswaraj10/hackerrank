'''
Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
'''

if __name__ == '__main__':
    S = str(input())
    result = -1
    for i in range(0,len(S)-1):
        if S[i] == S[i+1]:
            result = i
            break
            
    print(result+1)