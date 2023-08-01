from flask import Flask, jsonify, json, request

#initial the app 
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_Password():
    greeting = 'Create Secure, Strong Password Fast And Easy Create a POST request With This Inputs: (passwordLength  IncludeSymbols  IncludeNumbers   IncludeLowerCaseCharters  IncludeUpperCaseCharters   ExcludeSimilarCharacters  ExcludeAmbiguousCharaters)'
    
    if request.method == 'POST':
        return json.dumps({'greeting': 'BuidlingYourpass'})


    return json.dumps(greeting)

if __name__ == '__main__':
    app.run(debug=True)