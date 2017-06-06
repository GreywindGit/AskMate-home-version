import dal


def get_five_recent_questions():
    sql_string = 'SELECT submission_time, view_number, vote_number, title FROM question ORDER BY submission_time DESC LIMIT 5;'
    return dal.get_data_from_table(sql_string)


def get_all_questions():
    sql_string = 'SELECT submission_time, view_number, vote_number, title FROM question ORDER BY submission_time;'
    return dal.get_data_from_table(sql_string)

