import math
from random import random

MUTATE_RATE = 0.01;
BREED_RATE = 0.75;
POPULATION_SIZE = 1000;
TARGET = 'Hello, World';


def generateCharacter():
    return chr(math.floor((random() * 94) + 32))


def selectParent(elders, totalScore):
    selection = random() * totalScore
    sum = 0
    for e in elders:
        sum += e['score']
        if selection <= sum:
            return e


def generatePopulation():
    p = []
    for i in range(POPULATION_SIZE):
        x = ''
        for c in TARGET:
            x += generateCharacter()
        p.append(x)
    return p


def checkFitness(x):
    r = {'value': x, 'score': 0}
    for i in range(len(TARGET)):
        if x[i] == TARGET[i]:
            r['score'] += 1
    return r


def breed(p1, p2):
    c = ''
    for i in range(len(TARGET)):
        if random() < MUTATE_RATE:
            c += generateCharacter()
        else:
            if random() < 0.5:
                c += p1[i]
            else:
                c += p2[i]
    return c

population = generatePopulation()
generation = 0

print('Using a population of size {}'.format(POPULATION_SIZE))
print('Regenerating {:%} of the population per generation'.format(BREED_RATE))
print('{:%} chance of mutation for each chromosome'.format(MUTATE_RATE))

while population[0] != TARGET:
    generation += 1

    results = list(map(checkFitness, population))
    results.sort(key=lambda x: x['score'], reverse=True)
    if results[0]['value'] != TARGET:
        elders = results[0:int(POPULATION_SIZE * (1 - BREED_RATE))]
        population = []
        [population.append(person) for person in map(lambda x: x['value'], elders)]
        totalScore = sum([n['score'] for n in elders])
        for i in range(int(POPULATION_SIZE * BREED_RATE)):
            p1 = selectParent(elders, totalScore)['value']
            p2 = selectParent(elders, totalScore)['value']
            population.append(breed(p1, p2))
    else:
        population = list(map(lambda x: x['value'], results))
    print('Generation {}: {}, score: {}'.format(generation, results[0]['value'], results[0]['score']))