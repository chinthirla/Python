persons={'name':'Sai', "Age":28}
#Tradional way of using keys in the sentence
print( "My name is " +persons['name']+ " and i am "+str(persons['Age'])+" years old") 
print( "My name is " ,persons['name'], " and i am ",str(persons['Age']), " years old")
#by using format function also we can use value with corresponding keys in the sentece
print("My name is {} and i am {} years old".format(persons['name'],persons['Age'])) 
print("My name is {0} and i am {1} years old".format(persons['name'],persons['Age'])) 
print("My name is {0[name]} and i am {1[Age]} years old".format(persons,persons)) 
print("My name is {0[name]} and i am {0[Age]} years old".format(persons))
for i in range(1,191): 
    msg="The current value is {} ".format(i) 
    print(msg)
