from flask import render_template, redirect, url_for
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.estado_dao import EstadoDao

noticia_dao = NoticiaDao()
estado_dao = EstadoDao()


@app.route("/noticia/<int:id>")
def noticia(id):
    for noticia in noticia_dao.listar_noticias():
        if noticia.get_id() == id:
            return render_template("noticia.html", noticia=noticia, estados=estado_dao.listar_estados(), curtidas=noticia.get_curtidas())
    return render_template("home.html", estados=estado_dao.listar_estados(), noticias=noticia_dao.listar_noticias())


@app.route("/noticia/like/<int:id>")
def curtida(id):
    for noticia in noticia_dao.listar_noticias():
        if noticia.get_id() == id:
            noticia.add_curtida()
            return redirect(url_for("noticia", id=id))
