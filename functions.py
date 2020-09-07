def area(width, height):
    result = width * height
    return result
result = area(5, 6)
print (result)
result = area(14,2)
print (result)
result = area(50,3)
print (result)
def subtract(current_year, model_year):
     how_old_is_mycar = current_year - model_year
     return how_old_is_mycar
how_old_is_mycar = subtract(2020,2005)
print(how_old_is_mycar)
how_old_is_mycar = subtract(2020,1998)
print(how_old_is_mycar)
#"Write a function called divide() which takes in two numbers and returns the first number divided by the second number"
#To write this function definition we first need to identify what the inputs or parameters are and then what the output should be or what the function should return.
#Q6
def divide(number_of_cookies,number_of_guests):
    cookies_per_guest = number_of_cookies / number_of_guests
    return cookies_per_guest
cookies_per_guest = divide(30,5)
print( cookies_per_guest)
#Q7 add() function:
def add(shirts, shorts):
     garments = shirts + shorts
     return garments
garments = add(6,3)
print(garments)

garments = add(10, 7)
print(garments)



