# Tutorial su come utilizzare la libreria GPT

La classe GPT in questo script Python è progettata per utilizzare il modello di linguaggio GPT di OpenAI per generare risposte basate sulle domande fornite.

## Installazione

Prima di tutto, assicurati di avere installato la libreria openai con il seguente comando:

```python
pip install openai
```

## Utilizzo

### Creazione del File di Configurazione

Il costruttore della classe GPT utilizza un file di configurazione per ottenere i parametri di default. Ecco un esempio di file di configurazione (config.ini):

```
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

## Utilizzo dell'Interfaccia GUI con PyQt

In aggiunta, esiste un interfaccia grafica chiamata GUI, fornita dal file `gui.pyw`, che utilizza il file di configurazione `config.ini` per impostare i parametri.

### Installazione di PyQt

Prima di poter utilizzare l'interfaccia GUI, è necessario installare PyQt. Questo può essere fatto con il seguente comando:

```python
pip install pyqt5
```
### Esecuzione dell'Interfaccia GUI

Per eseguire l'interfaccia GUI, usa il seguente comando:

```bash
python gui.pyw
```
L'interfaccia GUI ti permetterà di interagire con il modello GPT in modo più visuale, fornendo una finestra dove puoi inserire la tua domanda e ottenere una risposta.