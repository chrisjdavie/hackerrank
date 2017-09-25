from roads_and_libraries.solve import city, solve

q = int(input())

for _ in range(q):
    n, m, cost_lib, cost_road = map(int, input().split())
    cities = []
    for i in range(n):
        cities.append(city(i))    

    for _ in range(m):
        city_1, city_2 = map(int, input().split())
        cities[city_1-1].road_dests.append(cities[city_2-1])
        cities[city_2-1].road_dests.append(cities[city_1-1])

    solve(cities, cost_road, cost_lib)
