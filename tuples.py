fruits=("mango","banana","apple","pine apple","water melon")

print(type(fruits))
print(fruits[2])
print(fruits[2:])

# change to list 
# List()

fruits=list(fruits)
fruits.append('lemon')
print(fruits)
fruits.insert(2,'Avacado')
print(fruits)

# convert back to tuple
# tuple()

fruits=tuple(fruits)
print(fruits)







