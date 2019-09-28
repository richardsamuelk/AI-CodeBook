from flask import Flask,request,jsonify,render_template
from sklearn.externals import joblib
import pandas as pd
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('housing.html')


@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)

     print(query_df)
     prediction = regressor.predict(query_df)
     return jsonify({'prediction': list(prediction)})

@app.route('/train', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)

     print(query_df)
     prediction = regressor.fit(query_df)
     return 'Train score:',regressor.score(X_train, y_train)


@app.route('/result', methods=['POST'])
def result():
     json_ = request.form.to_dict(flat=False)
     print(json_)
     query_df = pd.DataFrame(json_)
     prediction = regressor.predict(query_df)
     log.info("PREDICTION REQUEST","inputs :", output :);
     #return jsonify({'prediction': list(prediction)})
     return render_template('result.html',results=list(prediction))


if __name__ == '__main__':
	regressor = joblib.load('housing_price_modelv1.pkl')
	app.run(port=5000)
