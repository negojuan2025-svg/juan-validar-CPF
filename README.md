# Validador de CPF
Este repositório contém uma aplicação em Python projetada para ler um Cadastro de Pessoas Físicas (CPF) e realizar sua validação matemática completa, determinando se ele é autêntico ou não. Através de uma interface simplificada, o script processa entradas numéricas, higieniza os dados removendo pontuações e aplica os algoritmos de verificação necessários para garantir que o número fornecido obedece às normas de construção do documento.

## 🎯 Objetivo do Projeto
O objetivo principal deste projeto é aplicar lógica de programação e operações matemáticas para reproduzir o algoritmo oficial da Receita Federal na validação de CPFs. O sistema verifica a integridade dos dígitos verificadores e trata exceções de falsos-positivos (como números repetidos) de forma eficiente.

O algoritmo processa a entrada limpando caracteres não numéricos, calcula o primeiro e o segundo dígito verificador através do método de pesos e somatórios (Módulo 11) e compara o resultado final com o número fornecido para garantir que o documento segue o padrão estrutural exigido nacionalmente.
