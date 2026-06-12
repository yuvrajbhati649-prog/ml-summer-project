from flask import Flask,request,jsonify
import joblib
import numpy as np
from flask import Response
app=Flask(__name__)
#load the model once
model=joblib.load("rf_model.pk1")
@app.route('/predict',methods=['POST'])
def predict() -> Response:
    try:
        data=request.get_json()
        input_data=np.array(data['input']).reshape(1,-1)
        prediction=model.predict(input_data)
        return jsonify({'prediction':int(prediction[0])})
    except Exception as o:
        return jsonify({'error':str(0)})
    
if __name__=='__main__':
    app.run(debug=True)
