a=[0,1,5,6,8,9]
n=int(input())
while len(a)!=n:
        p=a[-1]+1
        b=[i for i in str(p)]
        for i in b:
            if i in a:
                a.append(p)
            else:
                continue
      
print(a[-1]) 
