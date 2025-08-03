import random


class User:
    """
    Classe User representa um usuário com identificador único e nome gerado.

    Atributos:
        id (int): Identificador único do usuário.
        user_name (str): Nome do usuário gerado a partir de uma lista fixa.

    Métodos:
        __eq__(other): Verifica igualdade entre usuários pelo id.
        __lt__(other): Compara se o id do usuário é menor que o de outro.
        __gt__(other): Compara se o id do usuário é maior que o de outro.
        __repr__(): Retorna a representação em string do usuário.
    """

    def __init__(self, id):
        """
        Inicializa um usuário com id e nome gerado.

        Args:
            id (int): Identificador único do usuário.
        """
        self.id = id
        user_names = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"

    def __eq__(self, other):
        """
        Verifica se dois usuários são iguais pelo id.

        Args:
            other (User): Outro usuário para comparação.

        Returns:
            bool: True se ids forem iguais, False caso contrário.
        """
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other):
        """
        Verifica se o id do usuário é menor que o de outro.

        Args:
            other (User): Outro usuário para comparação.

        Returns:
            bool: True se id for menor, False caso contrário.
        """
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other):
        """
        Verifica se o id do usuário é maior que o de outro.

        Args:
            other (User): Outro usuário para comparação.

        Returns:
            bool: True se id for maior, False caso contrário.
        """
        return isinstance(other, User) and self.id > other.id

    def __repr__(self):
        """
        Retorna a representação em string do usuário.

        Returns:
            str: Nome do usuário.
        """
        return "".join(self.user_name)


def get_users(num):
    """
    Gera uma lista de usuários com ids aleatórios.

    Args:
        num (int): Quantidade de usuários a serem gerados.

    Returns:
        list[User]: Lista de instâncias User.
    """
    random.seed(1)
    users = []
    ids = []
    for i in range(num * 3):
        ids.append(i)
    random.shuffle(ids)
    ids = ids[:num]
    for id in ids:
        user = User(id)
        users.append(user)
    return users
