import random
from math import *
import os
import numpy as np
import matplotlib.pyplot as plt

from local_search_utils import cost, swap_classes
from local_search import local_search

clear = lambda: os.system('clear')

def simulated_annealing(So: list, classrooms: list, To: float, alpha: float, max_iter: int, outputName: str):
    S = np.copy(So)
    S1 = np.copy(S)
    T = To
    iter_T = 0
    total_iter = 0
    S_result = np.copy(S)

    x = []
    y = []

    while T > 1:
        while iter_T < max_iter:
            iter_T += 1

            print(
                "Executando o algoritmo " + outputName + ": {}%\n".format((1 - T/To)*100),
                "Temperatura Inicial: {}\n".format(To),
                "Temperatura corrente: {}\n".format(T),
                "Iterações máximas: {}\n".format(max_iter),
                "Iteração corrente: {}\n".format(total_iter),
                "Taxa de resfriamento: {}%\n".format((1 - alpha) * 100),
                "Melhor solução encontrada: {}\n".format(cost(S, classrooms))
            )

            # Gerar novo vizinho S' ∈ N(S)
            initial_cost = cost(S, classrooms)
            S1 = swap_classes(S, classrooms)
            final_cost = cost(S1, classrooms)

            delta = final_cost - initial_cost

            if (delta > 0):
                S = S1
            else:
                random.seed()
                r = random.random()

                if r < exp(-delta / To) - 1:
                    S = S1

            x.append(total_iter)
            y.append(cost(S, classrooms))
            total_iter += 1
            clear()

        T = alpha * T
        iter_T = 0

    plt.title("Resultados Simulated Annealing")
    plt.plot(x, y, color="red")
    plt.savefig(outputName + '.png')
    plt.cla()

    return S