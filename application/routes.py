from application import app
from application import db
import json

@app.route("/health")
def check_status():
    return "Status OK"

@app.route("/register/<titlenumber>", methods=["GET"])
def register(titlenumber):
    title = get_title_from_current_register(titlenumber)

    return json.dumps(title)


#gets the title from the current register.
def get_title_from_current_register(title_number):
    # Gets the version of title number with the latest ID on the table
    title = None
    if check_title_exists(title_number):
        sql_text = "SELECT * FROM registers WHERE record ->> 'title_number' = '%s' order by id desc limit 1;" % title_number
        result = db.engine.execute(sql_text)

        for row in result:
            title = row["record"]
    # import pdb; pdb.set_trace()

    return title

def check_title_exists(title_number):
    # Gets the version of title number with the latest ID on the table
    title_exists = False
    sql_text = "SELECT 1 FROM registers WHERE record ->> 'title_number' = '%s' order by id desc limit 1;" % title_number
    result = db.engine.execute(sql_text)
    for row in result:
        title_exists = True
    return title_exists
