import shutil
import os


doc_folder = os.path.expanduser("~/Documents")


current_folder = os.getcwd()


shutil.copytree(doc_folder, current_folder + "/Documents")

print("La carpeta 'Documentos' ha sido copiada a la carpeta actual.")
