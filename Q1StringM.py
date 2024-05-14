# Find String Length
print("String Length")
st = 'Hello World' 
print(len(st));print() #11

# String Index
print("String Index")
st = "Hello World! Hello Hello" 
print(st.index('Hello')) #0
st2 = "This is a sample is sentence"
st1 = st2.index('is',14,20) 
print(st1);print()

# String Strip
print("String Strip")
st = '       Hello World!   ' 
print(st)
print(st.strip());print()  #Hello World!

# String Lstrip
print("String Lstrip")
st = '      Hello World!   ' 
print(st)
print(st.lstrip());print()  #Hello World!   

# String Rstrip   
print("String Rstrip")
st = '       Hello World!   ' 
print(st)
print(st.rstrip());print()  #Hello World!

# String Split
print("String Split")
st = 'India is a Great Country'  
print(st.split());print()

# String Join
print("String Join")
st1 = 'HelloWorld!'
st2 = '-' 
print(st2.join(st1));print()

# String Find
print("String Find")
st = 'Hello World! Hello Hello' 
print(st.find('Hello',10,20)) #13 
print(st.find('Hello',15,25)) #19 
print(st.find('Hello')) #0 
print(st.find('Hee'));print() #-1

# String Upper
print("String Upper")
st = 'hello WORLD!' 
print(st.upper());print() #'HELLO WORLD!'

# Stirng Lower
print("String Lower")
st = 'hello WORLD!' 
print(st.lower());print() #'hello world!' 

# String Starts with
print("String Startswith")
st = 'Hello World!' 
if(st.startswith('He')):
    print("True")
else:
    print("False") # True
if(st.startswith('Hee')):
    print("True")
else:
    print("False") # False
print()

# String Ends with
print("String Endswith")
st = 'Hello World!' 
if(st.endswith('World!')):
    print("True") 
else:
    print("False") # True
if(st.endswith('!')):
    print("True")
else:
    print("False") # False
print()

# String Count
print("String Count")
st = 'Hello World! Hello Hello'
print(st.count('Hello',12,25)) #2 
print(st.count('Hello'));print() #3 

# String Concatenation
print("String Concatenation")
st="Hello"
st2=" World"
print(st+st2)