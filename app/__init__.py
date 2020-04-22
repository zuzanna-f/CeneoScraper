#import bibliotek
from flask import Flask

#utworzenie instancji (obiektu) klasy Flask reprezentującej aplikację
app = Flask(__name__)

from app import routes

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)