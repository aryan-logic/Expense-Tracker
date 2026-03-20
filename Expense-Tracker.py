# Python Expense Tracker :

#This is a beginner friendly project made by a 16Y/0 

ExpenseList = [] #where i am going to add my expense list

print("====WELCOME🥰 TO THE EXPENSE TRACKER====")

while True:
        print("\n-------Overview-------")
        print("1.Add Expense💲\n"
                        "2.View Your Expense💸\n"
                        "3.View Your Total🤑\n"
                        "4.Exit😶")
        try:       
                choice = int(input("Enter Your Choice👉 (1-4) : "))
        except ValueError:
                print("Please enter a number only")
                continue
#1 Add Expense
        if choice == 1:
                date = input("Date of Expense (YY-MM-DD) : ")
                category = input(" category (Fashion👔 , Sports⚽ , Education📚 , etc🎨...) : ")
                description = input("Descibe shortly🧐 : ")      
                amount = float(input("What was the price 💲 ? : "))

                expense = {
                                        "date": date,
                                        "category": category,
                                        "description": description,
                                        "amount": amount
                                }

                        
                ExpenseList.append(expense)
                print("\n Expense Added Successfully✅ ..")

#2 View Your Expense
        elif choice == 2:
                if not  ExpenseList:
                                print("No Exxpenses Added yet")
                else:
                        print("\n Your Expense is as follows 👇:")
                        for i , item in enumerate(ExpenseList,start=1):
                                        print(f"""

Expense no. {i}
Date : {item["date"]}
Category : {item["category"]}
Description : {item["description"]}
Amount : ${item["amount"]}
""")

#3 View Total Spending
        elif choice == 3:
                total = sum(item["amount"] for item in ExpenseList)
                print(f"Total Spend 🤑: 💲{total}")

#4Exit 
        elif choice == 4:
                print("Thanks For using | Bye !!")
                break

        #Any issue
        else:
                print("Invalid Choice | Please Pick Between (1-4)")
                print("Thanks")
