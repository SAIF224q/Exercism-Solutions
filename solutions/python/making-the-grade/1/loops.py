"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    round_scores = []
    for i in student_scores:
        round_scores.append(round(i))
    round_scores.sort()
    return round_scores
        



def count_failed_students(student_scores):
    failed_studens = 0
    for i in student_scores:
        if i <= 40:
            failed_studens += 1
    return failed_studens
            



def above_threshold(student_scores, threshold):
    best_scores = []
    for i in student_scores:
        if i >= threshold:
            best_scores.append(i)
    return best_scores



def letter_grades(highest):
    interval_size = (highest - 41) / 4
    thresholds = [
        41,
        int(41 + round(interval_size)),
        int(41 + 2 * round(interval_size)),
        int(41 + 3 * round(interval_size))
    ]
    return thresholds



def student_ranking(student_scores, student_names):
    student_ranking = []
    rank = 1
    for i in range(len(student_scores)):
        student_ranking.append(f"{rank}. {student_names[i]}: {student_scores[i]}")
        rank +=1
    return student_ranking
        



def perfect_score(student_info):
    perfect_score_student = []
    for i in student_info:
        if i[1] == 100:
            perfect_score_student = i
            return i
            break
    return perfect_score_student
            

