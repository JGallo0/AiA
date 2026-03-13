from datetime import datetime

def ask():
    print("\nAstraCarbon Intelligence Assistant\n")

    question = input("Pergunta: ")

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file = f"outputs/saida_{now}.txt"

    with open(file, "w", encoding="utf-8") as f:
        f.write("Pergunta:\n")
        f.write(question)

    print(f"\nResposta salva em {file}\n")

if __name__ == "__main__":
    ask()