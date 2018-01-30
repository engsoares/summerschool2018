
Este repositório contém todo o código do curso _Perceptron, Backpropagation e Multilayer Perceptron_ ministrado na __Deep Learning Summer School 2018__, cujo conteúdo ministrado é:

- __Perceptron__: os alunos aprendem o que é o perceptron, como funciona e implementam o algoritmo utilizando a linguagem python.
- __Adaline__: os alunos aprendem a diferença do Adaline pro Perceptron e como ele melhora o aprendizado. A implementação também é feita utilizando apenas python.
- __Backpropagation__: essa etapa do curso desmitifica a etapa de backpropagation das redes neurais, tornando simples de entender e aplicar.
- __Redes Neurais__: ao final do curso, os alunos implementam um rede neural do zero em poucas linhas de código utilizando apenas python e numpy. A rede neural implementada é capaz de resolver problemas de regressão, classificação binária e classificação multi-classe.

Para facilitar a execução do código dessa pasta pelos alunos, foi criado um ambiente conda. Siga as instruções abaixo para instalação e configuração desse ambiente.

# Instalação
1. Baixe ou clone o repositório.
2. Baixe e instale o [Miniconda](https://conda.io/miniconda.html).
3. Abra o terminal e digite o seguinte comando para instalar o ambiente:
    ```sh
    $ conda create -n summerschool python=3.6 numpy pandas matplotlib=2.0.2 scikit-learn jupyter
    ```

# Uso do ambiente

> __Nota:  É obrigatório seguir as ordens da seção "Instalação" antes de utilizar o ambiente__.

Siga os passos abaixo sempre que quiser executar os códigos desse repositório.
1. Abra o terminal e digite:

    - __Windows__:
    ```sh
    $ activate summerschool
    ```
    - __Linux/Mac__:
    ```sh
    $ source activate summerschool
    ```
2. Execute o Jupyter Notebook:
    ```sh
    $ jupyter notebook
    ```

Sinta-se à vontade para sanar qualquer dúvida diretamente com o professor do curso:

:bust_in_silhouette: __Arnaldo Gualberto__:

* arnaldo.g12@gmail.com
* [Github](https://github.com/arnaldog12)
* [Site Pessoal](http://arnaldogualberto.com)
