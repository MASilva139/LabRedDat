import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Proyecto 01",
    page_icon=':shinto_shrine:',
    layout="wide"
)
# class MultiApp:
#     def __init__(self):
#         self.apps = {
#             "Inicio": self.page_inicio,
#             "Proyecto": self.page_proyecto,
#             "Conclusiones": self.page_conclusiones
#         }

#     def page_inicio(self):
#         st.title('Inicio')
#         # Aquí va el contenido de la página de inicio

#     def page_proyecto(self):
#         st.title('Proyecto')
#         # Aquí va el contenido de la página de proyecto

#     def page_conclusiones(self):
#         st.title('Conclusiones')
#         # Aquí va el contenido de la página de conclusiones

#     def run(self):
#         if 'page' not in st.session_state:
#             st.session_state.page = 'Inicio'
        
#         st.sidebar.title('Navegación')
#         st.session_state.page = st.sidebar.radio("Ir a", list(self.apps.keys()))
        
#         if st.button('Ir a Proyecto'):
#             st.session_state.page = 'Proyecto'
            
#         page = self.apps[st.session_state.page]
#         page()

# if __name__ == "__main__":
#     app = MultiApp()
#     app.run()

#####################################################
###               Página HTML                      ##
#####################################################
# def page1():
#     st.title("Página 1")
#     st.write("Contenido de la página 1")

# def page2():
#     st.title("Página 2")
#     st.write("Contenido de la página 2")

# PAGES = {
#     "Página 1": page1,
#     "Página 2": page2
# }

# def main():
#     html_code = """
#         <button onclick="window.location.hash='Página 1';location.reload();">Página 1</button>
#         <button onclick="window.location.hash='Página 2';location.reload();">Página 2</button>
#     """
#     components.html(html_code, height=50)

#     page = st.session_state.get("page", "Página 1")
#     if page in PAGES:
#         PAGESpage
#     else:
#         st.error("La página seleccionada no existe.")

# if __name__ == "__main__":
#     main()

#################################################################
##                      Arcivo Css externo                     ##
#################################################################
def main():
    st.title('Mi aplicación con CSS')

    # Lee tu archivo CSS
    with open('Notas/prac02-02/styles.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    st.write('Este es un ejemplo de cómo usar CSS en Streamlit.')

if __name__ == "__main__":
    main()