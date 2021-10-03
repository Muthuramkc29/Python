
# The best data structure to use here was a list because all we wanted was access of temperature elements

nyc_weather = []                             # No_need of Dictionary becuase we dont match anything here...
                                             # just need the temperature and to do so list operations here
with open("nyc_weather.txt", "r") as f:
    for line in f:
        token = line.split(',')
        temperature = int(token[1])
        nyc_weather.append(temperature)

print("1st Exercise:")
# average temperature in first week of Jan?
frst_week = nyc_weather[0:7]
avg = sum(frst_week)/len(frst_week)
# print('%.2f'%avg)
print(avg)

# maximum temperature in first 10 days of Jan
max_temp = max(nyc_weather[0:10])
print(max_temp)

# 2nd Ques...

print("2nd Exercise:")
nyc2_weather = {}
with open("nyc_weather.txt", "r") as f:
    for line in f:
        token = line.split(',')
        day = token[0]
        temperature = int(token[1])
        nyc2_weather[day] = temperature

# What was the temperature on Jan 9?
print(nyc2_weather['Jan 9'])

# What was the temperature on Jan 4?
print(nyc2_weather['Jan 4'])

# The best data structure to use here was a dictionary (internally a hash table)
#  because we wanted to know temperature for specific day, requiring key, value pair access
#  where you can look up an element by day using
#  O(1) complexity
