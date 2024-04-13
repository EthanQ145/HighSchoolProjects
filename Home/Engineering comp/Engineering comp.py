""""
This program takes in the chances of extreme weather events and performs
multiple simulations to give an average amount of events that happen across
a given amount of time.
"""

# Imports
import random
import math
# Constants
MOISTURE = 0
TEMPERATURE = 0
NEW_EVENT_RATE = 1.01358
EXTREME_EVENTS = ("flood", "rainfall", "storm")
SIMULATED_YEARS = 10


def simulate():
    year = 0
    event_chance = 4.4
    event_list = []
    while year <= SIMULATED_YEARS:
        event_chance *= NEW_EVENT_RATE
        print(event_chance)
        chance = event_chance - math.floor(event_chance)
        chnce_num = round(1 / chance)
        if random.randint(1, chnce_num) == 1:
            event_list.append(random.choice(EXTREME_EVENTS))
        for certain in range(math.floor(event_chance)):
            event_list.append(random.choice(EXTREME_EVENTS))
        year += 1
    num_evnt = len(event_list)
    return num_evnt


def main(sim_num):
    sim_count = 0
    total_events = 0
    while sim_count < sim_num:
        total_events += simulate()
        sim_count += 1
    average_events = total_events / sim_num
    print(average_events)


# Main
if __name__ == "__main__":
    main(int(input()))
