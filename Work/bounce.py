# bounce.py
#
# Exercise 1.5
height = 100

bounces = 1


while bounces < 11:
    
    height = round( height /5 *3, 4) 
    print( bounces, height)
    bounces = bounces + 1

