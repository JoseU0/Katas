# Función Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

# def mission_report(pre_launch_time, flight_time, destination, external_tank, main_tank):
#     return f"""
#     Mission to {destination}
#     Total travel time: {pre_launch_time + flight_time} minutes
#     Total fuel left: {external_tank + main_tank} gallons
#     """

# print(mission_report(14, 51, "Moon", 5896, 14482))

# # Escribe tu nueva función de reporte considerando lo anterior En lugar de usar *args y **kwargs *minutes y **fuel_reservoirs

# def mission_report(destination, *minutes, **fuel_reservoirs):
#     return f"""
#     Mission to {destination}
#     Total travel time: {sum(minutes)} minutes
#     Total fuel left: {sum(fuel_reservoirs.values())}
#     """

# print(mission_report("Moon", 5, 8, 27, main=5896, external_tank=14482))

# Escribe tu nueva función

def mission_report(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank {gallons} gallons left\n"
    return main_report

print(mission_report("Moon", 8, 11, 55, main=8596, external=14482))