
"""FIT1045 Algorithms and programming in Python, S1-2019 Assignment 1 - Race to Pi (Enoch Leow: 30600022)"""

"""Part A - Pi Functions"""

from math import pi
from math import sqrt


"""Basel Function"""


def basel(precision):
    baselresult = 0                                             #setting initial variables
    i=1
    trials=0
    while (abs((sqrt(6*baselresult))-pi)) > precision:          #loop condition
        comp = (1/pow(i, 2))
        baselresult = baselresult+comp                          #adding loop to approximation
        i=i+1                                                   #stepping variable counts
        trials=trials+1
    return (sqrt(6*baselresult), trials)                        #return approximation and num of trials


""""Taylor function"""


def taylor(precision):
    taylorresult = 0                                            #setting initial variables
    i=1
    trials=0
    while (abs(4*taylorresult-pi)) > precision:                 #loop condition for sum loop
        comp = (1/i)
        taylorresult = taylorresult+comp
        i=i+2
        trials=trials+1
        if (abs(4*taylorresult-pi)) > precision:                #continuing to subtract if loop condition is true
            comp = (1 / i)
            taylorresult = taylorresult - comp
            i = i + 2
            trials = trials + 1
    return ((4*taylorresult), trials)                           #return approximation and num of trials

""""Wallis function"""


def wallis (precision):
    wallisresult = 1                                            #setting initial variables
    x=2
    y=1
    z=3
    trials=0
    while (abs(2*wallisresult-pi)) > precision:                 #loop condition
        comp = ((x*x)/(y*z))                                    #computation variable
        wallisresult = wallisresult*comp
        x=x+2                                                   #stepping variable counts
        y=y+2
        z=z+2
        trials=trials+1
    return ((2*wallisresult), trials)                           #return approximation and num of trials


""""Spigot function"""


def spigot(precision):
    spigotresult = 1                                             #setting initial variables
    top=1
    bot=3
    product=1
    trials=1
    while (abs(2*spigotresult-pi)) > precision:                  #loop condition
        comp = (product*(top/bot))
        spigotresult = spigotresult+comp
        product=product*(top/bot)
        top=top+1                                               #stepping variable counts
        bot=bot+2
        trials=trials+1
    return ((2*spigotresult), trials)                           #return approximation and num of trials


"""Part B - Race"""


list_alg = [basel, taylor, wallis, spigot]                      #list of available algorithms


def min_index(list):                                            #minimum index function
    minimum = list[0]                                           #sets minimum to first index in list =
    for i in range(0, len(list)):
        if int(list[i][1]) < minimum[1]:                        #checks each element in list if it is smaller than current min
            minimum = list[i]                                   #if so, new min index set to element index
    return list.index(minimum)                                  #returns min element index


def selection_sort(list):                                       #selection sort function
    for i in range(len(list)):
        j = min_index(list[i:]) + i                             #swaps element at index with min in list[i:] (unsorted list)
        list[i], list[j] = list[j], list[i]
    return list                                                 #returns sorted list


def bring_index(variable, list):                                #bring index function of algorithm in list
    index = "none"
    for i in range(0, len(list)):                               #check if element in matches variable
        if list[i] == variable:
            index = i
    return index                                                #return its index


def race(precision, alg):                                       #race function
    alg_approx = []                                             #list of results to be sorted
    int_approx = []                                             #list of results in initial order
    for i in alg:                                               #appending each algorithms race result to approx list
        alg_approx.append(i(precision))
    for i in alg:                                               #appending each algorithms race result to approx list
        int_approx.append(i(precision))
    selection_sort(alg_approx)                                  #sorts alg_approx
    sorted = []
    for i in alg_approx:
        sorted.append((bring_index(i, int_approx), i[1]))       #output (index, step count) in ascending order
    return sorted


precision_input = float(input("Desired precision: "))

print(race(precision_input, list_alg))                          #race ouput

race_results = race(precision_input, list_alg)


"""Part C - Readable Format"""


def print_results(output):                                      #printing in a readable format
    for i in range(0, len(output)):
        print("Algorithm "+str(output[i][0])+" finished in "+str(str(output[i][1]))+" steps")


print_results(race_results)                                     #print_result output


