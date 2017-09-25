class city:

    def __init__(self, index):
        self.index = index
        self.road_dests = []


def solve(cities, cost_road, cost_lib):
    lowest_price = len(cities)*cost_lib
    if cost_road >= cost_lib:
        return len(cities)*cost_lib

    # DFS
    current_city = cities[0]
    explored_cities = set([current_city])

    # TODO - keep track of total number of roads travelled, to minimize
    #      - keep lowest around, cut off other explorations
    #      - deal with regions cut off from each other


def explore(city, explored_cities):
    for next_city in city.road_dests:
        if next_city not in explored_cities:
            explored_cities.add(next_city)
            explore(next_city, explored_cities)
            explored_cities.remove(next_city)
