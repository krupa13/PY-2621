# List Methods / Operations: What Actions Can Be Done On Lists 

# append(): Add element to end of the list
data = [10,20,30,40]
# data.append() # TypeError: atleast one element is required for append
data.append(50)
print(data)

# extend(): Add iterable to the list
data = [10,20,30]
# data.extend(60) # TypeError: "int" object is not iterable
data.extend([40,50])
print(data)

# insert(): Add element on specific position i.e using index
data = [10,20,30]
# data.insert(30) # TypeError: insert expected 2 arguements
data.insert(3,40)
print(data)

# pop(): removes last element by default last element i.e based on index
data = [10,20,30]
data.pop()
print(data)

data = [10,20,30,40]
data.pop(2)
print(data)

# remove(): Removes element by value
data = [10,20,30,40,50]
data.remove(20)
print(data)

# Remove all 10's
data = [10,20,10,30,40,10,50,10]
for num in data:
    if num == 10:
        data.remove(num)
print(data)

data = [10,20,10,30,40,10,50,10]
while 10 in data:
    data.remove(10)
print(data)

# clear(): empty the list
data = [10,20,30,40,50]
data.clear()
print(data)

# index(): used to get the index position of the value
data = [10,20,30,40,50]
print(data.index(30))

# count(): used to get count of occurances
data = [10,20,10,30,40,10,50,10]
print(data.count(10))

# reverse(): reverse the list
data = [10,20,30,40,50]
data.reverse()
print(data)

# sort(): Sorts list
data = [10,30,50,40,20]
data.sort()
print(data) # By default is ascending order

data = [10,30,50,40,20]
data.sort(reverse = True) # Descending order
print(data)

# copy(): Makes copy of list
data = [10,30,50,40,20]
print(data)
backup = data.copy()
print(backup)

# Employee PAN ID's 
pan = ["AAAAA1234A","AAAAA1234B","AAAAA1234C","AAAAA1234D","AAAAA1234D","AAAAA1234D"]
print(pan[1])
# Trying To Change PAN ID 
pan[1] = "BBBBB1234B"
print(pan[1])