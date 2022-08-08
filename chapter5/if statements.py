#5-1/5-2 conditional tests
animal="cat"
print("Is animal == 'cat?' I predict TRUE")
print(animal=="cat")
print("Is animal == 'dog'? I predict FALSE")
print(animal=="dog")
list_animals=["cat","dog","fish"]
print("cat" in list_animals)
print("dog" not in list_animals)
print(4<=5)
print("DOG".lower()=="dog")
print(4==5 or 4==4)
print(4==5 and 4==4)

#5-3 Alien colors
alien_color="green"
if alien_color=="green":
    print("You get 5 points!")
print("V2")
alien_color="yellow"
if alien_color=="green":
    print("You get 5 points!")

#5-4 Alien Colors #2
alien_color="yellow"
if alien_color=="green":
    print("You get 5 points!")
else:
    print("You get 10 points!")

#5-5 Alien colors #3
alien_color="red"
if alien_color=="green":
    print("You get 5 points!")
elif alien_color=="yellow":
    print("You get 10 points!")
elif alien_color=="red":
    print("You get 15 points!")

#5-6 stages of life
age=64
if age<2:
    print("baby")
elif age<4:
    print("toddler")
elif age<13:
    print("kid")
elif age<20:
    print("teen")
elif age<65:
    print("adult")
else:
    print("elder")

#5-7 favorite fruit
fruit_list=["apple","strawberry","pear"]
if("kiwi" in fruit_list):
    print("I like kiwi!")
if("apple" in fruit_list):
    print("I like apple!")


#In python if you do if with a list, it returns true if there is at least one item in the list and false if the list is empty


#5-8 Hello Admin
user_list=["kimberly","steven","mom","dad","admin","becca"]
for user in user_list:
    if user=="admin":
        print("Hellow admin, would you like to see the user data?")
    else:
        print(f"Hello {user}, how are you today?")


#5-9 Check for empty list
user_list=["kimberly","steven","mom","dad","admin","becca"]
user_list=[]
if user_list:
    for user in user_list:
        if user=="admin":
            print("Hellow admin, would you like to see the user data?")
        else:
            print(f"Hello {user}, how are you today?")
else:
    print("We need users, stat!")

#5-10 check usernames
user_list2=["JOHN","Kimberly","Bob"]
new_user=["John","Dan"]
user_list2_lower=user_list2[:]
user_list2_lower = [x.lower() for x in user_list2_lower]
for user in new_user:
    if user.lower() in user_list2_lower:
        print(f"{user} Username already taken")
    else:
        print(f"Adding {user}")


#5-11 ordinal numbers
numbers=list(range(1,10))
for number in numbers:
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(f"{number}th")