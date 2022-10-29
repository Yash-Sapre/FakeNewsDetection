from flask import Flask,render_template, request
import pickle


app = Flask(__name__)
result = ''
file = open('C:/Users/yss05/OneDrive/Desktop/FakeNewsPrediction/model','rb')
model = pickle.load(file)
file.close()

file = open('C:/Users/yss05/OneDrive/Desktop/FakeNewsPrediction/cv','rb')
cv = pickle.load(file)
file.close()



@app.route("/",methods=['GET', 'POST'])
def hello_world():
    global model,cv,result
    if request.method == "POST":
        txt = [request.form['in']]
        mat = cv.transform(txt) 
        result = "Fake" if model.predict(mat) == [0] else "Not Fake"

    if result == "":
        return render_template('home.html')
    else :
        return render_template('home.html',result = result)