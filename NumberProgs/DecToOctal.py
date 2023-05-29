def dec_to_oct(decimal):
    if decimal == 0:
        return ""
    quotient = decimal // 8
    remainder = decimal % 8
    return dec_to_oct(quotient) + str(remainder)
    
decimal = int(input("Please Enter a decimal number: "))
octal = dec_to_oct(decimal)
print("Octal number is ", octal, " for ", decimal)
