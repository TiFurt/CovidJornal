from application.model.dao import lista_noticias
from application.model.dao import bubble_sort
from application.model.entity.comentario import Comentario


class NoticiaDao:
    def listar_noticias(self):
        return lista_noticias

    def listar_mais_curtidas(self):
        return bubble_sort(lista_noticias)

    def add_comentario(self, id, nome, email, comentario, curtida):
        for noticia in lista_noticias:
            if noticia.get_id() == id:
                id_comentario = len(noticia.get_comentarios()) + 1
                noticia.add_comentario(Comentario(id_comentario, nome, email, comentario, curtida))


    def listar_comentarios(self, id):
        return lista_noticias[id].get_comentarios()



