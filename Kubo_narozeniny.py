import streamlit as st

st.set_page_config(page_title="Všechno nejlepší!", page_icon="🎂", layout="centered")

# --- 1. ZABEZPEČENÍ HESLEM ---
TAJNE_HESLO = "1812"  # <-- Nastav si vlastní heslo nebo PIN

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Vstup jen pro oslavence!")
    heslo_input = st.text_input("Zadej tajné heslo pro odemknutí dnešního večera (zkus jeden náš společný datum):", type="password")
    
    if st.button("Odemknout 🔓"):
        if heslo_input == TAJNE_HESLO:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Špatné heslo, zkus to znovu! 😉")
    st.stop()


# --- 2. INICIALIZACE POČÍTADLA KROKŮ ---
if "current_step" not in st.session_state:
    st.session_state.current_step = 0


# --- 3. ÚVODNÍ STRÁNKA ---
st.title("🎂 Všechno nejlepší k narozeninám! 🎉")
st.write("Éra papírových přání je fuč! Letos máš v rukách tuto malou aplikaci s programem dnešního večera ❤️")
st.divider()


# KROK 0: Jsi připraven?
if st.session_state.current_step == 0:
    st.subheader("Jsi připraven?")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Ano! 🔥", use_container_width=True):
            st.session_state.current_step = 1
            st.balloons()
            st.rerun()
    with col2:
        if st.button("Heeej! 🚀", use_container_width=True):
            st.session_state.current_step = 1
            st.balloons()
            st.rerun()


# --- DEFINICE BODŮ HARMONOGRAMU ---
kroky_vecera = [
    {
        "čas": "17:30", 
        "název": "Příjezd, zahájení a přípitek 🥂", 
        "popis": "Slavnostní drink a předání dárku."
    },
    {
        "čas": "18:00", 
        "název": "Zahájení pikniku 🍕", 
        "popis": "Máme s sebou kupu krabiček. Bašti, co hrdlo ráčí, ať ti to v následující hodince pálí!"
    },
    {
        "čas": "18:15", 
        "název": "Cesta k výhře vede přes duhový most! 🌈", 
        "popis": "Protože víme, jak moc máš rád hry, pojďme si jednu zahrát!"
    },
    {
        "čas": "19:20", 
        "název": "Vesmírná zábava 🎬", 
        "popis": "Během další části večera si užijeme jednu vesmírnou hitparádu, která připadla právě na tvoje narozeniny! Čeká nás částečné zatmění Slunce, které bude vrcholit ve 20:12!"
    },
    {
        "čas": "20:12", 
        "název": "Vesmírná zábava 2.0 🌠", 
        "popis": "Jestli stále nemáš dost, můžeš si vybrat jednu z těch stovek padajících hvězd a něco si přát. ✨"
    }
]


# ==========================================
# POSTUPNÉ ODEMYKÁNÍ KROKŮ
# ==========================================

# KROK 1: Instrukce k odjezdu autem
if st.session_state.current_step >= 1:
    st.success("### 🎉 Mise zahájena!")
    st.info("🚗 **Krok 1:** Teď nasedni do auta a dojeď domů. Na další instrukce počkej.")
    
    # Tlačítko pro odemčení dalšího kroku (mapy)
    if st.session_state.current_step == 1:
        if st.button("Jsem doma, připraven vyrazit dál! 🚘"):
            st.session_state.current_step = 2
            st.rerun()

# KROK 2: Odkaz na mapu a tajné místo
if st.session_state.current_step >= 2:
    st.write("---")
    st.write("Nech se vézt... kam? Klikni na odkaz níže a dozvíš se víc! 👇")
    
    st.link_button(
        label="📍 Otevřít tajné místo na mapě", 
        url="https://mapy.com/cs/turisticka?source=base&id=1979355&x=16.3689760&y=49.3675235&z=17", 
        type="primary"
    )
    
    # Tlačítko pro potvrzení příjezdu na místo
    if st.session_state.current_step == 2:
        st.write("")
        if st.button("Jsme na místě! Co nás čeká? 🔓"):
            st.session_state.current_step = 3
            st.rerun()

# KROK 3 A DÁLE: Harmonogram a závěr
if st.session_state.current_step >= 3:
    st.write("---")
    st.write("📍 *Dojel jsi na místo, kde se bude dneska slavit!*")
    st.subheader("🗺️ A jaký je harmonogram?")

    # Počet odemčených bodů harmonogramu (krok 3 = 1 bod, krok 4 = 2 body, atd.)
    pocet_odemcenych = st.session_state.current_step - 2

    for i in range(min(pocet_odemcenych, len(kroky_vecera))):
        krok = kroky_vecera[i]
        with st.expander(f"⏰ **{krok['čas']}** – {krok['název']}", expanded=True):
            st.write(krok["popis"])

    # 1. Postupné odemykání jednotlivých bodů programu
    if pocet_odemcenych < len(kroky_vecera):
        st.write("")
        if st.button(f"👉 Odemknout další bod programu ({pocet_odemcenych + 1}/{len(kroky_vecera)})"):
            st.session_state.current_step += 1
            st.rerun()

    # 2. Tlačítko pro odemčení závěrečného dopisu
    elif st.session_state.current_step == len(kroky_vecera) + 2:
        st.divider()
        st.write("✨ **Dnešní program se chýlí ke svému konci! Ještě tu pro tebe ale něco mám...**")
        if st.button("💌 Odemknout závěrečný vzkaz"):
            st.session_state.current_step += 1
            st.rerun()

    # 3. Zobrazení dopisu a finálního vyznání
    elif st.session_state.current_step >= len(kroky_vecera) + 3:
        st.balloons()
        st.divider()
        
        st.info("""
        💌 **Milý Kubko,**
        
        doufám, že sis dnešní večer maximálně užil! 
        Chtěla jsem ti udělat radost něčím aktuálním, netradičním a ukázat ti, jak moc pro mě znamenáš. 
        Děkuju ti za všechny společné chvíle, za to, jaký jsi, a přeji ti ten nejkrásnější nový rok života plný zdravý a splněných přání! ✨
        """)
        
        st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>Ľúbim ťě! ❤️</h2>", unsafe_allow_html=True)
