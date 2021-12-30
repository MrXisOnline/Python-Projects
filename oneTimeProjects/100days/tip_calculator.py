print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, 15? "))
heads = int(input("How many people to split the bill? "))
tip = bill*tip_percent/100
total_bill_per_head = round((bill + tip)/heads, 2)

print("Each person should pay : $%f" %total_bill_per_head)