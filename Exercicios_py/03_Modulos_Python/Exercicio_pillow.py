import image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
WORK_FILE = ROOT_FOLDER / 'LYR.png'
NEW_FILE = ROOT_FOLDER / 'LYR_NEW.png'

pil_image = open(WORK_FILE)

print(pil_image.__sizeof__)
