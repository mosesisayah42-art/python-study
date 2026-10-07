#loops r used to repetitive task multiple time or until certain condition is met

#Techcamp 20 time on the terminal

no=list(range(1,21))
for moi in no:
    print('Techcamp')


# hello 
numbers=[10,20,30,40,50]
for i in numbers:
    print('hello')


#Isayah five times in the terminal
fruits=['mango','banana','apple','lemon','casava']
for otis in fruits:
    print('Isayah') 



# print even numbers btwn 20 to 100 

lst=list(range(20,100))

for moi in lst:
    if moi%2==0:
        print(moi)


#Display odd no. btwn 30 and 100

lst=list(range(30,101))

for m in lst:
    if m%2==1:
        print(m)



 # store items in a list
  # btwn 1 to 100 display no. divisible by 3 and 5 

lst2=list(range(1,101))
issah=[]
for otis in lst2:
    if otis%3 ==0 and otis%5 ==0:
        issah.append(otis)
        
print(issah)



# how to create mpesa pin by use of loop 

lst=list(range(1,4))
attempt=3
for m in lst:
     pin=input('Enter ur pin:')
     correct_pin='1234'
     if pin==correct_pin:
         print('correct pin')
         break
     else:
         rem_att=attempt-m
         if rem_att==0:
             print('pin blocked')
         else:
             print(f'wrong pin u ve {rem_att} attempts remaining')
        






