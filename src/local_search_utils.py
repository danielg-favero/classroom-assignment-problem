import pandas as pd
import numpy as np
import random

def get_cleaning_hour_cost(subjects: list):
    cleaning_hour_cost = 0

    '''
    f) Se possível, cada uma das salas deve ser deixada vazia em pelo menos um horário
    ao longo do dia, de forma a possibilitar sua limpeza
    '''
    for subject in subjects:
        # Quanto menos aulas alocadas, mais horários de limpeza há disponível
        if subject == 0:
            cleaning_hour_cost += 1

    return  cleaning_hour_cost  

def get_less_classrooms_cost(subjects: list):
    less_classrooms_cost = 0

    # g) Se possível, utilizar o menor número de salas possível
    # Se uma sala inteira está vazia, estamos utilizando menos salas
    if (subjects == 0).all():
        less_classrooms_cost += 1

    return less_classrooms_cost

def get_same_period_cost(subjects: list):
    same_period_cost = 0
    visited_cells = []

    # e) Sempre que possível, alocar a uma mesma sala alunos de um mesmo período
    for j in range(0 , 15):
        if subjects[j] != 0 and subjects[j] != 'RESERVADO' and subjects[j] not in visited_cells:
            visited_cells.append(subjects[j])

    for i in range(0, len(visited_cells)):
        if i + 1 < len(visited_cells):
            if visited_cells[i][4] == visited_cells[i + 1][4]:
                same_period_cost += 1

    return same_period_cost

def get_same_course_cost(subjects: list):
    same_course_cost = 0
    visited_cells = []

    # h) Sempre que possível, alocar a uma mesma sala alunos de um mesmo curso
    for j in range(0 , 15):
        if subjects[j] != 0 and subjects[j] != 'RESERVADO' and subjects[j] not in visited_cells:
            visited_cells.append(subjects[j])

    visited_cells.sort(key=lambda j: j[5])

    for i in range(0, len(visited_cells)):
        if i + 1 < len(visited_cells):
            if visited_cells[i][5] == visited_cells[i + 1][5]:
                same_course_cost += 1

    return same_course_cost

def get_eficient_assigment_cost(subjects: list, classrooms: list, classroomIndex: int):
    eficient_assigment_cost = 0
    visited_cells = []

    # d) Evitar alocar aulas de turmas pequenas em salas de maior capacidade
    for j in range(0 , 15):
        if subjects[j] != 0 and subjects[j] != 'RESERVADO' and subjects[j] not in visited_cells:
            visited_cells.append(subjects[j])

    for i in range(0, len(visited_cells)):
        eficient_assigment_cost += classrooms[classroomIndex][1] - visited_cells[i][3]

    return eficient_assigment_cost
     
def cost(S: list, classrooms: list):
    C = np.copy(S)

    # Calcular o custo baseado nas restrições não essenciais
    same_period_cost = 0
    same_course_cost = 0
    cleaning_hour_cost = 0
    less_classrooms_cost = 0
    eficient_assigment_cost = 0

    for i in range(0, len(C)):
        Ck = pd.DataFrame(C[i])

        for (columnIndex, subjects) in Ck.iteritems():
            cleaning_hour_cost += get_cleaning_hour_cost(subjects)
            less_classrooms_cost += get_less_classrooms_cost(subjects)
            same_period_cost += get_same_period_cost(subjects)
            same_course_cost += get_same_course_cost(subjects)
            eficient_assigment_cost += get_eficient_assigment_cost(subjects, classrooms, columnIndex)

    '''
    eficient_assigment_cost é negativo pois quanto maior a diferença entre a capacidade
    da sala e a quantidade de alunos na turma, menos eficiente foi nossa alocação
    '''
    return cleaning_hour_cost + less_classrooms_cost + same_period_cost + same_course_cost - eficient_assigment_cost

def swap_classes(C: list, classrooms: list):
    Ck = np.copy(C)
    i = 0

    # Realizar uma troca de turma por dia de semana
    while(i < len(Ck)):
        # Selecionar uma linha e uma coluna aleatória para realizar a troca
        random.seed()
        first_row = round(random.random() * 15)
        first_column = round(random.random() * len(Ck[0]))
        
        first_selected_class = Ck[i][first_row][first_column]

        if first_selected_class != 0 and first_selected_class != 'RESERVADO':
            first_start_time = first_selected_class[1]
            first_end_time = first_selected_class[2]

            second_column = -1

            # Encontrar a primeira turma cujo horário é compatível com a turma selecionada
            for j in range(0, len(Ck[0])):
                if(
                    Ck[i][first_start_time][j] != 0 and
                    Ck[i][first_start_time][j] != 'RESERVADO' and
                    Ck[i][first_start_time][j] != first_selected_class
                ):
                    second_selected_class = Ck[i][first_start_time][j]
                    second_start_time = second_selected_class[1]
                    second_end_time = second_selected_class[2]
                    second_column = j

            if (
                second_column >= 0 and
                Ck[i][first_start_time][first_column][3] <= classrooms[first_column][1] and
                Ck[i][second_start_time][second_column][3] <= classrooms[second_column][1]
            ):
                # Há 5 situaçãoes para que seja possível a troca das turmas
                """
                    1)          
                        0 B
                        A B
                        A 0
                    2)          
                        A 0
                        A B
                        0 B
                    3)          
                        A 0
                        A B
                        A B
                        A 0
                    4)          
                        0 B
                        A B
                        A B
                        0 B
                """
                if (
                    (
                        Ck[i][second_start_time][first_column] == 0 and
                        Ck[i][first_end_time][second_column] == 0
                    ) or
                    (
                        Ck[i][first_start_time][second_column] == 0 and
                        Ck[i][second_end_time][first_column] == 0
                    ) or
                    (
                        Ck[i][first_start_time][second_column] == 0 and
                        Ck[i][first_end_time][second_column] == 0
                    ) or
                    (
                        Ck[i][second_start_time][first_column] == 0 and
                        Ck[i][second_end_time][first_column] == 0
                    ) or
                    (
                        Ck[i][first_start_time][second_column] == second_selected_class and
                        Ck[i][first_end_time][second_column] == second_selected_class and
                        Ck[i][second_start_time][first_column] == first_selected_class and
                        Ck[i][second_end_time][first_column] == first_selected_class
                    )
                ):
                    # Limpar a 1º sala selecionada
                    for j in range(first_start_time, first_end_time + 1):
                        Ck[i][j][first_column] = 0

                    # Limpar a 2º sala selecionada
                    for j in range(second_start_time, second_end_time + 1):
                        Ck[i][j][second_column] = 0

                    # Alocar a 2º turma na sala da 1º turma
                    for j in range(second_start_time, second_end_time + 1):
                        Ck[i][j][first_column] = second_selected_class

                    # Alocar a 1º turma na sala da 2º turma
                    for j in range(first_start_time, first_end_time + 1):
                        Ck[i][j][second_column] = first_selected_class
                    
                    i += 1
    
    return Ck