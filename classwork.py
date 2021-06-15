users = [{'name':'sharon','account_number':'9034466', 'pin': '9037','balance': 40000},
    {'name':'omot','account_number':'9984379', 'pin': '9007','balance': 40000}
]

print('''
  welcome to my bank
  you better not be poor
 ''')

account_number = input('please input your account number: ')
pin = input('please input your secret pin: ')

for user in users:
    if user['account_number'] == account_number and user['pin'] == pin:
        def func():
            print('''
               Main Menu
            1 - view my balance
            2 - withdraw cash
            3 - deposit funds
            4 - Exit ''')
            choice = input('        Enter a choice: ')

            if choice == '1':
                user['balance'] =str(user['balance'])
                print('your balance: '+ user['balance'])
                transact = input('do you want to make another transaction yes/no: ')
                if transact == 'yes':
                    func()

            elif choice == '2':
                print('''
                Withdrawal menu
                    1 - N1000  4 - N10000
                    2 - N2000  5 - 20000
                    3 - N5000  6 - cancel transaction ''')
                pick = input('        Enter a choice: ')
                if pick == '1':
                    user['balance'] = user['balance'] - 1000
                    print('your balance: '+ str(user['balance']))
                    if user['balance'] < 1000:
                        print('insufficient funds')
                elif pick == '2':
                    user['balance'] = user['balance'] - 2000
                    print('your balance: '+ str(user['balance']))
                    if user['balance'] < 2000:
                        print('insufficient funds')
                elif pick == '3':
                    user['balance'] = user['balance'] - 5000
                    print('your balance: '+ str(user['balance']))
                    if user['balance'] < 5000:
                        print('insufficient funds')
                elif pick == '4':
                    user['balance'] = user['balance'] - 10000
                    print('your balance: '+ str(user['balance']))
                    if user['balance'] < 10000:
                        print('insufficient funds')
                elif pick == '5':
                    user['balance'] = user['balance'] - 20000
                    print('your balance: '+ str(user['balance']))
                    if user['balance'] < 20000:
                        print('insufficient funds')
                elif pick == '6':
                    print('''

               thanks for banking with us
                    ''')
                transact = input('do you want to make another transaction yes/no: ')
                if transact == 'yes':
                    func()


            elif choice == '3':
                ammount = float(input('        Enter an ammount: '))
                user['balance'] = user['balance'] + ammount
                print('your balance: '+ str(user['balance']))
                transact = input('do you want to make another transaction yes/no: ')
                if transact == 'yes':
                    func()

            elif choice == '4':
                print('''

           thanks for banking with us
                ''')
        func()
