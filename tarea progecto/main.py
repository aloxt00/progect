from flask import Flask, render_template


app = Flask(__name__)

def calk(value,value2,value3,value4):
    cal = value+value2+value3+value4
    if calk==12 or 11 or 10 or 8 or 9:
        return "cambia tu estilo de vida haora es muy dallino para el medio anbiente"
    elif calk==8 or 9 or 6 or 7:
        return "sigue asi estan ni tan mal ni tan bien"
    elif calk==4 or 5:
        return "eres muy bueno para el medio anbiente"
    else:
        return "a abido un eror, intenta otraves"

    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<value>')
def cuetionario_1(value):
    return render_template('cuetionario 1.html',
                           value=value)

@app.route('/<value2>')
def cuetionario_2(value,value2):
    return render_template('cuetionario 2.html',
                           value=value,
                           value2=value2)
@app.route('/<value3>')
def cuetionario_3(value,value2,value3):
    return render_template('cuetionario 3.html',
                           value=value,
                           value2=value2,
                           value3=value3)
@app.route('/<value4>')
def cuetionario_4(value,value2,value3,value4):
    return render_template('cuetionario 4.html',
                           value=value,
                           value2=value2,
                           value3=value3,
                           value4=value4)
@app.route('/<result>')
def result(result):
    return render_template("resultado.html")



app.run(debug=True)














