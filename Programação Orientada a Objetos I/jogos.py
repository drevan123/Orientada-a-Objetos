def calcular_premio(V, N, M):
    """
    Calcula o valor do prêmio com base nos critérios estabelecidos.
    Parâmetros:
    V (float): Valor da aposta.
    N (int): Número da loteria do apostador.
    M (int): Número sorteado.
    """
    # Garantir que N e M sejam strings de 6 dígitos
    N_str = str(N).zfill(6)
    M_str = str(M).zfill(6)
    # Comparar quatro últimos dígitos
    if N_str[-4:] == M_str[-4:]:
        return V * 3000.0
    # Comparar três últimos dígitos
    if N_str[-3:] == M_str[-3:]:
        return V * 500.0
    # Comparar dois últimos dígitos
    if N_str[-2:] == M_str[-2:]:
        return V * 50.0
    # Verificar se os dois últimos dígitos estão no mesmo grupo
    grupo_n = (int(N_str[-2:]) - 1) // 4
    grupo_m = (int(M_str[-2:]) - 1) // 4
    if grupo_n == grupo_m:
        return V * 16.0
    
    # Se nenhum dos casos acima ocorrer, não há prêmio
    return 0

def calcular_minutos(h1, m1, h2, m2):
    """
    Calcula a diferença em minutos entre dois horários fornecidos.
    Parâmetros:
    h1, m1 (int): Hora e minuto de início.
    h2, m2 (int): Hora e minuto de fim.
    """
    if not (0 <= h1 <= 23 and 0 <= m1 <= 59 and 0 <= h2 <= 23 and 0 <= m2 <= 59):
        raise ValueError("Horas devem estar entre 0 e 23, e minutos devem estar entre 0 e 59")
    
    minutos_inicio = h1 * 60 + m1
    minutos_fim = h2 * 60 + m2
    
    if minutos_inicio == minutos_fim:
        return 1440  # Dormiu exatamente 24 horas
    elif minutos_inicio < minutos_fim:
        return minutos_fim - minutos_inicio
    else:
        return 1440 - (minutos_inicio - minutos_fim)

def movimentoSoldado(N, arrayDirecoes):
    """
    Simula o movimento de um soldado baseado em comandos de direção.
    Parâmetros:
    N (int): Número de comandos.
    arrayDirecoes (str): String com comandos ('D' para direita, 'E' para esquerda).
    """
    olharDoRecruta = ['Norte', 'Leste', 'Sul', 'Oeste']
    direcaoOlharDoRecruta = ['↑↑↑↑', '>>>>', '↓↓↓↓', '<<<<']
    olharDoRecruta_atual = 0

    comandos = arrayDirecoes.split()
    direcoes_olhadas = [olharDoRecruta[olharDoRecruta_atual]]  # Lista para armazenar as direções olhadas

    if len(comandos) < N:
        print("O número de comandos fornecidos é menor que N.")
        return

    for i in range(N):
        direcao = comandos[i]

        if direcao == 'D':
            print("\nSargento: Direita, volver!!!")
            olharDoRecruta_atual = (olharDoRecruta_atual + 1) % 4
        elif direcao == 'E':
            print("\nSargento: Esquerda, volver!!!")
            olharDoRecruta_atual = (olharDoRecruta_atual - 1) % 4
        else:
            print("Comando inválido, encerrando.")
            break
        
        # Adiciona a nova direção olhada na lista
        direcoes_olhadas.append(olharDoRecruta[olharDoRecruta_atual])

    print(f"Recruta está olhando para: {olharDoRecruta[olharDoRecruta_atual]} {direcaoOlharDoRecruta[olharDoRecruta_atual]}")
    print("Direções olhadas pelo recruta: ", " -> ".join(direcoes_olhadas))

# Código principal
selecionar = ""
while selecionar != "4":
    print("\nInforme qual das 3 avaliações deseja testar:")
    print("1 para JOGO DO BICHO")
    print("2 para CALCULAR TEMPO DE SONO")
    print("3 para PARA QUAL DIREÇÃO O SOLDADO OLHA")
    print("4 para SAIR")
    
    selecionar = input().strip()
    
    try:
        if selecionar == "1":
            entrada = input("\nDigite sua aposta (V N M): ").split()
            V = float(entrada[0])
            N = int(entrada[1])
            M = int(entrada[2])

            premio = calcular_premio(V, N, M)
            print("Resultado da aposta: {:.2f}".format(premio))

        elif selecionar == "2":
            print("\nDigite os valores de h1, m1, h2, m2 separados por espaço: ")
            h1, m1, h2, m2 = map(int, input().split())
            minutos = calcular_minutos(h1, m1, h2, m2)
            print(f"Minutos de sono: {minutos}")

        elif selecionar == "3":
            print("Prova do soldado selecionada")
            qtdOrdens = input("Quantas ordens você deseja: ")
            N = int(qtdOrdens)
            direcoes = input("Digite as ordens de direção D(direita), E(esquerda): ")
            movimentoSoldado(N, direcoes)

    except Exception as e:
        print(f"Erro: {str(e)} \nDigite os valores corretamente!\n")
