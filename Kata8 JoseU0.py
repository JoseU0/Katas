# demo = {
#     'key': 'value',
#     'number': 42
# } 
# name: Mars
# moons: 2

from unicodedata import name


planet = {
        'name' : 'Mars',
        'moons': '2'

}

print(planet.get('name'), 'has %s moons' % planet.get('moons'))

# Agrega un nuevo valor con una clave de 'circunferencia (km)'. Este nuevo valor debería almacenar un diccionario con las dos circunferencias del planeta:
# polar: 6752
# equatorial: 6792
planet['circunference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(planet.get('name'), 'has a circunference of %s ' % planet['circunference (km)']['polar'])
