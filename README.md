# Biomorph Mutation
Implementation of the algorithm to generate biomorphs described by Richard Dawkins in [The Evolution of Evolvability](https://richarddawkins.net/wp-content/uploads/2014/06/Evolution-of-Evolvability.pdf). An initial biomorph is created with length of 1. Each generation consists of a random mutation in one of the nine different genes of the biomorph. Genes control the angles and length of the strokes. No selection of any kind is applied. 

<p align="center">
    <img width="400" height="400" src="images/biomorphs.gif">
</p>



## Installation

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

If using Conda, you can also create an environment with the requirements:

```bash
conda env create -f environment.yml
```

By default the environment name is `biomorph-mutation`. To activate it run:

```bash
conda activate biomorph-mutation
```


## Usage

Run the algorithm from the command line with:

```python
python -m biomorph_mutation
```

Biomorphs will be saved in a generated directory named `biomorphs`.





