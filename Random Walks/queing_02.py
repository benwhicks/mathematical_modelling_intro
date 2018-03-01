from random import random, randint
 
# Setting up parameters
max_service_time = 9 # The maximum time it takes to serve 1 person
max_time_between = 5 # The maximum time between arrivals
 
queue = []
new_person = randint(1, max_time_between)
for n in range(200):
    new_person = new_person - 1
    if new_person == 0:
        queue.append(randint(1, max_service_time))
        new_person = randint(1, max_time_between)
    if len(queue) > 0:
        queue[0] = queue[0] - 1
        if queue[0] == 0:
            queue.remove(0)
    print(queue)
