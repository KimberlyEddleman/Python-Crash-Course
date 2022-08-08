#4-1 Pizza loop
pizza_flavors=["cheese","hawaiian","margartia"]
for pizza in pizza_flavors:
    print(f"I love {pizza} pizza")
print("Pizza is so yummy!")

#4-2 Animal Loop
animal_list=["squirrel","cat","hamster"]
for animal in animal_list:
    print(f"A {animal} is furry and cute")
print("I like these animals!")

# 4-3 For loop print 1 to 20 inclusive
number_list=list(range(1,21))
for number in number_list:
    print(number)


#4-4 One million
#not doing a million numbers


#4-5 Make a list from one to one million and use sum, max and min
mil_list=list(range(1,1000001))
print(sum(mil_list))
print(max(mil_list))
print(min(mil_list))

#4-6 Make list of odd numbers
odd_list=list(range(1,20,2))
print(odd_list)

#4-7 Make list of multiples of 3
three_list=list(range(3,31,3))
print(three_list)
for three in three_list:
    print(three)

#4-8 Cubes make list of first 10 cubes
cube_list=[]
for cube in range(1,11):
    cube_list.append(cube**3)
print(cube_list)

#4-9 Make list of cubes using list comprehension
cube_list2=[value**3 for value in range(1,11)]
print(cube_list2)

#4-10 Slices, get first 3 entries in list and print them, get middle 3 items and get last 3 items
easy_list=["item 1","item 2","item 3","item 4","item 5","item 6"]
first_list=easy_list[:4]
middle_list=easy_list[2:5]
end_list=easy_list[-3:]
print(first_list)
print(middle_list)
print(end_list)

#4-11 pizza and friend pizza, make copy of pizza list for friend and add different elements to it
friend_pizza=pizza_flavors[:]
friend_pizza.append("pepperoni")
pizza_flavors.append("double cheese")
print(friend_pizza)
print(pizza_flavors)

#4-13 Buffet
buffet_menu=("pizza","salad","soup","tomato","cheese")
for item in buffet_menu:
    print(item)
buffet_menu=("cheeseburger","taco","soup","tomato","cheese")
print(buffet_menu)