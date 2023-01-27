# Api utilizando Django

Desenvolva um projeto de Web API de pontos turísticos com Python + Django + Django Rest Framework e deploy no Heroku, utilizando as melhores práticas de desenvolvimento de software, desenvolvimento de web API's e de deploy seguro e confiável utilizando o PaaS Heroku.

Neste curso desenvolveremos e colocaremos no ar ( publicado na web ) um projeto com as seguintes características:

RESTful Web API para exposição de pontos turísticos de uma região

* Propor um novo ponto turístico

* Moderação dos pontos turísticos cadastrados

* Listagem básica dos pontos turísticos ( Lista resumida )

* Listagem completa dos pontos turísticos

* Detalhe de um ponto turístico

* Atualização de um ponto turístico por usuários autorizados

* Deleção de um ponto turístico por usuários autorizados

### 📋 Pré-requisitos

- Linux 
- PostgreSQL mais recente
- Python 3.10
- pip (https://pip.pypa.io/en/stable/)
- virtualenv 

### 🔧 Instalação

1. Instale o virtualenvwrapper:
```bash
sudo apt install python3-pip python-dev build-essential
sudo pip install virtualenv
```

2. Crie um ambiente virtual :

```bash
virtualenv nome_da_virtualenv
```

3. Ativando uma virtualenv:

- Linux ou macOS: 

```bash
source nome_da_virtualenv/bin/activate 
```
- Windows: 

```bash
nome_da_virtualenv/Scripts/Activate 
```

4. Obtenha o código:
```bash
git clone https://github.com/leocassiosilva/api_django.git
```

5. Instale as dependências utilizando o pip:
```bash
pip install -r requirements.txt
```

6. Instale as dependências utilizando o pip:
```bash
pip install -r requirements.txt
```

7. Executar as migrações do proojeto no banco de dados:
```bash
python manage.py migrate
```

8. Executar o projeto:
```bash
python manage.py runserver
```

## 🛠️ Construído com
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src ="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www. python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## ✒️ Autores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/leocassiosilva">
        <img src="https://avatars.githubusercontent.com/u/56235626?s=400&u=e1d65eb62c2af0330761629420be56f266033655&v=4" width="100px;" alt="Foto de Leocassio Silva no GitHub"/><br>
        <sub>
          <b>Leocassio</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


