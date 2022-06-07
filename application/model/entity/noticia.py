class Noticia:

    def __init__(self, id, titulo, subtitulo, conteudo, estado, imagem, data):
        self.__id = id
        self.__titulo = titulo
        self.__subtitulo = subtitulo
        self.__conteudo = conteudo
        self.__estado = estado
        self.__imagem = imagem
        self.__data = data
        self.__like = 0
        self.__dislike = 0
        self.__visualizacoes = 0
        self.__comentarios = []

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

    def add_like(self):
        self.__like += 1

    def get_like(self):
        comment_like = 0
        for comentario in self.__comentarios:
            if comentario.get_curtida():
                comment_like += 1
        return self.__like + comment_like

    def add_dislike(self):
        self.__dislike += 1

    def get_dislike(self):
        comment_dislike = 0
        for comentario in self.__comentarios:
            if not comentario.get_curtida():
                comment_dislike += 1
        return self.__dislike + comment_dislike

    def add_comentario(self, comentario):
        self.__comentarios.append(comentario)

    def get_comentarios(self):
        return self.__comentarios

    def add_visualizacao(self):
        self.__visualizacoes += 1

    def get_visualizacoes(self):
        return self.__visualizacoes