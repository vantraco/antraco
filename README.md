# Antraco

Antraco é um protótipo de plataforma preditiva farmacotécnica. O projeto
fornece um aplicativo simples em Streamlit que apresenta uma formulação
simulada e calcula métricas como higroscopicidade, compressibilidade e
risco de incompatibilidade. O gráfico gerado demonstra uma curva de
dissolução estimada. Para um guia completo de como uma solução web mais
robusta pode ser estruturada, consulte `docs/Guia_Plataforma_Web_IA.md`.

## Instalação

1. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use venv\\Scripts\\activate
   ```

2. Instale as dependências listadas em `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Execução do aplicativo

Inicie o aplicativo Streamlit executando:

```bash
streamlit run streamlit_app.py
```

O navegador será aberto exibindo a formulação de exemplo e os valores
preditos.
