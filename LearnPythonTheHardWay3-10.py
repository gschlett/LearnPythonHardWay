#### Learn Python the Hard Way Exercises 3-10 ####


### Exercise 3 Numbers and Math ###

print(3 * 8)

print(10 % 4)

print(100 % 6)


# Greater than or equal to, evaluates to True #
print(5 >= -2)

# Less than or equal to, evaluates to False #
print(5 <= -2)

### Exercise 4 Variables and Names ###

cars = 100

space_in_car = 4.0

drivers = 30

passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers


### Exercise 5 More Variables and Printing ###
my_name = 'Gunther Schletter'

my_age = 24

my_height = 71 # Inches

my_weight = 185 # Pounds

my_eyes = 'Blue'

my_teeth = 'White'

my_hair = 'Dirty Blonde'

print("Let's talk about %s." % my_name) # I think %s is to do variable that has string value # 

print("He's %d inches tall." % my_height) # I think %d is to do variable that has integer value #

print("He's %d pounds heavy." % my_weight)

print("Actually that's not too heavy.")

print("He's got %s eyes and %s hair." % (my_eyes, my_hair))

print("His teeth are usually %s depending on the coffee." % my_teeth)

print("If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight))


### Exercise 6 Strings and Text ###

# %r or s or whatever means formatter, takes what's on the right and put it in the to replace the %  #
# value on the left #
# Converting 
x = 'There are %d types of people.' % 10

binary = 'binary'

do_not = "don't"

y = 'Those who know %s and those who %s' % (binary, do_not)

print(x)

print(y)

print("I said: %r." % x)

print("I also said: '%s." % y)

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r" # Putting %r in a variable #

print(joke_evaluation % hilarious) # putting variable in a function #

w = "This is the left side of..."

e = "a string with a right side."

print(w + e)
# The difference between %r and %s is that r is best for debugging since it displays raw data of variable #
  


### Exercise 7 More Printing ###

print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

print(end1 + end2 + end3 + end4 + end5 + end6,
      end7 + end8 + end9 + end10 + end11 + end12)


### Exercise 8 Printing, Printing ###

formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))

print(formatter % ('one', 'two', 'three', 'four'))

print(formatter % (True, False, False, True))

print(formatter % (formatter, formatter, formatter, formatter))

print(formatter % ("I had this thing.",
                   "That you could type up right",
                   "But it didn't sing",
                   "so I said goodnight"
                   ))

### Exercise 9 Printing, Printing, Printing ### 

days = "Mon Tue Wed Thu Fri Sat Sun"

# \n means new line #
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print("Here are the days:", days)

print("Here are the months: ", months)

print("""

There's something going on here. 
With three double quotes.
We can type as much as we want
A hundred lines
even an apostraphe'
As many lines as we want 5 or 6'

""")

### Exercise 10 What Was That? ###
# Escape characters in strings #

print("I am 6'2\" tall ") # Escaping a double quote by putting backslash before it 

tabby_cat = "\tI'm tabbed in" # \t tabs in #

persian_cat = "I'm split\non a line" # \n put contents of string on two separate lines #

backslash_cat = "I'm \\ a \\ cat" # If you need a slash in a string just do two slashes \\ outputs to one slash #

fat_cat = """

I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass'
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)








                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                



