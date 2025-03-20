"""
Chapter 3 example (page 67)
program: grading.py
2/26/2025

Application that accepts  numeric grade as an input nd then determines and outputs the letter grade the student will receieve.
"""
#input phase
number= int(input("Please enter the numeric grade: "))

# processing phase
if number > 89:
	letter = "A"
elif number > 79:
	letter = "B"
elif number > 69:
	letter = "C"
elif number >= 65:
	letter = "D"
else: 
	letter ="F"

#output phase
print("The letter grade is" , letter)
input("Exit by pressing ENTER...")
