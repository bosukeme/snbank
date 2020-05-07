import re
import random

import os

with open('staff.txt') as text:
    text_var=text.readlines()
    
username1=text_var[0][10:].strip("\n").strip(" '' ")
password1=text_var[1][10:].strip("\n").strip(" '' ")
username2=text_var[6][11:].strip("\n").strip(" '' ")
password2=text_var[7][11:].strip("\n").strip(" '' ")

	

try:
    print('------------------------------')
    welcome=("""
        <<< Welcome. Staff Login Page >>>
               Press 1 for Staff Login
               press 2 to Close App
    """)
    print(welcome)

    print('------------------------------')
    user_response=int(input())

    #loggin in
    while user_response!='quit':
        if user_response==1:
            print('Logging In')
            user_response_username=input('What is your username? :').lower()
            user_response_password=input('What is your password? :').lower()
            if user_response_username==username1 and user_response_password==password1 or user_response_username==username2 and user_response_password==password2:

                print(' \n Welcome. Log in successfully')
                print('------------------------------')
                
                session=open('session.txt', 'a+')
                
                
                
                
                print("""
                Press 1: Create new bank account

                Press 2: Check Account Details

                Press 3: Logout

                """)
                print('--------------------------------------')

                user_response1=int(input())
                while user_response1 !=4:
                    if user_response1==1:
                        print("Fill the following details")
                        print()
                        account_name=input('Type your account name: ').lower()
                        opening_balance=int(input('Type the amount you wish to open: [Hint: Integer]: '))
                        account_type=input('Savings or Fixed: ').lower()
                        account_email=input('Enter your email address: ').lower()

                        print()
                        #generate 10 digit account number
                        account_number= ''.join(map(str, [random.randint(1,9) for a in range(0,10)]))

                        print("This is your account number: ", account_number)

                        #saving details
                        customer_text=open('customer.txt', "w+")
                        customer_text.write("Account Name: %s \n" % account_name )
                        customer_text.write("Opening Balance: %s \n" % opening_balance)
                        customer_text.write("Account Type: %s \n" % account_type)
                        customer_text.write("Account Email: %s \n" % account_email)
                        customer_text.close()
                        print('--------------------------------------')
                        
                        print("""
                    Press 1: Create new bank account

                    Press 2: Check Account Details

                    Press 3: Logout

                    """)

                        user_response2=int(input())
                        if user_response2==2:
                            request_account_number=input("Type in your Account number: [Hint: Integer] ")
                            print()
                            if account_number==request_account_number:
                                with open('customer.txt') as customer_details:
                                    print(customer_details.read())
                                    print('--------------------------------------')
                                    break
                            
                            else:
                                print("Wrong Account number. Try again")
                            
                                    
                            
                            

                    elif user_response1==2:
                        print('Create an account first.')
                        print()
                        break
                    elif user_response1==3:
                        print('Logging Out')
                        print()
                        break
            
                print("""
                                Press 1: Create new bank account

                                #Press 2: Check Account Details

                                #Press 3: Logout

                                """) 
                user_response3=int(input())
                if user_response3==3:
                    print(welcome)
                    session.close()
                    os.remove('session.txt')
                    user_response4=int(input())
                    if user_response4==2:
                        print('Closing App')
                        break
                
            else:
                print()
                print('Try again. Check Username and Password')



        elif user_response==2:
            print('Closing App')
            break
        else:
            print('Wrong Choice. Try Again ')
            break

except:
    print('Wrong Choice. Try Again ')
#session.close()
#os.remove('session.txt')