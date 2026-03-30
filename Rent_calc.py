#this is a python project :-> Rent calculator
#there are 3 person
#charges be like : total rent , food , water , electricity


print("🏠 RENT CALCULATOR SYSTEM")

# program loop
while True:

    print("\n-----------------------------")
    print("Enter All Monthly Expenses")
    print("-----------------------------")

    # inputs
    house_rent = float(input("Enter House Rent: "))
    food_bill = float(input("Enter Food Bill: "))
    electricity_units = float(input("Enter Electricity Units: "))
    charge_per_unit = float(input("Enter Cost per Unit: "))
    water_bill = float(input("Enter Water Bill: "))
    internet_bill = float(input("Enter Internet Bill: "))
    people = int(input("Enter Number of People: "))

    # calculations
    electricity_bill = electricity_units * charge_per_unit

    total_expense = (
        house_rent 
        + food_bill 
        + electricity_bill 
        + water_bill 
        + internet_bill
    )

    per_person = total_expense / people

    # detailed output
    print("\n========== BILL DETAILS ==========")
    print("House Rent        :", house_rent)
    print("Food Bill         :", food_bill)
    print("Electricity Bill  :", electricity_bill)
    print("Water Bill        :", water_bill)
    print("Internet Bill     :", internet_bill)
    print("---------------------------------")
    print("Total Expense     :", total_expense)
    print("Each Person Pays  :", round(per_person, 2))
    print("=================================")

    # extra feature (basic logic)
    if per_person > 5000:
        print("⚠️ Expense is High! Try to reduce costs.")
    else:
        print("✅ Expense is under control.")

    # option menu
    print("\nWhat do you want to do next?")
    print("1. Calculate Again")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("👋 Thank you for using Rent Calculator!")
        break