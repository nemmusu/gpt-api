import argparse
import configparser
import openai

class GPT:
    def __init__(self, config_file='config.ini', api_key=None, domanda=None, temperature=None, model=None, system_role_message=None):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        # Utilizza i valori dal file di configurazione se non sono forniti come argomenti
        self.api_key = api_key if api_key else self.config['OPENAI']['api_key']
        self.domanda = domanda if domanda else self.config['OPENAI']['domanda']
        self.temperature = float(temperature) if temperature else float(self.config['OPENAI']['temperature'])
        self.model = model if model else self.config['OPENAI']['model']
        self.system_role_message = system_role_message if system_role_message else self.config['OPENAI']['system_role_message']
        
        openai.api_key = self.api_key

    def get_chat_response(self):
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_role_message},
                    {"role": "user", "content": self.domanda}
                ],
                temperature=self.temperature
            )
            return response.choices[0].message.content
        except openai.Error as e:
            print(f"Errore nell'esecuzione della richiesta: {e}")
            return None

def main():
    parser = argparse.ArgumentParser(description="Utilizzo del modulo GPT")
    parser.add_argument("--config", default="config.ini", help="Percorso del file di configurazione (default: ./config.ini)")
    parser.add_argument("--api_key", help="Chiave API di OpenAI")
    parser.add_argument("--domanda", help="Domanda da passare al modello GPT")
    parser.add_argument("--temperature", type=float, help="Temperatura per il modello GPT")
    parser.add_argument("--model", help="Modello GPT da utilizzare")
    parser.add_argument("--system_role_message", help="Messaggio del ruolo di sistema per il modello GPT")
    args = parser.parse_args()

    try:
        chatbot = GPT(config_file=args.config, api_key=args.api_key, domanda=args.domanda,
                      temperature=args.temperature, model=args.model, system_role_message=args.system_role_message)
        risposta_gpt = chatbot.get_chat_response()
        if risposta_gpt:
            print(risposta_gpt)
        else:
            print("Si è verificato un errore durante la richiesta.")
    except FileNotFoundError as e:
        print(f"File di configurazione non trovato: {e}")
    except ValueError as e:
        print(f"Errore nel valore fornito: {e}")

if __name__ == "__main__":
    main()