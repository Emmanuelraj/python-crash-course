def fun():
    print('Run')

fun()

#params
def func(x,y):
    print(x,y)

func(1,2)

# return func

def listFun(x,y):
    return x*y;

print(listFun(8,2))


#Global and local scope
name = 'Tim';

def func(name):
    name ='Tech'

print(name); # print Global

x= 'name'
# but you change local into global

def funclocalintoglobal(name):
    global x 
    x= 'localbecomesglobal'
    return x 


print(funclocalintoglobal(x))





