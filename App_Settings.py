from Imports import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DATABASE.db'

# paypalrestsdk.configure({
#     "mode": "sandbox", # sandbox or live
#     "client_id": "AaLx9_MIwUr-3Rj7QseSKfsmPz7T880s7szPKvitBvfoQw5wPXwsoGc8JopPi1ML7oYAm5pPRxMcz_fS",
#     "client_secret": "EDod5Ffm8McgxGPHgjYQN1ghrEe64qFYssmn9x2m30KTCDXT2liw0T12eFf1_bz37SPCr126jeIOfjgI" })

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Login_Manager = LoginManager(app)
