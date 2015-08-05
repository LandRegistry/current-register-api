from application import app
from application import db
from .utils import convert_register_format
from flask import request
import json

@app.route("/health")
def check_status():
    return "Status OK"

@app.route("/register/<titlenumber>", methods=["GET"])
def register(titlenumber):
    register = get_register_from_current_register(titlenumber)

    if register:
        register_format = request.args.get('format')

        if register_format:
            register = convert_register_format(register, register_format)

        return json.dumps(register)
    else:
        return "register not found", 404


#gets the title from the current register.
def get_register_from_current_register(title_number):
    # Gets the version of title number with the latest ID on the table
    register = None
    if check_register_exists(title_number):
        sql_text = "SELECT * FROM registers WHERE record ->> 'title_number' = '%s' order by id desc limit 1;" % title_number
        result = db.engine.execute(sql_text)

        for row in result:
            register = row["record"]

    return register

def check_register_exists(title_number):
    # Gets the version of title number with the latest ID on the table
    register_exists = False
    sql_text = "SELECT 1 FROM registers WHERE record ->> 'title_number' = '%s' order by id desc limit 1;" % title_number
    result = db.engine.execute(sql_text)
    for row in result:
        register_exists = True
    return register_exists
