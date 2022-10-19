from setuptools import setup, find_packages # Parametros relacionados o pacote

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing-test", # Nome do pacote
    version="0.0.2", # Versão tem que ser alterada conforme for publicando.
    author="",
    author_email="",
    description="Test version - Image processing. This project belongs to Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp developer full stack Python. E-mail:karinatkato@gmail.com.",
    long_description=page_description, # usa a descrição da pagina do proprio pypi
    long_description_content_type="text/markdown", # trabalhar como o readme usando esses dados.
    url="", # link do projeto no github
    packages=find_packages(), # Especifica os modulos e submodulos do pacote. (Usar o valor para ajudar na busca)
    install_requires=requirements, # Pacote basico, dependencia de pacotes 
    python_requires='>=3.8', # versão base do Python que seu pacote pode funcionar.
)

# O Arquivo requiements.txt
# Usado par passar as dependencias que devem ser instalas com o seu pacote.
# Opcional, especificar as versões