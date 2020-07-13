# gallery
Uma simples aplicação para galeria de imagens com recursos de propriedade e imagens publicas, views em lista ou cards 

## Configuração e uso

### Instalação dos programas necessários (sem docker)

Para instalar este aplicativo localmente em uma máquina devemos ter previamente instalados
alguns pacotes no seu SO, que são:

1. *Python 3.8.x:* ou maior;
2. *PostgresSQL:* versão 11 ou maior;
3. *Criar Ambiente virtual*;

### Tecnologias utilizadas

- *Django 3.0:* Optei pelo django em vez do Flask por ser uma plataforma mais robusta e segura para I/O de dados, e além de possuir ORM própio sem necessidade de ferramentas de terceiros;
- *PostgreSQL 12:* Banco de dados relacional para armazenamento de grandes quantidades de dados sem o risco de perda das informações;
- *JQuery:* Para o frontend optei por usar o ajax pela facilidade e por oferecer maior controle na manipulação do DOM. Ainda aguardo um framework que me ofereça todo o controle dos componentes como o JQuery;
- *Bootstrap 4:* Framework extremamente versártil com vários componentes e 100% integrado ao JQuery.

### Instalação da aplicação

```bash
git clone https://github.com/AlcindoSchleder/gallery.git
cd gallery

python3 -m venv venv
 
pip install -r requirements.txt
django-admin createsuperuser
```

Após o último comando você deve digitar o nome do usuário, e-mail e senha.
Desta forma está apto a fazer o login para acessar a administração do sistema.


### Execução local

```bash
./manage.py runserver
```
no browser digite: http://localhost:8000
para admin: http://localhost:8000/admin
 
### Testes

```bash
./manage.py tests
```

### Docker

#### Rodar a imagem pronta (via docker)

Basta usar o docker-compose run para rodar a imagem pronta

```bash
docker-compose up -d
```


#### Recursos

Utilize o menu Gallery para criar novas categorias e novas imagens ou pela administração da aplicação.
