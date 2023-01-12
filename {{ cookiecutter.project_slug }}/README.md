# Cookiecuter Personal

<!-- badges: start -->
[![@kalebsampaco](https://img.shields.io/badge/@kalebsampaco-github-blue?&logoColor=white)](https://github.com/kalebsampaco) 

<!-- badges: end -->

Creación de plantilla personalizada utilizando cookiecutter.

## Requiremientos

- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    Esto puede ser instalado con `pip` o `conda` dependiendo cómo tú manejas tus paquetes de Python:

``` bash
pip install cookiecutter
```

o

``` bash
conda install -c conda-forge cookiecutter
```

## Crear un nuevo proyecto

En el directorio en el que quieras guardar tu proyecto generado:

```bash
cookiecutter https://github.com/kalebsampaco/cookiecutter-personal --checkout cookiecutter-personal
```


## Estructura de directorios y archivos resultantes

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering), `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        ├── outputs          <- outputs of project,
        ├── reports          <- reports of project,
        ├── src          <- data source,
        │                         the creator's initials, and a short 
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
Proyecto creado  
por [@kalebsampaco](https://www.linkedin.com/in/william-caleb-s%C3%A1enz-camacho-5a538a241/).