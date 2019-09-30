def stud_names(student_list):
    for i in student_list:
        yield i


s_list = ['vamsi', 'krishna', 'sai']
for i in range(len(s_list)):
    print(stud_names(s_list).__next__())
