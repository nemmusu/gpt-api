import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QFileDialog
import zipfile

class StrongholdCrusaderEditorUnlocker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stronghold Crusader 2 Editor Unlocker")
        self.setGeometry(100, 100, 200, 80)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Questo programma sblocca le mappe originali\n di Stronghold Crusader 2 in modo che \npossano essere modificate dal map editor")
        self.layout.addWidget(self.info_label)

        self.unlock_button = QPushButton("Sblocca Mappe")
        self.unlock_button.setFixedSize(100, 30)
        self.unlock_button.clicked.connect(self.unlock_maps)
        self.layout.addWidget(self.unlock_button)

        self.central_widget.setLayout(self.layout)

    def unlock_maps(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleziona il file .shmap", "", "File .shmap (*.shmap)")

        if file_name:
            modified_file_name = os.path.join("./", f"{os.path.splitext(os.path.basename(file_name))[0]}-unlocked.shmap")

            with zipfile.ZipFile(modified_file_name, 'w', compression=zipfile.ZIP_DEFLATED) as modified_archive:
                with zipfile.ZipFile(file_name, 'r') as original_archive:
                    for file_name in original_archive.namelist():
                        with original_archive.open(file_name) as original_file:
                            if 'editor.ed' in file_name.lower():  # Cerca il file "editor.ed" nell'archivio zip
                                content = original_file.read().decode('latin-1')
                                modified_content = content.replace("<MapLocked>true</MapLocked>", "<MapLocked>false</MapLocked>")
                                modified_archive.writestr(file_name, modified_content.encode('latin-1'))
                            else:
                                modified_archive.writestr(file_name, original_file.read())  # Scrive gli altri file senza modifiche

            QMessageBox.information(self, "Operazione completata", "Sblocco riuscito! Il file modificato è stato salvato.")

def run_gui():
    app = QApplication(sys.argv)
    window = StrongholdCrusaderEditorUnlocker()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_gui()
