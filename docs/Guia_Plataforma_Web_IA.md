# Guia Completo: Plataforma Web com IA para Formulações Farmacêuticas

Este documento apresenta um passo a passo resumido inspirado no FormulationAI para construir uma plataforma web simples que permite prever propriedades de formulações farmacêuticas a partir de dados de fármacos e excipientes. O texto base foi fornecido pelo usuário e aqui mantemos os pontos principais em português.

## Funcionalidades
- Interface web para entrada de dados (fármaco, excipiente, proporções e propriedades físico-químicas).
- Processamento via modelos de IA (Random Forest, SVM, LightGBM, XGBoost) para predizer propriedades como solubilidade ou dissolução.
- Armazenamento de entradas e resultados em banco de dados relacional (ex.: MySQL).
- Execução local ou em nuvem, acessível via navegador.

## Tecnologias sugeridas
1. **Python 3** – linguagem principal.
2. **Django** – framework web para estruturação em MTV.
3. **scikit-learn** – biblioteca de machine learning.
4. **XGBoost/LightGBM** – alternativas de boosting.
5. **MySQL** – banco de dados relacional (pode-se iniciar com SQLite).
6. **Pandas/Joblib** – apoio à manipulação de dados e persistência de modelos.

## Configuração básica do ambiente
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django scikit-learn xgboost lightgbm mysqlclient pandas joblib
```
Crie o banco de dados e configure-o em `settings.py`.

## Estrutura inicial do projeto
```text
formulacaoAI/
├── manage.py
├── formulacaoAI/
│   ├── settings.py
│   └── urls.py
└── predicao/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── predicao/
            ├── form.html
            └── resultado.html
```

## Exemplo de modelos (`predicao/models.py`)
```python
from django.db import models

class Farmaco(models.Model):
    nome = models.CharField(max_length=100)
    peso_molecular = models.FloatField(null=True, blank=True)
    logP = models.FloatField(null=True, blank=True)

class Excipiente(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, null=True, blank=True)

class Formulacao(models.Model):
    farmaco = models.ForeignKey(Farmaco, on_delete=models.CASCADE)
    excipiente = models.ForeignKey(Excipiente, on_delete=models.CASCADE)
    proporcao_excipiente = models.FloatField()
    solubilidade = models.FloatField(null=True, blank=True)
    solubilidade_predita = models.FloatField(null=True, blank=True)
```

## Treinamento e uso do modelo
Use `scikit-learn` para treinar modelos a partir de dados históricos. Salve o modelo com `joblib.dump` e carregue na aplicação:
```python
import joblib
model = joblib.load('modelo_solubilidade.pkl')
previsao = model.predict([[peso, logP, proporcao]])[0]
```

## View simplificada (`predicao/views.py`)
```python
from django.shortcuts import render
from .models import Farmaco, Excipiente, Formulacao
import joblib, os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modelo_solubilidade.pkl')
model = joblib.load(MODEL_PATH)

def prever_solubilidade(request):
    if request.method == 'POST':
        peso = float(request.POST.get('peso_molecular', 0) or 0)
        logP = float(request.POST.get('logP', 0) or 0)
        proporcao = float(request.POST.get('proporcao_excipiente', 0) or 0)
        sol_pred = model.predict([[peso, logP, proporcao]])[0]
        contexto = {'solubilidade_predita': sol_pred}
        return render(request, 'predicao/resultado.html', contexto)
    return render(request, 'predicao/form.html')
```

## Templates básicos
*`form.html`*
```html
<form method="post">
  {% csrf_token %}
  <input type="number" name="peso_molecular" step="0.01">
  <input type="number" name="logP" step="0.01">
  <input type="number" name="proporcao_excipiente" step="0.1">
  <button type="submit">Predizer</button>
</form>
```
*`resultado.html`*
```html
<h1>Solubilidade Predita: {{ solubilidade_predita }}</h1>
```

## Implantação
É possível implantar em serviços como Heroku ou PythonAnywhere ou em infraestrutura própria. Ajuste variáveis de ambiente, configure `ALLOWED_HOSTS` e defina `DEBUG=False` em produção.

