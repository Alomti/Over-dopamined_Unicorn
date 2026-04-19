expenses = []

def display_expenses(month):
    for expenses_amount, expenses_type, expenses_month in expenses:
        if expenses_month == month:
            print("f{expenses_amount} + zł, {expenses_type}")
def add_expense(month):
    expenses_amount = int(input("podaj kwote wydatku: "))
    expenses_type = input("podaj typ wydatku:")
    expense = (expenses_amount, expenses_type, month)
    expenses.append(expense)

while True:
    month = int(input("Podaj miesiąc od 1 do 12: "))
    if month == 0:
        break
    while True:
        print("")
        print("powrót do wyboru miesiąca - 0")
        print(f"wyświetl wszystkie wydatki dla miesiąca {month} - 1")
        print("dodaj wydatek - 2")
        choice = int(input("Wybierz opcję: "))
        if choice == 0:
            break
        elif choice == 1:
            display_expenses(month)
        elif choice == 2:
            add_expense(month)