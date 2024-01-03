#Storing Object in a list

class Movie(object):
    def __init__(self,title,mins,hero):
        self.title = title
        self.mins = mins
        self.hero = hero
    
    def printer(self):
        print(f"Movie Title: {self.title}, with length : {self.mins}mins. and starring {self.hero}\n")
        
list_of_movies = []

while True:
    title,mins,hero = input('Title:'),int(input('Length(in mins.):')),input("Starring: ")
    obj = Movie(title,mins,hero)
    list_of_movies.append(obj)
    print("Movie added to the list")
    ans =input("Any other movie to add?\n")   
    if ans != "Yes":
        break

print("All movie info.")

for obj in list_of_movies:
    obj.printer()