#tkinter and func arguments

#default arguments
#*args
#**kwargs


#gui = graphical user interface

#components
#labels
my_label = tkinter.Label(text="this is my label", font=("Arial", 24, "bold")) #can't see label
my_label.pack(expand="true") #can see label expand is middle of screen

#**kw

#NOTE keyword arguments
# def my_function(a,b,c):
#     #do ths with a
#     #then do this with b
#     #finally do this with c
#my_function(1,2,3)

#NOTE arguments with default values
# def my_function(a=1, b=2, c=3):
    #do this with a
    #then do this with b
    #finally do this with c
#my_function() (no need to put 1,2,3 because already specified)
#my_function(b=5) - changes value of b and rest are same
#default values make arguments optional

#NOTE *args, many positional arguments
print("normal func")
def add(n1, n2):
    return n1 + n2
print(add(n1=5, n2=3))
print("*args func")
def add(*args): #* tells python that it can be any num of arguments
    for n in args:
        print(n)
add(3, 5, 7, 8)
 

# def calculate(**kwargs):#kwargs turns arguments to key value dictionary
#     print(kwargs) 
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#         print(kwargs["add"]) #gives value from key
def calculate(n, **kwargs):#kwargs turns arguments to key value dictionary
    print(kwargs)
    n += kwargs["add"] #2 + 3 = 5
    n *= kwargs["multiply"] #5 x 5 = 25
    print(n)

