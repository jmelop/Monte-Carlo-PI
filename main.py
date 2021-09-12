import math
import random
import statistics


def throw_needles(needles):
    inside_circle = 0

    for _ in range(needles):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distance_from_center = math.sqrt(x ** 2 + y ** 2)

        if distance_from_center <= 1:
            inside_circle += 1

        return (4 * inside_circle) / needles


def estimation(needles, number_attemps):
    estimations = []
    for _ in range(number_attemps):
        estimation_pi = throw_needles(needles)
        estimations.append(estimation_pi)

    estimated_average = statistics.mean(estimations)
    sigma = statistics.stdev(estimations)
    print(f'Est={round(estimated_average, 5)}, sigma={round(sigma, 5)}, agujas={needles}')

    return estimated_average, sigma


def estimate_pi(accuracy, number_attemps):
    number_of_needles = 1000
    sigma = accuracy

    while sigma >= accuracy / 1.96:
        accuracy, sigma = estimation(number_of_needles, number_attemps)
        number_of_needles *= 2

    return accuracy


if __name__ == '__main__':
    estimate_pi(0.01, 1000)
