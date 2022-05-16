from flask import render_template
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.estado_dao import EstadoDao

noticia_dao = NoticiaDao()
estado_dao = EstadoDao()


@app.route("/")
def home():
    return render_template("home.html", estados=estado_dao.listar_estados(), noticias=noticia_dao.listar_noticias(),
                           maisCurtidas=noticia_dao.listar_mais_curtidas())
