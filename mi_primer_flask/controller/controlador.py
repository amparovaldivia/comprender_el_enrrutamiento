from mi_primer_flask import  app

@app.route('/')
def  hola_mundo():
    return 'hola mundo!'

@app.route('/dojo')
def clan ():
    return 'dojo'    

@app.route('/say/<flask>')
def decir(flask):
    print(flask)
    return 'say,'+flask  

@app.route('/repeat/<string:hello>/<int:num>')
def repetir (hello,num):
    if type(hello) is not str:
        return "el nombre debe ser string"
    if type(num) is not int: 
        return "el elemento debe ser un entero"   
    return f'hello{hello*35}'          
@app.errorhandler(404)
def error (e):
    return 'Lo siento'
