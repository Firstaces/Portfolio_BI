import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Função para gerar datas aleatórias
def gerar_data_inicial():
    return datetime(2023, 1, 1) + timedelta(days=random.randint(0, 730))

def gerar_data_fechamento(data_inicio):
    if random.random() > 0.2:  # 80% de chance de ter data de fechamento
        return data_inicio + timedelta(days=random.randint(1, 30), hours=random.randint(1, 23))
    return np.nan

# Listas de valores possíveis
sistemas = ['SAP', 'ServiceNow', 'SAP Hana', 'Ariba', 'Oracle']
prioridades = ['Baixa', 'Média', 'Alta', 'Urgente']
responsaveis = ['João', 'Maria', 'Carlos', 'Ana', 'Fernanda']

# Gerar registros de chamados
registros = []

for i in range(200):
    data_abertura = gerar_data_inicial()
    data_fechamento = gerar_data_fechamento(data_abertura)

    tempo_resolucao = (data_fechamento - data_abertura).days if pd.notna(data_fechamento) else np.nan
    tempo_resolucao_horas = (data_fechamento - data_abertura).total_seconds() / 3600 if pd.notna(data_fechamento) else np.nan

    status = 'Fechado' if pd.notna(data_fechamento) else 'Aberto'

    sla_cumprido = 'Sim' if (pd.notna(data_fechamento) and tempo_resolucao <= 15) else 'Não'

    registros.append([
        f'CH-{i+1:04d}',
        data_abertura.date(),
        data_fechamento.date() if pd.notna(data_fechamento) else np.nan,
        random.choice(sistemas),
        random.choice(prioridades),
        random.choice(responsaveis),
        sla_cumprido,
        tempo_resolucao,
        tempo_resolucao_horas,
        status
    ])

# Criar DataFrame
df = pd.DataFrame(registros, columns=[
    'ID do Chamado', 'Data de Abertura', 'Data de Fechamento', 'Sistema', 'Prioridade', 'Responsável', 'SLA Cumprido', 'Tempo de Resolução (Dias)', 'Tempo de Resolução (Horas)', 'Status'
])

# Salvar em CSV
df.to_csv('chamados_ti.csv', index=False)

print("Arquivo 'chamados_ti.csv' gerado com sucesso!")
