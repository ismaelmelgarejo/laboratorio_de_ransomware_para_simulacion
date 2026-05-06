import os
import platform
import subprocess
from os_detector import detect_os
from file_scanner import scan_pdfs
from encryptor_sim import simulate_encryption
from logger import log

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "..", "assets", "alert.png")

DOCUMENTS = os.path.join(BASE_DIR, "..", "sandbox", "documentos")
DESKTOP = os.path.join(BASE_DIR, "..", "sandbox", "escritorio")

def open_image(path):
    os_name = platform.system()

    if os_name == "Windows":
        os.startfile(path)
    elif os_name == "Darwin":
        subprocess.run(["open", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif os_name == "Linux":
        subprocess.run(["xdg-open", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    log("=== Inicio de simulación ===")

    os_detected = detect_os()
    log(f"Sistema operativo detectado: {os_detected}")

    files = scan_pdfs(DOCUMENTS)
    log(f"Archivos encontrados: {len(files)}")

    encrypted = simulate_encryption(files, DESKTOP)
    log(f"Archivos 'cifrados': {len(encrypted)}")

    create_ransom_note(DESKTOP)

    open_image(IMAGE_PATH)

    log("=== Fin de simulación ===")

def create_ransom_note(path):
    note = f"""
    ⚠️ SIMULACIÓN EDUCATIVA ⚠️

    Tus archivos han sido "cifrados" (esto es solo una simulación).

    En un ataque real:
    - Los archivos serían inaccesibles
    - Se pediría un pago (ransom)

    Recomendaciones:
    - Mantener backups
    - No abrir archivos sospechosos
    - Actualizar sistemas

    """
    with open(f"{path}/README_RESTORE.txt", "w") as f:
        f.write(note)

if __name__ == "__main__":
    main()