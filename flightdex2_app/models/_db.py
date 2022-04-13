from flask_sqlalchemy import SQLAlchemy


# SHARED DATABASE FOR MODELS IN SEPARATE .PY FILES.
# MODELS.__INIT__.PY IMPORTS DB (AS WELL AS OTHER MODELS) AND
# THEN THE MAIN __INIT__.PY FOR THE APP WILL IMPORT * FROM MODELS.__INIT__.PY.


db = SQLAlchemy()