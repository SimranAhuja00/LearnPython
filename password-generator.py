import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase 
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    p_len = int(input("Enter the length of the required password\n"))
    # p_len is the password length
    s = [] #creating an empty list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print('Your password is : ')
    print("".join(s[0:p_len]))
