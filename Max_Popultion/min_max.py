countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
population = [17_500_000, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]

res = []
for country in zip(countries, population):
    res.append(country)

max_population = max(res, key=lambda x: x[1])

print(max_population)