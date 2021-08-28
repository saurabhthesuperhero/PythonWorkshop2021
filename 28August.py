#List

# #Creation of list

# ls=[1,2,3,4,5]
# print(ls)

#Print Specific index

# print(ls[0]) #?-> 1
# print(ls[2])

#negative index
# print(ls[-1])  

#Len function
# print(len(ls))

# List insert function
# ls.insert(1,"python")
# print(ls)
# ls.insert(3,"kotlin")
# print(ls)

# Append

# ls.append("gorilla")
# print(ls)

# #Pop operation

# # ls.pop()
# # print(ls)

# ls.pop(2)
# print(ls)
# # Remove
# # ls.remove(3)
# # print(ls)

# #Clear 
# ls.clear()
# print(ls)


# lt=["hello","dance","sheeran"]
# print(lt)

# newls=[ls,lt]
# print(newls)


#### Dictinoary

#Creating a dictionary
# The key value are separated by colon ":" and two key-value pair  are spearted by ","
dt={"name":"taylor","song":"blank space"}

#Print dictionary
print(dt)

# Access single element
#access -> square bracket and pass key name
print(dt["name"])
print(dt["song"])

# Adding values

dt.update({"Age":23})

print(dt)

# pop 

# dt.pop("song")
# print(dt)

# #pop latest item
# dt.popitem()
# print(dt)

# #Clear

# dt.clear()

# print(dt)

# overrite value with key

dt.update({"name":"Ed sheeran"})
print(dt)

## Keys and Values printing

#Print keys

print(dt.keys())

#Print values

print(dt.values())