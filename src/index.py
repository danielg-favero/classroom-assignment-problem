from time import process_time

from file_reader import file_reader
from parse_classrooms_data import parse_classrooms_data
from parse_subjects_data import parse_subjects_data
from write_results import write_results
from greedy_method import greedy_classroom_assign
from local_search import local_search
from local_search_utils import cost

# Ler arquivos das instâncias de testes
classroomFile = file_reader("data/utfpr/rooms.txt")
subjectsFile = file_reader("data/utfpr/subjects-01.txt")

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

# Execução do algoritmo de busca local
algorithm_start_time = process_time()
local_search_solution = local_search(S, classrooms)
algorithm_end_time = process_time()

write_results(
    'local_search_results',
    local_search_solution,
    'Total de turmas: {}\nAtendimento dos requisitos não essenciais: {}\n'.format(len(subjectsFile), cost(local_search_solution, classrooms)),
    algorithm_end_time - algorithm_start_time
)