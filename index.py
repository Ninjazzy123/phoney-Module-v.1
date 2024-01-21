import phoney
import csv

def present_menu(data):
  # TODO: Write a function that asks the user if they want to search for a (F) phone number, (A) area code, (E) exchange, or (X) exit
  while True:
    answer = input("\nPlease choose from the following options. \nF: Search for full phone number \nA: Search for area code \nE: Search for exchange \nX: Exit program \nEnter your selection: ")

    if answer.lower() == 'x':
      break

    digits = input("please enter the digits to search: ")
    match answer.lower():
      case "f":
        phoney.find_number(data, digits)
      case "a":
        phoney.find_areacode(data, digits)
      case "e":
        phoney.find_exchange(data, digits)
      case _:
        print("invalid selection. Please choose F, A, E, or X.")
  
def main():
  # TODO: Import CSV file as Python list
  data = []
  with open('phone_numbers_sample.csv', mode='r') as f:
    reader = csv.reader(f)
    data = list(reader)
    
  # TODO: Report to the user how many numbers were in the original list
  print(f"there are {len(data)} phone numbers in the CSV file.")
  # TODO: Use the `phoney.clean_phone_numbers` function to return a list of valid, digit-only phone numbers
  cleaned_list = phoney.clean_phone_numbers(data)
  print(f"{len(cleaned_list)} valid phone numbers were found.")
  # TODO: Start a loop that allows the user to search the phone number data
  present_menu(cleaned_list)

if __name__== "__main__":
  main()