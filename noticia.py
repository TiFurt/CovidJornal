class Noticia:

    def __init__(self, id, titulo, subtitulo, conteudo, estado, imagem, data):
        self.__id = id
        self.__titulo = titulo
        self.__subtitulo = subtitulo
        self.__conteudo = conteudo
        self.__estado = estado
        self.__imagem = imagem
        self.__data = data

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_subtitulo(self):
        return self.__subtitulo

    def get_conteudo(self):
        return self.__conteudo

    def get_estado(self):
        return self.__estado

    def get_imagem(self):
        return self.__imagem

    def get_data(self):
        return self.__data
