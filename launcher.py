import time
import os
import subprocess
import platform

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typing_effect(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def fake_loading():
    steps = [
        "Inicializando sistema...",
        "Cargando módulos de análisis...",
        "Verificando entorno sandbox...",
        "Escaneando archivos...",
        "Preparando simulación..."
    ]

    for step in steps:
        typing_effect(f"[+] {step}")
        time.sleep(0.5)

def run_simulator():
    typing_effect("\n[+] Ejecutando simulación...\n")
    
    if platform.system() == "Windows":
        subprocess.run(["python", "simulator/main.py"])
    else:
        subprocess.run(["python3", "simulator/main.py"])

def main():
    clear()
    
    print("="*50)
    typing_effect("   RANSOMWARE SIMULATION LAB", 0.02)
    print("="*50)
    
    time.sleep(1)
    
    typing_effect("\n⚠️  Entorno educativo controlado")
    typing_effect("⚠️  No se realizan acciones maliciosas\n")
    
    input("Presiona ENTER para iniciar la simulación...")
    
    clear()
    
    fake_loading()
    run_simulator()
    
    typing_effect("\n[✔] Simulación finalizada")
    typing_effect("[✔] Revisa los logs y resultados\n")

if __name__ == "__main__":
    main()