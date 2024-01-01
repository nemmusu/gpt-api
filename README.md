# GPT Chat Bot

Questo progetto fornisce uno script Python per interfacciarsi con il modello di linguaggio GPT di OpenAI e una GUI per utilizzarlo.

## Indice

- [Installazione](#installazione)
- [Utilizzo](#utilizzo)
- [Interfaccia](#interfaccia)
- [Creazione dell'eseguibile](#creazione-delleseguibile)

## Installazione

Prima di tutto, dovrai scaricare il progetto dal repository GitHub. Apri il terminale e posizionati nella cartella in cui desideri scaricare il progetto. Puoi farlo utilizzando il comando `cd`, seguito dal percorso della cartella. Ad esempio:

```shell
cd /percorso/alla/cartella
```

Successivamente, clona il repository utilizzando il comando `git clone`, seguito dall'URL del repository:

```shell
git clone https://github.com/nemmusu/gpt-api.git
```

Ora dovresti avere una copia del progetto nella tua cartella locale. Per accedere alla cartella del progetto, usa ancora il comando `cd`:

```shell
cd gpt-api
```

Per installare la libreria `openai` necessaria per questo progetto, eseguire il seguente comando:

```shell
pip install openai
```

## Utilizzo

### File di configurazione

Il file `config.ini` viene utilizzato per configurare vari aspetti del chat bot, si consiglia di configurarlo per un corretto funzionamento prima di avviare gli script. Ecco un esempio:

```ini
[OPENAI]
api_key = tua_api_key
domanda = Cosa consigli di fare oggi?
temperature = 0.7
model = gpt-3.5-turbo
system_role_message = Siamo qui per aiutarti a rispondere alle tue domande.
```

### Utilizzo della Classe GPT

Per utilizzare la classe GPT, creiamo un'istanza di GPT e chiamiamo il metodo get_chat_response(). Tutti i parametri sono opzionali e, se non specificati, verranno prelevati dal file di configurazione.

### Esempio d'uso senza parametri
```python
from gpt import GPT

chatbot = GPT() # Utilizza i valori predefiniti del file di configurazione
risposta = chatbot.get_chat_response()
print(risposta)
```

### Esempio d'uso con parametri

```python
from gpt import GPT

chatbot = GPT(api_key='your_api_key', domanda='Qual è il significato della vita?', 
              temperature=0.5, model='gpt-4', 
              system_role_message='Questo è un esempio di sistema di messaggi')
risposta = chatbot.get_chat_response()
print(risposta)
```

## Parametri

- `config_file`: Il percorso del file di configurazione (default: `config.ini`)
- `api_key`: La chiave API di OpenAI
- `domanda`: La domanda da passare al modello GPT
- `temperature`: La temperatura per il modello GPT
- `model`: Il modello GPT da utilizzare
- `system_role_message`: Il messaggio del ruolo di sistema per il modello GPT

### Script gpt.py

Lo script `gpt.py` può essere eseguito da solo o importato come modulo. Tutti i parametri sono opzionali e, se non specificati, verranno prelevati dal file di configurazione. Per eseguirlo, utilizzare il seguente comando:

```shell
python gpt.py --domanda "Cosa consigli di fare oggi?" --temperature 0.7 --model gpt-3.5-turbo
```

## I parametri disponibili sono:

- `--config`: Percorso del file di configurazione (default: `config.ini`).
- `--api_key`: La chiave API per OpenAI.
- `--domanda`: La domanda da passare al modello GPT.
- `--temperature`: La temperatura per il modello GPT.
- `--model`: Il modello GPT da utilizzare.
- `--system_role_message`: Il messaggio del ruolo di sistema per il modello GPT.

Per visualizzare l'help del comando, eseguire:

```shell
python gpt.py --help
```

## Interfaccia

L'interfaccia implementata in `gui.pyw`, utilizza PyQt5. Per installare PyQt5, eseguire il comando:

```shell
pip install pyqt5
```

Per eseguire l'interfaccia GUI, eseguire il comando:

```shell
python gui.pyw
```

## Creazione dell'eseguibile

### PyInstaller

Per creare un eseguibile con PyInstaller, utilizzare il seguente comando:

```shell
pyinstaller --onefile --name "GUI_ChatGPT" gui.pyw --hidden-import=gpt --hidden-import=argparse --hidden-import=configparser --hidden-import=openai --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtWidgets
```

### cx_Freeze

Per creare un eseguibile con cx_Freeze, è necessario avere il file `compile_cx_freeze.py` nella stessa directory e poi eseguire il comando:

```shell
python compile_cx_freeze.py build
```

Il comando creerà un pacchetto strutturato con cartelle contenenti l'eseguibile e le librerie necessarie.
