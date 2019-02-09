def get_answer(prompt):
    '''(str) -> str '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer

def up_to_vowel(s):
    '''(str) -> str '''

    before_vowel = ''
    i = 0

    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel

print(up_to_vowel("Shubham"))
print(get_answer("Are you exhausted? Answer in yes or no."))