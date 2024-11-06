# Bibliotecas

import pandas as pd
import inspect


#Entrada Inicial

opcoes_validas = {"rurais", "urbanos", "rurais e urbanos"}
entrada = input("Dados rurais e/ou urbanos? ").strip().lower()
while entrada not in opcoes_validas:
    entrada = input("Entrada inválida. Digite 'rurais', 'urbanos' ou 'rurais e urbanos': ").strip().lower()


# Definir números iseridos como floats obrigatoriamente
def entrada_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

#Entrada de dados

if entrada == 'rurais e urbanos':
    # Variáveis Rurais
    print('\nInsira os dados para o cálculo de Tc em regiões rurais:\n')
    i_r = entrada_float("Valor de i: ")
    i2_r = entrada_float("Valor de i2: ")
    Cr_r = 0.06
    L_r = entrada_float("Valor de L: ")
    S_r = entrada_float("Valor de S: ")
    N_r = 0.8
    n_r = 0.03
    C_r = 0.01
    A_r = entrada_float("Valor de A: ")
    CN_r = 70
    Sscs_r = round((25400/CN_r)-254, 2)
    k_r = 3
    p_r = 0.5
    Aimp_r = entrada_float("Valor de Aimp: ")
    R_r = 0.2
    φ_r = 1
    TC_r = entrada_float("Valor de referência de Tc: ")

    # Variáveis Urbanas
    print('\nInsira os dados para o cálculo de Tc em regiões urbanas:\n')
    i_ur = entrada_float("Valor de i: ")
    i2_ur = entrada_float("Valor de i2: ")
    Cr_ur = 0.012
    L_ur = entrada_float("Valor de L: ")
    S_ur = entrada_float("Valor de S: ")
    N_ur = 0.02
    n_ur = 0.016
    C_ur = 0.9
    A_ur = entrada_float("Valor de A: ")
    CN_ur = 90
    Sscs_ur = round((25400/CN_ur)-254, 2)
    k_ur = 5
    p_ur = 0
    Aimp_ur = entrada_float("Valor de Aimp: ")
    R_ur = 0.02
    φ_ur = 0.3
    TC_ur = entrada_float("Valor de referência de Tc: ")

elif entrada == 'rurais':
    # Variáveis Rurais
    print('\nInsira os dados para o cálculo de Tc em regiões rurais:\n')
    i_r = entrada_float("Valor de i: ")
    i2_r = entrada_float("Valor de i2: ")
    Cr_r = 0.06
    L_r = entrada_float("Valor de L: ")
    S_r = entrada_float("Valor de S: ")
    N_r = 0.8
    n_r = 0.03
    C_r = 0.01
    A_r = entrada_float("Valor de A: ")
    CN_r = 70
    Sscs_r = round((25400/CN_r)-254, 2)
    k_r = 3
    p_r = 0.5
    Aimp_r = entrada_float("Valor de Aimp: ")
    R_r = 0.2
    φ_r = 1
    TC_r = entrada_float("Valor de TC: ")

    # Vazios urbanos
    i_ur = i2_ur = Cr_ur = L_ur = S_ur = N_ur = n_ur = C_ur = A_ur = CN_ur = Sscs_ur = k_ur = p_ur = Aimp_ur = R_ur = φ_ur = TC_ur = None

elif entrada == 'urbanos':
    # Vazios rurais
    i_r = i2_r = Cr_r = L_r = S_r = N_r = n_r = C_r = A_r = CN_r = Sscs_r = k_r = p_r = Aimp_r = R_r = φ_r = TC_r = None

    # Variáveis Urbanas
    print('\nInsira os dados para o cálculo de Tc em regiões urbanas:\n')
    i_ur = entrada_float("Valor de i: ")
    i2_ur = entrada_float("Valor de i2: ")
    Cr_ur = 0.012
    L_ur = entrada_float("Valor de L: ")
    S_ur = entrada_float("Valor de S: ")
    N_ur = 0.02
    n_ur = 0.016
    C_ur = 0.9
    A_ur = entrada_float("Valor de A: ")
    CN_ur = 90
    Sscs_ur = round((25400/CN_ur)-254, 2)
    k_ur = 5
    p_ur = 0
    Aimp_ur = entrada_float("Valor de Aimp: ")
    R_ur = 0.02
    φ_ur = 0.3
    TC_ur = entrada_float("Valor de TC: ")


#Listas

dados_variaveis = {
    'Variável': ['i', 'i2', 'Cr', 'L', 'S', 'N', 'n', 'C', 'A', 'CN', 'Sscs', 'k', 'p', 'Aimp', 'R', 'φ', 'TC'],
    'Rurais': [i_r, i2_r, Cr_r, L_r, S_r, N_r, n_r, C_r, A_r, CN_r, Sscs_r, k_r, p_r, Aimp_r, R_r, φ_r, TC_r],
    'Urbanas': [i_ur, i2_ur, Cr_ur, L_ur, S_ur, N_ur, n_ur, C_ur, A_ur, CN_ur, Sscs_ur, k_ur, p_ur, Aimp_ur, R_ur, φ_ur, TC_ur],
}
equacoes = ['izzard', 'kerby_hathaway', 'onda_cinematica', 'faa', 'kirpich', 'scs_lag', 'simas_hawkins', 'ven_te_chow', 'dooge', 'johnstone', 'corps_engineers', 'giandotti', 'pasini', 'ventura', 'picking', 'dnos', 'george_ribeiro', 'schaake', 'mccuen', 'carter', 'eagleson', 'desbordes', 'espey_winslow']
equacoes_formatadas = ["Izzard", "Kerby - Hathaway", "Onda Cinemática", "FAA", "Kirpich", "SCS Lag", "Simas-Hawkins", "Ven te Chow", "Dooge", "Johnstone", "Corps Engineers", "Giandotti", "Pasini", "Ventura", "Picking", "DNOS", "Geoge Ribeiro", "Schaake et al", "McCuen et al", "Carter", "Eagleson", "Desbordes", "Espey-Winslow"]

#Data frame das variaveis
df_variaveis = pd.DataFrame(dados_variaveis)


# Equações

def izzard(i, Cr, L, S):
    return 85.5 * (i / (36286 + Cr)) * (i**-0.667) * (L**0.33) * (S**-0.333)

def kerby_hathaway(N, L, S):
    return 0.619 * N**0.47 * L**0.47 * S**-0.235

def onda_cinematica(n, i2, L, S):
    return 7.35 * (n**0.6) * (i2**-0.4) * (L**0.6) * (S**-0.3)

def faa(C, L, S):
    return 0.37 * (1.1 - C) * (L**0.5) * (S**-0.333)

def kirpich(L, S):
    return 0.0663 * (L**0.77) * (S**-0.385)

def scs_lag(CN, L, S):
    return 0.057 * ((1000 / (CN - 9))**0.7) * (L**0.8) * (S**-0.5)

def simas_hawkins(A, L, S, Sscs):
    return 0.322 * (A**0.594) * (L**-0.594) * (S**-0.150) * (Sscs**0.313)

def ven_te_chow(L, S):
    return 0.160 * (L**0.64) * (S**-0.32)

def dooge(A, S):
    return 0.365 * (A**0.41) * (S**-0.17)

def johnstone(L, S):
    return 0.462 * (L**0.5) * (S**-0.25)

def corps_engineers(L, S):
    return 0.191 * (L**0.76) * (S**-0.19)

def giandotti(A, L, S):
    return 0.0559 * ((4 * A**0.5) + (1.5 * L)) * (L**-0.5) * (S**-0.5)

def pasini(A, L, S):
    return 0.107 * (A**0.333) * (L**0.333) * (S**-0.5)

def ventura(A, S):
    return 0.127 * (A**0.5) * (S**-0.5)

def picking(L, S):
    return 0.0883 * (L**0.667) * (S**-0.333)

def dnos(k, A, L, S):
    return 0.419 * (k**-1) * (A**0.3) * (L**0.2) * (S**-0.4)

def george_ribeiro(p, L, S):
    return 0.222 * ((1.05 - 0.2 * p)**-1) * L * (S**-0.04)

def schaake(L, S, Aimp):
    return 0.0828 * (L**0.24) * (S**-0.16) * (Aimp**-0.26)

def mccuen(i2, L, S):
    return 2.25 * (i2**-0.7164) * (L**0.5552) * (S**-0.2070)

def carter(L, S):
    return 0.0977 * (L**0.6) * (S**-0.3)

def eagleson(n, R, L, S):
    return 0.274 * n * (R**-0.67) * L * (S**-0.5)

def desbordes(A, S, Aimp):
    return 0.0869 * (A**0.3039) * (S**-0.3832) * (Aimp**-0.4523)

def espey_winslow(φ, L, S, Aimp):
    return 0.343 * φ * (L**0.29) * (S**-0.145) * (Aimp**-0.6)


# Funções para calcular e armazenar resultados

def calcular_tc_rurais(equacoes, tipo_terreno='Rurais'):
    resultados_tc_rurais = []
    for eq_nome in equacoes:
        eq_func = globals().get(eq_nome)
        if eq_func:
            parametros = inspect.signature(eq_func).parameters
            try:
                args = [df_variaveis.loc[df_variaveis['Variável'] == nome, tipo_terreno].values[0] 
                        for nome in parametros.keys()]
                # Verifica se há algum valor None e ignora essa equação
                if None in args:
                    continue
                resultado = eq_func(*args)
                resultados_tc_rurais.append((eq_nome, resultado))
            except Exception as e:
                print(f"Erro ao calcular {eq_nome}: {e}")
    return resultados_tc_rurais


def calcular_tc_urbanos(equacoes, tipo_terreno='Urbanas'):
    resultados_tc_urbanos = []
    for eq_nome in equacoes:
        eq_func = globals().get(eq_nome)
        if eq_func:
            parametros = inspect.signature(eq_func).parameters
            try:
                args = [df_variaveis.loc[df_variaveis['Variável'] == nome, tipo_terreno].values[0] 
                        for nome in parametros.keys()]
                # Verifica se há algum valor None e ignora essa equação
                if None in args:
                    continue
                resultado = eq_func(*args)
                resultados_tc_urbanos.append((eq_nome, resultado))
            except Exception as e:
                print(f"Erro ao calcular {eq_nome}: {e}")
    return resultados_tc_urbanos


# Função para formatar e exibir a tabela - Rurais e Urbanas

def formatar_tabela_reur(resultados_rurais, resultados_urbanos, title, larguras, alinhamentos):
    dados_tabela = {
        'Equação': equacoes_formatadas,
        'Rurais': [f"{resultado:.2f}" for _, resultado in resultados_rurais],
        'Urbanos': [f"{resultado:.2f}" for _, resultado in resultados_urbanos]
    }
    df_tabela = pd.DataFrame(dados_tabela)

    """Colunas e alinahmentos"""
    colunas = df_tabela.columns
    formato_colunas = [f"{{:^{larguras[i]}}}" if alinhamentos[i] == '<' else
                       f"{{:^{larguras[i]}}}" if alinhamentos[i] == '>' else
                       f"{{:^{larguras[i]}}}" for i in range(len(colunas))]

    """Print da tabela formatada"""
    print(' - ' * 24)
    print(f'{title:^70}')
    print(' - ' * 24)

    cabecalho = ' '.join([formato_colunas[i].format(colunas[i]) for i in range(len(colunas))])
    print(cabecalho)
    print(' - ' * 24)

    for _, row in df_tabela.iterrows():
        linha = ' '.join([formato_colunas[i].format(row[colunas[i]]) for i in range(len(colunas))])
        print(linha)

    print(' - ' * 24)
    print('\n \n \n')


# Função para formatar e exibir a tabela - Rurais

def formatar_tabela_r(resultados_rurais, title, larguras, alinhamentos):
    dados_tabela = {
        'Equação': equacoes_formatadas,
        'Rurais': [f"{resultado:.2f}" for _, resultado in resultados_rurais]
    }
    df_tabela = pd.DataFrame(dados_tabela)

    """Colunas e alinhamento"""
    colunas = df_tabela.columns
    formato_colunas = [f"{{:^{larguras[i]}}}" if alinhamentos[i] == '<' else
                       f"{{:^{larguras[i]}}}" if alinhamentos[i] == '>' else
                       f"{{:^{larguras[i]}}}" for i in range(len(colunas))]

    """Print da tabela formatada"""
    print(' - ' * 17)
    print(f'{title:^50}')
    print(' - ' * 17)

    cabecalho = ' '.join([formato_colunas[i].format(colunas[i]) for i in range(len(colunas))])
    print(cabecalho)
    print(' - ' * 17)

    for _, row in df_tabela.iterrows():
        linha = ' '.join([formato_colunas[i].format(row[colunas[i]]) for i in range(len(colunas))])
        print(linha)

    print(' - ' * 17)
    print('\n \n \n')


# Função para formatar e exibir a tabela - Urbanas

def formatar_tabela_ur(resultados_urbanos, title, larguras, alinhamentos):
    dados_tabela = {
        'Equação': equacoes_formatadas,
        'Urbanos': [f"{resultado:.2f}" for _, resultado in resultados_urbanos]
    }
    df_tabela = pd.DataFrame(dados_tabela)

    """ Colunas e alinhamento"""
    colunas = df_tabela.columns
    formato_colunas = [f"{{:^{larguras[i]}}}" if alinhamentos[i] == '<' else
                       f"{{:^{larguras[i]}}}" if alinhamentos[i] == '>' else
                       f"{{:^{larguras[i]}}}" for i in range(len(colunas))]

    """Print da tabela formatada"""
    print(' - ' * 17)
    print(f'{title:^50}')
    print(' - ' * 17)

    cabecalho = ' '.join([formato_colunas[i].format(colunas[i]) for i in range(len(colunas))])
    print(cabecalho)
    print(' - ' * 17)

    for _, row in df_tabela.iterrows():
        linha = ' '.join([formato_colunas[i].format(row[colunas[i]]) for i in range(len(colunas))])
        print(linha)

    print(' - ' * 17)
    print('\n \n \n') 


# Executar cálculos

if entrada == 'rurais e urbanos':
    resultados_tc_rurais = calcular_tc_rurais(equacoes)
    resultados_tc_urbanos = calcular_tc_urbanos(equacoes)

elif entrada == 'rurais':
    resultados_tc_rurais = calcular_tc_rurais(equacoes)

elif entrada == 'urbanos':  
    resultados_tc_urbanos = calcular_tc_urbanos(equacoes)


# Execução da tabela final

if entrada == 'rurais e urbanos':
    formatar_tabela_reur(resultados_tc_rurais, resultados_tc_urbanos, "Cálculo do Tempo de Concentração (Tc)", 
                larguras=[30, 20, 20], alinhamentos=['^', '^', '^'])
elif entrada =='rurais':
    formatar_tabela_r(resultados_tc_rurais, "Cálculo do Tempo de Concentração (Tc)", 
                larguras=[30, 20], alinhamentos=['^', '^'])
elif entrada =='urbanos':
    formatar_tabela_ur(resultados_tc_urbanos, "Cálculo do Tempo de Concentração (Tc)", 
                larguras=[30, 20], alinhamentos=['^', '^'])

#Término do Código