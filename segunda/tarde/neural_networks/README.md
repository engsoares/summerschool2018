
Este repositório contém todo o código do curso _Perceptron, Backpropagation e Multilayer Perceptron_ ministrado na __Deep Learning Summer School 2018__, cujo conteúdo ministrado é:

- __Perceptron__: os alunos aprendem o que é o perceptron, como funciona e implementam o algoritmo utilizando a linguagem python.
- __Adaline__: os alunos aprendem a diferença do Adaline pro Perceptron e como ele melhora o aprendizado. A implementação também é feita utilizando apenas python.
- __Backpropagation__: essa etapa do curso desmitifica a etapa de backpropagation das redes neurais, tornando simples de entender e aplicar.
- __Redes Neurais__: ao final do curso, os alunos implementam um rede neural do zero em poucas linhas de código utilizando apenas python e numpy. A rede neural implementada é capaz de resolver problemas de regressão, classificação binária e classificação multi-classe.

Para rodar os código desse repositório fora do ambiente Docker desenvolvido para o curso, siga os passos a seguir:

1. Baixe ou clone o repositório.
2. Baixe e instale o [Miniconda](https://conda.io/miniconda.html).
3. Abra o terminal e digite o seguinte comando para instalar o ambiente:
```sh
$ conda create -n summerschool python=3.6 numpy pandas matplotlib=2.0.2 scikit-learn jupyter
```
4. Siga as instruções abaixo para ativar o ambiente de acordo com o seu sistema operacional:
    - No __Windows__:
    ```sh
    $ activate summerschool
    ```
    - No __Linux/Mac__:
    ```sh
    $ source activate summerschool
    ```
5. Execute o Jupyter Notebook:
    ```sh
    $ jupyter notebook
    ```
> A instalação do ambiente (passos 1-3) deve ser executada somente uma vez, enquanto os passos 4 e 5 devem ser feitos sempre que você quiser rodar os códigos do repositório.

Sinta-se à vontade para sanar qualquer dúvida diretamente com o professor do curso:

:bust_in_silhouette: __Arnaldo Gualberto__:

* arnaldo.g12@gmail.com
* [Github](https://github.com/arnaldog12)
* [Site Pessoal](http://arnaldogualberto.com)
