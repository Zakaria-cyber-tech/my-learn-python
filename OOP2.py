class movies:
    def __init__(self,title,Director,release_year,genre):
        self.title=title
        self.director=Director
        self.release_year=release_year
        self.genre=genre
    def display(self):
        print("----------------------------")
        print(self.title)
        print(self.director)
        print(self.release_year)
        print(self.genre)
        print("----------------------------")
    def changing(self,new_director):
            self.director=new_director

#.......
A=movies("Dragon ball","Zakaria Al-ouardighi",2009,"Criativity")
B=movies("Naruto","Mohammed",2008,"Ninja")
C=movies("DORAYMON","japan",2014,"future")
A.display()
B.display()
C.display()




print("change is looding...")




A.changing("Sam")
B.changing("Ibrahim Aadil")
C.changing("B3a9li")
A.display()
B.display()
C.display()
