def calculate_average(subject_grades):
    '''(list of list of [str, number]) -> float

    Return the average of the grades in subject_grades.

    '''
    total = 0

    for i in range(len(subject_grades)):
        total = total + subject_grades[i][1]

    return total / len(subject_grades)

def average_of_inner_lists(grades):
    ''' (list of list of number) -> list of float'''
    averages = []
    for item in grades:
        averages.append(sum(item)/len(item))
    
    return averages
