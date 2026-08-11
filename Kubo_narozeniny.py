import streamlit as st

# Nastavení stránky
st.set_page_config(page_title="Všechno nejlepší!", page_icon="🎂", layout="centered")

# Úvodní přání
st.title("Všechno nejlepší k narozeninám! 🎉")
st.write("Éra papírových přání je fuč! Letos máš v rukách tuto malou aplikaci s programem dnešního večera ❤️")

st.divider()

# Dotaz s výběrem tlačítek vedle sebe
st.subheader("Jsi připraven?")
col1, col2 = st.columns(2)

with col1:
    btn_ano = st.button("Ano! 🔥", use_container_width=True)
with col2:
    btn_heej = st.button("Heeej! 🚀", use_container_width=True)

# Uložíme si stav, aby stránka zůstala odemčená po kliknutí na kterékoliv tlačítko
if "started" not in st.session_state:
    st.session_state.started = False

if btn_ano or btn_heej:
    st.session_state.started = True
    st.balloons()  # Vystřelí narozeninové balónky!

# --- OBSAH PO KLIKNUTÍ ---
if st.session_state.started:
    st.success("Tak pojďme na to! 🎉")
    
    # 1. Instrukce k cestě
    st.info("🚗 **Krok 1:** Teď nasedni do auta a dojeď domů. Na další instrukce počkej.")
    
    st.write("Nech se vézt... kam? Klikni na odkaz níže a dozvíš se víc! 👇")
    
    # Odkaz na mapu (zadej sem svůj odkaz na Mapy.cz nebo Google Maps)
    # Příklad: https://mapy.cz/zakladni?q=Brno nebo souřadnice
    st.link_button(
        label="📍 Otevřít tajné místo na mapě", 
        url="https://mapy.com/cs/turisticka?source=base&id=1979355&x=16.3632147&y=49.3676772&z=17", 
        type="primary"
    )
    
    st.write("---")
    
    # 2. Příjezd na místo
    st.write("📍 *Dojel jsi na místo, kde se bude dnešní oslava odehrávat.*")
    st.write("Co nás zde čeká?")

    # 3. Harmonogram večera
    st.subheader("🗺️ Harmonogram dnešní tajné mise:")

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

    for krok in kroky_vecera:
        with st.expander(f"⏰ **{krok['čas']}** – {krok['název']}"):
            st.write(krok["popis"])

    st.divider()

    # Závěrečný vzkaz
    st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>Ľúbim ťa! ❤️</h2>", unsafe_allow_html=True)