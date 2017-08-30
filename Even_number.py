#Write a fucntion is_even that takes in a number and returns
#True if it is even,
#Otherwese false.
#Hint:
#Question:What does it mean for a number to be divisible by another number???
#Answer: number%another_number==0
#Gives you true
#Eg. 12%3==0---->True
#---->This means 12 is divisible by 3.
#Bonus chalenge:- Write the fuction solution in 1 line of code without using
#if statements.

def is_even(number):
     return number%2==0
def test_is_even():
     assert is_even(2)==True
     assert is_even(4)==True
     assert is_even(6)==True
     assert is_even(8)==True
     assert is_even(200)==True
     assert is_even(900)==True
     print("Congratulations sirjee, your code is correct")

test_is_even()     
          

