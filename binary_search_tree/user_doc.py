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
        __hash__(): Retorna o hash baseado no id do usuário.
    """

    def __init__(self, id):
        """
        Inicializa um usuário com id e nome gerado.

        Args:
            id (int): Identificador único do usuário.
        """
        self.id = id  # Armazena o ID único do usuário

        # Lista de nomes base para gerar o nome do usuário
        user_names = [
            "Blake", "Ricky", "Shelley", "Dave", "George", "John", "James",
            "Mitch", "Williamson", "Burry", "Vennett", "Shipley", "Geller",
            "Rickert", "Carrell", "Baum", "Brownfield", "Lippmann", "Moses",
        ]

        # Gera o nome do usuário baseado no ID
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"

    def __eq__(self, other):
        """
        Verifica se dois usuários são iguais pelo id.

        Args:
            other (User): Outro usuário para comparação.

        Returns:
            bool: True se ids forem iguais, False caso contrário.
        """
        return isinstance(other, User) and self.id == other.id  # Compara usuários pelo ID

    def __lt__(self, other):
        """
        Verifica se o id do usuário é menor que o de outro.

        Args:
            other (User): Outro usuário para comparação.

        Returns:
            bool: True se id for menor, False caso contrário.
        """
        return isinstance(other, User) and self.id < other.id  # Verifica se o ID atual é menor

    def __gt__(self, other):
        """
        Verifica se o id do usuário é maior que o de outro.

        Args:
            other (User): Outro usuário para comparação.

        Returns:
            bool: True se id for maior, False caso contrário.
        """
        return isinstance(other, User) and self.id > other.id  # Verifica se o ID atual é maior

    def __repr__(self):
        """
        Retorna a representação em string do usuário.

        Returns:
            str: Nome do usuário.
        """
        return "".join(self.user_name)  # Retorna a string formatada do nome do usuário

    def __hash__(self):
        """
        Retorna o hash baseado no id do usuário.

        Returns:
            int: Hash do id.
        """
        return hash(self.id)  # Permite uso do objeto como chave em dicionários e em conjuntos


def get_users(num):
    """
    Gera uma lista de usuários com ids aleatórios.

    Args:
        num (int): Quantidade de usuários a serem gerados.

    Returns:
        list[User]: Lista de instâncias User.
    """
    random.seed(1)  # Define uma semente fixa para reprodutibilidade

    users = []  # Lista para armazenar os usuários gerados
    ids = []  # Lista para armazenar os ids disponíveis

    for i in range(num * 3):
        ids.append(i)  # Cria uma lista de possíveis IDs (3 vezes mais que o necessário)

    random.shuffle(ids)  # Embaralha os IDs

    ids = ids[:num]  # Seleciona os primeiros 'num' IDs após o embaralhamento

    for id in ids:
        user = User(id)  # Cria o usuário com o ID selecionado
        users.append(user)  # Adiciona o usuário à lista

    return users  # Retorna a lista de usuários