from flask import Flask, escape, request, render_template
import numpy as np
import pickle
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello():
    #name = request.args.get("name", "World")
    return render_template('index.html')
	
@app.route('/predict',methods=['POST'])
def predict():
	#data = request.get_json(force=True)
        n1 = int(request.form['inp1'])
        n2 = int(request.form['inp2'])
        n3 = int(request.form['inp3'])
        n4 = int(request.form['inp4'])
        n5 = int(request.form['inp5'])
        n6= int(request.form['inp6'])
        n7 = int(request.form['inp7'])
        f=[n1,n2,n3,n4,n5,n6,n7]
        final_f = np.array([f])
        prediction = model.predict(final_f)
        result= str(prediction[0])
        return render_template('index.html',prediction_text="Predicted o/p is:  {}".format(result))

if __name__ == "__main__":
    app.run(debug=True)		