
## Main Code
def display_intro():
  print('------------------ABC Stores-----------------')
  print('\n1. Store hours')
  print('2. Available products/prices')
  print('3. Discounts/coupons')
  print('4. Feedback submissions')
  print('5. Exit')
display_intro()

def exit_function():
  selection = input('Would you like to continue or exit?')
  #Stack Overflow: yes/no questions (https://stackoverflow.com/questions/17953940/yes-or-no-output-python)
  if selection == 'continue':
    display_intro()
    user_direction()
  elif selection == 'exit':
    print('Thank you for using our program! We hope you were able to find everything you needed. Have a nice day!')

def store_hours():
  print('Our 15 ABC Stores all operate:')
  print('Monday- Friday: 9-9')
  print('Saturday/Sunday: 10-8')
  print('\nABC Stores are also closed on all national holidays.')
  exit_function()

def products_prices():
  print('ABC Stores currently sells:')
  print('Shirts: $15-$20')
  print('Dresses: $25-$55')
  print('Suits: $50-$100')
  print('Pants: $20-$55')
  print('For more info, please go to www.abcstores.com/products!')
  exit_function()

def discounts_prices():
  discount_list = [1111, 2222, 3333, 4444]
  discount_input = input("Enter discount code to check if your discount code is valid:")
  if discount_input == '1111':
    print('Discount code is valid!')
    exit_function()
  elif discount_input == '2222':
    print('Discount code is valid!')
    exit_function()
  elif discount_input == '3333':
    print('Discount code is valid!')
    exit_function()
  elif discount_input == '4444':
    print('Discount code is valid!')
    exit_function()
  else:
    print('Discount code is invalid')
    exit_function()

def feedback_submission():
  location = input('Enter zip code of store you are providing feedback for:')
  experience = int(input('Rate your experience at your local ABC Store from 1 to 10:\n'))
  if experience <= 5:
      print(f"We're sorry to hear that at our location at {location}, you recieved an experience of {experience} out of 10. We will take your feedback and improve our stores so that you may have a better experience next time.\n ")
      exit_function()
  if experience > 5:
      print("That's good to hear! We're glad you enjoyed your experience at ABC Stores. Thank you for your feedback.\n")
      exit_function()



def user_direction():
  user_input = int(input('\nWelcome to the ABC Store Customer Service FAQ! Please select a number above to continue.'))
  if user_input == 1:
    store_hours()
  elif user_input == 2:
    products_prices()
  elif user_input == 3:
    discounts_prices()
  elif user_input == 4:
    feedback_submission()
  elif user_input == 5:
          print('\nThank you for using our program! We hope you were able to find everything you needed. Have a nice day!')

    
user_direction()