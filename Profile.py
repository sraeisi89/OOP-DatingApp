import datetime

class Profile:
    id = 0

    def __init__(self, gender, age, looking_for):
        self.age = age
        self.gender = gender
        self.looking_for = looking_for
        Profile.id += 1
        self.id = Profile.id
        self.liked_list = []
        self.last_liked_date = datetime.datetime.now()
        self.now = datetime.datetime.now()
        self.likes_limit = 1

    def check_is_match(self, profile):
        for i in profile.liked_list:
            if self.id == i.id:
                return True
        return False

    def like_own_profile(self, profile):
        if profile.id == self.id:
            return True

    def same_profile_twice(self, profile):
        for p in self.liked_list:
            if p.id == profile.id:
                return True

    def time_limit(self, profile):
        likes = len(self.liked_list)
        date_diff = (self.now - self.last_liked_date).days
        if date_diff < 1 and likes >= self.likes_limit:
            return True

    def likes(self, profile):
        if self.like_own_profile(profile):
            print("You can't like your own profile.")
            return

        if self.same_profile_twice(profile):
            print("You already liked this profile.")
            return

        if self.time_limit(profile):
            print("You can't like more, you've reached your like limit.")
            return

        if self.check_is_match(profile):
            print("It's a match!")

        self.liked_list.append(profile)
        self.last_liked_date = self.now




class FreeProfile(Profile):
    def __init__(self, gender, age, looking_for):
        super().__init__(gender, age, looking_for)

    def __str__(self):
        return f"{self.age} year old {self.gender}, looking for a {self.looking_for}. (id: {self.id})"

    def send_message(self, profile, text):
        print(f"Unable to send message, upgrade your profile to Pro.")


class ProProfile(Profile):
    def __init__(self, name, gender, age, looking_for):
        super().__init__(gender, age, looking_for)
        self.name = name
        self.likes_limit = 1000

    def __str__(self):
       return f"{self.name} is a {self.age} year old {self.gender}, looking for a {self.looking_for}. (id: {self.id})"

    def send_message(self, profile, text):
        print(f"Message is sent to profile #{profile.id}.")




