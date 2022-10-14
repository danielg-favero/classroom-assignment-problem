import re


def parse_subjects_data(scheduleFile):
    parsed_schedules = []  # Horários formatados

    # Percorrer todos os dias da semana
    for i in range(2, 7):
        week_day_schedule = []

        # Organizar os horários por dia de semana
        for j in range(0, len(scheduleFile) - 1):
            current_subject_data = scheduleFile[j].split(' ')

            if re.match("{:1d}".format(i), current_subject_data[1]):
                week_day_schedule.append([
                    # Código da disciplina
                    current_subject_data[0],
                    # Horário de início
                    int(current_subject_data[1]) % 100,
                    # Horário de fim
                    int(current_subject_data[2]) % 100,
                    # Quantidade de alunos matriculados
                    int(current_subject_data[3]),
                    # Período da disciplina
                    current_subject_data[4],
                    # Turnos de preferencia da disciplina
                    current_subject_data[5].replace('\n', '')
                ])

        parsed_schedules.append(week_day_schedule)

    return parsed_schedules
