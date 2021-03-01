class person:
 
    def Hello(self, name=None, age=None):
 
        if name is not None and age is None:
            print ('Hello ' + name)
        elif name is not None and age is not None:
            print ('Hello '+ name + 'your age='+ str(age))
        else:
            print ('hello')
obj=person()
obj.Hello()
obj.Hello('akshay')
obj.Hello('akshay',21)