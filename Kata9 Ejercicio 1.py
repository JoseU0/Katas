

# def report_tanks(main_tank, second_tank, third_tank):
#     total_average = (main_tank + second_tank + third_tank) / 3
#     return f"""Report:
#     Total Average: {total_average} %
#     Main tank: {main_tank} %
#     Second tank: {second_tank} %
#     Third tank: {third_tank} % 
#     """

# print(report_tanks(4,6,8))

def average(tanks_value):
    total = sum(tanks_value)
    number_of_items = len(tanks_value)
    return total / number_of_items

# Test the averaging function with a list of integers:
print(average([4, 6, 8]))

def report_tanks(main_tank, second_tank, third_tank):
    
    return f"""Report:
    Total Average: {average([main_tank,second_tank,third_tank])} %
    Main tank: {main_tank} %
    Second tank: {second_tank} %
    Third tank: {third_tank} % 
    """
print(report_tanks(4,6,8))