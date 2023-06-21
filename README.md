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

#### Dependências

- Ambiente Linux (Usado no desenvolvimento: Ubuntu 22.04 LTS)
- Python3.10+ (https://www.python.org/downloads/)
- Docker e Docker Compose (https://www.docker.com/)

Dê permissões para os scripts do projeto:

```
cd ppd-project

chmod +x *.sh

```

Instale o Docker a partir do script abaixo:

```
./install_docker.sh
```

Para gerar as imagens dos dois serviços Docker, rode no diretório raiz do projeto:

```
./build.sh
```

Para definir a quantidade de contadores, deve ser alterado no arquivo .env:

Mínimo de 6 counters.

```
COUNTER_NUMBER=6
```

Para reiniciar os containers e executar o código dos programas rode:

```
./start.sh
```
