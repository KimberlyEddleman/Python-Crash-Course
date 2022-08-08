#append puts element at end of list
#insert(location,name) inserts an element at a specific index

#del permanatly removes an item with a given index del list[0]
#.pop removes the last element of the list
#remove removes an element by name, only removes the first instance of it though
# 3-1 Names
#Store names of friends in a list called names
names=["Steven","Joyce","Becca"]
print(names)
print(names[0])
print(names[1])
print(names[2])

#3-2 Greetings
#print a message to each friend in the list
print(f"I love {names[0]}")
print(f"Hello {names[1]}")
print(f"Hi {names[2]}")

#3-3 Your Own List
#make list of transportations
transport=["car","bike","walking"]
print(f"I use my {transport[0]} to drive")

#3-4 Guest list
guest_list=["Steven","Mom","Dad"]
print(f"Welcome to the party, {guest_list[0]}")


#3-5 Changing guest list
print(f"Oh no, {guest_list[1]} can't make it!")
guest_list[1]="Kathleen"
print(f"Yay, {guest_list[1]} can come instead")

#3-6 More Guests
print("I found a bigger table!")
guest_list.insert(0,"Becca")
guest_list.insert(2,"Joyce")
guest_list.append("David")
for guest in guest_list:
    print(f"Welcome {guest}")

#3-7 Shrinking Guest List
print("Oh no! My table won't arrive in time :(")
num_list=range(0,len(guest_list)-2)
print(num_list)
print(guest_list)
for person in enumerate(num_list):
    person_val=guest_list.pop()
    print(f"Sorry {person_val} you can't sit with us")

print(guest_list)
del guest_list[0]
del guest_list[0]

print(guest_list)

#sort permanatly sorts list
#sorted temporarily sorts the list
#reverse to reverse order of a list
#len finds length of a list


#3-8 Seeing the world
location_list=["Spain","Italy","Iceland","Switzerland","Portugal"]
print(location_list)
print(sorted(location_list))
print(location_list)
print(sorted(location_list,reverse=True))
print(location_list)
location_list.reverse()
print(location_list)
location_list.reverse()
print(location_list)
location_list.sort()
print(location_list)
location_list.sort(reverse=True)
print(location_list)

#3-9 Dinner Guests
guest_list=["Steven","Kathleen","David"]
print(f"I am having {len(guest_list)} people for dinner")

