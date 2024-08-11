from pathlib import Path
import json
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie


# ---- PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "atouts" / "CV de MAHAMAT HASSAN ABDOULAYE.pdf"
profile_pic = current_dir / "atouts" / "abdoulaye.png"

# ---- GENERAL SETTINGS ----
PAGE_TITLE = "MON_PORTFOLIO"
PAGE_ICON = ":computer:"
DESCRIPTION = """

"Je suis un étudiant en informatique, avec une forte
orientation vers la maîtrise des technologies émergentes
dans le développement web , machine learning et l'analyse de données."
Animé  par une grande curiosité , j'aspire à avoir un impact 
significatif dans le domaine de l'informatique en développant 
des solutions optimisées et sécurisées. Mon expérience académique
et personnelle m'a permis d'acquérir une solide base technique, 
ainsi qu'une capacité à travailler de manière autonome et en équipe.
Je suis constamment à la recherche de nouvelles opportunités pour 
appliquer mes compétences et continuer à évoluer en tant que professionnel."

"""

EMAIL = "elkariganosa@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mahamat-hassan-abdoulaye-4a6853234/",
    "GitHub": "https://github.com/MahamatHassanAbdoulaye",
    "FaceBook": "https://www.facebook.com/mahamathass1166/",
    "Instagram": "https://www.instagram.com/elkariganosa_man_waris/",
}

PROJECTS = {
    "🗂️ AgrI_Sense - Une plateforme technologique agricole de pointe alimentée par des algorithmes d'apprentissage automatique de pointe. Notre mission ? Fournir aux agriculteurs du monde entier des informations et des recommandations basées sur des données, révolutionnant ainsi la façon dont les cultures sont cultivées..": "https://acom/",
    "🗂️ SMART-SALES -site Web est une plate-forme en ligne complète conçue pour donner aux entreprises des informations précieuses et des capacités de prise de décision basées sur les données. Ce projet vise à fournir une interface conviviale pour analyser les données de vente, identifier les tendances et faire des choix commerciaux éclairés..": "https://smart-sales/",
  
    
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# ---- LOAD CSS, PDF & PROFILE PIC ----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# ---- MAIN SECTION WITH TABS ----
tabs = st.tabs(["Accueil", "À propos", "Éducation", "Compétences", "Projets","Certification","Mes Reseaux"])

# ---- ACCUEIL ----
with tabs[0]:
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.image(profile_pic, width=360)
    with col2:
        st.title(":orange[MAHAMAT HASSAN ]")
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Telecharger Mon_CV",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫 :gray[**EMAIL** :] ", EMAIL)
    with col3:
        lottie_hello = load_lottiefile("dossier_json/Hello animation.json")
        st_lottie(lottie_hello, speed=1, reverse=False, loop=True, quality="high")
        lottie_hi = load_lottiefile("dossier_json/Robo Hi.json")
        st_lottie(
        lottie_hi,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height =None,
        width=None,
        key=None,
    )

# ---- À PROPOS ----
with tabs[1]:
    st.subheader(":green[À PROPOS DE MOI]")
    st.write("---")
    st.write("Étudiant en intelligence artificielle, je suis dédié à l'exploration des technologies émergentes et à la création de solutions intelligentes basées sur des données pour résoudre des défis complexes.")
    st.write("Je suis passionné par la création de solutions logicielles innovantes qui répondent à des problèmes du monde réel.")
    lottie_hello = load_lottiefile("dossier_json/Hello animation.json")
    st_lottie(lottie_hello, speed=1, reverse=False, loop=True, quality="high", height=450, width=600)

    # Ajouter du contenu supplémentaire si nécessaire
    

# ---- ÉDUCATION ----
with tabs[2]:
    st.subheader(":green[ÉDUCATION ET QUALIFICATIONS]")
    st.write("---")
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.write(
            """
            - 🔭 Actuellement étudiant en Informatique à :orange[l'universite de science D'Alger 1 ].
            - ⚡ Diplômé de  en ingenerie de systeme dinformation et du logiciel  à:orange[l'universite D'Alger 1].
            - 🌱 Apprentissage en MERN STACK, STREAMLIT, PANDAS, BOOTSTRAP et DJANGO.
            - 💬 Bonne compréhension de TKINTER, PYTHON, HTML, CSS, OOPS, DBMS, ainsi que le développement web et l'analyse de données exploratoire.
            - ✔️ Excellent esprit d'équipe et sens de l'initiative.
            """
        )
    with col2:
        lottie_education = load_lottiefile("dossier_json/Education.json")
        st_lottie(lottie_education, speed=1, reverse=False, loop=True, quality="high", height=350, width=600)

# ---- COMPÉTENCES ----
with tabs[3]:
    st.subheader(":green[COMPÉTENCES]")
    st.write("---")
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.write(
            """
            - 🌐 Technologies Web : React, Node, SASS, HTML, CSS, Bootstrap, Tkinter, Streamlit.
            - 👩‍💻 Langages de programmation : Python, SQL, C, JavaScript .
            - 📊 Visualisation des données : PowerBi, MS Excel, Plotly, Matplotlib.
            - 📚 Concepts : DSA, OOPS, DBMS, Git, GitHub.
            - 🗄️ Bases de données : PostgreSQL, MongoDB, MySQL.
            """
        )
    with col2:
        lottie_skills = load_lottiefile("dossier_json/Skills.json")
        st_lottie(lottie_skills, speed=1, reverse=False, loop=True, quality="high", height=350, width=600)

# ---- PROJETS ----
with tabs[4]:
    st.subheader(":green[PROJETS]")
    st.write("---")
    col1, col2 = st.columns(2, gap="small")
    with col1:
        for project, link in PROJECTS.items():
            st.write(f"[{project}]({link})")
    with col2:
        lottie_projects = load_lottiefile("dossier_json/Projects.json")
        st_lottie(lottie_projects, speed=1, reverse=False, loop=True, quality="high", height=550, width=600)
 # ------ CERTIFICATES AND ACCOMPLISHMENTS ----------
with tabs[5]:
    st.subheader(":green[CERTIFICATIONS]")
    st.write("---")
    col1, col2 = st.columns(2, gap="small")
    with col1:
     st.write(
        """
    - ► JavaScript avec HTML et CSS de :orange[**OPENCLASROOM**]
    - ► Programmation Python de base de :orange[**COURSERA**]
    """
    )
with col2:
    lottie_hello = load_lottiefile("dossier_json/Certifiactions.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 350,
        width= 600,
        key=None,
    )
    

# ---- Mes Reseaux sociaux ----
with tabs[6]:
    lottie_projects = load_lottiefile("dossier_json/Animation_contact.json")
    st_lottie(lottie_projects, speed=1, reverse=False, loop=True, quality="high", height=150, width=300)

    st.subheader(":green[Mes Reseaux sociaux]")
    st.write("---")
    st.write('📲:orange[Connectez-vous avec moi :]👇\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
#  Ajouter un pied de page
footer = """

<div class="footer">
    <p>© 2024 elkariganosa Tous droits réservés.</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)