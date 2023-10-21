import threading

arquivos_log = ['access_log_1.txt', 'access_log_2.txt', 'access_log_3.txt']

total_requisicoes = 0
erros_404 = 0

def analisar_log(arquivo):
    global total_requisicoes, erros_404
    with open(arquivo, 'r') as file:
        for linha in file:
            total_requisicoes += 1
            if '404' in linha:
                erros_404 += 1

# Cria uma thread para cada arquivo de log
threads = []

for arquivo in arquivos_log:
    thread = threading.Thread(target=analisar_log, args=(arquivo,))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads concluírem
for thread in threads:
    thread.join()

print(f'Total de requisições: {total_requisicoes}')
print(f'Total de erros 404: {erros_404}')
