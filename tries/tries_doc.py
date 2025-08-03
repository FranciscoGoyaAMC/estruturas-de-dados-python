class Trie:
    """
    Classe Trie implementa uma árvore de prefixos para armazenar e buscar palavras de forma eficiente.

    Métodos:
        add(word): Adiciona uma palavra ao trie.
        exists(word): Verifica se uma palavra existe no trie.
        search_level(current_level, current_prefix, words): Busca recursiva de palavras a partir de um prefixo.
        words_with_prefix(prefix): Retorna todas as palavras que começam com o prefixo.
        find_matches(document): Encontra todas as substrings do documento presentes no trie.
        longest_common_prefix(): Retorna o maior prefixo comum entre todas as palavras do trie.
        advanced_find_matches(document, variations): Busca substrings considerando variações de caracteres.
    """

    def __init__(self):
        """
        Inicializa o trie com um dicionário raiz vazio e um símbolo especial para marcar o fim de palavra.
        """
        self.root = {}  # Dicionário raiz do trie
        self.end_symbol = "*"  # Símbolo especial para indicar fim de palavra

    def add(self, word):
        """
        Adiciona uma palavra ao trie.

        Args:
            word (str): Palavra a ser inserida.
        """
        current_level = self.root  # Começa na raiz
        for char in word:  # Para cada caractere da palavra
            if char not in current_level:
                current_level[char] = {}  # Cria novo nível se necessário
            current_level = current_level[char]  # Avança para o próximo nível
        current_level[self.end_symbol] = True  # Marca o fim da palavra

    def exists(self, word):
        """
        Verifica se uma palavra existe no trie.

        Args:
            word (str): Palavra a ser buscada.

        Returns:
            bool: True se a palavra existe, False caso contrário.
        """
        current = self.root  # Começa na raiz
        for char in word:  # Para cada caractere da palavra
            if char not in current:
                return False  # Se faltar algum caractere, não existe
            current = current[char]  # Avança para o próximo nível
        return self.end_symbol in current  # Só existe se o fim de palavra estiver marcado
 
    def search_level(self, current_level, current_prefix, words):
        """
        Busca recursiva de todas as palavras a partir de um determinado nível e prefixo.

        Args:
            current_level (dict): Nível atual do trie.
            current_prefix (str): Prefixo acumulado até aqui.
            words (list): Lista para armazenar as palavras encontradas.

        Returns:
            list: Lista de palavras encontradas.
        """
        if self.end_symbol in current_level:
            words.append(current_prefix)  # Se encontrou fim de palavra, adiciona à lista
        current_sorted = sorted(current_level)  # Ordena os caracteres para busca ordenada
        for char in current_sorted:
            if char != self.end_symbol:
                new_prefix = current_prefix + char  # Atualiza o prefixo
                self.search_level(current_level[char], new_prefix, words)  # Busca recursiva
        return words

    def words_with_prefix(self, prefix):
        """
        Retorna todas as palavras do trie que começam com o prefixo fornecido.

        Args:
            prefix (str): Prefixo a ser buscado.

        Returns:
            list: Lista de palavras que começam com o prefixo.
        """
        matching_words = []  # Lista para armazenar as palavras encontradas
        current_level = self.root  # Começa na raiz
        for char in prefix:  # Para cada caractere do prefixo
            if char not in current_level:
                return matching_words  # Se faltar algum caractere, retorna lista vazia
            current_level = current_level[char]  # Avança para o próximo nível
        self.search_level(current_level, prefix, matching_words)  # Busca todas as palavras a partir daqui
        return matching_words
  
    def find_matches(self, document):
        """
        Encontra todas as substrings do documento que estão presentes no trie.

        Args:
            document (str): Texto a ser analisado.

        Returns:
            set: Conjunto de substrings encontradas.
        """
        matches = set()  # Conjunto para armazenar as correspondências
        for i in range(len(document)):  # Para cada posição inicial no texto
            current_level = self.root  # Começa na raiz
            for j in range(i, len(document)):  # Para cada posição final
                char = document[j]
                if char not in current_level:
                    break  # Se não encontrar o caractere, para
                current_level = current_level[char]
                if self.end_symbol in current_level:
                    matches.add(document[i:j+1])  # Adiciona substring encontrada
        return matches

    def longest_common_prefix(self):
        """
        Retorna o maior prefixo comum entre todas as palavras do trie.

        Returns:
            str: O maior prefixo comum.
        """
        current_level = self.root  # Começa na raiz
        prefix = ''  # Prefixo acumulado
        while True:
            child = list(current_level.keys())  # Lista de filhos do nível atual
            if self.end_symbol in child:
                break  # Se encontrar fim de palavra, para
            if len(child) == 1:
                prefix += child[0]  # Adiciona o único caractere ao prefixo
                current_level = current_level[child[0]]  # Avança para o próximo nível
            else:
                break  # Se houver bifurcação, para
        return prefix

    def advanced_find_matches(self, document, variations):
        """
        Busca substrings no documento considerando variações de caracteres.

        Args:
            document (str): Texto a ser analisado.
            variations (dict): Dicionário de variações de caracteres (ex: {'á': 'a'}).

        Returns:
            set: Conjunto de substrings encontradas considerando variações.
        """
        matches = set()  # Conjunto para armazenar as correspondências
        for i in range(len(document)):  # Para cada posição inicial no texto
            current_level = self.root  # Começa na raiz
            for j in range(i, len(document)):  # Para cada posição final
                char = document[j]
                if char in variations:
                    char_to_check = variations[char]  # Usa a variação se existir
                else:
                    char_to_check = char  # Caso contrário, usa o próprio caractere
                if char_to_check not in current_level:
                    break  # Se não encontrar, para
                current_level = current_level[char_to_check]
                if self.end_symbol in current_level:
                    matches.add(document[i:j+1])  # Adiciona substring encontrada
        return matches
