print( "The Love Calculator is calculating your score..." )
name1 = input("Enter your name and surname ")  
name2 = input("Enter your loves name ")  

combined = name1 + name2
lower_names = combined.lower()

t = lower_names.count( "t" )
r = lower_names.count( "r" )
u = lower_names.count( "u" )
e = lower_names.count( "e" )

l = lower_names.count( "l" )
o = lower_names.count( "o" )
v = lower_names.count( "v" )
e = lower_names.count( "e" )

calculation1 = t + r + u + e
calculation2 = l + o + v + e
calculation_str = str( calculation1 ) + str( calculation2 )
calculation3 = int( calculation_str )

if calculation3 < 10 and calculation3 > 90:
    print( f"Your score is {calculation3}, you go together like coke and mentos." )

elif calculation3 > 40 and calculation3 < 50:
    print( f"Your score is {calculation3}, you are alright together." )
else:
    print( f"Your score is {calculation3}, you go together like coke and mentos." )



