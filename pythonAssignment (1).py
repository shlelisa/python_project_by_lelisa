# python project to github

def studentName():
    
    firstName="Lelisa"
    lastName="Shashura"
    university="Bule Hora University"
    college="Informatics College"
    department="Software Engineering"
    assignment="Individual Assignment"
    idNumber="Ru-0976/12"
    teacherName="Daniel"

    print("*************************************************")
    print(f"*****   University: {university} ")
    print(f"*****   College: {college} ")
    print(f"*****   Department: {department} ")
    print(f"*****   Assignment: {assignment}")
    print(f"*****   Name: {firstName} {lastName}")
    print(f"*****   Id Number: {idNumber}")
    print("****")
    print("****  ")
    print("****")
    print(f"*****             Submitted To: Mr. {teacherName}  ")
    print("*****             Submission Date: 1/25/2024  ")
    print("************************************************")
studentName()


# In[19]:


"""
Q1 There are 5280 feet in a mile.
    Write a Python statement that 
   calculates and prints the number of feet in 13 miles 
"""

def feetToMile():#function used to calculate the number of feet in the given miles, when it is called
    mile_in_feet = 5280

    while True:
        try:
            miles = float(input("Enter miles in number: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a numerical value for miles.")

    # Calculation will only proceed if valid input is received
    mile_to_feet = mile_in_feet * miles
    print(f"{miles} Miles is {mile_to_feet} in Feet")


feetToMile()#calling the function

"""
Q2 Write a Python statement that calculates and 
prints the number of seconds in 7 hours, 21 minutes and 37 seconds.
 
 """

def toSecondFunction():#function used to change the hour, minute and second to second when it is called
    while True:
        try:
            hour = int(input("Enter hour in number: "))
            minute = int(input("Enter minute in number: "))
            second = int(input("Enter second in number: "))
            break  # Exit the loop if all inputs are valid
        except ValueError:
            print("Invalid input. Please enter numerical values for hour, minute, and second.")

    # Calculation will only proceed if all inputs are valid
    to_second = 60 * 60 * hour + minute * 60 + second
    print(f"{hour} hour {minute} minute and {second} second is changed to {to_second} second")
    

toSecondFunction()#calling the function


""" 
Q3 The perimeter of a rectangle is 2w+2h, 
where w and h are the lengths 	of its sides. 
Write a Python statement that calculates and prints the  
length in inches of the perimeter of a rectangle with sides of length 4 and 7 inches. 

 """

def calculatePerimeter():#function used to calculate the perimeter of the rectangle when it is called
    while True:
        try:
            width = float(input("Enter width of Rectangle: "))
            height = float(input("Enter height of Rectangle: "))
            break  # Exit the loop if both inputs are valid
        except ValueError:
            print("Invalid input. Please enter numerical values for width and height.")
    
    # Calculation will only proceed if both inputs are valid
    perimeter = 2 * (width + height)
    print(f"The perimeter of Rectange with {width} witdh and {height} height is : {perimeter} inches")
    

calculatePerimeter()#calling the function


# In[2]:


"""
Q4 The circumference of a circle is 2πr where r is the radius of the circle. 
Write a Python statement that calculates and prints the 
circumference in inches of a circle whose radius is 8 inches. Assume that the constant π=3.14. 

"""

def calculateCircumference():#function used to calculate the circumference of the circle when it is called
    pi = 3.14

    while True:
        try:
            radius = float(input("Enter the radius of the circle in inches: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a numerical value for the radius.")

    # Calculation will only proceed if the input is valid
    circumference = 2 * pi * radius

    print(f"The circumference of the circle is {circumference:.2f} inches.")


calculateCircumference() #function calling

"""  
Q5 Given p dollars, the future value of this money when compounded
yearly at a rate of r percent interest for y years is p(1+0.01r)y. 
Write a Python statement that calculates and prints the value of 1000 dollars 
compounded at 7 percent interest for 10 years. 

"""

def futureValue():
    while True:
        try:
            # Get input from the user
            principal = float(input("Enter the principal amount (in dollars): "))
            interest_rate = float(input("Enter the interest rate (in percent): "))
            years = int(input("Enter the number of years: "))

            # Calculate the future value
            future_value = principal * (1 + 0.01 * interest_rate) ** years

            # Print the result
            print(f"The future value of ${principal:.2f} compounded at {interest_rate:.2f}% interest for {years} years is ${future_value:.2f}")
            break  # Exit the loop if no errors occur

        except ValueError:
            print("Invalid input. Please enter numbers only.")

futureValue() #function calling


# In[12]:


"""  
Q6 Write a Python expression that combines the string "Joe Warren is 52 years old."
from the string "Joe Warren" and the number 52 and then prints the result 
(Hint: Use the function str to convert the number into a string.) 
"""

def getName_and_Age_From_User():
    while True:
        try:
            # Get input from the user
            name = input("Enter the person's name (letters only): ")
            age = int(input("Enter the person's age: "))

            # Validate name - check if all alphabetical characters
            if not all(char.isalpha() for char in name):
                raise ValueError("Name must contain only letters.")

            # Combine the strings and print the result
            print(f"{name} is {age} years old.")
            break  # Exit the loop if no errors occur

        except ValueError:
            print("Invalid input. Please enter a valid name and a number for the age.")


getName_and_Age_From_User() #function calling


# In[14]:


"""  
Q7 Write a single Python statement that combines the three strings "My name is", "Joe" and "Warren" 
(plus a couple of other small strings) into one larger string "My name is Joe Warren." and prints the result. 
"""

def combine_names():
    """
    Combines two strings into a sentence "My name is {first_name} {last_name}."

    Prints:
        The combined sentence with the first and last name.
    """

    while True:
        try:
            first_name = input("Enter your first name (letters only): ")
            last_name = input("Enter your last name (letters only): ")

            # Validate name using string.isalpha()
            if not first_name.isalpha() or not last_name.isalpha():
                raise ValueError("Names must contain only letters.")

            sentence = f"My name is {first_name} {last_name}."

            print(sentence)
            break  # Exit the loop if no errors occur

        except ValueError:
            print("Invalid input. Please enter names containing only letters.")


combine_names() #function calling


# In[18]:


"""  
Q8 The distance between two points (x0,y0) and (x1,y1) is (x0−x1)2+(y0−y1)2.
Write a Python statement that calculates and prints the distance between the points (2,2) and (5,6). 

"""

import math

def calculate_distance():
    while True:
        try:
            # Get input from the user
            x0 = float(input("Enter the x-coordinate of the first point: "))
            y0 = float(input("Enter the y-coordinate of the first point: "))
            x1 = float(input("Enter the x-coordinate of the second point: "))
            y1 = float(input("Enter the y-coordinate of the second point: "))

            # Calculate the distance using the distance formula
            distance = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

            # Print the result
            print("The distance between the two points is:", "{:.2f}".format(distance))
            break  # Exit the loop if no errors occur

        except ValueError:
            print("Invalid input. Please enter numbers only.")


calculate_distance() #function calling


# In[26]:


def main():
    while True:
        try:
            # Offer various calculations
            print("\nChoose a calculation to perform:")
            print("0. Student Name")
            print("1. Feet to miles")
            print("2. Seconds from hours, minutes, and seconds")
            print("3. Perimeter of a rectangle")
            print("4. Circumference of a circle")
            print("5. Future value of an investment")
            print("6. Combine name and age")
            print("7. Combine first name and last name")
            print("8. Calculate distance between two points")
            print("Q. Quit")

            choice = input("Enter your choice: ")

            if choice == "0":
                studentName()
            elif choice == "1":
                feetToMile()
            elif choice == "2":
                toSecondFunction()
            elif choice == "3":
                calculatePerimeter()
            elif choice == "4":
                calculateCircumference()
            elif choice == "5":
                futureValue()
            elif choice == "6":
                getName_and_Age_From_User()
            elif choice == "7":
                combine_names()
            elif choice == "8":
                calculate_distance()
            elif choice.lower() == "q":
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
            
if __name__ == "__main__":
    main()


# In[ ]:




