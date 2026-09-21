fruits=["mango","banana","apple","pine apple","water melon"]
print(fruits)
print(type(fruits))

# indexing and slicing
print(fruits[2])
print(fruits[-2])

# slice> extracting part of a list
# [start-index : end-index ]
print(fruits[1:4])
print(fruits[2:5])

# displa day of the week
# display today
# display tuesday to friday

days=["sun","mon","tue","wed","thur","fri","sato"]
print(days[2])
print(days[2:-2])

days.append('january')
days.insert(4,'december')
days[4]=("thursday")
print(days)

days.remove('january')
print(days)
days.remove('fri')
print(days)
days.remove('sun')
print(days)
days.clear()
print(days)