total_nodes, edges = list(map(int, input().split()))
edge_pair = []
shopper_locations = []

for edge in range(edges):
    start_of_edge, end_of_edge = list(map(int, input().split()))
    edge_pair.append([start_of_edge, end_of_edge])


no_shopper_edge_pairs = edge_pair

total_shopper, min_distance = list(map(int, input().split()))
for shopper in range(total_shopper):
    shopper_location = int(input())
    shopper_locations.append(shopper_location)

removed = 0

for location in shopper_locations:
    for pair in edge_pair:

        while removed < min_distance:
            if location in pair:
                for one in pair:
                    # Replace location with the other half of the pair
                    # for distance of more than 1
                    if one != location:
                        location = one
                print('run', pair)
                no_shopper_edge_pairs.remove(pair)
                removed += 1
    removed = 0

print(edge_pair)
print(no_shopper_edge_pairs)


