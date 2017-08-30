#Write a function square _number that takes in a number and squares it.

def square_number(number):
     return number ** 2
#print(square_number(789))

def test_square_number():
     assert square_number(2)==4
     assert square_number(8)==64
     assert square_number(10)==100
     print('Congratulations,Your Code is correct sirjee')

test_square_number()     


