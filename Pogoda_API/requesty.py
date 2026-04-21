from upienkrzanie import get_locations, show_history
while True:
    print("")
    try:
        choice = int(input(
            'Choose option:\n'
            '1-Show weather in location\n'
            '2-Show your history\n'
            '3-exit'
            ))
    except ValueError:
        print("")
        print('Invalid option. Please choose number between 1-3')
        continue
    if choice not in [1, 2, 3]:
        print("")
        print('Invalid option. Please choose number between 1-3')
        continue
    elif choice == 1:
            location = input("Enter a location: ")
            print("")
            get_locations(location)
    elif choice == 2:
        show_history()
    else:
        break