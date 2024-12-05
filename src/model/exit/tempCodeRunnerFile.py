from datetime import datetime

# Defina as datas e horários
inicio = datetime(2024, 9, 5, 14, 30)
fim = datetime(2024, 9, 7, 18, 0)
print(inicio)
print(fim)
# Calcule a diferença
diferenca = fim - inicio
print(diferenca)

# Converta a diferença para horas
diferenca_em_horas = diferenca.total_seconds() / 3600
