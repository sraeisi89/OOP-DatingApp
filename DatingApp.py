from Profile import FreeProfile
from Profile import ProProfile
import datetime

class DatingApp:
    def __init__(self, name):
        self.name = name
        self.profile_list = []

    def register(self, *profiles):
        for p in profiles:
            self.profile_list.append(p)

    def new_day(self):
        for p in self.profile_list:
            p.now += datetime.timedelta(1)

    def recommend_profiles(self, profile):
        recommendation_list = []
        for p in self.profile_list:
            if p not in profile.liked_list and profile.looking_for != p.looking_for:
                recommendation_list.append(p.id)
        return recommendation_list

    def advanced_recommend_profiles(self, profile):
        recommendation_list = []
        for p in self.profile_list:
            if profile in p.liked_list and profile.looking_for != p.looking_for:
                recommendation_list.append(p.id)
        return recommendation_list

    def who_liked_profile(self, profile):
        list = []
        for p in self.profile_list:
            if profile in p.liked_list:
                list.append(p.id)
        return list

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