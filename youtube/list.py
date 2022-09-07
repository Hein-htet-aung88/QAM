notfriends = ["you","me","yes you"]
friends = ["hi","hi","hi","hello","bye","dk you"]
friends.extend(notfriends)
friends.append("cooollll") #add to the end of list
friends.insert(2,"sotsot")
friends.remove("hello")
friends.pop()             #remove last element in the list
#friends.clear
#friends.sort() #alphebatical order
#friends.reverse

sotfriends = friends.copy()

print(friends[2])
print(friends[-1])
print(friends[1:8])
friends[1]="not hello"
print(friends.index("hi"))
print(friends.count("hi"))

#tuples
LOL = (8,8,1,2,4,1)  #cannot be modified

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(number_grid[2][1]) #row and column start at 0

for row in number_grid:
    for column in row:
        print(column)