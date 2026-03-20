# Python Expense Tracker :

#This is a beginner friendly project made by a 16Y/0 

ExpenseList = [] #where i am going to add my expense list

print("====WELCOME🥰 TO THE EXPENSE TRACKER====")

while True:
        print("-------Overview-------")
        print("1.Add Expense💲\n"
                "2.View Your Expense💸\n"
                "3.View Your Total🤑\n"
                "4.Exit😶")
        
        choice = int(input("Enter Your Choice👉 (1-4) : "))

#1 Add Expense
        if choice == 1:
                date = input("Date of Expense (YY-MM-DD) : ")
                type = input(" Type (Fashion👔 , Sports⚽ , Education📚 , etc🎨...) : ")
                description = input("Descibe shortly🧐 : ")      
                amount = float(input("What was the price 💲 ? : "))

                expense = {
                        "date": date,
                        "type": type,
                        "description": description,
                        "amount": amount
                }

        
                ExpenseList.append(expense)
                print("\n Expense Added Successfully✅ ..")

#2 View Your Expense
        elif choice == 2:
                if len(ExpenseList) == 0:
                        print("You have To add an Expense")
                else:
                        print("Your expenses💸 are as follows 👇:")
                        count = 1
                        for items in ExpenseList:
                                print(f"Expense no.{count}:\n{items['date']},\n{items['type']},\n{items['description']},\n{items['amount']}\n ---------------")
                                count = count+1

#3 View Total Spending
        elif choice == 3:
                total = 0
                for items in ExpenseList:
                        total = total + items["amount"]
                        
                print(f"Total Spend 🤑: \n{total}")

#4Exit 
        elif choice == 4:
                print("Thanks For using | Bye !!")
                break

#Any issue
        else:
                print("Invalid Choice | Please Pick Between (1-4)")
                print("Thanks")
