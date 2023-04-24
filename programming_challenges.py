
# Code-cademy.com: 10 Python Code Challenges for Beginners:
# These challenges are a great way to practice core concepts and exhibit understanding of the language.

# 1. convert radians to degrees:
radians = float(input("Enter number of radians: "))

import math as M


def convert():
    degrees = (radians * 180) / M.pi
    return round(degrees, 2) 
                             
degrees = convert()          
print(str(radians) + " radians is equililant to " + str(degrees) + " degrees.")



# 2. sort a list:               
print("1 = asc \n2 = desc \n3 = none")
selection = (input("please select a sorting method by number: "))

my_list = [23, 5, 8, 27, 4, 9, 33, 16, 0, 12]

def sorter(selection):
    if selection == '1':
        return sorted(my_list)
    elif selection == '2':
        return sorted(my_list, reverse = True)                
    elif selection == '3':                           
        return my_list
    else:
        selection = (input("Your selection is invalid. Please enter one of the options above: "))
        result = sorter(selection)
        return result
result = sorter(selection)        
print("The sorted values are: ", result)



# 3. Convert a decimal number into binary: 
decimal = int(input("     *Decimal to Binary Converter* \nPlease insert a decimal to be converted: "))

def convert(x):
    binary_result = bin(x)
    return int(binary_result.lstrip('0b'))

result = convert(decimal)
print(result)



# 4. Count the vowels in a string:
string = input("provide a random string for analysis: ")

def vowel_counter(string):
    
    result = list(filter(lambda x : x == 'a' or x == 'e' or x =='i' or x == 'o' or x == 'u', string.lower()))
    return result 

vowel_total = (vowel_counter(string)) 
print("The total number of vowels in this string is: ", len(vowel_total))



# 5. Hide the credit card number:
cc_num = (input("please enter 16 digit credit card number: "))

def secure_num():
    for i in range(12):
        i = '*'
        yield i

result = (list(secure_num()))
print(''.join(result), end = cc_num[12::]) 
print("")



# 6. Are the X's equal to O's?:
random = input("""      *X/O comparator*\nIf X's and O's are equal: Returns True
If X's and O's are not equal: Returns False
Please provide a random string for X/O comparison: """)

def comparator(random):
    x_count = random.count("x") + random.count('X')
    o_count = random.count('o') + random.count('O')
    print("X-count =", x_count)
    print("O-count =", o_count) 
    if x_count == o_count:
        return True
    else:
        return False

result = comparator(random)
print("Is X-count and O-count equal?:", result)



# 7. create a calculator function:
print("Input two numbers to multiply:")
num1 = int(input("first number: "))
num2 = int(input("second number: "))

def multi(num1, num2):
    product = num1 * num2
    return product

result = multi(num1, num2)
print("The product is:", result)



# 8. Apply discount 15%OFFDERBY:
discode = input("Please enter discount code: ")

def authenticate(d):
    if d == "15%OFFDERBY":
        x = .85
        return x
    else:
        print("Error: discount code", d, "is not valid.") ; d = input("Please try another code: ")
        x = authenticate(d)
        return x
    
trxns = [9.99, 23.51, 17.08, 7.84]

def apply_discount(arg):
    return round(arg * auth, 2)

auth = authenticate(discode)
disc_result = list(map(apply_discount, trxns))
print("Your totals after discount applied: ", disc_result)



# 9. Return a list with just the integers:
x = list(input("Please provide a list of characters and all numeric values will be returned: "))

def char_list(x):
    num_list = [i for i in x if i.isnumeric()]
    return num_list

result = char_list(x)
print(result)



# 10. Repeat the characters:
x = (input("Please provide a string of characters and they will be doubled: "))

def double_char(x):
    num_list = [i * 2 for i in x]
    return (num_list)

result = double_char(x)
print(''.join(result)) ; print('')



# 'The Zen of Python':
input("Hi! I'm Python. press 'Enter' in the terminal to read a poem about my guiding principles") ; print('')

import this