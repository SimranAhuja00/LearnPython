n = int(input("Enter the length of the fibonacci series : "))
first,second=0,1
print("fibonacci series is : ")
for i in range(0,n):
    if i<=1:
        result=i
    else:
      result = first + second;
      first = second;
      second = result;
    print(result)
