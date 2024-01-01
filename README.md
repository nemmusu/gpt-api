# Tutorial su come utilizzare la libreria GPT
La classe GPT in questo script Python è progettata per utilizzare il modello di linguaggio GPT di OpenAI per generare risposte basate sulle domande fornite.

## Installazione
Prima di tutto, assicurati di avere installato la libreria openai con il seguente comando:
```bash
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

```bash
python gpt.py --domanda "Cosa consigli di fare oggi?" --temperature 0.7 --model gpt-3.5-turbo
```

### Parametri

- **config_file**: Percorso del file di configurazione (default: config.ini).
- **api_key**: La chiave API per OpenAI.
- **domanda**: La domanda da passare al modello GPT.
- **temperature**: La temperatura per il modello GPT.
- **model**: Il modello GPT da utilizzare.
- **system_role_message**: Il messaggio del ruolo di sistema per il modello GPT.

### Gestione degli Errori
Il modulo gestisce i seguenti errori:
- **openai.Error**: Questo errore viene sollevato se c'è un problema con la richiesta a OpenAI.
- **FileNotFoundError**: Questo errore viene sollevato se il file di configurazione non può essere trovato.
- **ValueError**: Questo errore viene sollevato se viene fornito un valore non valido per un parametro.

## Interfaccia grafica con PyQt
Esiste un file chiamato `gui.pyw` che funziona con `config.ini` e fornisce un'interfaccia grafica per il chatbot utilizzando PyQt. 

### Installazione di PyQt
Puoi installare PyQt con il seguente comando:
```bash
pip install pyqt5
```

## Creazione di un file eseguibile
Puoi creare un file eseguibile del tuo chatbot utilizzando `pyinstaller` o `cx_freeze`.

### Utilizzo di PyInstaller
Esegui il seguente comando per creare un file eseguibile con PyInstaller:
```bash
pyinstaller --onefile --name "GUI_ChatGPT" gui.pyw --hidden-import=gpt --hidden-import=argparse --hidden-import=configparser --hidden-import=openai --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtWidgets
```

### Utilizzo di cx_Freeze
Esegui il seguente comando per creare un file eseguibile con cx_Freeze:
```bash
python compile_cx_freeze.py build
```