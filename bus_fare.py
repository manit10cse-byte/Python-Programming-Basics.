# Bus fare calculation based on age and day of the week
#Author : Manit Kumar | B.Tech CSE (IOT & Cyber security)
print("---Welcome to the Automated Bus Fare System ---")
age = int(input("Enter the age of the passenger : " ))
distance = float(input("Enter the distance traveled in km: "))
# 1. Determine the base price per km based on age
if age<=12:
    base_price =2.5
    fare = base_price * distance
    print(fare)
elif age>=60:
    base_price = 3
    fare = base_price * distance
    print(fare)
# 2. Determine the day of the week and apply discounts if applicable
else :
    day = input("Enter the day of the week (e.g. monday, tuesday, etc.) : ").strip().lower()
# 3. Calculate the fare based on the day of the week using match-case statement
    match day :
        case "monday":
            base_price = 5 # no discount
            fare = base_price * distance
            print(f" Fare for {day}   : {fare}")
        case "tuesday":
            base_price = 5 # no  discount
            fare = base_price * distance
            print(f" Fare for {day}   : {fare}")
        case "wednesday":
            base_price = 5 # no discount
            fare = base_price * distance
            print(f" Fare for {day}   : {fare}")
        case "thursday":
            base_price = 5 # no discount
            fare = base_price * distance
            print(f" Fare for {day}   : {fare}")
        case "friday":
            base_price = 5 # no discount
            fare = base_price * distance
            print(f" Fare for {day}   : {fare}")
        case "saturday":
            base_price = 4.5 # 10% discount
            fare = base_price * distance 
            print(f" Fare for {day}   : {fare}")   
        case "sunday":
            base_price = 4.5 # 10% discount
            fare = base_price * distance

            print(f" Fare for {day}   : {fare}")
