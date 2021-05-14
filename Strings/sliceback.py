letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters [ : : -1 ]
print ( backwards )

# Slice the string 'letters' to produce the letters 'qpo'
qpo = letters [ 16 : 13 : -1 ]
print ( qpo )

# Slice the string 'letters' to produce the letters edcba
edcba = letters [ 4 : 0 : -1 ]
print ( edcba )

# Slice the string 'letters' to produce the last 8 letters
last8 = letters [ 25 : -9 : -1 ]
# Can also do last8 = letters [ -9 : -1 ]
print ( last8 )

print ( letters [ -4 : ] )
print ( letters [ -1 : ] )
print ( letters [ : 1 ] )
print ( letters [ 0 : ] )

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])