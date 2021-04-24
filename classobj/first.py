class myclass:
    var="Pyhton"
    def function(self):
        print("Pyhton is simple")
objname1=myclass()
objname2=myclass()
objname2.var='Developer'
objname1.function()
print(myclass.__doc__)
print(objname1.var)
print(objname2.var)
  
