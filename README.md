# Bem vindo ao projeto **Django Event Calendar**
<p><img height="20" src="https://img.shields.io/badge/Version-1.0.0-blue"/><img height="20" src="https://img.shields.io/badge/Project-EventCalendar-green"/></p>

A ideia deste projeto surgiu de várias pesquisas, com a ideia de criar um calendário de eventos. Criação de eventos que serão implementadas em um calendário de forma visual, que sejá  mais fácil de ver os horários disponíveis e o nível de prioridade dos eventos.

## Redes Sociais
* [Instagram](https://www.instagram.com/claudiogfez/)
* [Linkedin](https://www.linkedin.com/in/clcostaf/)

## Instalação

- Primeiramente você pode clonar este repositório.

```
$ git clone https://github.com/clcosta/DEC-django-event-calendar.git
```

- Agora a instalação das bibliotecas

```
pip install -r requirements.txt
```

## Como utilizar

- Com tudo já instalado precisamos iniciar o banco de dados !

```
python manage.py makemigrations

python manage.py migrate
```

- Agora só iniciar o servidor!
```
python manage.py runserver
```

### Tempo de Evento
**Durante o preenchimento do Formulário de criação do evento você pode alterar manualmente este valor.**

Caso queira manter os valores default, no arquivo _settings.py_ existe uma variável que determina a quantidade de tempo de cada evento, por padrão se não é determinada o valor default é 60 minutos, a partir da hora atual.    
Podendo ser alterada determinando a seguinte variável:
```py
TEMPO_EVENTO = 60
```

### Criando um evento

- **Podemos Criar um evento preenchendo o Formulário de criação do evento:**

    ![Formulário-Criar-Evento](https://i.ibb.co/Th2bTDT/image.png)

### Visualizando o evento

- **Temos basicamente três formas de visualizar os eventos, sendo a primeria no calendario**

    _No Calendario só vai aparecer os eventos que não estão marcados como concluido, separado por cores de acordo com o nivel de prioridade do evento!_
    
    - ![Calendario1](https://i.ibb.co/tcqW8pn/image.png)

    _É possivel modificar a visualização nos botões em cima do calendario_    

    - ![Calendario2](https://i.ibb.co/8XJjyS7/image.png)

- **A Segunda Forma de visualizar os eventos é pela lista de eventos**

    _Na lista de eventos mesmo os eventos marcados como concluído vão ser mostrados, por padrão a ordenação da lista é na ordem de prioridade, da mais alta para a mais baixa._

    - ![ListaEvents1](https://i.ibb.co/yFfSCQd/image.png)

    _Pode-se aplicar um filtro de busca no campo de **"Procurar"**, onde será feita um busca por toda lista de eventos que tenha o nome escrito, também pode-se pesquisar por data e prioridade._

    - ![ListaEvents1](https://i.ibb.co/Y3bgQny/image.png)

- **A Terceira Forma de visualizar os eventos, é pela lista de eventos no botão azul, onde vamos pros detalhes do evento**

    _Nos detalhes temos as informações de nome, descricão, datas, nivel de prioridade e status._    
    **Se o evento não estiver concluído terá um botão para atualizar o status do evento.**

    - ![EventDetail](https://i.ibb.co/XjnGqZJ/image.png)


### Modificando o evento

- _Se o evento não estiver concluído terá um botão para atualizar o status do evento dentro da visualização dos detalhes, ou na lista de eventos no botão amarelo._

    - ![UpdateEvent](https://i.ibb.co/W0xSVYn/image.png)

### Excluindo o evento

- _Para excluir o evento, na lista de eventros terá um botão vermelhor que vai redirecionar para uma página de confirmação da exclusão do evento._

    - ![DeleteEvent](https://i.ibb.co/K98n7kH/image.png)

## Autor
| [<img src="https://avatars.githubusercontent.com/u/83929403?v=4" width=120><br><sub>@clcostaf</sub>](https://github.com/clcosta) |
| :---: |
