# without using function
a=["sanjay","yuvasri","vijayalakshmi"]
m=0
v="aeiouAEIOU"
for i in a:
    for j in i:
        if j in v:
            m+=1
print("Sum of positive no's in the arr: ",m)
