# GPT Chat Bot

Questo progetto fornisce uno script Python per interfacciarsi con il modello di linguaggio GPT di OpenAI e una GUI per utilizzarlo.

## Tabella dei contenuti

1. [Readme](#readme)
    - [README: Italiano](./README_IT.md)
    - [README: English](./README.md)
2. [Installazione](#installazione)
3. [Utilizzo](#utilizzo)
   - [File di configurazione](#file-di-configurazione)
   - [Utilizzo della classe GPT](#utilizzo-della-classe-gpt)
   - [Script gpt.py](#script-gptpy)
4. [Interfaccia](#interfaccia)
5. [Creazione dell'eseguibile](#creazione-delleseguibile)
   - [PyInstaller](#pyinstaller)
   - [cx_Freeze](#cxfreeze)
6. [Eseguibile](#eseguibile)
7. [Screenshots](#screenshots)

## Installazione <a name="installazione"></a>
Per installare il progetto, segui questi passaggi:

1. Scarica il progetto dal repository GitHub. Apri il terminale e naviga nella cartella in cui desideri scaricare il progetto. Puoi farlo utilizzando il comando `cd` seguito dal percorso della cartella.
    ```shell
    cd /percorso/alla/cartella
    ```
2. Clona il repository utilizzando il comando `git clone` seguito dall'URL del repository:
    ```shell
    git clone https://github.com/nemmusu/gpt-api.git
    ```
3. Accedi alla cartella del progetto:
    ```shell
    cd gpt-api
    ```
4. Installa la libreria `openai` richiesta per questo progetto:
    ```shell
    pip install openai
    ```

## Utilizzo <a name="utilizzo"></a>

### File di configurazione <a name="file-di-configurazione"></a>
Il file `config.ini` viene utilizzato per configurare vari aspetti del chat bot. Ecco un esempio di come potrebbe essere configurato:

```ini
[OPENAI]
api_key = la_tua_api_key
question = Cosa consigli di fare oggi?
temperature = 0.7
model = gpt-3.5-turbo
system_role_message = Sei un assistente esperto e risponderai alle mie domande in maniera specifica e dettagliata esclusivamente in formato markdown.
```

### Utilizzo della classe GPT <a name="utilizzo-della-classe-gpt"></a>
Per utilizzare la classe GPT, istanzia un oggetto GPT e chiama il metodo `get_chat_response()`. Tutti i parametri sono opzionali e se non specificati verranno recuperati dal file di configurazione.

Ecco un esempio di utilizzo senza parametri:
```python
from gpt import GPT

chatbot = GPT() # Utilizza i valori predefiniti dal file di configurazione
response = chatbot.get_chat_response()
print(response)
```

E un esempio di utilizzo con parametri:
```python
from gpt import GPT

chatbot = GPT(config_file='/percorso/al/file/config.ini', api_key='la_tua_api_key', question='Qual è il significato della vita?', 
              temperature=0.5, model='gpt-4', 
              system_role_message='Sei un assistente esperto e risponderai alle mie domande in maniera specifica e dettagliata esclusivamente in formato markdown.')
response = chatbot.get_chat_response()
print(response)
```

I parametri disponibili sono:

- `config_file`: Il percorso del file di configurazione (predefinito: `config.ini`)
- `api_key`: La chiave API di OpenAI
- `question`: La domanda da passare al modello GPT
- `temperature`: La temperatura per il modello GPT
- `model`: Il modello GPT da utilizzare
- `system_role_message`: Il messaggio di ruolo del sistema per il modello GPT

### Script gpt.py <a name="script-gptpy"></a>
Lo script `gpt.py` può essere eseguito autonomamente o importato come modulo. Tutti i parametri sono opzionali e se non specificati verranno recuperati dal file di configurazione.

Puoi eseguirlo utilizzando il seguente comando:
```shell
python gpt.py --question "Cosa consigli di fare oggi?" --temperature 0.7 --model gpt-3.5-turbo
```
I parametri disponibili sono:

- `--config`: Il percorso del file di configurazione (predefinito: `config.ini`).
- `--api_key`: La chiave API per OpenAI.
- `--question`: La domanda da passare al modello GPT.
- `--temperature`: La temperatura per il modello GPT.
- `--model`: Il modello GPT da utilizzare.
- `--system_role_message`: Il messaggio di ruolo del sistema per il modello GPT.

Per visualizzare l'aiuto del comando, esegui:
```shell
python gpt.py --help
```

## Interfaccia <a name="interfaccia"></a>
L'interfaccia implementata in `gui.pyw` utilizza PyQt5. Per installare PyQt5, esegui il seguente comando:
```shell
pip install pyqt5
```
Per eseguire l'interfaccia grafica, esegui il seguente comando:
```shell
python gui.pyw
```

## Creazione dell'eseguibile <a name="creazione-delleseguibile"></a>

### PyInstaller <a name="pyinstaller"></a>
Per creare un eseguibile utilizzando PyInstaller, è necessario installare PyInstaller sul tuo sistema. Puoi farlo utilizzando il seguente comando:

```
pip install pyinstaller
```

Una volta installato PyInstaller, puoi creare l'eseguibile utilizzando il seguente comando:

```
pyinstaller --onefile --name "GUI_ChatGPT" gui.pyw --hidden-import=gpt --hidden-import=argparse --hidden-import=configparser --hidden-import=openai --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtWidgets
```

Questo comando crea un singolo file eseguibile chiamato "GUI_ChatGPT" utilizzando "gui.pyw" come punto di ingresso. Vengono specificate anche le dipendenze nascoste come "gpt", "argparse", "configparser", "openai", "PyQt5.QtCore" e "PyQt5.QtWidgets" da includere nell'eseguibile.

### cx_Freeze <a name="cxfreeze"></a>
Per creare un eseguibile utilizzando cx_Freeze, è necessario installare cx_Freeze sul tuo sistema. Puoi farlo utilizzando il seguente comando:

```
pip install cx_Freeze
```

Una volta installato cx_Freeze, puoi creare l'eseguibile utilizzando il seguente comando:

```
python compile_cx_freeze.py build
```

Questo comando creerà un pacchetto strutturato con le cartelle contenenti l'eseguibile e le librerie necessarie.

## Eseguibile <a name="eseguibile"></a>

Nella cartella `dist` è presente una versione eseguibile del programma (già compilato e pronto per l'uso) e il relativo file di configurazione da modificare con i dati corretti.

## Screenshots <a name="screenshots"></a>

![Screenshot GPT API](https://github.com/nemmusu/gpt-api/blob/main/screenshots/interface-example.png)
