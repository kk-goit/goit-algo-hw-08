import heapq

def calculate_min_cost(cables):
    cost = 0
    heapq.heapify(cables)

    while len(cables) > 1:
        #take two shortest cables
        cable_1 = heapq.heappop(cables)
        cable_2 = heapq.heappop(cables)

        #connect it and update cost
        cable_3 = cable_1 + cable_2
        cost += cable_3

        #prepare to continue connecting
        heapq.heappush(cables, cable_3)
        print(f'Connected {cable_1} and {cable_2}, total cost is: {cost}')

    return cost

for cables in [[15], [4, 4], [15, 4, 4, 2, 1], [7, 15, 4, 4, 2, 1]]:
    print(f'Minimum cost of connecting cables {cables} is {calculate_min_cost(cables)}\n')
