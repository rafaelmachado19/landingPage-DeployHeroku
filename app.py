from flask import Flask, render_template


app = Flask (__name__)

#criar a primeira pagina do site
#route ->  dominio.com/formulario
#templates
@app.route("/")
#função -> o que voce quer exibir na pagina
def homepage ():
 return render_template("homepage.html")

#route ->  dominio.com/formulario
@app.route("/saude")
#função -> o que voce quer exibir na pagina
def saude():
   return render_template ("saude.html")

@app.route("/usuarios/<nome_usuario>")
def usarios(nome_usuario):
   return render_template ("usuarios.html", nome_usuario=nome_usuario)
#colocar o site no ar
if __name__ == "__main__":
   app.run (debug=True)

   #depoly do heroku

