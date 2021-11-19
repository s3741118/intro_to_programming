def flour_order(large_thick, large_thin, medium_thick, medium_thin):
    import numpy as nmp
    while True:
        try:
            large_thick = int(input('please enter number large_thick pizza: '))
            large_thin = int(input('please enter number large_thin pizza: '))
            medium_thick = int(input('please enter number medium_thick pizza: '))
            medium_thin = int(input('please enter number medium_thin pizza: '))
            break
        except ValueError:
            print("Please input again !!!")
            continue

    total = (large_thick * 550 + large_thin * 500 + medium_thick * 450 + medium_thin * 400) / 1000
    total_plus_waste = total * (1 + 0.06)
    total_flour = int(nmp.ceil(total_plus_waste))  # convert float to integer to remove .0

    if total_flour % 2 != 0:  # is flour's weigh an odd number ?
        total_flour += 1  # in case it is an odd number then it is added 1 kg

    cost = []  # create a list to store the cost buy from provider A and B
    if total_flour < 30:
        cost_a = total_flour * 30000 * (1 - 0.03)  # discount 3% when flour < 30kg
        cost.append(cost_a)
    elif total_flour >= 30:
        cost_a = total_flour * 30000 * (1 - 0.05)  # discount 5% when flour >= 30kg
        cost.append(cost_a)

    # provider B's condition
    if total_flour < 40:
        cost_b = total_flour * 31000 * (1 - 0.05)  # discount 5% when flour < 40kg
        cost.append(cost_b)
    elif total_flour >= 40:
        cost_b = total_flour * 31000 * (1 - 0.1)  # discount 10% when flour >= 40kg
        cost.append(cost_b)

    providers = ['provider A', 'provider B']
    for i in providers:
        if cost[0] < cost[1]:
            selected_provider = providers[0]
            total_cost = int(nmp.ceil(cost[0]))  # remove .0 of the total cost
        elif cost[0] > cost[1]:
            selected_provider = providers[1]
            total_cost = int(nmp.ceil(cost[1]))  # remove .0 of the total cost
        else:  # this case is cost to buy flour from provider A equal cost to buy flour from provider B
            total_cost = cost[0]  # also total_cost = cost[1]

    return total_flour, total_cost, selected_provider  # , selected_provider, total_cost

