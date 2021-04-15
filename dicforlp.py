emps = {1001: {'name': 'Narayana', 'age': '27', 'sex': 'Male','loc':"Hyderabad"}, 1002: {'name': 'Veni', 'age': '25', 'sex': 'Female','loc':"Hyderabad"}, 1003: {'name': 'Sivani', 'age': '24', 'sex': 'Female','loc':"Bangalore"}, 1004: {'name': 'Nagaraju', 'age': '29', 'sex': 'Male',"loc":"Chennai"}}
#for i in emps:
for empid,empinfo in emps.items():
    print("Emp id :",empid)
for key in empinfo: 
    print(key +':',empinfo[key])

