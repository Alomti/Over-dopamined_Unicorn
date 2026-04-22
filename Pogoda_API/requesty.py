from upienkrzanie import get_locations, weather_manager
while True:
    print("")
    try:
        choice = int(input(
            'Choose option:\n'
            '1-Show weather in location\n'
            '2-Show your history\n'
            '3-Show your history and sort it unusual\n'
            '4-exit'
            ))
    except ValueError:
        print("")
        print('Invalid option. Please choose number between 1-3')
        continue
    if choice not in [1, 2, 3, 4]:
        print("")
        print('Invalid option. Please choose number between 1-3')
        continue
    elif choice == 1:
            location = input('Enter a location: ')
            print('')
            get_locations(location)
    elif choice == 2:
        print(weather_manager)
    elif choice == 3:
            sort = input('How to sotr your history? 1-By last three days, Anything but 1-By city')
            if int(sort) == 1:
                 weather_manager.sort_by_lastthreedays()
                 print(weather_manager)
            else:
                 city = input('Location Name:')
                 weather_manager.sort_by_city(city)
                 print(weather_manager)
    else:
        break