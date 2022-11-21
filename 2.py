from collections import Counter
s1=input()
s2=input()
a=s2[-1]
s1=[i for i in s1]
d1=Counter(s1)
print(d1)
print(d1[a])
