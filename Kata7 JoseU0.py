
planets= []
new_planet = ''
user_input = ''

while user_input.lower() != 'done':
    if user_input:
        # Almacenamos ese valor en la lista
        planets.append(user_input)
    # Capturamos un nuevo valor
    user_input = input('Enter a new planet, or done when done: ')

print (planets)

for planet in planets:
    print (planet + ' :D ')