import math
import random
import time

def firstEq(alpha, x, y, z):
    # returns difference from 0
    return abs((alpha * x) + (y * (x ** 2)) + (y ** 3) + (z ** 3))


def secondEq(beta, x, y, z):
    # returns difference from 0
    return abs((beta * y) + math.sin(y) + 2 ** y - z + math.log10(abs(x) + 1))


def thirdEq(teta, x, y, z):
    # returns difference from 0
    return abs((teta * z) + y - math.cos(x + y) / (math.sin((z * y) - (y ** 2) + z) + 2))


def fitnessFunc(x, y, z, alpha, beta, teta):
    return (firstEq(alpha, x, y, z) * firstEq(alpha, x, y, z) + secondEq(beta, x, y, z) * secondEq(beta, x, y, z) + thirdEq(teta, x, y, z) * thirdEq(teta, x, y, z))/3


def crossover(chromosomes, fitnesses,alpha,beta,teta):
    new_pop = []
    for j in range(len(chromosomes)):
        t1 = random.sample(chromosomes,k=15)
        t2 = random.sample(chromosomes,k=15)

        fmin = fitnessFunc(t1[0][0],t1[0][1],t1[0][2],alpha,beta,teta)
        fmini = 0
        fmin2 = fitnessFunc(t2[0][0], t2[0][1], t2[0][2], alpha, beta, teta)
        fmini2 = 0
        for i in range(15):
            check = fitnessFunc(t1[i][0],t1[i][1],t1[i][2],alpha,beta,teta)
            if check < fmin:
                fmin = check
                fmini = i
        for i in range(15):
            check1 = fitnessFunc(t2[i][0],t2[i][1],t2[i][2],alpha,beta,teta)
            if check1 < fmin2 :
                fmin2 =check
                fmini2 = i


        x = (t1[fmini][0] + t2[fmini2][0]) / 2
        y = (t1[fmini][1] + t2[fmini2][1]) / 2
        z = (t1[fmini][2] + t2[fmini2][2]) / 2


        new_pop.append([x, y, z])

        fitnesses[j] = fitnessFunc(x,y,z,alpha,beta,teta)

    print("fitnesses: ",fitnesses)
    return new_pop,fitnesses

def mutation(chromosomes, fitnesses, alpha, beta, teta):
    Replacing_num = [random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10)]

    print("mutation: ",Replacing_num)
    replacing_place = random.randint(0,len(chromosomes)-1)
    print(" Numbers to be replaced : ", Replacing_num)


    row = replacing_place
    chromosomes[row] = Replacing_num
    fitnesses[row] = fitnessFunc(chromosomes[row][0],chromosomes[row][1],chromosomes[row][2],alpha,beta,teta)
    return chromosomes,fitnesses


def solver(alpha, beta, teta):
    start = time.process_time()
    gen_num = 0;
    number_of_chromosomes = 1500
    chromosomes = list(range(number_of_chromosomes))
    for i in range(number_of_chromosomes):
        chromosome = [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)]
        chromosomes[i] = chromosome
    print(chromosomes)

    fitnesses = list(range(number_of_chromosomes))

    while True:
        fsum = 0
        for i in range(number_of_chromosomes):
            fitnesses[i] = fitnessFunc(chromosomes[i][0], chromosomes[i][1], chromosomes[i][2], alpha, beta, teta)
            fsum += fitnesses[i]
        print(fitnesses)
        count = 0
        for i in fitnesses:
            end = time.process_time()
            if i <= 0.000000000001 or end - start >= 4.7:
                #print(fitnesses[count])
                return chromosomes[count][0], chromosomes[count][1], chromosomes[count][2]
            count += 1
        end = time.process_time()
        
        chromosomes, fitnesses = crossover(chromosomes, fitnesses,alpha,beta,teta)
        Z = random.choices([chromosomes for _, chromosomes in sorted(zip(fitnesses, chromosomes), key=lambda pair: pair[0])],k=number_of_chromosomes)
        
        fitnesses.sort()    
        chromosomes = Z[0:number_of_chromosomes]
        gen_num += 1


        # mutation rate is 4 percent
        if gen_num % 25 == 0:
            print("entered mutation")
            chromosomes,fitnesses = mutation(chromosomes, fitnesses,alpha,beta,teta)
            
        print(chromosomes)
        print(numpy.min(fitnesses))
