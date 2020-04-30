def workbook(n, k, arr):
    chapter = 1
    page = 1
    questions_on_page = 0
    question_in_chapter = 0
    special_questions = 0
    total_questions = sum(arr)
    current_question = 1
    while current_question <= total_questions:
        question_in_chapter += 1
        questions_on_page += 1
        if question_in_chapter == page:
            special_questions += 1
        if questions_on_page == k or question_in_chapter == arr[chapter-1]:
            #flip
            page += 1
            questions_on_page = 0
        if question_in_chapter == arr[chapter-1]:
            question_in_chapter=0
            chapter += 1
        current_question += 1


    return special_questions

print(workbook(5,3,[4,2,6,1,10]))
print(workbook(10,5,[3, 8, 15, 11, 14, 1, 9, 2, 24, 31]))
