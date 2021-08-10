# class
# define Course class
class Course:
    # construtor
    def __init__(self, name, hrs):
        self.name = name
        self.hrs = hrs
    # method
    def display_course(self):
        print('name =',self.name)
        print('hours =',self.hrs)
        
    def show_course(self):
        return self.name

# create object
c1 = Course('Python', 18)

# call method
c1.display_course()
print('c1.show_course() =',c1.show_course())

# get data member
print('c1.name =',c1.name)
print('c1.hours =',c1.hrs)
