#Sum of even numbers in the list

a=[12,32,43,34,44,54,76,98,65,78,99]
m=0
for i in a:
    if(i%2==0):
        m+=i
print("Sum of even no in the arr: ",m)

#With using function

a=[12,32,43,34,44,54,76,98,65,78,99]
m=[]
for i in a:
    if(i%2==0):
        m.append(i)
s=sum(m)
print("Sum of even no in the arr: ",s)

