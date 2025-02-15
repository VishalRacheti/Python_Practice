def marks_subject (**kwargs):
    def total_marks (marks_list):
        return sum (marks_list)
    marks_list = []

    for sub , marks in kwargs.items():
        marks_list.append(marks)

    return total_marks(marks_list)
    
#need to study more on this