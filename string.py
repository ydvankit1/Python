# str= '''
# Hi 
# My name is Ankit yadav
# I am Learning Python
# Bye
# '''
# print (str);  // no need to use \n for the new line in case of triple quotes


# str='Hello World';
# for ch in str:
#     print(ch);



# print('Hello World'[8])  // r


# string slicing

# str= "Hello";
# print(str[1]);   // e

# print(str[-2]);   //l = second last charachter)

# print(str[:-3]);   // He  == ((len=5)-3)=2 (CHAR 0 TO 1)

# print(str[-4:-1]); // ell  == ((len=5)-4)=1 (CHAR 1 TO 3)

# print(str[:3]);   // Hel
# print(str[1:]);   // ello
# print(str[2:4]);  // ll
# print(str[::]);   // hello
# print(str[::2]);  // hlo
# print(str[::-1]);   //olleH


# letter = 'z';
# print(letter*10);  // zzzzzzzzzz

# str= "ank yad";      // strings are immutable it create new string when we perform any operation

# print(str.upper());  // ANK YAD
# print(str.lower());  // ank yad

# print(str.find('y'));  // 4   and if not found return -1
# print(str.find('ad')) // 5  // first charachter index  that is a of word ad
# index method similar to find method but if not found it will give error that is value error substring not found

# print(str.count('a'));  // 2

# print(str.startswith('a')); // true
# print(str.endswith('d'));  // true
# print(str.endswith("ad", 4,6));  // true

# str = "ankit!!!!"

# rstrip  (removes the trailing charachter and doesnot remove trailing spaces)
# print(str.strip('!'));   // ankit

# replace  (replace all occurences of that word or charachter)
# print (str.replace('ankit', "yadav"));   // yadav!!!!

# str = "ankit !!!!"

# split (divide  the string into list of words)
#print(str.split(""));  // ["ankit", "!!!!"]

# str= "ank yad";
# print(str.split('a'));  // ['', 'nk y', 'd']


# capitalize  (first charachter of string)

# str = "ankit yadav"
# print(str.capitalize());  // Ankit yadav

# isalpha() (check if all charachters are alphabet or not)
# isalnum() (check if all charachters are alphabet or number or not)
# isdigit() (check if all charachters are digit or not)
# isspace()  (return if their is whitespace)
#  islower() (chaeck if all charachter in lower case or not)
# isupper() (chaeck if all charachter in upper case or not)


# print(len('hello'));    // 5


# string formatting

# letter ='Hey my name is {1} and I belongs from {0}';
# country="India";
# name="ankit";

# print(letter.format(country,name));

# using fstring

# print(f"hey my name is {name} and I belongs from {country}");    # for up to 2 decimal place - {price:.2f}
# to retain f string in output that is to not get replaced with variable :  {{name}} => {name}

# Docstring

# def square(n):
#     '''
#     Takes number n, return the square of n  // always written before print statement in function body
#     '''
#     print(n**2);
# square(5);
# print(square.__doc__); // print the docstring







