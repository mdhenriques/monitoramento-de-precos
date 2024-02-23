class Produto:
    def __init__(self, nome, preco, avaliacao_media, num_avaliacoes):
        self.nome = nome
        self.preco = preco
        self.avaliacao_media = avaliacao_media
        self.num_avaliacoes = num_avaliacoes

    def __str__(self):
        return f"Produto: {self.nome}\nPreço: {self.preco}\nAvaliação Média: {self.avaliacao_media}\nNúmero de Avaliações: {self.num_avaliacoes}"


