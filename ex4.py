# There are 100 cars
cars = 100
# There are 4 spaces in the car
space_in_a_car = 4.0
# There are 30 drivers
drivers = 30
# There are 90 pasengers
passengers = 90
# The cars not driven are the cars subtracted by the number of drivers
cars_not_driven = cars - drivers
# The cars driven are equal to the number of drivers
cars_driven = drivers
# The capacity of the cars is the number of cars being driven multiplied by the number of spaces in each car
carpool_capacity = cars_driven * space_in_a_car
# The average passenger per car is the number of passengers divided by the number of cars
average_passengers_per_car = passengers / cars_driven

# Print the number of cars available
print "There are", cars, "cars available."
# Print the number of drivers available
print "There are only", drivers, "drivers available."
# Print the number of empty cars
print "There will be", cars_not_driven, "empty cars today."
# Print the capacity of all the cars that can be driven
print "We can transport", carpool_capacity, "people today."
# Print the number of passengers
print "We have", passengers, "to carpool today."
# Print the avergage passenger per car
print "We need to put about", average_passengers_per_car, "in each car."