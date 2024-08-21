#without funtion
a=[12,32,43,34,44,54,76,98,65,78,99]
s=3
b=[]
for i in a:
    if(i%3==0):
        b.append(i)
print("specific element is: ",s)
print("no of specific element in arr: ",len(b))
print("The elements are: ",b)
