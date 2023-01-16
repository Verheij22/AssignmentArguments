# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#part 1 Greet template
def greet (name = 'dibbes', template = "Hello, <name>!"):
    return template.replace('<name>', name)


#part 2 Force
def force (mass = 0.0, body = 'earth'):         #surface gravity of planets & the sun
        planet = {
            'sun': 274,
            'jupiter': 24.9,
            'neptune': 11.2,
            'saturn': 10.4,
            'earth': 9.8,
            'uranus': 8.9,
            'venus': 8.9,
            'mars': 3.7,
            'mercury': 3.7,
            'moon': 1.6,
            'pluto': 0.6 
        }
        return round(mass*planet[body],1)


#part 3 
def pull (m1, m2, d):
    G = 6.674 * (10 ** -11)         #this is the gravitational constant
    return G * ((m1 * m2) / (d ** 2))         #this is the gravitational pull 
    
    
print (greet("Marcel", "What's up, <name>!"))
print (greet("Marcel"))
print (greet())

print (pull(0.1, 5.972 * 10 ** 24, 6371))           #https://www.mathsisfun.com/physics/gravity.html