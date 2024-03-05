from faker import Faker

import pymysql
from os import environ

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


# Função para inserir escolas no banco de dados
def insert_pacientes(num_paciente):
    cursor.execute("SELECT id FROM unidades")
    unidades_id = [row[0] for row in cursor.fetchall()]
    for _ in range(num_paciente):
        nome = fake.first_name()
        data_nasc = fake.date_of_birth(minimum_age=11, maximum_age=100)
        endereco = fake.address()
        telefone = fake.phone_number()[:20]
        email = fake.email()
        # Selecionar uma unidade aleatória para associar o paciente
        cursor.execute("SELECT id FROM unidades ORDER BY RAND() LIMIT 1")
        unidades_id = cursor.fetchone()[0]
        cursor.execute(
                "INSERT INTO pacientes (nome, data_nasc, endereco, telefone, email, unidades_id) VALUES (%s, %s, %s, %s, %s, %s)", (nome, data_nasc, endereco, telefone, email, unidades_id))  # noqa E501
        db.commit()


# Inserir escolas
insert_pacientes(50)

# Fechar a conexão com o banco de dados
db.close()
