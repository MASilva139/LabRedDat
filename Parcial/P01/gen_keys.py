#importando librerias
import pickle
from pathlib import Path
import streamlit_authenticator as stauth #pip install streamlit-authenticator

#Creación de usuarios
nm = ["Administrador", "Iskandar"]
usn = ["admin", "isk"]
psw = ["XXX", "XXX"] #Clave: 1a2b1309, def456

hashed_psw = stauth.Hasher(psw).generate()
file_path = Path(__file__).parent / "hash.yml"
with file_path.open("wb") as file:
    pickle.dump(hashed_psw, file)
