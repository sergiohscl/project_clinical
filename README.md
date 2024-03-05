# SCRIPT CLINICAS MÉDICAS

## Foi criado um script para cada tabela para popular o banco com dados fakes.

### AMBIENTE VIRTUAL
python -m venv venv

### ATIVANDO AMBIENTE VIRTUAL
. venv/bin/activate

### INSTALANDO BIBLIOTECA FAKER
pip install Faker

### INSTALANDO BIBLIOTECA PYMYSQL PARA CONECTAR Banco Dados
pip install pymysql

### CRIANDO ARQUIVO REQUIREMENTS
pip freeze > requirements.txt

### DEPENDÊNCIAS DO PROJETO
pip install -r requirements.txt

### RODANDO ENV
source .env

### RODANDO SCRIPTS
python3 <nome_arquivo>

## Configurar o git
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
git push -u origin main