import re

def clean_phone_numbers(numbers):
    # TODO: Create a function that accepts a list of strings and returns a list that consists of valid 10-digit North American phone numbers
    clean_list = []
    for number in numbers:
        for i in number:
            clenaed_number = re.sub(r'\D', '', i)
            # print(f"Removed Specials: {clenaed_number}") test cases
            if len(clenaed_number) == 10:
                clean_list.append(clenaed_number)
                # print(f"Cleaned: {clenaed_number}") test cases
    return clean_list

def find_number(numbers, search_term):
    # TODO: Create a function that accepts a list and a search term and returns information about whether or not the search_term appears in the list
    # This function searches for an entire US phone number
    if search_term in numbers:
        return print(f"{search_term} is in the list")
    else:
        return print("Number not found")

def find_areacode(numbers, search_term):
    # TODO: Create a function that accepts a list and a search term and returns information about whether or not the search_term appears in the list
    # This function searches for the area code of a phone number
    matching_numbers = []
    for number in numbers:
        if search_term[:3] == number[:3]:
            matching_numbers.append(number)
    return print(f"Area code: {search_term} was found in {len(matching_numbers)} phone numbers, {matching_numbers}")

def find_exchange(numbers, search_term):
    # TODO: Create a function that accepts a list and a search term and returns information about whether or not the search_term appears in the list
    # This function searches for the exchange of a phone number
    matching_numbers = []
    for number in numbers:
        if search_term == number[3:-4]:
            matching_numbers.append(number)
    return print(f"Exchange code: {search_term} was found in {len(matching_numbers)} phone numbers, {matching_numbers}")
    