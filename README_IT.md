# Readme
[README in italiano](./README_IT.md)

[English README](./README.md)

# GPT Chat Bot
Questo progetto fornisce uno script Python per interfacciarsi con il modello di linguaggio GPT di OpenAI e una GUI per utilizzarlo.

## Indice
1. [Installazione](#installazione)
2. [Utilizzo](#utilizzo)
   - [File di configurazione](#file-di-configurazione)
   - [Utilizzo della Classe GPT](#utilizzo-della-classe-gpt)
   - [Script gpt.py](#script-gptpy)
3. [Interfaccia](#interfaccia)
4. [Creazione dell'eseguibile](#creazione-delleseguibile)
   - [PyInstaller](#pyinstaller)
   - [cx_Freeze](#cxfreeze)

## Installazione <a name="installazione"></a>
Per installare il progetto, segui i seguenti passaggi:

1. Scarica il progetto dal repository GitHub. Apri il terminale e posizionati nella cartella in cui desideri scaricare il progetto. Puoi farlo utilizzando il comando `cd`, seguito dal percorso della cartella.
    ```shell
    cd /percorso/alla/cartella
    ```
2. Clona il repository utilizzando il comando `git clone`, seguito dall'URL del repository:
    ```shell
    git clone https://github.com/nemmusu/gpt-api.git
    ```
3. Accedi alla cartella del progetto:
    ```shell
    cd gpt-api
    ```
4. Installa la libreria `openai` necessaria per questo progetto:
    ```shell
    pip install openai
    ```

## Utilizzo <a name="utilizzo"></a>

### File di configurazione <a name="file-di-configurazione"></a>
Il file `config.ini` viene utilizzato per configurare vari aspetti del chat bot. Ecco un esempio di come potrebbe essere configurato:

```ini
[OPENAI]
api_key = tua_api_key
domanda = Cosa consigli di fare oggi?
temperature = 0.7
model = gpt-3.5-turbo
system_role_message = Siamo qui per aiutarti a rispondere alle tue domande.
```

### Utilizzo della Classe GPT <a name="utilizzo-della-classe-gpt"></a>
Per utilizzare la classe GPT, creiamo un'istanza di GPT e chiamiamo il metodo `get_chat_response()`. Tutti i parametri sono opzionali e, se non specificati, verranno prelevati dal file di configurazione.

Ecco un esempio d'uso senza parametri:
```python
from gpt import GPT

chatbot = GPT() # Utilizza i valori predefiniti del file di configurazione
risposta = chatbot.get_chat_response()
print(risposta)
```

E un esempio d'uso con parametri:
```python
from gpt import GPT

chatbot = GPT(config_file='/etc/gpt-api/config.ini', api_key='your_api_key', domanda='Qual è il significato della vita?', 
              temperature=0.5, model='gpt-4', 
              system_role_message='sei un assistente esperto e risponderai alle mie domande scrivendo in maniera specifica e dettagliata esclusivamente in formato markdown')
risposta = chatbot.get_chat_response()
print(risposta)
```

I parametri che puoi utilizzare sono i seguenti:

- `config_file`: Il percorso del file di configurazione (default: `config.ini`)
- `api_key`: La chiave API di OpenAI
- `domanda`: La domanda da passare al modello GPT
- `temperature`: La temperatura per il modello GPT
- `model`: Il modello GPT da utilizzare
- `system_role_message`: Il messaggio del ruolo di sistema per il modello GPT

### Script gpt.py <a name="script-gptpy"></a>
Lo script `gpt.py` può essere eseguito da solo o importato come modulo. Tutti i parametri sono opzionali e, se non specificati, verranno prelevati dal file di configurazione.

Puoi eseguirlo utilizzando il seguente comando:
```shell
python gpt.py --domanda "Cosa consigli di fare oggi?" --temperature 0.7 --model gpt-3.5-turbo
```
I parametri disponibili sono:

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

## Interfaccia <a name="interfaccia"></a>
L'interfaccia implementata in `gui.pyw` utilizza PyQt5. Per installare PyQt5, eseguire il comando:
```shell
pip install pyqt5
```
Per eseguire l'interfaccia GUI, eseguire il comando:
```shell
python gui.pyw
```

## Creazione dell'eseguibile <a name="creazione-delleseguibile"></a>

### PyInstaller <a name="pyinstaller"></a>
Per creare un eseguibile con PyInstaller, utilizzare il seguente comando:
```shell
pyinstaller --onefile --name "GUI_ChatGPT" gui.pyw --hidden-import=gpt --hidden-import=argparse --hidden-import=configparser --hidden-import=openai --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtWidgets
```

### cx_Freeze <a name="cxfreeze"></a>
Per creare un eseguibile con cx_Freeze, è necessario avere il file `compile_cx_freeze.py` nella stessa directory e poi eseguire il comando:
```shell
python compile_cx_freeze.py build
```
Il comando creerà un pacchetto strutturato con cartelle contenenti l'eseguibile e le librerie necessarie.