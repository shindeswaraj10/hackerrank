'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    varList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        varList.append([name, score] )
    #print (varList)
    minOfMin_ = []
    for _ in range(len(varList)):
        minOfMin_.append(varList[_][1])
    #print (minOfMin_)
    minOfMin_ = sorted(set(minOfMin_))
    #print (minOfMin_)
    minOfMin_ = minOfMin_[1]
    #print (minOfMin_)
    varNames = []
    for _ in range(len(varList)):
        if minOfMin_ == varList[_][1]:
            varNames.append(varList[_][0])
    
    for i in sorted(varNames):
        print(i)
    
