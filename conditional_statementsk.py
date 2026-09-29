
#Take three inputs from a user, separately. Print the largest of the numbers.
   # Hint: Determine what type of data is taken in as input.


    
#2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

temp =25
if temp>30:
    print('the temperature is too high')
elif temp>15:
    print('normal temperature')
else:
    print('cold temperature')

#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

x = 10
y = 110

if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")




#4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"

password='secret123'

if password==1234:
    print('access granted')
else:
    print('Access Denied')

#.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
#If start_date comes before end_date, print "Valid period",
#If start_date is after end_date, print "Invalid period".
#If b#oth dates are the same, print "One-day period".

start_date = '2024-01-01'
end_date = '2024-12-31'
if start_date<end_date:
    print('valid period')
elif start_date>end_date:
    print('invalid period')
else:
    print('one day period')




#2.Given two strings str1 and str2, write a conditional statement that checks:
#If str1 is longer than str2, print "str1 is longer".
#If str2 is longer than str1, print "str2 is longer".
#If both have equal length, print "Both are of equal length".

#use len function
str1 = "two"
str2 = "four"

if str1>'four':
    print("str1 is longer")
elif str2>'one':
    print("str2 is longer")
else:
    print("Both are of equal length")



#Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
#Prints "Access Granted" if user_id is in valid_ids.
#Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = 105

if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")




