import sys

men = float(input("Please enter the number of men: "))
women = float(input("Please enter the number of women: "))
if women <= 0 or men <= 0 or men % 1 != 0 or women % 1 != 0:
    print("Error: Please enter positive intagers greater than 0!")
    sys.exit()
else:
    total_population = men + women
print(f"percentage of men: {((men/total_population) *100):.2f}")
print(f"percentage of women: {((women/total_population) *100):.2f}")
