import re


def parse_schedules_data(scheduleFile, weekDay):
    all_subjects_per_week_day = []
    parsed_schedules = []

    # Selecionar todas as matérias por dia da semana
    for i in range(0, len(scheduleFile) - 1):
        subjects_schedules = scheduleFile[i].split('\t')

        if re.match("{:1d}".format(weekDay), subjects_schedules[2]):
            all_subjects_per_week_day.append([
                subjects_schedules[0],
                int(subjects_schedules[2].replace('\n', '')) % 100
            ])

    current_subject = all_subjects_per_week_day[0][0]
    current_subject_schedule_depth = 0

    # Formatar as disciplinas com horário de início e fim
    for i in range(0, len(all_subjects_per_week_day) - 1):
        if current_subject == all_subjects_per_week_day[i + 1][0]:
            current_subject_schedule_depth += 1
        else:
            parsed_schedules.append([
                all_subjects_per_week_day[i][0],
                all_subjects_per_week_day[i][1] -
                current_subject_schedule_depth,
                current_subject_schedule_depth
            ])
            current_subject_schedule_depth = 0

        i += 1
        current_subject = all_subjects_per_week_day[i][0]

    return parsed_schedules
