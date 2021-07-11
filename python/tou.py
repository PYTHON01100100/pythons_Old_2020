class student:
    def __init__(self, name, age): #2
        self.name = name
        self.age  = age
        print("-----------------------------------------------------------------------------------------------")
        print('the name is {} and the age is {}. '.format(name, age))
        print("-----------------------------------------------------------------------------------------------")
        '''
    def __init__(self):
        print('welcome')
        '''


s1 = student('ali', 22)
#s1.details('ahmed', 22)
