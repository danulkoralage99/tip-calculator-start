#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print ("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15?")
number_of_people = input("How many people to split the bill?")

tip = float(total_bill)/100*int(tip_percentage)

bill_with_tip = float(total_bill) + tip

bill_divided = bill_with_tip/int(number_of_people)

bill_divided_final = round(bill_divided,2)

print(F"Each person should pay: {bill_divided_final}")