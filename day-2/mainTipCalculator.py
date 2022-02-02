#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")

tip = input("How much tip you like to give? 10, 12, or 15? ")

totalPeople = input("How many people to split the bill? ")

total_bill = float(bill) + float(bill)*(int(tip)/100)
total_bill = round(total_bill, 2)

share = total_bill/int(totalPeople)

share = round(share, 2)

message = f"Each person should pay: ${share}"

print(message)
