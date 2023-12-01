from py2neo import Graph, Node, Relationship

class RedeSocialNeo4j:
    def __init__(self):
        self.graph = Graph("bolt://localhost:7687", user="neo4j", password="12345678")

    def adicionar_pessoa(self, nome, idade, localizacao):
        query = f"MATCH (p:Pessoa {{nome: '{nome}'}}) RETURN p"
        result = self.graph.run(query)

        existing_person = result.data()
        if existing_person:
            print(f"Pessoa {nome} já existe no sistema.")
            return existing_person[0]['p']
        else:
            pessoa = Node("Pessoa", nome=nome, idade=idade, localizacao=localizacao)
            self.graph.create(pessoa)
            print(f"Pessoa {pessoa.identity} ({nome}) adicionada com sucesso.")
            return pessoa

    def listar_pessoas(self):
        query = "MATCH (p:Pessoa) RETURN ID(p) as id, p.nome as nome"
        result = self.graph.run(query)
        for row in result:
            print(f"ID: {row['id']}, Nome: {row['nome']}")

    def adicionar_amizade(self, id_pessoa1, id_pessoa2):
        query = (
            f"MATCH (p1:Pessoa), (p2:Pessoa) "
            f"WHERE ID(p1)={id_pessoa1} AND ID(p2)={id_pessoa2} "
            f"CREATE (p1)-[:AMIGO_DE]->(p2), (p2)-[:AMIGO_DE]->(p1)"
        )
        self.graph.run(query)
        print(f"Amizade entre ID {id_pessoa1} e ID {id_pessoa2} estabelecida.")

    def visualizar_amizades(self, id_pessoa):
        query = f"MATCH (p:Pessoa)-[:AMIGO_DE]-(amigo) WHERE ID(p)={id_pessoa} RETURN ID(amigo) as id, amigo.nome as nome"
        result = self.graph.run(query)
        amigos = [(row['id'], row['nome']) for row in result]
        print(f"Amigos de {id_pessoa}:")
        for amigo_id, amigo_nome in amigos:
            print(f"ID: {amigo_id}, Nome: {amigo_nome}")

    def remover_pessoa(self, id_pessoa):
        query = f"MATCH (p:Pessoa) WHERE ID(p)={id_pessoa} DETACH DELETE p"
        self.graph.run(query)
        print(f"Pessoa {id_pessoa} removida do sistema.")

# Função para exibir o menu
def exibir_menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar Pessoa")
    print("2. Listar Pessoas")
    print("3. Adicionar Amizade")
    print("4. Visualizar Amizades")
    print("5. Remover Pessoa")
    print("0. Sair")

# Exemplo de uso com menu interativo
rede_social_neo4j = RedeSocialNeo4j()

while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        localizacao = input("Digite a localização da pessoa: ")
        rede_social_neo4j.adicionar_pessoa(nome, idade, localizacao)
    elif escolha == "2":
        rede_social_neo4j.listar_pessoas()
    elif escolha == "3":
        id_pessoa1 = int(input("Digite o ID da primeira pessoa: "))
        id_pessoa2 = int(input("Digite o ID da segunda pessoa: "))
        rede_social_neo4j.adicionar_amizade(id_pessoa1, id_pessoa2)
    elif escolha == "4":
        id_pessoa = int(input("Digite o ID da pessoa: "))
        rede_social_neo4j.visualizar_amizades(id_pessoa)
    elif escolha == "5":
        id_pessoa = int(input("Digite o ID da pessoa a ser removida: "))
        rede_social_neo4j.remover_pessoa(id_pessoa)
    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
