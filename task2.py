def update_car_info(**kwargs):
    car = kwargs

    car['is_available'] = True

    return car


result = update_car_info(brand='Toyota', price=30000)

print(result)
