# En primer lugar, crea una variable denominada `planets`. Agrega los ocho planetas (sin Plutón) a la lista. A continuación, muestra el número de planetas.

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# print (planets[2])
planets.append('Pluto')
print(planets[-1])

usr_planet = input("Diga un planeta de favor con la primera leta mayúscula: ")

usr_planet_index = planets.index(usr_planet)

# print(usr_planet_index)

# Muestra los planetas más cercanos al sol
print('Planetas más cercanos al sol ' + usr_planet)
print(planets[0:usr_planet_index])

# Muestra los planetas más lejanos al sol
print('Planetas más lejanos al sol ' + usr_planet)
print(planets[usr_planet_index + 1:])