#!/usr/bin/env python
# coding: utf-8

# # python basics- practice problem

# In[1]:


import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def main():
    try:
        radius = float(input("Enter the radius: "))
        if radius < 0:
            print("Radius cannot be negative.")
        else:
            area = calculate_circle_area(radius)
            print(f"Area of Circle is {area:.11f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")

if __name__ == "__main__":
    main()


# In[2]:


def main():
    name = input("Enter the name: ")
    roll_number = input("Enter the roll number: ")
    mark = input("Enter the mark: ")

    print("Name:", name)
    print("Roll No:", roll_number)
    print("Mark:", mark)

if __name__ == "__main__":
    main()


# In[3]:


def get_largest_number(numbers):
    if not numbers:
        return None
    else:
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        return largest

def main():
    try:
        input_str = input("Enter a list of numbers separated by commas: ")
        numbers = [int(x.strip()) for x in input_str.split(",")]
        largest_number = get_largest_number(numbers)
        if largest_number is not None:
            print(f"{largest_number} is the largest number.")
        else:
            print("The list is empty.")
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
if __name__ == "__main__":
    main()


# In[4]:


def main():
    previous_number = 0
    for current_number in range(1, 11):
        current_sum = current_number + previous_number
        print(f"Current Number {current_number} Previous Number {previous_number} Sum: {current_sum}")
        previous_number = current_number

if __name__ == "__main__":
    main()
    


# In[5]:


def main():
    input_str = input("Enter a list of numbers separated by commas: ")
    numbers = [int(x.strip()) for x in input_str.split(",")]
    
    divisible_by_5 = [num for num in numbers if num % 5 == 0]
    
    print("Numbers divisible by 5:", ", ".join(map(str, divisible_by_5)))

if __name__ == "__main__":
    main()


# # practice problem 2

# In[6]:


def count_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def main():
    input_string = input("Enter a string value: ")
    character_count = count_characters(input_string)
    
    output = ", ".join([f"{char}={count}" for char, count in character_count.items()])
    print("Sample output:", output)

if __name__ == "__main__":
    main()


# In[7]:


def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    try:
        num1, num2, num3 = map(int, input("Enter three numbers separated by commas: ").split(","))
        maximum = find_maximum(num1, num2, num3)
        print("Maximum of the three numbers:", maximum)
    except ValueError:
        print("Invalid input. Please enter three valid numbers separated by commas.")

if __name__ == "__main__":
    main()


# In[8]:


def exponent(base, exp):
    return base ** exp

def main():
    try:
        base = float(input("Enter the base: "))
        exp = int(input("Enter the exponent: "))
        result = exponent(base, exp)
        print(f"{base} raised to the power of {exp} is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()


# In[9]:


def sum_of_cubes(n):
    if n <= 0:
        return "Input must be a positive integer."
    
    sum_cubes = sum([i**3 for i in range(1, n)])
    return sum_cubes

def main():
    try:
        num = int(input("Enter a positive integer: "))
        result = sum_of_cubes(num)
        print(f"The sum of the cubes of all positive integers smaller than {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()


# In[10]:


def fizz_buzz():
    for num in range(1, 11):
        if num % 2 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 2 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def main():
    fizz_buzz()

if __name__ == "__main__":
    main()


# In[11]:


from collections import Counter

def most_frequent_item(numbers):
    # Count the occurrences of each item in the list
    counts = Counter(numbers)
    # Find the most common item
    most_common_item = counts.most_common(1)[0][0]
    return most_common_item

def main():
    input_str = input("Enter a list of numbers separated by commas: ")
    numbers = [int(x.strip()) for x in input_str.split(",")]
    
    most_frequent = most_frequent_item(numbers)
    print("Most frequent item:", most_frequent)

if __name__ == "__main__":
    main()


# In[12]:


def sum_of_squares(numbers):
    sum_squares = sum(num**2 for num in numbers)
    return sum_squares

def main():
    input_str = input("Enter a list of numbers separated by commas: ")
    numbers = [int(x.strip()) for x in input_str.split(",")]
    
    sum_squares = sum_of_squares(numbers)
    print("Sum of squares of the numbers:", sum_squares)

if __name__ == "__main__":
    main()
    


# In[13]:


def main():
    for num in range(1, 16):
        if num % 2 == 0:
            print(f"{num}-even")
        else:
            print(f"{num}-odd")

if __name__ == "__main__":
    main()


# In[ ]:




