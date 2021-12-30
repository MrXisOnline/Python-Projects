import random
seednum = int(input("Enter seed : "))
random.seed(seednum)
name = input("Give me everybody\'s name separated by comma : ")
names = name.split(",")
r_in_num = random.randint(0,len(names)-1)
print(f"{names[r_in_num]} is going to buy the meal today")