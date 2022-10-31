import random
from math import *

from local_search_utils import cost, swap_classes
from local_search import local_search

def simulated_annealing(So: list, classrooms: list, To: float, alpha: float, max_iter: int):
    S = So
    S1 = S
    T = To
    iter_T = 0
    S_result = []

    while T > 1:
        while iter_T < max_iter:
            iter_T += 1

            # Gerar novo vizinho S' ∈ N(S)
            S1 = swap_classes(S, classrooms)

            delta = cost(S1, classrooms) - cost(S, classrooms)

            if (delta > 0):
                S = S1

                if cost(S1, classrooms) > cost(S_result, classrooms):
                    S_result = S1
                else:
                    random.seed()

                    x = random.random()
                    if x < exp(-delta / T):
                        S = S1

        T = alpha * T
        iter_T = 0

    return S_result