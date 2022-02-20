# Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!

# Calcular la distancia entre planetas
# Dos distancias de planetas: Tierra (149.597.870 km) y Júpiter (778.547.200 km).

dist_earth= 149597870
dist_jupiter=778547200
diff_distances_km= (dist_jupiter-dist_earth)
diff_distances_mi= (dist_jupiter-dist_earth)*0.621
print(diff_distances_mi)

# Almacenar las entradas del usuario
distancia_1 = input("¿Cuál es la primera distancia? ")
distancia_2 = input("\n¿Cuál es la segunda distancia? ")

delta_dist= abs(int(distancia_1)-int(distancia_2))
print("La distancia al Sol es de ", str(delta_dist) + ' km ')
print("\nLa distancia al Sol es de ", str(delta_dist*.621) + ' mi ')