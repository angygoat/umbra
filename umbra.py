from datetime import datetime

TIPOS = ["mental", "habito", "tiempo", "creativo"]

def elegir_tipo():
    print("\nElige tipo de evento:\n")
    for i, t in enumerate(TIPOS, 1):
        print(f"{i}. {t}")
    while True:
        try:
            opcion = int(input("\nNúmero: "))
            if 1 <= opcion <= len(TIPOS):
                return TIPOS[opcion - 1]
        except:
            pass
        print("Opción inválida.")

def main():
    print("\n=== UMBRA EVENTOS ===")
    tipo = elegir_tipo()
    descripcion = input("\nDescribe el evento: ").strip()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    linea = f"{tipo} | {descripcion} | {fecha}\n"

    with open("eventos.log", "a", encoding="utf-8") as f:
        f.write(linea)

    print("\nGuardado:")
    print(linea)

if __name__ == "__main__":
    main()
