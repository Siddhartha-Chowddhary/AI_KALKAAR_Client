from Imports import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '46d43883b3b396b34c48587f015be5d62694e08d198a1a4d215af19a1555'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_BINDS'] = {'PAINTINGS': 'sqlite:///PAINTINGS.db',
                                  'BUY_PROPOSAL': 'sqlite:///BUY_PROPOSAL.db'}

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Login_Manager = LoginManager(app)

