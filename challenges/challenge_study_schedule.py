def is_valid_schedule(schedule):
    """
    Verifica se a lista de tuplas de permanência é válida
    """
    for period in schedule:
        for time in period:
            if not isinstance(time, int):
                return False
    return True


def count_students_present(schedule, target_time):
    """
    Conta o número de estudantes presentes em um determinado horário
    """
    count = 0
    for period in schedule:
        if period[0] <= target_time <= period[1]:
            count += 1
    return count


def study_schedule(permanence_period, target_time):
    """
    Retorna a quantidade de estudantes presentes para um horário específico
    """
    if (
        not is_valid_schedule(permanence_period)
        or not isinstance(target_time, int)
        or target_time < 1
    ):
        return None

    return count_students_present(permanence_period, target_time)


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 2
print(study_schedule(permanence_period, target_time))
