
from numpy import average


text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#Primero, divide el texto en cada oración para trabajar con su contenido:

text_div=text.split('. ')
""" print(text_div.split('.')) """

# Define las palabras pista: average, temperature y distance suenan bien
key_words = ["average", "temperature", "distance"]

print(key_words) 

for list in text_div:
    for word in key_words:
        if word in list:
            print(list)
            break

 # Ciclo para cambiar C a Celsius
for list in text_div:
    for word in key_words:
        if word in list:
            print(list.replace(' C', ' Celsius'))
            break