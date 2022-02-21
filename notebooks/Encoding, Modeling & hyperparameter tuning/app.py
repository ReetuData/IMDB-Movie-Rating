import pandas as pd
from flask import Flask, jsonify, request
import pickle
#import request 
import json

# load model
model = pickle.load(open('model1.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)


# local url
url = 'http://127.0.0.1:5000/' 

# sample data
data = {'region': 'US',
'directors': 'nm0932055',
'Age_of_movie': 40,
'Decade': 'D3'}
data = json.dumps(data)

send_request = request.post(url, data)
print(send_request)

print(send_request.json())