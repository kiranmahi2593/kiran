'''
#convert list to tuple
a=[1,2,3,4,5,6]
a=tuple([1,2,3,4,5,6])
print(a)

#convert tuple to list
x=(4,5)
a=list(x)
print(a)
#a=(1,2,3,4,5,6)
#a=list(a)
#print(a)


#list to set
a=[1,2,3,4,5,6]
x=set([1,2,3,4,5,6])
print("list to set is ",x)

#set to list
a={1,2,3,4,5,6,7}
x=list(a)
#x=list(1,2,3,4,5,6,7)
print("set to list is",x)

#tuple to set
a={1,2,3,4,5,6,7}
x=tuple(a)
print("tuple to set is",a)

#set to tuple
a={1,2,3,4,5,6,7}
x=set(a)
print("set to tupleis",a)

#clear
b={1,2,3,4,5,6}
b.clear()
print(b)

#copy#deep copy
a={"kiran"}
b=a
print(b)
c=a.copy()
a={"mahi"}
print(a)
print(c)       
'''
