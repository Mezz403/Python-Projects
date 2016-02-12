cars = 100 # Assign cars a value of 100
space_in_a_car = 4.0 # Assign space in a car as floating point 4.0 for accuracy in later mathematical operations
drivers = 30 # Assign drivers a value of 30 
passengers = 90 # Assign passengers a value of 90
cars_not_driven = cars - drivers # Assign cars not driven as the difference between cars and drivers
cars_driven = drivers # Assign cars driven as the same amount of drivers
carpool_capacity = cars_driven * space_in_a_car # Assign carpool capacity as the number of cars driven times the amount of space in a car
average_passengers_per_car = passengers / cars_driven # Assign the average passengers per car as the number of passengers divided by the number of cars driven

print "There are", cars, "cars available." # There are 100 cars available.
print "There are only", drivers ,"drivers available." # There are only 30 drivers available.
print "There will be", cars_not_driven, "empty cars today." # There will be 70 empty cars today.
print "We can transport", carpool_capacity, "people today." # We can transport 120.0 people today.
print "We have", passengers, "to carpool today." # We have 90 passengers to carpool today.
print "We need to put about", average_passengers_per_car, "in each car." # We need to put about 3 in each car.