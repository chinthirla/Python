import os
files=["empdetails.txt",'custdata.docx','productsdata.csv','salesdetails.txt']
for i in files:
    print(os.path.join("C:\\Users\\Narayana\\AppData\\Local\\Programs\\Python\\Python36-32",i))
