import unittest

### Olivia Criscione

### The file name should be renamed to your Student ID (00XXXXXXX_pa2.py)
### Each question in section 1 is worth 12.5 points. 
### Each question in section 2 is worth 25 points. 
### Your programs should pass the provided test cases. 
### Read the instructions and examples for each question. 
### Find the insert-your-code messages!
### When you want to test your program, uncomment the appropriate test case from bottom, run the program. 
### Depending on the test results, modify the code or move to the next question.
### The questions are separate, and the earlier results do not affect your ability to complete other question. 
### Do not modify the structure of the code. 


### Start of PA2

# 1a
# Make a dictionary called fruits_dict with fruit names as keys and the color of the fruit as values. Use the following key-value pairs.
# Key    | Value
# --------------
# Apple  | Red
# Banana | Yellow
# Kiwi   | Green
def q1a():
    # Insert your code
    fruits_dict = {
        'Apple': 'Red',
        'Banana':'Yellow',
        'Kiwi':'Green'
    }
    return fruits_dict

# 1b 
# Fill in the q1b function.
# Inputs:
# states_dict is a dictionary of state abbreviation: state name, for example 'HI': 'Hawaii'
# state_abbreviation is a string state abbreviateion, for example 'HI'
# Outputs:
# The function should return the state name from the dictionary provided for the abbreviation provided, for example q1b({"HI": "Hawaii"}, "HI") should return "Hawaii"
def q1b(states_dict, state_abbreviation):
    # Insert your code
    if state_abbreviation in states_dict:
        return states_dict[state_abbreviation]
    else:
        return None

# 1c
# Fill in the q1c function
# Inputs:
# input_dict is a dictionary
# key is a string
# value is a string
# Output:
# This function should return the input_dict but with the new key-value pair in it. 
# So, if input_dict was {"A":"B"} and a new key is "C" with value of "D", the returned dictionary would be {"A":"B", "C": "D"} 
def q1c(input_dict, key, value):
    # Your code here
    input_dict[key] = value
    return input_dict # Return modified dict here

# 1d
# Fill in the q1d function
# Inputs:
# input_dict is a dictionary
# key is a string
# Output:
# The function should return the dictionary with key-value pair removed.
# If the input_dict was {"A":"B", "C":"D"} and the key is "A", the returned dictionary would be {"C":"D"}
def q1d(input_dict, key):
    # Your code here
    if key in input_dict:
        del input_dict[key]
    return input_dict # Return modified dictionary here

# 1e
# Fill in the q1e function
# Inputs:
# age_dict is a dictionary
# Output:
# The function should return the average of all the values in the dictionary. 
# If the age_dict was {"Abby":25, "Ben": 23, "Chris": 28, "Dave", 37, "Emily": 42}, the returned value should be 31.
def q1e(age_dict):
    # Your code here (HINT: You may want to use the the .items() or .values() function on the dict to help you.)
    if not age_dict:
        return 0 # Return correct average age
    values = age_dict.values()
    average = sum(values) / len(values)
    return average

# 1f
# Fill in the q1f function
# Inputs:
# fruits_dict is a dictionary
# prices_dict is also a dictionary
# key is a string
# The key can be used in both dictionaries!
# discounted_price is a number
# Output:
# The function should return the updated prices_dict: 
# if the value of the key in fruits_dict is more than 5, then the new price for that key should be replaced or updated with the discounted_price.
# For example, if fruits_dict is {"Orange":5, "Papaya":6}, prices_dict is {"Oranges":10, "Papaya":20}, key is "Papaya", discounted_price is 5
# then the returned prices_dict should be {"Oranges":10, "Papaya":5}
def q1f(fruits_dict, prices_dict, key, discounted_price):
    # Your code here!
    if key in fruits_dict and fruits_dict[key] > 5:
        prices_dict[key] = discounted_price
    return prices_dict

# 2a
# Inputs:
# key_list is a list
# val_list is also a list
# Output:
# The function should return the new_dict with key-value pairs made from key_list and val_list.
# The lengths of key_list and val_list should be checked, they should be equal. 
# If the key_list was ['a', 'b'] and val_list was [1, 2], the function should return a dictionary with {'a':1, 'b':2}
# If the key_list was ['a'] and val_list was [1, 2], the function should return an empty dictionary.
def q2a(key_list, val_list):
    # Insert your code here (HINT: check the lengths first!)
    new_dict = {}
    if len(key_list) == len(val_list):
        new_dict = dict(zip(key_list, val_list))
    return new_dict


### End of PA2 






# Test
# Tells you which test case the program has failed in terminal. 
# These are examples of test cases provided for you to test your program during the homework. 
# All test cases should pass. 
# Uncomment the class when you want to test your program! 



class TestQuestion1a(unittest.TestCase):

    def test_dict_vals(self):
        fruits_dict = q1a()
        self.assertIn('Apple', fruits_dict)
        self.assertIn('Banana', fruits_dict)
        self.assertIn('Kiwi', fruits_dict)
        self.assertEqual(fruits_dict['Apple'], 'Red')
        self.assertEqual(fruits_dict['Banana'], 'Yellow')
        self.assertEqual(fruits_dict['Kiwi'], 'Green')

class TestQuestion1B(unittest.TestCase):

    state_lookup = {'NY': 'New York', 'PA': 'Pennsylvania', 'FL': 'Florida', 'CA': 'California'}
    def test_new_york(self):
        self.assertEqual(q1b(self.state_lookup, 'NY'), 'New York')

    def test_california(self):
        self.assertEqual(q1b(self.state_lookup, 'CA'), 'California')

    def test_florida(self):
        self.assertEqual(q1b(self.state_lookup, 'FL'), 'Florida')

class TestQuestion1C(unittest.TestCase):

    def test_one(self):
        self.assertEqual(q1c({"A":"B"}, "C", "D"), {"A":"B", "C":"D"})

    def test_two(self):
        self.assertEqual(q1c({"Elephant":"Large"}, "Mouse", "Small"), {"Elephant":"Large", "Mouse":"Small"})

    def test_three(self):
        self.assertEqual(q1c({"This class is":"Torture"}, "Other classes", "are too"), {"This class is":"Torture", "Other classes":"are too"})

class TestQuestion1D(unittest.TestCase):

    def test_one(self):
        self.assertEqual(q1d({"A":"B", "C":"D"}, "A"), {"C":"D"})

    def test_two(self):
        self.assertEqual(q1d({"Puppy":"Cute", "Snake":"Scary"}, "Snake"), {"Puppy":"Cute"})

    def test_three(self):
        self.assertEqual(q1d({"Hungry":"Food", "Thirsty":"Water"}, "Thirsty"), {"Hungry":"Food"})

class TestQuestion1E(unittest.TestCase):

    def test_one(self):
        self.assertEqual(q1e({"Zach":30, "Yanni":40, "Xyla":20}), 30)

    def test_two(self):
        self.assertEqual(q1e({"Cat":10, "Dog":15, "Elephant":20}), 15)

    def test_three(self):
        self.assertEqual(q1e({"Burger":10, "Fries":5, "Steak":15}), 10)

class TestQuestion1F(unittest.TestCase):

    def test_one(self):
        self.assertEqual(q1f({"Apple":5, "Mango":3, "Watermelon":6},{"Apple":2, "Mango":5, "Watermelon":10}, "Watermelon", 1),{"Apple":2, "Mango":5, "Watermelon":1})

    def test_two(self):
        self.assertEqual(q1f({"Guava":2, "Grapes":4},{"Guava":10, "Grapes":8}, "Guava", 4), {"Guava":10, "Grapes":8})

    def test_three(self):
        self.assertEqual(q1f({"Strawberry":2, "Blueberry":3, "Blackberry":4, "Elderberry":5, "Raspberry":6}, {"Strawberry":7, "Blueberry":8, "Blackberry":9, "Elderberry":10, "Raspberry":11}, "Raspberry", 2), {"Strawberry":7, "Blueberry":8, "Blackberry":9, "Elderberry":10, "Raspberry":2})

class TestQuestion2A(unittest.TestCase):
    def test_one(self):
        self.assertEqual(q2a(['a', 'b', 'c'], [1, 2, 3]),{'a':1, 'b':2, 'c':3})

    def test_two(self):
        self.assertEqual(q2a([1], [0,0]),{})
    
    def test_three(self):
        self.assertEqual(q2a(['hello', 'goodbye'],[0, 1]), {'hello':0, 'goodbye':1})

    def test_four(self):
        self.assertEqual(q2a(['happy', 'sad'], ['smile']), {})


if __name__ == '__main__':
    unittest.main()