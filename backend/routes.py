from . import app
from .password_generator import generate_password
import os
import json
from flask import jsonify, request, make_response, abort, url_for 


@app.route('/', methods=['GET', 'POST'])
def generate_Password():
    greeting = 'Create Secure, Strong Password Fast And Easy Create a POST request With This Inputs: (passwordLength,  IncludeSymbols,  IncludeNumbers,   IncludeLowerCaseCharters,  IncludeUpperCaseCharters,   ExcludeSimilarCharacters,  ExcludeAmbiguousCharaters)'
    
    if request.method == 'POST':    
        passwordData = request.json

        passwordLength = passwordData['passwordLength'] 
        IncludeSymbols = passwordData['IncludeSymbols'] 
        IncludeNumbers = passwordData['IncludeNumbers'] 
        IncludeLowerCaseCharters = passwordData['IncludeLowerCaseCharters'] 
        IncludeUpperCaseCharters = passwordData['IncludeUpperCaseCharters'] 
        ExcludeSimilarCharacters = passwordData['ExcludeSimilarCharacters'] 
        ExcludeAmbiguousCharaters = passwordData['ExcludeAmbiguousCharaters'] 
        # generate_password()
    return json.dumps(greeting)