import os, time

def show_introduction():
    print('=-'*15)
    print(f'\n{" " * 8} Car Rental\n')
    print('=-'*15)
    time.sleep(2)

def show_cars(list_cars):
    for i, cars in enumerate(list_cars):
        for car, value in cars.items():
            print(f'[ {i + 1} ] - {car} - R$ {value} / day')

def main_operation():

    os.system('cls')

    portfolio = [
        {'Chevrolet Tracker': '120'},
        {'Chevrolet Onix': '90'},
        {'Chevrolet Spin': '150'},
        {'Hyundai Tucson': '120'},
        {'Fiat Uno': '60'},
        {'Fiat Mobi': '70'},
        {'Fiat Pulse': '130'}
    ]

    new_portfolio = []

    while True:
        print('''
============================     
            
What do you wanna do?
        
[ 1 ] - Show Portfolio
[ 2 ] - Rent a Car
[ 3 ] - Return a Car
        
============================           
            ''')

        option_user = str(input('Choose an option: '))[0]
        os.system('cls')
        print()
        match option_user:
            case '1':
                show_cars(portfolio)
            case '2':
                print('\n[ RENT A CAR ] Look our Portfolio.\n')
                
                show_cars(portfolio)

                code_car = 0
                while True:
                    code_car = int(input('\nChoose a car code: '))

                    if code_car <= len(portfolio) - 1:
                        break
                    print('Invalid Code.')

                rent_days = int(input('How many days do you wanna rent it? '))

                rent_value = 0
                for value in portfolio[code_car].items():
                    rent_value = int(value[1]) * rent_days

                option_user_rent = str(input(f'The rent value is R${rent_value}. Do you wanna rent it? [ Y / N ] '))[0].lower()

                if option_user_rent == 'y':
                    new_portfolio.append(portfolio.pop(code_car))
                    print(f'Congratulations! You rent a car for {rent_days} days.')

            case '3':

                if len(new_portfolio) == 0:
                    print('You dont have rented cars.')
                    input()  
                    continue

                print('Below is the list of rent cars: \n\n')
                show_cars(new_portfolio)
                
                while True:
                    user_return_car_code = int(input('\nChoose a car code to return: '))  

                    if user_return_car_code <= len(new_portfolio):
                        print('Thanks for returning the car.')
                        portfolio.append(new_portfolio.pop(user_return_car_code))
                        break
                    print('Invalid Code.')

            case _:
                print('Invalid Option.')
                continue
        
        option_leave = str(input('''
\n\n===================\n
[ 0 ] - Continue
[ 1 ] - Exit

-> '''))
        
        if option_leave == '1':
            print('\nBye ;)')
            break
        
        os.system('cls')


show_introduction()
main_operation()