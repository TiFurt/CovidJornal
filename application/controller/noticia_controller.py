from flask import render_template, redirect, url_for, request
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.estado_dao import EstadoDao

noticia_dao = NoticiaDao()
estado_dao = EstadoDao()


@app.route("/noticia/<int:id>")
def noticia(id):
    for noticia in noticia_dao.listar_noticias():
        if noticia.get_id() == id:
            noticia.add_visualizacao()
            return render_template("noticia.html", noticia=noticia, estados=estado_dao.listar_estados(),
                                   like=noticia.get_like())
    return render_template("home.html", estados=estado_dao.listar_estados(), noticias=noticia_dao.listar_noticias())


@app.route("/noticia/like/<int:id>")
def like(id):
    for noticia in noticia_dao.listar_noticias():
        if noticia.get_id() == id:
            noticia.add_like()
            return redirect(url_for("noticia", id=id))


@app.route("/noticia/dislike/<int:id>")
def dislike(id):
    for noticia in noticia_dao.listar_noticias():
        if noticia.get_id() == id:
            noticia.add_dislike()
            return redirect(url_for("noticia", id=id))


@app.route("/comentario/salvar/<int:id>", methods=['POST', 'GET'])
def salvar(id):
    nome = request.form.get('nome', 'none')
    email = request.form.get('email', 'none')
    comentario = request.form.get('comentario', 'none')
    curtida = (request.form.get('curtida', 'none'))
    curtida_boolean = bool(curtida)
    for noticia in noticia_dao.listar_noticias():
        if noticia.get_id() == id:
            noticia_dao.add_comentario(id, nome, email, comentario, curtida_boolean)
            return redirect(url_for("noticia", id=id))
    return redirect(url_for("noticia", id=id))
