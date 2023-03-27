
#PSET-1

s = 'azcbobobegghakl'
count=0
for i in s:
    if i in"aeiou":
        count+=1
print(count)

print(sum(1 if i in "aeiou" else 0 for i in s))

#PSET1 -2

count1=0
sub = "bob"
for i in range(len(s)-2):
    if s[i:i+3]=="bob":
        count1+=1
print(count1)

#PSET1-3

a=""
temp=""
for i in range(0,len(s)-1):    
    if s[i]<=s[i+1]:
        if temp=="":
            temp=s[i]+s[i+1]
        else:
            temp=temp+s[i+1]
        if len(temp)>=1 and len(temp)>len(a):
            a=temp
    else:
        temp=""
print(a)
