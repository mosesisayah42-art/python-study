sentence1 ="     PYthon Programing"
# clean to "Python programing"

sentence2=sentence1.strip()
print(sentence2)
sentence3=sentence2.capitalize()
print(sentence3)

# clean to "SOFTWARE DEVELOPMENT"

sentence4="software DEVELOPMENT"

sentence5=sentence4.upper()
print(sentence5)


# clean to "computer science"
sentence6="COMputer SCIence"

sentence7=sentence6.lower()
print(sentence7)

# change to Alex Mwangi
sentence8="Alex Kimani"

sentence8=sentence8.replace('Kimani','Mwangi')
print(sentence8)

# count no of o has appered in sentence9

sentence9="Python programing"
sentence9=sentence9.count('o')

print(sentence9)


# split sentence 10 using colon 

sentence10="Alex:Brian:mike:Kevin"
sentence11=sentence10.split(':')

print(sentence11)


# name = “  JOHn  .“ to “john”
name="  JoHn "
name=name.strip()
name=name.lower()

print(name)

sentence_one = 'The Dog Breed is German Shepherd” only display “Breed is German'
sentence_one ='The Dog Breed is German Shepherd'
sentence_one=(sentence_one[8:23])

print(sentence_one)

sentence_two = 'Defeats for the Clinton forces, this was her moment of triumph” only display ''Clinton forces'

sentence_two = 'Defeats for the Clinton forces, this was her moment of triumph'
print(sentence_two[16:30])

# Split the below sentence using a semicolon i.e ; And display length of the result. 

text='The lazy dog; ran so fast; it hit the wall.'
text=text.split(';')
print(text)
print(len(text))

# first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="Joh.n" 
last_name="Do,e"

first_name=first_name.replace('Joh.n','John')
last_name=last_name.replace('Do,e','Doe')

full=first_name+" "+last_name
print(full)

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC

r = '["E","W","C"]'
r=r.replace('["E","W","C"]','EWC')
print(r)