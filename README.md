# Tutorial su come utilizzare la libreria GPT

La classe GPT in questo script Python è progettata per utilizzare il modello di linguaggio GPT di OpenAI per generare risposte basate sulle domande fornite.

## Installazione

Prima di tutto, assicurati di avere installato la libreria openai con il seguente comando:

```shell
pip install openai
```

## Utilizzo

### Creazione del File di Configurazione

Il costruttore della classe GPT utilizza un file di configurazione per ottenere i parametri di default. Ecco un esempio di file di configurazione (config.ini):

```ini
[OPENAI]
api_key = tua_api_key
domanda = "Cosa consigli di fare oggi?"
temperature = 0.7
model = "gpt-3.5-turbo"
system_role_message = "Siamo qui per aiutarti a rispondere alle tue domande."
```

### Utilizzo della Classe GPT

Per utilizzare la classe GPT, creiamo un'istanza di GPT e chiamiamo il metodo get_chat_response(). Tutti i parametri sono opzionali e, se non specificati, verranno prelevati dal file di configurazione.

```python
from gpt import GPT
chatbot = GPT()
risposta = chatbot.get_chat_response()
print(risposta)
```

### Utilizzo dello Script come Modulo da CommandLine

Lo script può anche essere utilizzato come modulo da linea di comando. Ecco un esempio di utilizzo:

```shell
python gpt.py --domanda "Cosa consigli di fare oggi?" --temperature 0.7 --model gpt-3.5-turbo
```

#### Parametri

- config_file: Percorso del file di configurazione (default: config.ini).
- api_key: La chiave API per OpenAI.
- domanda: La domanda da passare al modello GPT.
- temperature: La temperatura per il modello GPT.
- model: Il modello GPT da utilizzare.
- system_role_message: Il messaggio del ruolo di sistema per il modello GPT.

### Gestione degli Errori

Il modulo gestisce i seguenti errori:

- openai.Error: Questo errore viene sollevato se c'è un problema con la richiesta a OpenAI.
- FileNotFoundError: Questo errore viene sollevato se il file di configurazione non può essere trovato.
- ValueError: Questo errore viene sollevato se viene fornito un valore non valido per un parametro.

## Interfaccia GUI con PyQt

Esiste anche un'interfaccia grafica utente (GUI) per il bot, implementata nel file `gui.pyw`. Questa interfaccia utilizza la libreria PyQt e funziona con il file `config.ini` sopra descritto.

### Installazione di PyQt

Per installare PyQt, puoi usare pip:

```shell
pip install pyqt5
```

### Esecuzione di gui.pyw

Per eseguire l'interfaccia GUI, esegui il seguente comando:

```shell
python gui.pyw
```

## Creazione dell'eseguibile

Per creare un eseguibile del tuo bot, puoi utilizzare PyInstaller o cx_Freeze. 

### PyInstaller

Per PyInstaller, esegui il seguente comando:

```shell
pyinstaller --onefile --name "GUI_ChatGPT" gui.pyw --hidden-import=gpt --hidden-import=argparse --hidden-import=configparser --hidden-import=openai --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.Widgets
```

### cx_Freeze

Per cx_Freeze, esegui il seguente comando:

```shell
python compile_cx_freeze.py build
```
Ricorda di avere il file `compile_cx_freeze.py` nella stessa directory in cui stai eseguendo il comando.