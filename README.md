# Projeto de Detecção e Monitoramento de Doenças e Pragas em Plantas usando Visão Computacional

O objetivo deste projeto é utilizar visão computacional e processamento de imagem para detectar e monitorar doenças e pragas em plantas. Essa solução visa auxiliar os agricultores a identificar rapidamente problemas em suas culturas, permitindo a implementação de medidas adequadas. O sistema fornece informações sobre a porcentagem de área afetada e recomendações para o controle e tratamento.

## Processo

1. **Captura de Imagens:** O sistema é capaz de capturar imagens por meio de uma webcam, carregar uma imagem estática ou ler um vídeo MP4.

2. **Processamento de Imagem:** As imagens capturadas ou lidas são processadas para identificar as áreas afetadas nas plantas. Primeiramente, é realizada a conversão da imagem do espaço de cores RGB para o espaço de cores HSV, facilitando assim a segmentação das áreas de interesse.

3. **Segmentação das Áreas Afetadas:** Com base nos intervalos de valores definidos para o espaço de cores HSV, é criada uma máscara que destaca as áreas da imagem correspondentes às plantas afetadas.

4. **Detecção de Contornos:** Os contornos das áreas afetadas são identificados utilizando o algoritmo de detecção de contornos do OpenCV. Esses contornos representam as formas das áreas afetadas nas plantas.

5. **Cálculo da Porcentagem de Área Afetada:** Com os contornos obtidos, é possível calcular a porcentagem de área afetada em relação à área total da imagem. Esse cálculo é feito somando as áreas de todos os contornos e dividindo pelo tamanho total da imagem.

6. **Análise e Tomada de Decisão:** Com base na porcentagem de área afetada, critérios são estabelecidos para avaliar o nível de gravidade da infestação. São exibidas mensagens indicando o nível de gravidade e ações recomendadas, como medidas de controle e tratamento específicas para cada nível identificado.

7. **Visualização dos Resultados:** Os resultados são exibidos na imagem original, destacando as áreas afetadas por meio de contornos. Além disso, são exibidas mensagens indicando a porcentagem de área afetada e as ações recomendadas de acordo com o nível de gravidade.

# Exemplo

[Download do Vídeo](video.mp4)
