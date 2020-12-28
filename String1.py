#basic assignment of strings and rules to follow
a='Hi,I am Dhanush .'
b="What is  your name ?"
c=""" From where did you come? """
print(a)
print(b)
print(c)
print(len(a))
print(len(b))
print(len(c))
#a='hey,he's dhanush'
#b=""What is your name? ,Sam Said"
#(These two statements  gives you error because they have specific
# meaning in python ).If you want to use these character 
#  in your sentence then you need to keep \
a='I wasn\'t there' 
b="\"She was not a criminal\",He said"
print(a)
print(b)
#String manuplilation functons in python
#to find length we use len()
print(len(a))
print(len(b))
#To concatinate two strings we use + operator
d='dhanush '
e='Hamsraj'
f=d+e
print(f)
#if you want to print it for 10 times then
print(d*10)
#If you want print in same line
print(a+str(len(a)))
print(a.count("I"))