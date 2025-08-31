# Mini-rag App

This is a minimal implementation of the RAG model for question answering 

## Requirments

- Python 3.12 or later

#### How to install python using MiniConda 

1. Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions)

2. Create a new environment using the following command : 
```bash
$ conda create -n mini-rag
```

3.Activate the new environment using the following command :
```bash
$ conda activate mini-rag
```

### (Optional) Setup your command line interface for better readability

```bash
$ export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```  

## Installation

### Install required packages

```bash
$ pip install -r requirements
```

### Setup the environment variables

```bash
cp .env.example .env
```

Set your environment variables in the `.env` file. like the api keys