'''
Created on Feb 9, 2019

@author: Shubham Mundada
'''
def assign_grades(subjects):
    subject_count = len(subjects)
    grades = []
    print( 'The number of subjects = ' + str(subject_count))
    i = 0
    while i < subject_count:
        grades.append((i+1) * 30)
        i = i + 1
        
    return grades

def add_grades(subjects, grades):
    subject_count = len(subjects)
    grades_count = len(grades)
    print( 'The number of subjects = ' + str(subject_count))
    print( 'The number of grades = ' + str(grades_count))
    if(subject_count == grades_count):
        print('Both lists are equal, all grades have been assigned already.')
    else:
        print('assigning new grades')
        while grades_count < subject_count:
                grades.append(sum(grades)/subject_count)
                grades_count = grades_count + 1
                        
subjects = ['math','bio','chem']
grades = assign_grades(subjects)
print(subjects)
print(grades)
subjects.append('physics')
subjects.append('english')
print(subjects)
add_grades(subjects, grades)
print(grades)