#Iterating through a list of tuples

mylist = [(1,2),(3,4),(5,6),(7,8)]
#length of this list is 4

for item in mylist:
    print(item)

# Output:-
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)

for a,b in mylist:
    print(a)

# Output:-
# 1
# 3
# 5
# 7

for a,b in mylist:
    print(b)

# Output:-
# 2
# 4
# 6
# 8
