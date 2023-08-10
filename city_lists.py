lists_city = "київ,оДеса     Львів.житоМИР,уЖгОрОд.....ХарКІВ       , слАвУтИч".replace('.', ' ').replace(',', ' ').replace('  ', '').title().split()

print_city = "Я \U00002764"

for city in lists_city:
    print(f'{print_city} {city}')
