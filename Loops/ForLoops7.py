#Iterating through a dictionary
d = {'k1' : 1, 'k2' : 2, 'k3' : 3}

for item in d:
    print(item)

# Output:-
# k1
# k2
# k3

#By default when you iterate through a dictionary, you only iterate through the keys

for item in d.items():
    print(item)

# Output:-
# ('k1', 1)
# ('k2', 2)
# ('k3', 3)

#to only display the values 
for key,value in d.items():
    print(value)

# Output:-
# 1
# 2
# 3
