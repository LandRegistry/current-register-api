from application import app
from application import db

@app.route("/health")
def check_status():
    return "Status OK"

@app.route("/register/<caseid>", methods=["GET"])
def register(titlenumber):
    title = get_title_from_current_register(titlenumber)

    return title, 200


#gets the title from the current register.
def get_title_from_current_register(title_number):
    # Gets the version of title number with the latest ID on the table
    title = None
    if check_title_exists(title_number):
        sql_text = "SELECT * FROM records WHERE registers ->> 'title_number' = '%s' order by id desc limit 1;" % title_number
        result = db.engine.execute(sql_text)
        for row in result:
            title = row['record']

    return title

def check_title_exists(title_number):
    # Gets the version of title number with the latest ID on the table
    title_exists = False
    sql_text = "SELECT 1 FROM records WHERE registers ->> 'title_number' = '%s' order by id desc limit 1;" % title_number
    result = db.engine.execute(sql_text)
    for row in result:
        title_exists = True
    return title_exists