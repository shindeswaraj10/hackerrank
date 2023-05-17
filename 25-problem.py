def count_substring(string, sub_string):
    return sum(string[i:].startswith(sub_string) for i in range(len(string)))
    # count = 0
    # if len(string)<=200:
    #     for i in range(0,len(string)+2-len(sub_string)):
    #         print(sub_string[0].lower(),string[i].lower(),sub_string.lower(),string[i:(i+len(sub_string)+1)].lower())
    #         if(sub_string[0].lower() == string[i].lower()) and (sub_string.lower() == string[i:(i+len(sub_string)+1)].lower()):
    #             count = count + 1
    #             print(count)
    #             sub_string.lower()

    #     return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

'''
ABCDCDC
CDC




12jlka445kljakldfjlaksjdfdka3942
3akd
'''