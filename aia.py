from datetime import datetime
import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():

    print("\nAiA — AstraCarbon Inteligência Artificial\n")

    while True:

        question = input("Pergunta (ou digite sair): ")

        if question.lower() == "sair":
            print("Encerrando.")
            break

        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        file = f"{OUTPUT_DIR}/aia_{now}.txt"

        with open(file, "w", encoding="utf-8") as f:
            f.write("Pergunta:\n")
            f.write(question)

        print("\nPergunta registrada.")
        print(f"Arquivo salvo em {file}\n")

if __name__ == "__main__":
    main()