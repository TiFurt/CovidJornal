from flask import render_template, redirect, url_for
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.estado_dao import EstadoDao

noticia_dao = NoticiaDao()
estado_dao = EstadoDao()


@app.route("/estado/<string:uf>")
def noticias_do_estado(uf):
    for estado in estado_dao.listar_estados():
        if estado_dao.listar_estados()[estado].get_uf() == uf.upper() and estado_dao.listar_estados()[estado].get_noticias() != []:
            return render_template("noticias-estado.html", noticias=estado_dao.listar_estados()[estado].get_noticias(), estados=estado_dao.listar_estados())
    return render_template("home.html", estados=estado_dao.listar_estados(), noticias=noticia_dao.listar_noticias())
