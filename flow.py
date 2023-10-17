

from contacts import contact_book_manager
from models import Contact
import re

def phone_validator(phone):
  """
  This function takes a phone number as input and returns True if it is valid, False otherwise.

  Args:
    phone (str): The phone number to validate.

  Returns:
    bool: True if the phone number is valid, False otherwise.
  """
  return re.match(r"^([+]\d{1,4})?(\d{10})$", phone) is not None

def email_validator(email):
  """
  This function takes an email address as input and returns True if it is valid, False otherwise.

  Args:
    email (str): The email address to validate.

  Returns:
    bool: True if the email address is valid, False otherwise.
  """
  return re.match(r"^\w+@\w+\.\w+$", email) is not None

def required_input(prompt, validator=lambda x: True):
  """
  Prompts the user for input until a non-empty and valid value is entered.

  Args:
    prompt (str): The prompt to display to the user.
    validator (function, optional): A function that takes the user's input as a
      parameter and returns True if the input is valid, False otherwise. Defaults
      to a function that always returns True.

  Returns:
    str: The user's input.

  """
  while True:
    value = input(prompt)
    if not value:
      print("This field is compulsory.")
      continue

    if not validator(value):
      print("Invalid input.")
      continue
    return value

def create_contact():

  """
  This function prompts the user for the details of a contact and creates a Contact object.
  """

  name = required_input("Enter name: ")
  phone = required_input("Enter phone: ", validator=phone_validator)
  email = required_input("Enter email: ", validator=email_validator)
  address = required_input("Enter address: ")
  contact = Contact(name, phone, email, address)
  return contact

def decide(choice):
  """
  This function takes a choice as input and performs the corresponding action based on the choice.

  Args:
    choice (str): The user's choice of action to perform.

  Returns:
    None
  """
  if choice == "1":
    print("Enter new contact details below. \n If a contact with the same name already exists, it will be overwritten.")
    contact = create_contact()

    contact_book_manager.add_contact(contact)
    print(f"Contact {contact.name} added successfully")

  elif choice == "2":
    query = input("Enter query to search contact and edit \n(If multiple contacts are present, the first one would be edited): ")
    results = contact_book_manager.search_contact(query)
    if not results:
      print(f"No matching Contacts not found")
      return
    
    current = results[0]

    print("Currently Editing:")
    print(current)
    print()

    contact = create_contact()

    if current.name != contact.name:
      contact_book_manager.delete_contact(current.name)
      contact_book_manager.add_contact(contact)
    else:
      contact_book_manager.update_contact(current.name, contact)

    print(f"Contact {contact.name} updated successfully")

  elif choice == "3":
    query = input("Enter query to search contact and delete \n(If multiple contacts are present, the first one would be deleted): ")
    results = contact_book_manager.search_contact(query)

    if not results:
      print(f"No matching Contacts not found")
      return

    current = results[0]
    print("Found Contact:")
    print(current)
    confirm = input("Are you sure you want to delete this contact? (Y/N): ")

    if confirm.lower() != "y":
      print("Contact not deleted")
      return
    
    name = results[0].name
    contact_book_manager.delete_contact(name)
    print(f"Contact {name} deleted successfully")

  elif choice == "4":
    query = input("Enter query to search: ")
    results = contact_book_manager.search_contact(query)

    if not results:
      print(f"No results found for {query}")
      return
    
    print(Contact.prettify(results))

  elif choice == "5":
    print(contact_book_manager)
  elif choice == "6":
    return
  else:
    print("Invalid choice")

def step(choice):
  """
  This is a wrapper to the decide function.
  It calls the decide function and then prompts the user to press Enter to go back to the main menu, 
  as long as the user does not choose to exit the program.

  Args:
    choice (str): The user's choice of action to perform.

  Returns:
    None
  """
  if choice != "6":
    decide(choice)
    input("\nPress Enter to go back to main menu")
  else:
    print("Bye 👋")
    contact_book_manager.save_contacts()
  

def prompt():
  """
  This function displays the main menu and prompts the user for their choice of action.

  Args:
   None

  Returns:
    str: The user's choice of action to perform.
  """
  print("Welcome to your contact book 📕")
  print("Below are the options: ")
  print("1. Add a contact ➕")
  print("2. Update a contact ✏️")
  print("3. Delete a contact ❌")
  print("4. Search a contact 🔍")
  print("5. View all contacts 📖")
  print("6. Exit 🚪")
  choice = input("Enter your choice: ")
  print()
  return choice

def clear():
  """
  This function clears the console screen.

  Args:
    None

  Returns:
    None
  """
  print("\033c", end='')


def main_loop():
  """
  This function is the main loop of the program. 
  It displays the main menu, prompts the user for their choice of action, 
  and performs the corresponding action.

  If the user unexpectedly exits the program, it saves the contacts to storage (Ctrl-C or Ctrl-Z).

  Args:
    None

  Returns:
    None
  """
  try:
    clear()
    choice = ""
    while choice != "6":
      choice = prompt()
      clear()
      step(choice)
      clear()

  except (KeyboardInterrupt, EOFError):
    print("Exiting Contact book forcefully...\nBye 👋")
    contact_book_manager.save_contacts()