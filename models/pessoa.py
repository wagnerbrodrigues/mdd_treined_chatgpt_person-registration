class Pessoa:
    def __init__(self, id, nome_pessoa, token):
        self.id = id
        self.nome_pessoa = nome_pessoa
        self.token = token

    def to_dict(self):
        return {
            "id": self.id,
            "nome_pessoa": self.nome_pessoa,
            "token": self.token
        }
