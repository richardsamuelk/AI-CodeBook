from flask import Flask, jsonify,request,render_template
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)

     print(query_df)
     # query = pd.get_dummies(query_df)
     prediction = regressor.predict(query_df)
     return jsonify({'prediction': list(prediction)})

@app.route('/')
@app.route('/index')
def index():
    return render_template('housing.html')

@app.route('/result', methods=['POST'])
def result():
     json_ = request.form.to_dict(flat=False)
     print(json_)
     query_df = pd.DataFrame(json_)

     print(query_df)
     # query = pd.get_dummies(query_df)
     prediction = regressor.predict(query_df)
     return jsonify({'prediction': list(prediction)})


if __name__ == '__main__':
     regressor = joblib.load('housing_price_modelv1.pkl',mmap_mode='r')
     app.run(port=5000)