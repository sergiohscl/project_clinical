from faker import Faker

import pymysql
from os import environ
import random

# Conectar ao banco de dados
db = pymysql.connect(
    host=environ["DB_LOCALHOST"],
    user=environ["DB_USER"],
    password=environ["DB_PASSWORD"],
    database=environ["DB_DATABASE"],
)
cursor = db.cursor()

# Inicializar o Faker
fake = Faker()


# Função para gerar número de CNPJ
def generate_cnpj(punctuation=False):
    n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
    v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
    # calcula dígito 1 e acrescenta ao total
    s = sum(x * y for x, y in zip(reversed(n), v))
    d1 = 11 - s % 11
    if d1 >= 10:
        d1 = 0
    n.append(d1)
    # idem para o dígito 2
    s = sum(x * y for x, y in zip(reversed(n), v))
    d2 = 11 - s % 11
    if d2 >= 10:
        d2 = 0
    n.append(d2)
    if punctuation:
        return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)
    else:
        return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)


# Função para inserir escolas no banco de dados
def insert_unidades(num_unidade):
    for _ in range(num_unidade):
        nome_unidade = fake.company()
        nome_fantasia = fake.unique.company_suffix()
        endereco = fake.address()
        CNPJ = generate_cnpj()
        cursor.execute(
            "INSERT INTO unidades (nome_unidade, nome_fantasia, endereco, CNPJ) VALUES (%s, %s, %s, %s)", (nome_unidade, nome_fantasia, endereco, CNPJ))  # noqa E501
        db.commit()


# Inserir escolas
insert_unidades(3)

# Fechar a conexão com o banco de dados
db.close()
