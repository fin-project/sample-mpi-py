
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mpi_test_secret'
app.config['KEY_PATH'] = "./key"

app.config['TEST_MID'] = "000000000000033"
app.config['MPI_URL'] = "https://devlinkv2.paydee.co/mpigw"

from project import routes