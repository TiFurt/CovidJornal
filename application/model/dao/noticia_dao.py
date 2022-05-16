from application.model.dao import lista_noticias
from application.model.dao import bubble_sort


class NoticiaDao:
    def listar_noticias(self):
        return lista_noticias

    def listar_mais_curtidas(self):
        return bubble_sort(lista_noticias)



