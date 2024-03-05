CREATE TABLE IF NOT EXISTS unidades (
   id INT NOT NULL AUTO_INCREMENT,
   nome_unidade VARCHAR(255) NOT NULL,
   nome_fantasia VARCHAR(255) NOT NULL,
   endereco VARCHAR(255) NOT NULL,
   CNPJ VARCHAR(20) NOT NULL,  
   PRIMARY KEY (id)
);

 CREATE TABLE IF NOT EXISTS pacientes (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    data_nasc DATE NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    telefone  VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    unidades_id INT NOT NULL,
    FOREIGN KEY (unidades_id) REFERENCES unidades (id) ON DELETE CASCADE,
    PRIMARY KEY (id)
);