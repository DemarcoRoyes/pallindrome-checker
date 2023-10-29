def reverse_string(string):
    return string[::-1]

def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    reversed_string = reverse_string(cleaned_string)
    print("Reversed string:", reversed_string)
    return cleaned_string == reversed_string

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("This is a palindrome")
else:
    print("This is not a palindrome")
