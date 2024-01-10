from flask import Flask, make_response
from flask_cors import CORS
from subprocess import run, CalledProcessError
import json

api = Flask(__name__)
CORS(api)

@api.route('/data', methods=['GET'])
def data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        response = make_response(data, 200)
        return response
    except FileNotFoundError:
        response = make_response("Le fichier 'data.json' n'a pas été correctement généré sur /scrape", 404)
        return response
        
@api.route('/scrape', methods=['GET'])
def scrape():
    try:
        run(['python3', 'scraper.py'], check=True)
        response = make_response('OK', 200)
        return response
    except CalledProcessError:
        response = make_response("Le scraper n'a pas réussi à récupérer les données", 403)
        return response

if __name__ == '__main__':
    api.run(debug=True)