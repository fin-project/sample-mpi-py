
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mpi_test_secret'
app.config['KEY_PATH'] = "./key"

app.config["TEST_MPI_URL"] = "tx"
app.config['TEST_MID'] = "000000000000033"
app.config["TEST_APP_KEY"] = "txid"
app.config['MPI_URL'] = "https://devlink.paydee.co/mpi"

from project import routes