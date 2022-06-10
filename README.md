Dating app
Create a simple dating application, where people can register, they can have a Free or a Pro profile with different rights and limitations, they can like other profiles and the system can recommend other profiles.

FreeProfile
A free profile:

has an auto generated id

can be created by giving the user’s age, gender and the gender who the user is looking for

is represented in the following format: «age» year old «gender», looking for a «looking for gender». (id: «id»)

have only 1 like for a day (can like only one profile in a day). If they try to like more, they get the error: You can't like more, you've reached your like limit.

can’t like their own profile. If they try: You can't like your own profile.

can’t like the same profile twice. If they try: You already liked this profile.

can’t send a message to another profile. If they try: Unable to send message, upgrade your profile to Pro.

ProProfile
A pro profile:

has an auto generated id

can be created by giving the user’s name, age, gender and the gender who the user is looking for

is represented in the following format: «name» is a «age» year old «gender», looking for a «looking for gender». (id: «id»)

have 1000 likes for a day. If they try to like more, they get the error: You can't like more, you've reached your like limit.

can’t like their own profile. If they try: You can't like your own profile.

can’t like the same profile twice. If they try: You already liked this profile.

can send a message to another profile by giving the other profile and a message. The message sending is a simple print operation now in the following format: Message is sent to profile #«the id of the target profile».

DatingApp
we want to create a dating application by giving its name

functionalities:

register(profile1, profile2, ...): registers the given profiles in the application

new_day(): resets the like counts of all the registered profiles

recommend_profiles(target): returns a list of profile ids that the application recommends to the target profile. A profile is recommended if the target hasn’t liked it yet and if the two persons would like each other based on their gender preferences.

who_liked_profile(profile): returns the list of profile ids, who liked the given profile.

advanced_recommend_profiles(target): returns a list of recommended profiles the same way as the recommend_profiles method, the only difference is that the advanced version sorts those profile ids first, who have already liked the target profile.

Sample code to run
Using your solution, the following code should run without errors and print the expected results.

ibsnder = DatingApp('IBSnder')
john = ProProfile('John', 'male', 30, 'female') # should have profile id 1
jane = FreeProfile('female', 28, 'male') # should have profile id 2
kate = ProProfile('Kate', 'female', 34, 'female') # should have profile id 3
jack = FreeProfile('male', 23, 'male') # should have profile id 4
jill = ProProfile('Jill', 'female', 28, 'male') # should have profile id 5
bob = ProProfile('Bob', 'male', 42, 'female') # should have profile id 6
david = FreeProfile('male', 37, 'female') # should have profile id 7
ibsnder.register(john, jane, kate, jack, jill, bob, david)
print(john) # should print: John is a 30 year old male, looking for a female. (id: 1)
print(jane) # should print: 28 year old female, looking for a male. (id: 2)
john.likes(jane)
jane.likes(john) # should print: It's a match!
jane.likes(bob) # should print: You can't like more, you've reached your like limit.
john.likes(john) # should print: You can't like your own profile.
john.likes(kate)
jill.likes(john)
david.likes(jill)
print(ibsnder.recommend_profiles(jill)) # since Jill already liked John, it should print only: [6, 7]
print(ibsnder.advanced_recommend_profiles(jill)) # since David liked Jill, it should print only: [7, 6]
print(ibsnder.who_liked_profile(john)) # should print [2, 5]
ibsnder.new_day()
jane.likes(john) # should print: You already liked this profile.
jane.likes(bob) # no error, because Jane again has a free like
john.send_message(jane, 'hello') # should print: Message is sent to profile #2.
jane.send_message(john, 'hi') # Unable to send message, upgrade your profile to Pro.
