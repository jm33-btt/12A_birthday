import streamlit as st

st.set_page_config(page_title="Všechno nejlepší!", page_icon="🎂", layout="centered")

# --- 1. ZABEZPEČENÍ HESLEM ---
TAJNE_HESLO = "1812"  

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Vstup jen pro oslavence!")
    heslo_input = st.text_input("Zadej tajné heslo pro odemknutí dnešního večera (Jeden náš společný datum?):", type="password")
    
    if st.button("Odemknout 🔓"):
        if heslo_input == TAJNE_HESLO:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Špatné heslo, zkus to znovu! 😉")
    st.stop()


# --- 2. INICIALIZACE POČÍTADLA KROKŮ ---
# Krok 0 = Úvodní otázka "Jsi připraven?"
# Krok 1 = Cesta domů / odkaz na mapu
# Krok 2+ = Jednotlivé body harmonogramu
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
        "popis": "Máme s sebou kupu krabiček, bašti, co hrdlo ráčí, ať ti to v následující hodince pálí!"
    },
    {
        "čas": "18:15", 
        "název": "Cesta k výhře přes duhový most! 🌈", 
        "popis": "Protože víme, jak moc máš rád hry, pojďme si jednu zahrát!"
    },
    {
        "čas": "19:20", 
        "název": "Vesmírná zábava 🎬", 
        "popis": "Pojďme si část večera užít s jednou vesmírnou hitparádou, která připadla právě na tvoje narozeniny! Čeká na nás částečné zatmění Slunce, které bude vrcholit ve 20:12!"
    },
    {
        "čas": "20:12", 
        "název": "Vesmírná zábava 2.0 🌠", 
        "popis": "Jestli stále nemáš dost sledování oblohy, čeká nás sledování Perseidů."
    }
]


# KROK 1 A DÁLE: Postupné zobrazování
if st.session_state.current_step >= 1:
    st.success("### 🎉 Mise zahájena!")
    st.info("🚗 **Krok 1:** Teď nasedni do auta a dojeď domů. Na další instrukce počkej.")
    st.write("Nech se vézt... kam? Klikni na odkaz níže a dozvíš se víc! 👇")
    
    st.link_button(
        label="📍 Otevřít tajné místo na mapě", 
        url="https://mapy.com/cs/turisticka?source=base&id=1979355&x=16.3689760&y=49.3675235&z=17", 
        type="primary"
    )
    
    st.write("---")

    # Pokud jsme na místě (Krok 1), zobrazíme tlačítko pro zahájení harmonogramu
    if st.session_state.current_step == 1:
        st.write("📍 *Až dorazíš na místo, klikni pro odemčení prvního bodu programu:*")
        if st.button("Jsme na místě! Co nás čeká? 🔓"):
            st.session_state.current_step = 2
            st.rerun()

    # KROK 2 AŽ N: Postupné zobrazování harmonogramu
    if st.session_state.current_step >= 2:
        st.subheader("🗺️ Harmonogram dnešní tajné mise:")

        # Spočítáme, kolik bodů z harmonogramu se má zobrazit
        # current_step 2 zobrazí 1 bod (index 0), current_step 3 zobrazí 2 body (indexy 0 a 1), atd.
        pocet_odemcenych = st.session_state.current_step - 1

        for i in range(min(pocet_odemcenych, len(kroky_vecera))):
            krok = kroky_vecera[i]
            with st.expander(f"⏰ **{krok['čas']}** – {krok['název']}", expanded=True):
                st.write(krok["popis"])

        # Tlačítko pro odemčení dalšího kroku
        if pocet_odemcenych < len(kroky_vecera):
            st.write("")
            if st.button(f"👉 Odemknout další bod programu ({pocet_odemcenych + 1}/{len(kroky_vecera)})"):
                st.session_state.current_step += 1
                st.rerun()
        else:
            # Všechny kroky jsou odemčeny
            st.balloons()
            st.divider()
            st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>Doufám, že sis dnešní večer užil! Ľúbim tě ❤️</h2>", unsafe_allow_html=True)

