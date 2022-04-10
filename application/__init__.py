import flask
app = flask.Flask(__name__)
conn_string = 'postgresql://postgres:PeanutSmoothie5000@localhost:5432/wuzzaworld'
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string	
app.config['SECRET_KEY'] = "SECRET_KEY"
import application.views
