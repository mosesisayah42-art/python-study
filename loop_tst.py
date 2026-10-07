# display 1 to 50
lst1=list(range(1,51))
for moi in lst1:
    print(moi)


#display no. divisible by 7 nd 5 in no. 1 above

lst1=list(range(1,51))
for moi in lst1:
    if moi % 7==0 and moi % 5==0:
        print(moi)


#tsk 4 put the first 10 odds btwn 10 nd 50
 
count=0

for moi in range(10,51):
    if moi % 2==1:
        print(moi)
        count +=1

        if count==10:
            break



# 


list=list(range(1,5))
attempts=4

for moi in list:
    email=input('enter your email:')
    correct_email='admin@123'
    if email==correct_email:
        print('access granted')
        break
    else:
        rem_trials=attempts-moi
        if rem_trials==0:
            print('BLOCKED')
        else:
            print(f'{rem_trials} attempts remaining')


