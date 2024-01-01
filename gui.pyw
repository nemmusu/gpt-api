import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QProgressBar, QHBoxLayout, QPlainTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
import configparser
from gpt import GPT  

class GPTWorker(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, api_key, domanda, temperature, model, system_role_message):
        super().__init__()
        self.api_key = api_key
        self.domanda = domanda
        self.temperature = temperature
        self.model = model
        self.system_role_message = system_role_message

    def run(self):
        try:
            chatbot = GPT(api_key=self.api_key, domanda=self.domanda, temperature=self.temperature, model=self.model, system_role_message=self.system_role_message)
            risposta_gpt = chatbot.get_chat_response()
            if risposta_gpt:
                self.finished.emit(risposta_gpt)
            else:
                self.error.emit("Si è verificato un errore durante la richiesta.")
        except Exception as e:
            self.error.emit(f"Si è verificato un'eccezione: {str(e)}")

class GPTInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')  # Legge i dati dal file config.ini
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Interfaccia per modulo GPT')
        self.setGeometry(300, 300, 600, 400)

        self.api_key_label = QLabel('Chiave API di OpenAI:')
        self.api_key_input = QLineEdit(self.config['OPENAI'].get('api_key', ''))
        self.api_key_input.setEchoMode(QLineEdit.Password)

        self.domanda_label = QLabel('Domanda:')
        self.domanda_input = QPlainTextEdit(self.config['OPENAI'].get('domanda', ''))
        self.domanda_input.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.domanda_input.setFixedHeight(100)
        self.domanda_input.setPlaceholderText("Inserisci la domanda (max 5 righe)")

        self.temperature_label = QLabel('Temperatura per il modello GPT:')
        self.temperature_input = QLineEdit(self.config['OPENAI'].get('temperature', ''))

        self.model_label = QLabel('Modello GPT da utilizzare:')
        self.model_input = QLineEdit(self.config['OPENAI'].get('model', ''))

        self.system_role_message_label = QLabel('Messaggio del ruolo di sistema:')
        self.system_role_message_input = QLineEdit(self.config['OPENAI'].get('system_role_message', ''))

        self.run_button = QPushButton('Avvia Modulo GPT')
        self.run_button.clicked.connect(self.avviaGPT)

        self.risposta_label = QLabel('Risposta:')
        self.risposta_display = QTextEdit()
        self.risposta_display.setReadOnly(True)

        self.progress_bar = QProgressBar()  
        self.progress_bar.setVisible(False)

        hbox = QHBoxLayout()  # Nuovo layout orizzontale
        hbox.addWidget(self.progress_bar)  # Aggiunge la barra di avanzamento al layout orizzontale

        vbox = QVBoxLayout()
        vbox.addWidget(self.api_key_label)
        vbox.addWidget(self.api_key_input)
        vbox.addWidget(self.domanda_label)
        vbox.addWidget(self.domanda_input)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.temperature_input)
        vbox.addWidget(self.model_label)
        vbox.addWidget(self.model_input)
        vbox.addWidget(self.system_role_message_label)
        vbox.addWidget(self.system_role_message_input)
        vbox.addWidget(self.risposta_label)
        vbox.addWidget(self.risposta_display)
        vbox.addLayout(hbox)  # Aggiunge il layout orizzontale al layout verticale
        vbox.addWidget(self.run_button)

        self.setLayout(vbox)
        self.show()

        self.worker_thread = None

        # Connetti i campi di input alla funzione per salvare nel file config.ini
        self.api_key_input.textChanged.connect(self.salvaConfig)
        self.domanda_input.textChanged.connect(self.salvaConfig)
        self.temperature_input.textChanged.connect(self.salvaConfig)
        self.model_input.textChanged.connect(self.salvaConfig)
        self.system_role_message_input.textChanged.connect(self.salvaConfig)

    def salvaConfig(self):
        # Scrivi le modifiche nel file config.ini
        self.config['OPENAI']['api_key'] = self.api_key_input.text()
        self.config['OPENAI']['domanda'] = self.domanda_input.toPlainText()
        self.config['OPENAI']['temperature'] = self.temperature_input.text()
        self.config['OPENAI']['model'] = self.model_input.text()
        self.config['OPENAI']['system_role_message'] = self.system_role_message_input.text()

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def avviaGPT(self):
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)

        api_key = self.api_key_input.text() if self.api_key_input.text() else self.config['OPENAI'].get('api_key', '')
        domanda = self.domanda_input.toPlainText() if self.domanda_input.toPlainText() else self.config['OPENAI'].get('domanda', '')
        temperature = float(self.temperature_input.text()) if self.temperature_input.text() else float(self.config['OPENAI'].get('temperature', ''))
        model = self.model_input.text() if self.model_input.text() else self.config['OPENAI'].get('model', '')
        system_role_message = self.system_role_message_input.text() if self.system_role_message_input.text() else self.config['OPENAI'].get('system_role_message', '')

        self.worker_thread = GPTWorker(api_key, domanda, temperature, model, system_role_message)
        self.worker_thread.finished.connect(self.mostraRisposta)
        self.worker_thread.error.connect(self.mostraErrore)
        self.worker_thread.finished.connect(self.progress_bar.hide)
        self.worker_thread.error.connect(self.progress_bar.hide)
        self.worker_thread.finished.connect(lambda: self.progress_bar.setRange(0, 1))
        self.worker_thread.error.connect(lambda: self.progress_bar.setRange(0, 1))
        self.worker_thread.start()

    def mostraRisposta(self, risposta):
        self.risposta_display.setPlainText(risposta)

    def mostraErrore(self, errore):
        self.risposta_display.setPlainText(errore)

def main():
    app = QApplication(sys.argv)
    interfaccia = GPTInterface()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
