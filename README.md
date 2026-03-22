# 🚀 Secure Marketing Data Pipeline

Pipeline de dados focado em marketing de performance, com arquitetura modular, métricas de negócio e aplicação de boas práticas de segurança.

---

## 🚀 Highlights

- End-to-end ETL pipeline
- Marketing performance metrics (CTR, CPC, CPA, ROI)
- Logging and error handling
- Secure configuration with .env
- Data persistence (SQLite + CSV)

---

## 💰 Aplicação em Negócio

Este pipeline permite:

- Análise de performance de campanhas
- Otimização de ROI
- Redução de CAC
- Identificação de canais mais eficientes
- Base para dashboards e tomada de decisão

👉 Pode ser utilizado por:

- Agências de marketing
- E-commerces
- Infoprodutores
- SaaS

---

## 🎯 Objetivo

Construir um pipeline de dados completo que:

- Coleta dados de campanhas (simulação de API)
- Processa e valida os dados
- Calcula métricas de performance
- Armazena em banco de dados
- Exporta dados para análise

---

## 🧱 Arquitetura

Pipeline estruturado em camadas:

- **Extract** → Coleta de dados  
- **Transform** → Processamento e métricas  
- **Load** → Persistência em banco + exportação  

---

## 📊 Métricas Calculadas

- CTR (Click Through Rate)
- CPC (Cost per Click)
- CPA (Cost per Acquisition)
- Conversion Rate
- ROI (Return on Investment)

---

## ⚙️ Stack Tecnológica

- Python
- Pandas
- SQLite
- Dotenv
- Estrutura modular (ETL)

---

## 🔐 Camada de Segurança

- Uso de `.env` para variáveis sensíveis
- `.gitignore` para proteção de credenciais
- Validação de dados (`df.empty`)
- Proteção contra divisão por zero
- Estrutura preparada para IAM e expansão cloud

---

## 📦 Saídas do Pipeline

- Banco de dados SQLite:
  - `marketing_pipeline.db`

- Arquivo CSV:
  - `output/campaign_performance.csv`

---

## ▶️ Como executar

```bash
pip install -r requirements.txt
python main.py