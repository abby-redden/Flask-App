from flask import Flask, render_template

 

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('base.html')



@app.route('/cooking')
def cooking_info():
    return render_template('cooking.html')



@app.route('/hiking')
def hiking_details():
    return render_template('hiking.html')



@app.route('/photography')
def photography_world():
    return render_template('photography.html')



if __name__ == '__main__':
    app.run(debug=True)



