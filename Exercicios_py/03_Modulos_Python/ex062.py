from pathlib import Path
from PyPDF2 import PdfReader,PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORGINAIS = PASTA_RAIZ/ 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORGINAIS /'banco.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

#for page in reader.pages:
#    print(page)
#    print()

page0 =reader.pages[0]

writer = PdfWriter()
writer.add_page(page0)
with open(PASTA_NOVA / 'page0.pdf','wb' ) as arquivo:
    writer.write(arquivo) #type: ignore
