#                   1
#         012345678901234

parrot = "Norwegian Blue"

print ( parrot )

print ( )

print ( parrot [ 3 ] )
print ( parrot [ 4 ] )
print ( parrot [ 9 ] )
print ( parrot [ 3 ] )
print ( parrot [ 6 ] )
print ( parrot [ 8 ] ) 

print ( )

print ( parrot [ -11 ] )
print ( parrot [ -10 ] )
print ( parrot [ -5 ] )
print ( parrot [ -11 ] )
print ( parrot [ -8 ] )
print ( parrot [ -6 ] ) 

print ( )

print ( parrot [ 3 - 14 ] )
print ( parrot [ 4 - 14 ] )
print ( parrot [ 9 - 14 ] )
print ( parrot [ 3 - 14 ] )
print ( parrot [ 6 - 14 ] )
print ( parrot [ 8 - 14 ] ) 

print ( )

print ( parrot [ 0 : 6 ] ) # Norweg
print ( parrot [ 3 : 5 ] ) # we
print ( parrot [ 0 : 9 ] ) # Norwegian
print ( parrot [ : 9 ] ) # Norwegian

print ( )

print ( parrot [ 10 : 14 ] ) # Blue
print ( parrot [ 10 : ] ) # Blue

print ( )

print ( parrot [ : 6 ] ) # Norweg
print ( parrot [ 6 : ] ) # ian Blue

print ( )

print ( parrot [ : 6 ] + parrot [ 6 : ] ) # Norwegian Blue
print ( parrot [ : ] ) # Norwegian Blue

print ( )

print ( parrot [ -14 : -8 ] ) #Norweg
print ( parrot [ -4 : -2 ] ) # Bl
print ( parrot [ -4 : 12 ] ) # Bl

print ( )

print ( parrot [ 0 : 6 : 2 ] )
print ( parrot [ 0 : 6 : 3 ] )

print ( )

number = "9,223;372:036 854,775;807"
separators = number [ 1 : : 4 ]
print ( separators )

print ( )

values = "" . join ( char if char not in separators else " "  for char in number ) . split ( )
print ( [ int ( val ) for val in values ] )