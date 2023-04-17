"""
check username, password and login
"""



expected_user: str = 'Florin'
expected_password: str = '1234'
sold: int = 1000
actual_user = input('Please enter a valid username: ')
assert actual_user == expected_user
actual_password = input('Please enter a valid password: ')
assert actual_password == expected_password
input('Please enter to log in!')
print(f'Your sold is: {sold}')


"""todo sa contina cu operatiunea in care userul specifica cati bani vrea sa scoata,
 se face o verificare ca suma respectiva ii ajunge (ca poate sa scoata) si daca trece de 
 verificare este intampinat cu un mesaj: soldul tau este ...afisat sold"""

x = int(input(f'Your balance is {sold}.Please select how much money you want to withdraw: '))
assert sold > x, "Insufficient amount"
z = sold - x
assert sold >= x
print('You have enough money in your account!')
input(f'Please enter to withdraw: {x}')
print(f'You withdraw {x} from your account')
input('Please enter to see your remaining sold!')
print('Thank you for using withdraw service!')
print(f'Your remaining sold is: {z}!')
