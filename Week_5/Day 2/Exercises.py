# #Write a family class
# class Family():
#     def __init__(self):
#         self.members = [{'Man': {'name': 'Mikel', 'age': '36', 'sex': 'Male', 'is_child': False},
#         'Woman': {'name': 'Rebeca', 'age': '34', 'sex': 'Female', 'is_child': False},
#         'Boy': {'name': 'Kevin', 'age': '15', 'sex': 'Male', 'is_child': True}}]
#
#         self.last_name = ''
#
#     def born(self, **kwargs):
#         june = {}
#         for key, value in kwargs.items():
#             june.update(kwargs.items())
#             self.members.append(june)
#             print('Mazal tov')
#
#     def is_18(self, name):
#         for june in self.members:
#             if name in june.values():
#                 if june.get('age') > 18:
#                     return True
#                 else:
#                     return False
#
# #____________________________main
#
# family = Family()
# family.born(name='Tom', age=1, sex='Male', is_child=True)
# big = family.is_18('Sarah')
# print(family.members)
#
# class Account:
#
#     def __init__(self, account_owner, balance):
#         self.account_owner = account_owner
#         self.balance = balance
#         self.details_dict = {self.account_owner: self.balance}
#
# class Owner(Account):
#     def __init__(self, account_owner, balance, card_num, pw):
#
#         super().__init__(account_owner, balance)
#
#         self.card_num = card_num
#
#         self.pw = pw
#
#         # self.account_numbers.append([card_num])
#
#     def get_balance(self):
#         print(f"Current balance: ${self.balance}")
#         return self.balance
#
#     def withdraw(self):
#         while True:
#             amount = int(input("Enter amount you wish to withdraw: $"))
#             if amount > self.balance:
#                 print(f"You do not have ${amount} in your account to withdraw. Try again.")
#                 continue
#             elif amount < 0:
#                 print(f"You must enter a valid withdrawal amount. Try again.")
#                 continue
#             else:
#                 self.balance -= amount
#                 print(f"Successful withdrawal of ${amount}. Your new balance is ${self.balance}")
#             again = input("Enter 1 to make another withdrawal, or 2 to exit: ")
#             if again == "1":
#                 continue
#             else:
#                 break
#
#     def deposit(self):
#         while True:
#             amount = int(input("Enter amount you wish to deposit: $"))
#             if amount < 0:
#                 print(f"You must enter a valid deposit amount. Try again.")
#                 continue
#             else:
#                 self.balance += amount
#                 print(f"Successful deposit of ${amount}. Your new balance is ${self.balance}")
#
#             again = input("Enter 1 to make another deposit, or 2 to exit: ")
#
#             if again == "1":
#
#                 continue
#
#             else:
#
#                 break
#
#     def choose_action(self):
#
#         action = input("Enter 1 for withdrawal, 2 for deposit, 3 to get balance: ")
#
#         if action == '1':
#
#             self.withdraw()
#
#         elif action == '2':
#
#             self.deposit()
#
#         elif action == '3':
#
#             self.get_balance()
#
#         else:
#
#             print("Invalid entry. Goodbye.")
#
#
#
#     def check_owner_info(self):
#
#         in_card_num = int(input("Enter your card number: "))
#
#         in_pword = input("Enter your password: ")
#
#         trial = 1
#
#         while trial < 3:
#
#             if in_card_num == self.card_num and in_pword == self.pw:
#
#                 self.choose_action()
#
#                 break
#
#             else:
#
#                 print("Card number or password incorrect.")
#
#                 trial += 1
#
#                 continue
#
#         if trial == 3:
#
#             print("Too many attempts. Your card has been destroyed.")
#
#             self.card_num = None
#
#
#
#
#
# class Bank:
#
#     def __init__(self, bank_name):
#
#         self.bank_name = bank_name
#
#         self.owners = []
#
#
#
#     def create_account(self, account_owner, balance, card_num, pw):
#
#         if len(self.owners) < 10:
#
#             owner = Owner(account_owner, balance, card_num, pw)
#
#             self.owners.append(owner)
#
#             return owner
#
#
#
#         else:
#
#             print(f"There are already 10 accounts in {self.bank_name} bank.")
#
#             print("Please try again later.")
#
#
#
#     def get_bank_balance(self):
#
#         total_in_bank = 0
#
#         for item in self.owners:
#
#             total_in_bank += item.balance
#
#         print(f"Total amount of money in bank: ${total_in_bank}")
#
#         return total_in_bank
#
#
#
#
#
#
#
# if __name__ == '__main__':
#
#     bank = Bank("Huntington")
#
#     mitch1 = bank.create_account("Mitch1",1000,123,'pw123')
#
#     mitch2 = bank.create_account("Mitch2",999,456,'pw456')
#
#     # mitch3 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch4 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch5 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch6 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch7 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch8 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch9 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch10 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch11 = bank.create_account("Mitch",1000,123,'pw123')
#
#     # mitch10.check_owner_info()
#
#     mitch1.deposit()
#
#     bank.get_bank_balance()







