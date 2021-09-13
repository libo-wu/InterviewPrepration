# Metro Load Festival

# Metro Land is a country located on a 2D Plane. They are having a summer festival for everyone in the country 
# and would like to minimise the overall cost of travel for their‍‌‌‌‍‍‍‌‍‌‌‍‌‍‌‌‍‌‍‍ citizens. Costs of travel are calculated as follows:
# Determine the total cost of travel for all citizens to go to the festival at that location.

# A city is located at coordinates (x,y)
# The festival is located at coordinates (a,b)
# Cost of the travel from city to festival is |x-a|+|y-b|

# Find the optimal location of the festival is called minimum total travel cost assuming all people attend

# Example:
# numPeople=[1,2], the population of the city
# x=[1,3]
# y=[1,3]

# the minimum cost is 4

import math

def MetroLoad(numPeople, x, y):
    city_num = len(numPeople)
    result = 0
    all_x = []
    all_y = []
    for i in range(city_num):
        people_num = numPeople[i]   # population of this city
        while people_num > 0:
            all_x.append(x[i])
            all_y.append(y[i])
            people_num = people_num-1
    
    all_x.sort()
    all_y.sort()
    print(all_x)
    print(all_y)

    middle_x = all_x[math.floor(len(all_x)/2)]
    middle_y = all_y[math.floor(len(all_y)/2)]
    print("middle point is [{}, {}]".format(middle_x, middle_y))

    for i in range(city_num):
        result = result + numPeople[i] * (abs(middle_x-x[i]) + abs(middle_y-y[i]))

    return result

if __name__ == "__main__":
    numPeople=[1,2]
    x=[1,3]
    y=[1,3]
    total_cost = MetroLoad(numPeople, x, y)
    print("total cost is {}".format(total_cost))