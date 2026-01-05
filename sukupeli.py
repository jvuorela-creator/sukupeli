import streamlit as st

st.set_page_config(page_title="Sukututkijan Logiikkapähkinä - Taso 2", page_icon="🧩", layout="wide")

st.title("🧩 Sukututkijan Logiikkapähkinä: Kadonneet Kirkonkirjat")
st.markdown("""
**Tehtävä:** Selvitä neljän henkilön tiedot vihjeiden perusteella. 
Jokaisella henkilöllä on eri syntymävuosi, ammatti ja kotipaikkakunta.
""")

# --- OIKEAT VASTAUKSET ---
# Nämä ovat ratkaisut, joihin peli vertaa
oikeat = {
    "Matti": {"vuosi": "1850", "ammatti": "Seppä",    "paikka": "Turku"},
    "Liisa": {"vuosi": "1870", "ammatti": "Piika",    "paikka": "Lieto"},
    "Kalle": {"vuosi": "1890", "ammatti": "Renki",    "paikka": "Raisio"},
    "Anna":  {"vuosi": "1910", "ammatti": "Opettaja", "paikka": "Kaarina"}
}

# --- SIVUPALKKI: VIHJEET ---
# Laitetaan vihjeet sivupalkkiin, jotta ne näkyvät koko ajan, vaikka rullaisi sivua.
with st.sidebar:
    st.header("🔍 Vihjeet")
    st.info("""
    1. **Matti** on joukon vanhin.
    2. Turussa asuva henkilö on syntynyt vuonna **1850**.
    3. **Opettaja** on nuorin kaikista (s. 1910).
    4. **Piika** asuu **Liedossa**.
    5. Raisiossa asuva henkilö on ammatiltaan **Renki**.
    6. **Kalle** on syntynyt vuonna **1890**.
    7. **Seppä** ei ole nainen (ei Liisa eikä Anna).
    8. **Anna** ei asu Liedossa eikä Raisiossa.
    9. **Liisa** on vanhempi kuin Kalle.
    """)
    st.write("---")
    st.caption("Lue vihjeet tarkasti ja käytä poissulkumenetelmää!")

# --- ASETUKSET VALIKOILLE ---
vuodet = ["Valitse...", "1850", "1870", "1890", "1910"]
ammatit = ["Valitse...", "Seppä", "Piika", "Renki", "Opettaja"]
paikat = ["Valitse...", "Turku", "Lieto", "Raisio", "Kaarina"]

# --- PELIALUE (4 saraketta) ---
c1, c2, c3, c4 = st.columns(4)

# Funktio sarakkeen luomiseen koodin toiston vähentämiseksi
def luo_henkilo_sarake(sarake, nimi):
    with sarake:
        st.subheader(nimi)
        # Tallennetaan valinnat uniikeilla avaimilla (esim. "Matti_v")
        v = st.selectbox(f"Syntymävuosi", vuodet, key=f"{nimi}_v")
        a = st.selectbox(f"Ammatti", ammatit, key=f"{nimi}_a")
        p = st.selectbox(f"Paikkakunta", paikat, key=f"{nimi}_p")
        return v, a, p

# Luodaan sarakkeet
m_v, m_a, m_p = luo_henkilo_sarake(c1, "Matti")
l_v, l_a, l_p = luo_henkilo_sarake(c2, "Liisa")
k_v, k_a, k_p = luo_henkilo_sarake(c3, "Kalle")
a_v, a_a, a_p = luo_henkilo_sarake(c4, "Anna")

st.write("---")

# --- TARKISTUS ---
if st.button("Tarkista ratkaisu", type="primary"):
    
    # Kerätään käyttäjän vastaukset sanakirjaan helppoa tarkistusta varten
    vastaukset = {
        "Matti": {"vuosi": m_v, "ammatti": m_a, "paikka": m_p},
        "Liisa": {"vuosi": l_v, "ammatti": l_a, "paikka": l_p},
        "Kalle": {"vuosi": k_v, "ammatti": k_a, "paikka": k_p},
        "Anna":  {"vuosi": a_v, "ammatti": a_a, "paikka": a_p}
    }

    oikein_lkm = 0
    virheet = []

    # Tarkistuslooppi
    for nimi, tiedot in oikeat.items():
        kayttajan_tiedot = vastaukset[nimi]
        
        # Tarkistetaan onko rivi täysin oikein
        if (kayttajan_tiedot["vuosi"] == tiedot["vuosi"] and 
            kayttajan_tiedot["ammatti"] == tiedot["ammatti"] and 
            kayttajan_tiedot["paikka"] == tiedot["paikka"]):
            oikein_lkm += 1
        else:
            # Emme kerro MIKÄ kohta on väärin (se tekisi pelistä liian helpon),
            # kerromme vain kenen tiedoissa on vikaa.
            virheet.append(nimi)

    # Palaute
    if oikein_lkm == 4:
        st.success("🏆 MAHTAVAA! Ratkaisit sukututkijan logiikkapähkinän täydellisesti!")
        st.balloons()
    else:
        st.error(f"Sait oikein {oikein_lkm} / 4 henkilöä.")
        if virheet:
            st.warning(f"Tarkista seuraavien henkilöiden tiedot: {', '.join(virheet)}")
            st.markdown("💡 *Vinkki: Jos muutat yhden tiedon, muista että se voi vaikuttaa muihin, koska jokainen vuosi/ammatti/paikka esiintyy vain kerran.*")
