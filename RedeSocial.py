import networkx as nx

class RedeSocial:
    def __init__(self):
        self.grafo = nx.Graph()
        self.id_contador = 1  # Contador para gerar IDs únicos

    def adicionar_pessoa(self, nome, idade, localizacao):
        pessoa_id = self.id_contador
        self.grafo.add_node(pessoa_id, nome=nome, idade=idade, localizacao=localizacao)
        self.id_contador += 1
        print(f"Pessoa {pessoa_id} ({nome}) adicionada com sucesso.")

    def listar_pessoas(self):
        for node in self.grafo.nodes(data=True):
            print(f"ID: {node[0]}, Nome: {node[1]['nome']}")

    def adicionar_amizade(self, id_pessoa1, id_pessoa2):
        if self.grafo.has_edge(id_pessoa1, id_pessoa2):
            print("Essa amizade já existe.")
        elif id_pessoa1 not in self.grafo.nodes or id_pessoa2 not in self.grafo.nodes:
            print("Pelo menos uma das pessoas não existe.")
        else:
            self.grafo.add_edge(id_pessoa1, id_pessoa2, tipo_relacao="amigo_de")
            print(f"Amizade entre ID {id_pessoa1} e ID {id_pessoa2} estabelecida.")

    def visualizar_amizades(self, id_pessoa):
        if id_pessoa not in self.grafo.nodes:
            print("Essa pessoa não existe.")
        else:
            amigos = list(self.grafo.neighbors(id_pessoa))
            print(f"Amigos de {id_pessoa}:")
            for amigo in amigos:
                print(f"ID: {amigo}, Nome: {self.grafo.nodes[amigo]['nome']}")

    def remover_pessoa(self, id_pessoa):
        if id_pessoa not in self.grafo.nodes:
            print("Essa pessoa não existe.")
        else:
            self.grafo.remove_node(id_pessoa)
            print(f"Pessoa {id_pessoa} removida do sistema.")

# Exemplo de uso
rede_social = RedeSocial()

# Adiciona algumas pessoas
rede_social.adicionar_pessoa("Alice", 25, "Cidade A")
rede_social.adicionar_pessoa("Bob", 30, "Cidade B")
rede_social.adicionar_pessoa("Charlie", 22, "Cidade C")

# Lista as pessoas cadastradas
print("\nPessoas Cadastradas:")
rede_social.listar_pessoas()

# Adiciona relações de amizade
rede_social.adicionar_amizade(1, 2)
rede_social.adicionar_amizade(1, 3)

# Tenta adicionar amizade duplicada
rede_social.adicionar_amizade(1, 2)

# Tenta adicionar amizade com pessoa inexistente
rede_social.adicionar_amizade(1, 4)

# Visualiza a rede de amizades de uma pessoa específica
rede_social.visualizar_amizades(1)

# Tenta visualizar amizades de pessoa inexistente
rede_social.visualizar_amizades(4)

# Remove uma pessoa
rede_social.remover_pessoa(2)

# Tenta remover pessoa inexistente
rede_social.remover_pessoa(4)

# Lista as pessoas após a remoção
print("\nPessoas Cadastradas Após Remoção:")
rede_social.listar_pessoas()
