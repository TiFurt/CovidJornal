class Estado:   

    def __init__(self, id, nome, uf, flag):
        self.__id = id
        self.__nome = nome
        self.__uf = uf
        self.__flag = flag
        self.__noticia_lista = []
    
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_uf(self):
        return self.__uf

    def get_flag(self):
        return self.__flag

    def get_noticias(self):
        return self.__noticia_lista
    
    def set_noticia(self, noticia):
        self.__noticia_lista.append(noticia)
