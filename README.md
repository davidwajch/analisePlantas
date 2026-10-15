# Detector de Doenças em Plantas

Sistema de detecção e monitoramento de áreas afetadas por doenças/pragas em plantas usando visão computacional.

## Motivação

Ferramenta para auxiliar na identificação rápida de problemas em plantas através de análise de imagem, calculando a porcentagem de área afetada e sugerindo ações conforme a gravidade.

## Stack

- Python 3
- OpenCV (processamento de imagem e detecção de contornos)
- NumPy (operações com arrays)

## Como Rodar

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar
python codigo.py
```

O programa oferece três modos de operação:
- **webcam**: captura em tempo real da webcam
- **imagem**: análise de arquivo estático (`planta.jpg`)
- **video**: análise de arquivo MP4 (informe o caminho quando solicitado)

## Como Funciona

1. **Captura**: lê imagem da webcam, arquivo estático ou vídeo
2. **Conversão**: transforma a imagem de RGB para HSV
3. **Segmentação**: cria máscara para isolar áreas com coloração característica de doença (tons amarelo/marrom)
4. **Detecção**: identifica contornos das áreas afetadas
5. **Cálculo**: determina porcentagem de área afetada em relação ao total
6. **Análise**: classifica gravidade e sugere ações:
   - **< 10%**: baixa, nenhuma ação imediata necessária
   - **10-50%**: moderada, ações de controle recomendadas
   - **> 50%**: alta, tratamento urgente

## Estrutura

```
.
├── codigo.py           # código principal
├── requirements.txt    # dependências Python
├── planta.jpg          # imagem de exemplo
└── README.md
```

## Exemplo

O projeto inclui `planta.jpg` como imagem de teste. Para vídeos, utilize seus próprios arquivos MP4.

## Limitações e Próximos Passos

- Atualmente detecta apenas áreas com base em faixa HSV fixa (tons amarelo/marrom)
- Possíveis melhorias:
  - Detecção de múltiplos tipos de doenças/pragas
  - Classificação usando machine learning
  - Interface gráfica
  - Histórico de análises e evolução temporal

## Licença

MIT - veja [LICENSE](LICENSE)
