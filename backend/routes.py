from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for 


@app.route('/', methods=['GET', 'POST'])
def generate_Password():
    greeting = 'Create Secure, Strong Password Fast And Easy Create a POST request With This Inputs: (passwordLength  IncludeSymbols  IncludeNumbers   IncludeLowerCaseCharters  IncludeUpperCaseCharters   ExcludeSimilarCharacters  ExcludeAmbiguousCharaters)'
    
    if request.method == 'POST':    
        os = request.json
        return json.dumps(os)

    return json.dumps(greeting)