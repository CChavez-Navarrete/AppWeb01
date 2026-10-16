from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html', titulo='Home',mensaje='Bienvenido a mi sitio web')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Estos son los servicios que ofrecemos')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contacto', mensaje='Contáctanos')

@app.route('/productos')
def productos():
    return render_template('productos.html', titulo='Productos', mensaje='Estos son los productos que ofrecemos')





if __name__ == '__main__':
    app.run(debug=True,port=5050)