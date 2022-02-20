# Datos con los que vas a trabajar
from turtle import heading
from matplotlib.pyplot import title


# name = "Moon"
# gravity = 0.00162 # in kms
# planet = "Earth"

planet = 'Marte '
gravity  = 0.00143
name = 'Ganímedes'

# Creamos el título
heading = """ %s facts about %s.""" % ('gravity',planet)
print(heading.title(), '\n',"-" * 80)
gravity_m= gravity*1000
print("Gravity on %s :" % planet, str(gravity_m) + ' m/s2')