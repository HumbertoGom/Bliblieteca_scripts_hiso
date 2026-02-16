import os
from pathlib import Path
import zipfile


CAMINHO_COMPACTADO = r"C:\Users\sarge\OneDrive\Documentos\python-curso\hisoka\hisoka.zip"
CAMINHO_EXTRAIDO = r"C:\Users\sarge\OneDrive\Documentos\python-curso\hisoka\Extracao"


NOVOZIP= r"C:\Users\sarge\OneDrive\Documentos\python-curso\hisoka\Extracao\Naruto.zip"

SAIDATXT = r"C:\Users\sarge\OneDrive\Documentos\python-curso\hisoka\saida.txt"
LYRA= r"C:\Users\sarge\OneDrive\Documentos\python-curso\hisoka\LYR.png"

with zipfile.ZipFile(NOVOZIP,'w') as zip_ref:
    zip_ref.write(SAIDATXT)
    zip_ref.write(LYRA)