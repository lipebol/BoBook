<h1 align="center">
        BoBook
</h1>

<h4 align="center">
  Book Search Bot
</h4>
<h6 align="center">by way of WhatsApp</h6>

<p align="center">

  <img src="https://img.shields.io/static/v1?label=Python3&message=*&color=FFD700&style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/static/v1?label=Flask&message=*&color=03AB5D&style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/static/v1?label=Twilio&message=*&color=D14141&style=for-the-badge&logo=twilio"/>
  <img src="https://img.shields.io/static/v1?label=WhatsApp&message=*&color=34AF23&style=for-the-badge&logo=whatsapp"/>
  <img src="https://img.shields.io/static/v1?label=Size&message=584B&color=56696F&style=for-the-badge&logo="/>
  <img src="https://img.shields.io/static/v1?label=Last-Commit&message=May | 2022&color=56696F&style=for-the-badge&logo="/>
  <img src="https://img.shields.io/static/v1?label=Issues&message=0 open&color=1572B6&style=for-the-badge&logo="/>
</p>

<p align="center">
 <a href="#memo-Sobre">Sobre</a> &nbsp; | &nbsp;
 <a href="#mag_right-Status">Status</a> &nbsp; | &nbsp;
 <a href="#hammer_and_wrench-Tecnologias">Tecnologias</a> &nbsp; | &nbsp;
 <a href="#computer-Pré-requisitos">Pré-requisitos</a> &nbsp; | &nbsp;
 <a href="#heavy_check_mark-Rodando">Rodando...</a> &nbsp; | &nbsp;
 <a href="#man_technologist-Contribuidores">Contribuidores</a> &nbsp; | &nbsp;
 <a href="#bulb-Autor">Autor</a>
</p>

<p align="center">
  <img alt="" width="300" src="">
  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img alt="" width="300" src="">
  &nbsp;&nbsp;&nbsp;&nbsp;
</p>

## :memo: Sobre

**BoBook** é um *bot* que, por enquanto, pesquisa por livros na [**Amazon.com**](https://www.amazon.com.br/).

 > • nome do **livro**: retorna o link de compra do melhor resultado;

 > • nome do **autor(a)**: retorna todos os livros disponíveis;

Ele realiza ambas as pesquisas pelo [WhatsApp](https://www.whatsapp.com/), o aplicativo de mensagens instantâneas e chamada de voz para smartphones 
desenvolvido pela **WhatsApp Inc.**, subsidiária da empresa [**Meta Platforms, Inc.**](https://about.facebook.com/meta/).


## :mag_right: Status



<h3 align="center"> 
	🚧   Em construção...  🚧
</h3>



## :hammer_and_wrench: Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

> - [python 3.6.*](https://www.python.org/)
> - [Flask](https://flask.palletsprojects.com/en/2.1.x/)
> - [twilio](https://www.twilio.com/pt-br/)
> - [API WhatsApp](https://www.twilio.com/pt-br/whatsapp)
> - [ngrok](https://ngrok.com/)
> - [python-googlesearch](https://python-googlesearch.readthedocs.io/en/latest/)

## :computer: Pré-requisitos
Antes de começar, você vai precisar ter:

- [x] Conta:
  - [x] [twilio](https://www.twilio.com/try-twilio)
  - [x] [ngrok](https://dashboard.ngrok.com/signup)

- [x] Baixado:
  - [x] [ngrok](https://ngrok.com/download)

- [x] Instalado:
  - [x] ngrok
  - [x] python3
  - [x] python3-venv ou virtualenv

## :heavy_check_mark: Rodando...

<h6 align="center">
  ***As instruções a seguir são para fins de teste.***
</h6>


```bash
# Clone este repositório
$ git clone https://github.com/lipebol/BoBook

# Acesse a pasta do projeto no terminal/cmd
$ cd bot-search

# Crie um "ambiente virtual"
$ python3 -m venv bot-search-venv
```
> caso o código acima não funcione, instale "*virtualenv*"
```bash
$ [gerenciador-de-pacotes] install virtualenv

# Crie um "ambiente virtual" com virtualenv
$ virtualenv bot-search-venv -p $(which python3)
```

```bash
# Inicie o "ambiente virtual"
$ source bot-search-venv/bin/activate
```
> no "*Windows*"
```bash
$ bot-search-venvScripts\activate
```

```bash
# Instale os pacotes necessários
(bot-search-venv) $ pip install twilio flask requests beautifulsoup4 google

# Inicie o serviço
(bot-search-venv) $ python3 bot.py
```
> Nesse momento o serviço está rodando na porta **:5000**, mas de maneira "*interna*".

> Para ser acessível pela **API** é necessário direcionar o **ngrok** para essa porta,
> e ele irá gerar uma URL temporária acessível externamente.
```bash
# De preferência, abra outro terminal...
$ ngrok http 5000
```
> Já registrado na **twilio**, configure e ative o *WhatsApp Sandbox*: 
> [*Veja aqui*](https://www.twilio.com/blog/como-acessar-api-whatsapp-com-twilio)

> No console da **twilio**, nas configurações da *Sandbox*, existe com campo chamado **WHEN A MESSAGE COMES IN**.

> Cole nele a URL *https://* gerada pelo **ngrok**.
 
> Acrescente no final da URL  */bot*.

> Verifique se o método de solicitação está definido como *HTTP Post*.

> Clique em *Save* na parte inferior da página para registrar as alterações.

<h4 align="center">
  Agora é só testar!
</h4>

## :man_technologist: Contribuidores

<a href="https://github.com/lipebol">
  &nbsp;&nbsp;
  &nbsp;&nbsp;
  &nbsp;
        <img src="https://avatars.githubusercontent.com/u/72844312?v=4" width="140px;"/>
</a>

[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=for-the-badge&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lipebol/) 
[![Medium Badge](https://img.shields.io/badge/-Medium-000000?style=for-the-badge&logo=Medium&logoColor=white)]()

## :bulb: Autor

" Mas foi Deus quem fez a terra com o seu poder, criou o mundo com a sua sabedoria e com a sua inteligência estendeu o céu como se fosse uma coberta."

Jeremias 10.12



Agradeço a Deus o Pai que por meio de seu Filho Jesus Cristo nos enviou o Espírito Santo que nos ajuda em todas as nossas atividades e trabalhos!
A Ele toda Glória, Honra e Mérito!
