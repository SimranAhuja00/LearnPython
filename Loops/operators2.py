index_count = 0
word = 'abcde'

for item in enumerate(word):
    print(item)

# Output:-
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

my_list1 = [1,2,3]
my_list2 = ['a','b','c']
my_list3 = [100,200,300]

#zip function

for item in zip(my_list1,my_list2):
    print(item)

# (1, 'a')
# (2, 'b')
# (3, 'c')

for item in zip(my_list1,my_list2,my_list3):
    print(item)

# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)