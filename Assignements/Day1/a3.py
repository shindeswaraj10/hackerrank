'''
- You have given a nested list of three items in sublist which is in form of [[name, standard, marks]]
      -  Task is to
        - print nested list in tabular format
        - print summary of top scorers and low scorers in each standard
          like.  standard  | topper_name | lowest_scorer_name  |  highest_obtained_marks  |  lowest_obtained_marks
'''
varNestedList = list(input()[1:-1].split(" "))
print("Name\t\tStandard\tMarks")

varListOfList = list()
varStandards  = set()
for i in varNestedList:
    varTempList = list(i[1:-1].split(","))
    varStandards.add(varTempList[1])
    varListOfList.append(varTempList)
    print(varTempList[0].ljust(10)+"\t"+varTempList[1].ljust(10)+"\t"+varTempList[2].ljust(10)+"\t")

varStandards = sorted(varStandards)
print("\n***  Summary of top scorers and low scorers in each standard   ***")
print("standard  | topper_name   | lowest_scorer_name    |  highest_obtained_marks  |  lowest_obtained_marks")
for j in varStandards:
    maxName = ''
    maxMarks = 0
    minName = ''
    minMarks = 100  
    for k in varListOfList:
        if k[1] == j:
            if int(maxMarks) < int(k[2]):
                maxMarks = str(k[2])
                maxName = k[0]
            if int(minMarks) > int(k[2]):
                minMarks = str(k[2])
                minName = k[0]
    #print(j+"*** : "+maxMarks,maxName , minMarks,minName)

    print(str(j).ljust(10)+ "| "+ maxName.ljust(14) + "| " + minName.ljust(22) +"|  "+ maxMarks.ljust(24) + "|  " + minMarks.ljust(20))       
            


'''
python3 a3.py 
[[Swaraj,10,100] [Pratik,9,100] [Kishor,10,36] [Mangesh,9,36] [Satyjeet,10,75] [Krushna,9,88]]
'''