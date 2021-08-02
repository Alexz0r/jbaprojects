duration = int(input())
total_food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

print(total_food_cost * duration + flight_cost * 2 + hotel_cost * (duration - 1))
