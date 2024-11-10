# Cálculo de Tempo de Concentração (Tc) para Bacias Hidrográficas em Regiões Rurais e Urbanas

Este programa realiza o cálculo do tempo de concentração (Tc) em áreas rurais e urbanas, utilizando uma série de equações e parâmetros específicos.

## Bibliotecas Utilizadas
- **pandas**: para manipulação de dados em tabelas.
- **inspect**: para inspecionar assinaturas de funções.

## Funcionalidades

1. **Entrada de Dados**: 
   - Recebe parâmetros específicos para áreas rurais e/ou urbanas, como coeficientes de escoamento e valores de intensidade de precipitação.

2. **Definição das Funções de Cálculo**:
   - Implementa diversas equações para calcular o tempo de concentração (Tc) em áreas rurais e urbanas. Exemplos: `izzard`, `kerby_hathaway`, `onda_cinematica`, entre outras.

3. **Execução dos Cálculos**:
   - As funções são chamadas automaticamente para calcular Tc conforme os parâmetros fornecidos pelo usuário para cada região.

4. **Formatação e Exibição dos Resultados**:
   - Formata e exibe os resultados dos cálculos em tabelas distintas para regiões rurais, urbanas, ou ambas, dependendo da entrada inicial.

## Uso

Para rodar o script:
1. Execute o arquivo no ambiente Python.
2. Insira os dados conforme solicitado para as regiões rurais e/ou urbanas.
3. O resultado exibirá o cálculo do tempo de concentração (Tc) de acordo com as variáveis fornecidas.


## Equações Implementadas

Este projeto inclui as seguintes equações para o cálculo do tempo de concentração (Tc):

- **Izzard, Kerby - Hathaway, Onda Cinemática, FAA, Kirpich, SCS Lag, Simas-Hawkins, Ven te Chow, Dooge, Johnstone, Corps Engineers, Giandotti, Pasini, Ventura, Picking, DNOS, George Ribeiro, Schaake et al, McCuen et al, Carter, Eagleson, Desbordes, Espey-Winslow**

Cada equação calcula Tc com base em parâmetros como intensidade da chuva, coeficiente de escoamento e características de terreno (declividade e comprimento).

## Tabelas de Resultados

O programa exibe as tabelas dos valores de Tc calculados para as regiões especificadas:
- **Rurais e Urbanas**: Tabela com Tc para ambas as regiões.
- **Somente Rurais ou Urbanas**: Tabelas individuais para cada região, conforme a seleção inicial.

## Exemplo de Saída

A saída contém tabelas formatadas com o tempo de concentração para cada equação, permitindo uma comparação dos resultados conforme os parâmetros definidos.

