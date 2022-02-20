def report(pre_launchtime, flight_time, destination, external_tank, main_tank):
    return f'''
    Mission to {destination}
    Total travel time: {pre_launchtime + flight_time} minutes
    Total fuel left: {external_tank + main_tank} gallons
    '''
print(report(50, 100, "Moon", 5669, 8999))