class Comentario:
    def __init__(self, id, nome, email, comentario, curtida):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__comentario = comentario
        self.__curtida = curtida

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_comentario(self):
        return self.__comentario

    def get_curtida(self):
        return self.__curtida

    def set_nome(self, nome):
        self.__nome = nome

    def set_comentario(self, comentario):
        self.__comentario = comentario