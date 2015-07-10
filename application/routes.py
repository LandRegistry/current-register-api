from application import app

@app.route("/health")
def check_status():
    return "Status OK"

@app.route("/register")
def register():
    return "New route register", 200
