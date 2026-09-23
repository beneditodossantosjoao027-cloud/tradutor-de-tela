# Tradutor de Tela

Programa em Python que **traduz o que está escrito na tela do computador em tempo real**, sem precisar copiar e colar texto manualmente.

## O que ele faz

- Captura uma área da tela (print automático)
- Lê o texto que aparece nessa área (OCR)
- Traduz esse texto para o idioma escolhido
- Mostra a tradução na tela, sobreposta ou em uma janela separada

Serve pra traduzir jogos, sites, vídeos ou qualquer programa que não tenha tradução nativa.

## Tecnologias usadas

Python

## Como instalar

1. Baixe o projeto:
```bash
git clone https://github.com/beneditodossantosjoao027-cloud/tradutor-de-tela.git
cd tradutor-de-tela
```

2. Instale o Python (versão 3.10 ou mais nova) no site oficial: https://www.python.org/downloads/ — durante a instalação, marque a opção "Add Python to PATH".

3. Instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

## Como usar

1. Abra o programa:
```bash
python tradutor_de_tela.py
```
2. Selecione com o mouse a área da tela que você quer traduzir.
3. O texto traduzido vai aparecer automaticamente.
4. Para fechar o programa, feche a janela ou aperte a tecla ESC.

## Segurança

Este programa só lê o que está visível na sua própria tela — ele não acessa a internet além de enviar o texto pro serviço de tradução, não coleta dados pessoais e não precisa de permissões especiais além de capturar a tela.

## Autor

Benedito dos Santos — [GitHub](https://github.com/beneditodossantosjoao027-cloud)
