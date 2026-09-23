#1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
# list()
numbers = (10, 20, 30, 40, 50)
numbers=list(numbers)
print(numbers)
numbers.append(60)
numbers[2]=35
print(numbers)
# tuple()
numbers=tuple(numbers)
print(numbers)


#2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)
values=list(values)
values.sort(reverse=True)
valuess=tuple(values)
print(values)


#3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",Remove all occurrences of "banana".
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
fruits=list(fruits)
fruits.remove('banana')
fruits.remove('banana')
fruits.remove('banana')
fruits=tuple(fruits)
print(fruits)


#4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
names = ("Alice", "Bob", "Charlie", "David")


#list()
names=list(names)
print(names)
names.sort(reverse=True)
print(names)


#5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")
x=["purple", "orange"]
colors=list(colors)
colors.insert(2,'yellow')
colors.extend(x)
print(colors)



