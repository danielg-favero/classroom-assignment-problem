from time import process_time

from file_reader import file_reader
from parse_classrooms_data import parse_classrooms_data
from parse_subjects_data import parse_subjects_data
from write_results import write_results
from greedy_method import greedy_classroom_assign
from local_search import local_search
from simulated_annealing import simulated_annealing
from local_search_utils import cost
from random_solution import random_solution

# Ler arquivos das instâncias de testes
classroomFile = file_reader("data/utfpr/rooms.txt")
subjectsFile = file_reader("data/utfpr/subjects-01.txt")

# Formatar dados dos arquivos para execução dos algoritmos
classes = parse_subjects_data(subjectsFile)
classrooms = parse_classrooms_data(classroomFile)

# Execução do algoritmo guloso
algorithm_start_time = process_time()
S = greedy_classroom_assign(classes, classrooms)
algorithm_end_time = process_time()

write_results(
    'greedy_results', 
    S,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(S, classrooms)),
    algorithm_end_time - algorithm_start_time
)

# Gerar 3 soluções aleatórias
classes = parse_subjects_data(subjectsFile)
s1 = random_solution(classes, classrooms)
write_results(
    'r_1',
    s1,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(s1, classrooms)),
    0
)

classes = parse_subjects_data(subjectsFile)
s2 = random_solution(classes, classrooms)
write_results(
    'r_2',
    s2,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(s2, classrooms)),
    0
)

classes = parse_subjects_data(subjectsFile)
s3 = random_solution(classes, classrooms)
write_results(
    'r_3',
    s3,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(s3, classrooms)),
    0
)

# Execução do algoritmo de busca local
algorithm_start_time = process_time()
local_search_solution = local_search(S, classrooms)
algorithm_end_time = process_time()

write_results(
    'local_search/local_search_greedy',
    local_search_solution,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(local_search_solution, classrooms)),
    algorithm_end_time - algorithm_start_time
)

# Execução do algoritmo de simulated annealing com solução gulosa
algorithm_start_time = process_time()
simulated_annealing_solution = simulated_annealing(S, classrooms, 1200, 0.35, 30, 'results/simulated_annealing/simulated_annealing_greedy')
algorithm_end_time = process_time()

write_results(
    'simulated_annealing/simulated_annealing_greedy',
    simulated_annealing_solution,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(simulated_annealing_solution, classrooms)),
    algorithm_end_time - algorithm_start_time
)

# Execução do algoritmo de simulated annealing com solução de busca local
algorithm_start_time = process_time()
simulated_annealing_solution = simulated_annealing(local_search_solution, classrooms, 1200, 0.35, 30, 'results/simulated_annealing/simulated_annealing_local_search')
algorithm_end_time = process_time()

write_results(
    'simulated_annealing/simulated_annealing_local_search',
    simulated_annealing_solution,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(simulated_annealing_solution, classrooms)),
    algorithm_end_time - algorithm_start_time
)


# Execução do algoritmo de simulated annealing com solução aleatória
algorithm_start_time = process_time()
simulated_annealing_solution = simulated_annealing(s1, classrooms, 1200, 0.4, 30, 'results/simulated_annealing/simulated_annealing_random_1')
algorithm_end_time = process_time()

write_results(
    'simulated_annealing/simulated_annealing_random_1',
    simulated_annealing_solution,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(simulated_annealing_solution, classrooms)),
    algorithm_end_time - algorithm_start_time
)

algorithm_start_time = process_time()
simulated_annealing_solution = simulated_annealing(s2, classrooms, 1200, 0.4, 30, 'results/simulated_annealing/simulated_annealing_random_2')
algorithm_end_time = process_time()

write_results(
    'simulated_annealing/simulated_annealing_random_2',
    simulated_annealing_solution,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(simulated_annealing_solution, classrooms)),
    algorithm_end_time - algorithm_start_time
)

algorithm_start_time = process_time()
simulated_annealing_solution = simulated_annealing(s3, classrooms, 1200, 0.4, 30, 'results/simulated_annealing/simulated_annealing_random_3')
algorithm_end_time = process_time()

write_results(
    'simulated_annealing/simulated_annealing_random_3',
    simulated_annealing_solution,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(simulated_annealing_solution, classrooms)),
    algorithm_end_time - algorithm_start_time
)