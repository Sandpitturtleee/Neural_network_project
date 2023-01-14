import math
import random
from variables import random_wages, byte_A, byte_C, learning_rate


def print_letter(letter):
    x = 0
    while x < len(letter):
        print(
            str(letter[x]) + " " + str(letter[x + 1]) + " " + str(letter[x + 2]) + " " + str(letter[x + 3]) + " " + str(
                letter[x + 4]))
        x += 5


def optimize_wages(learning_rate_value):
    generate_random_wages(byte_A)
    x = 0
    learning_error = 1
    iterations = 100000
    while learning_error > 0.0000001 and x < iterations:
        random_letter, number = draw_random_letter()
        net_sum = calculate_net_sum(random_letter)
        learning_error = calculate_learning_error(number, net_sum)
        calculate_new_wages(number, random_letter, net_sum)
        learning_rate_value *= 0.98
        x += 1
        #print("Number: " + str(number))
        #print("Y: " + str(math_function(net_sum)))
        #print("Learning error: " + str(learning_error))
        #print()
    print("Number of loops: " + str(x) + " out of " + str(iterations))


def letter_recognition(byte_letter):
    print_letter(byte_letter)
    print("Y ~ 0 --> Letter = A")
    print("Y ~ 1 --> Letter = C")
    return math_function(calculate_net_sum(byte_letter))


def generate_random_wages(letter):
    for x in range(len(letter)):
        random_wages.append(random.uniform(-1.0, 1.0))


def draw_random_letter():
    probability = 0.5
    random_number = random.uniform(0.0, 1.0)
    if random_number < probability:
        random_letter = byte_A.copy()
        number = 0
    else:
        random_letter = byte_C.copy()
        number = 1
    return random_letter, number


def calculate_net_sum(random_letter):
    net_sum = 0
    for x in range(len(random_letter)):
        net_sum += random_letter[x] * random_wages[x]
    return net_sum


def calculate_learning_error(number, net_sum):
    learning_error = (1 / 2) * (number - math_function(net_sum)) ** 2
    return learning_error


def calculate_new_wages(number, random_letter, net_sum):
    # random_wages[x] = random_wages[x] + learning_rate * (random_letter[x] - math_function(net_sum)) * net_sum * (1 - net_sum)
    for x in range(len(random_wages)):
        random_wages[x] = random_wages[x] + learning_rate * (number - math_function(net_sum)) * random_letter[x]
    return random_wages


def math_function(net_sum):
    value = 1/(1+math.exp(-net_sum))
    return value
