import dal


def get_five_recent_questions():
    sql_string = 'SELECT id, submission_time, view_number, vote_number, title FROM question \
                  ORDER BY submission_time DESC LIMIT 5;'
    return dal.get_data_from_table(sql_string)


def get_all_questions():
    sql_string = 'SELECT id, submission_time, view_number, vote_number, title FROM question ORDER BY submission_time;'
    return dal.get_data_from_table(sql_string)


def add_new_question(new_question):
    sql_string = 'INSERT INTO question (submission_time, view_number, vote_number, title, message) \
                  VALUES(%s, %s, %s, %s, %s);'
    sql_variables = (new_question[0], new_question[1], new_question[2], new_question[3], new_question[4])
    dal.edit_table(sql_string, sql_variables)


def get_question_details(question_id):
    sql_string = 'SELECT question.id, question.submission_time, question.view_number, question.vote_number, question.title,\
                  users.username, question.message FROM question LEFT JOIN users ON question.user_id = users.id \
                  WHERE question.id = %s;'
    sql_variables = (question_id, )
    return dal.get_data_from_table(sql_string, sql_variables)


def increase_view_number(question_id):
    sql_string = 'UPDATE question SET view_number = view_number + 1 WHERE id = %s;'
    sql_variables = (question_id, )
    dal.edit_table(sql_string, sql_variables)
