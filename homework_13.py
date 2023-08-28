def vehicle_description(*, time: int, speed: int, weight: int) -> str:
    if time < 0 or speed < 0 or weight < 0:
        raise ValueError('Error, negative values are not available')
    distans = time * speed
    return f"Транспортний засіб вагою {weight} кг " \
           f"рухався {time} секунд зі швидкістю {speed} м/сек, " \
           f"і подолав відстань {distans} метрів"
