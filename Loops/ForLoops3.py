mylist = [1,2,3,4,5,6,7,8,9,10]

#displaying even and odd numbers, f-string literals are also used
for num in mylist:
    #check for even
    if num%2 == 0:
        print(f'Even Number: {num}')
    else:
        #odd since it's not even
        print(f'Odd Number:  {num}')

# Output:-
# Odd Number:  1
# Even Number: 2
# Odd Number:  3
# Even Number: 4
# Odd Number:  5
# Even Number: 6
# Odd Number:  7
# Even Number: 8
# Odd Number:  9
# Even Number: 10
