#importando librerias
import pickle
from pathlib import Path
import streamlit_authenticator as stauth #pip install streamlit-authenticator

#Creación de usuarios
nm = ["Administrador"]
usn = ["admin"]
psw = ["XXX"]

hashed_psw = stauth.Hasher(psw).generate()
file_path = Path(__file__).parent / "hash_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_psw, file)
