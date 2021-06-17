user1 = {'name':'sharon','account_number':'9034466', 'pin': '9037','balance': 40000}
user2 = {'name':'omot','account_number':'9444', 'pin': '9037','balance': 40000}


print('''
  welcome to my bank
  you better not be poor
 ''')

account_number = input('please input your account number: ')
pin = input('please input your secret pin: ')

transaction = False

login_no = user1['account_number'] or user2['account_number']
login_pin = user1['pin'] or user2['pin']

while account_number == login_no and pin == login_pin:
    print('''
       Main Menu
    1 - view my balance
    2 - withdraw cash
    3 - deposit funds
    4 - Exit ''')
    choice = input('        Enter a choice: ')

    if choice == '1':
        if account_number == user1['account_number']:
            print('your balance: '+ str(user1['balance']))
        elif account_number == user2['account_number']:
            print('your balance: '+ str(user2['balance']))
        transact = input('do you want to make another transaction yes/no: ')
        if transact == 'yes':
            transaction = False
        else:
            break

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
            transaction = False
        break
    elif choice == '3':
        ammount = float(input('        Enter an ammount: '))
        if account_number == user1['account_number']:
            user1['balance'] = user1['balance'] + ammount
            print('your balance: '+ str(user1['balance']))
        elif account_number == user2['account_number']:
            user2['balance'] = user2['balance'] + ammount
            print('your balance: '+ str(user2['balance']))
        transact = input('do you want to make another transaction yes/no: ')
        if transact == 'yes':
            transaction = False
        else:
            break

    elif choice == '4':
        print('''

   thanks for banking with us
        ''')
        break
