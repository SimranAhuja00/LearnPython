#in operator

print('x' in [1,2,3])
#False
print('x' in ['x','y'])
#True

d = {'mykey' : 345}
print('mykey' in d)
#True
print(345 in d)
#False
print(345 in d.keys())
#False
print(345 in d.values())
#True

my_list = [10,20,30,40,50]
print(f'The minimum number in this list is {min(my_list)}')
print(f'The maximum number in this list is {max(my_list)}')

# The minimum number in this list is 10
# The maximum number in this list is 50

