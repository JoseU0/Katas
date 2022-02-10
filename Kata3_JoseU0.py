# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

""" asteroide = 49
if asteroide > 25:
    print(' Advertencia. Un asteroide se acerca!')
else:
    print('Velocidad del Asteroide baja') """

""" asteroide = 19
if asteroide > 20:
    print('Hay un asteroide en el cielo')
elif asteroide == 20:
    print('Hay un asteroide en el cielo')
else:
    print('Buena noche') """

vel_ast = 25
size_ast = 40
if vel_ast > 25 and size_ast > 25:
    print('Advertencia! Un asteroide peligroso se acerca!')
elif vel_ast >= 20:
    print('Hay un asteroide en el cielo')
elif size_ast < 25:
    print('Buena noche')
else:
    print('Buena noche')