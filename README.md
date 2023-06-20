## Sobre o projeto

Dois programas que executam em conjunto um algoritmo de contagem de palavras a partir de um texto base. O processamento das tarefas é feito através de um ambiente distribuído modelado a partir de serviços Docker. 

#### text-processor

- Realiza a leitura do arquivo principal e os fragmenta em setores que serão processados pelos containers (processos) trabalhadores;
- Reduz as contagens de palavras recebidas pelos demais containers em uma só, constituindo o número total de palavras presentes no arquivo.

#### word-counter

- Programa executado por múltiplos containers (processos) que contabiliza o número de palavras existentes;
- Envia a contagem final de palavras do setor de arquivo recebido para o container principal.


---

## Como executar

Para gerar as imagens dos dois serviços Docker, rode no diretório raiz do projeto:

```
./build.sh
```

Para reiniciar os containers e executar o código dos programas rode:

```
./start.sh
```
