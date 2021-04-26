from flask import Flask, render_template

from controllers.members_controller import members_blueprint
from controllers.gymclass_controller import gymclass_blueprint
from controllers.schedule_controller import schedules_blueprint

app = Flask(__name__)

app.register_blueprint(gynclasses_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(schedules_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()