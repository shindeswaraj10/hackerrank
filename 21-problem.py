try:    
    n = int(input("Please provide the no which you ant to check for Automogrophic:"))
    print(len(str(n)))
    if(str(n**2)[-(len(str(n))):]==str(n)):
        print(1)
    else:
        print(-1)
except:
    print("Please provide valid Int entry")
