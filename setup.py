from setuptools import setup, find_packages

setup(
    name="mon_composant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Ajoute les dépendances si nécessaire
    description="Un composant bouton pour Django",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ton Nom",
    author_email="huguescodeur@gmail.com",
    url="https://github.com/ton_github/mon_composant",  # Lien vers ton dépôt GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
