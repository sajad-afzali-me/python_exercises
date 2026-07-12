num = float(input("Enter a number\n n: "))
if not num.is_integer():
    print("ERROR: Odd or Even is only for integer numbers , not decimals")
else:
    num = int(num)
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
