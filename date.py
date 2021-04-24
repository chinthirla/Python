import datetime
my_date=datetime.datetime(2021,10,16,23,20,44)
sen="{:%B %d,%Y}".format(my_date)
print(sen)
print("{0:%B %d, %Y} fell on {0:%A} and {0:%w} day of this week and {0:%d} day of this month and {0:%j} day of the year".format(my_date))
def method(c,b=10,*a):
    print(c)
    print()
    print(b)
    print(a)
method(1,4,'py')
