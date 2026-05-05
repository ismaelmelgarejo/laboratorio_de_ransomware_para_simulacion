from os_detector import detect_os
from file_scanner import scan_pdfs
from encryptor_sim import simulate_encryption
from logger import log

DOCUMENTS = "../sandbox/documentos"
DESKTOP = "../sandbox/escritorio"

def main():
    log("=== Inicio de simulación ===")

    os_detected = detect_os()
    log(f"Sistema operativo detectado: {os_detected}")

    files = scan_pdfs(DOCUMENTS)
    log(f"Archivos encontrados: {len(files)}")

    encrypted = simulate_encryption(files, DESKTOP)
    log(f"Archivos 'cifrados': {len(encrypted)}")

    create_ransom_note(DESKTOP)

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