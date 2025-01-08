# Documentação: Scalers no Scikit-Learn

Esta documentação explica o funcionamento de três scalers amplamente utilizados na normalização de dados: RobustScaler, MinMaxScaler e StandardScaler, bem como suas diferenças e casos de uso.

RobustScaler
-
O que faz:

- Escalona os dados com base na mediana (Q2) e no intervalo interquartil (IQR).
- Resistente a outliers: valores extremos têm pouco impacto no resultado.

Como funciona:

- Subtrai a mediana (Q2) de cada valor.
- Divide pelo intervalo interquartil (IQR = Q3 - Q1).

Quando usar:

- Dados com outliers (valores extremos) que podem distorcer outras escalas.
- Quando os dados não seguem uma distribuição normal.

MinMaxScaler
-
O que faz:

- Escalona os dados para um intervalo específico, como[0,1] (por padrão).
- Preserva as relações proporcionais entre os valores.

Como funciona:

- Subtrai o valor mínimo da feature (Xmin).
- Divide pela amplitude (Xmax - Xmin)

Quando usar:

- Dados sem outliers significativos.
- Modelos sensíveis ao intervalo de valores, como redes neurais e algoritmos baseados em gradientes.

StandardScaler
-
O que faz:

- Escalona os dados para que tenham média igual a 0 e desvio padrão igual a 1.
- Útil para transformar os dados em uma distribuição normal padrão.

Como funciona:

- Subtrai a média (𝜇) da feature.
- Divide pelo desvio padrão (𝜎).

Quando usar:

- Modelos que assumem que os dados são normalmente distribuídos.
- Algoritmos sensíveis à escala, como regressão logística, SVM, e PCA

Diferenças entre os Scalers
-
<table>
  <thead>
    <tr>
      <th>Método</th>
      <th>Base Estatística</th>
      <th>Resistência a Outliers</th>
      <th>Intervalo Resultante</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RobustScaler</td>
      <td>Mediana e IQR</td>
      <td>Alta</td>
      <td>Proporcional à mediana/IQR</td>
    </tr>
    <tr>
      <td>MinMaxScaler</td>
      <td>Mínimo e máximo</td>
      <td>Baixa</td>
      <td>Customizável (por padrão, [0, 1])</td>
    </tr>
    <tr>
      <td>StandardScaler</td>
      <td>Média e desvio padrão</td>
      <td>Baixa</td>
      <td>Média = 0, Desvio = 1</td>
    </tr>
  </tbody>
</table>

Quando Usar Cada Um
-

RobustScaler: Dados com outliers (valores extremos).
Quando os dados não precisam estar em um intervalo específico, mas precisam ser escalados.

MinMaxScaler: Quando os dados não possuem outliers significativos.
Modelos sensíveis a intervalos fixos, como redes neurais e visualizações.

StandardScaler: Dados que seguem ou precisam se aproximar de uma distribuição normal.
Algoritmos baseados em distância, como SVM, regressão logística e PCA.