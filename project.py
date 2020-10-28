def most_frequent(str1):
    L=[]
    L1=[]
    mydict={}
    for i in str1:
        if i not in L:
            L.append(i)
        else:
            pass

    for j in L:
        count=0
        for k in range(len(str1)):
            if j==str1[k]:
                count+=1
        mydict[j]=count


    for z in mydict:
        val= mydict[z]
        L1.append(val)
    L1.sort(reverse=True)

    for a in L1:
        keys = list(mydict.keys())
        vals = list(mydict.values())
        letter=keys[vals.index(a)]
        print(letter,":",a)
str1=input("Please enter a string ")
most_frequent(str1)
