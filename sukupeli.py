import streamlit as st

# Asetetaan sivu leveäksi (wide), jotta kuva ja peli mahtuvat rinnakkain
st.set_page_config(page_title="Sukututkijan Logiikkapähkinä - Taso 2", page_icon="🧩", layout="wide")

st.title("🧩 Sukututkijan Logiikkapähkinä: Kadonneet Kirkonkirjat")
st.markdown("""
**Tehtävä:** Selvitä neljän henkilön tiedot vihjeiden perusteella. 
Jokaisella henkilöllä on eri syntymävuosi, ammatti ja kotipaikkakunta.
""")

# --- OIKEAT VASTAUKSET ---
oikeat = {
    "Matti": {"vuosi": "1850", "ammatti": "Seppä",    "paikka": "Turku"},
    "Liisa": {"vuosi": "1870", "ammatti": "Piika",    "paikka": "Lieto"},
    "Kalle": {"vuosi": "1890", "ammatti": "Renki",    "paikka": "Raisio"},
    "Anna":  {"vuosi": "1910", "ammatti": "Opettaja", "paikka": "Kaarina"}
}

# --- SIVUPALKKI: VIHJEET ---
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

# --- PÄÄALUEEN JAKAMINEN (PELI vs KUVA) ---
# Luodaan kaksi pääsaraketta: Vasen (3 osaa) pelille, Oikea (1 osa) kuvalle
game_col, img_col = st.columns([3, 1])

# --- KUVA OIKEAAN LAITAAN ---
with img_col:
    st.write("### Alkuperäislähde")
    # Tässä käytetään Wikimedia Commonsin kuvaa esimerkkinä.
    # Voit vaihtaa URL-osoitteen tilalle paikallisen tiedostonimen, esim: "kirkonkirja.jpg"
    kuva_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/The_Crazy_Monday_-_church_register_from_Os_parish.jpg"
    
    st.image(kuva_url, caption="Ote vanhasta asiakirjasta", use_container_width=True)
    st.info("💡 Vinkki: Joskus vastaus löytyy tutkimalla alkuperäislähdettä tarkasti! (Tämä on vain kuvituskuva)")

# --- PELIALUE VASEMMALLE ---
with game_col:
    # Asetukset valikoille
    vuodet = ["Valitse...", "1850", "1870", "1890", "1910"]
    ammatit = ["Valitse...", "Seppä", "Piika", "Renki", "Opettaja"]
    paikat = ["Valitse...", "Turku", "Lieto", "Raisio", "Kaarina"]

    # Luodaan 4 saraketta PELIN sisälle
    c1, c2, c3, c4 = st.columns(4)

    # Funktio sarakkeen luomiseen
    def luo_henkilo_sarake(sarake, nimi):
        with sarake:
            st.subheader(nimi)
            v = st.selectbox(f"Syntymävuosi", vuodet, key=f"{nimi}_v")
            a = st.selectbox(f"Ammatti", ammatit, key=f"{nimi}_a")
            p = st.selectbox(f"Paikkakunta", paikat, key=f"{nimi}_p")
            return v, a, p

    # Luodaan henkilöiden valikot
    m_v, m_a, m_p = luo_henkilo_sarake(c1, "Matti")
    l_v, l_a, l_p = luo_henkilo_sarake(c2, "Liisa")
    k_v, k_a, k_p = luo_henkilo_sarake(c3, "Kalle")
    a_v, a_a, a_p = luo_henkilo_sarake(c4, "Anna")

    st.write("---")

    # --- TARKISTUS ---
    if st.button("Tarkista ratkaisu", type="primary"):
        
        # Tässä oli todennäköisesti virheen kohta aiemmin.
        # Varmista, että tämä sanakirja on kopioitu kokonaan sulkeineen päivineen:
        vastaukset = {
            "Matti": {"vuosi": m_v, "ammatti": m_a, "paikka": m_p},
            "Liisa": {"vuosi": l_v, "ammatti": l_a, "paikka": l_p},
            "Kalle": {"vuosi": k_v, "ammatti": k_a, "paikka": k_p},
            "Anna":  {"vuosi": a_v, "ammatti": a_a, "paikka": a_p}
        }

        oikein_lkm = 0
        virheet = []

        for nimi, tiedot in oikeat.items():
            kayttajan_tiedot = vastaukset[nimi]
            if (kayttajan_tiedot["vuosi"] == tiedot["vuosi"] and 
                kayttajan_tiedot["ammatti"] == tiedot["ammatti"] and 
                kayttajan_tiedot["paikka"] == tiedot["paikka"]):
                oikein_lkm += 1
            else:
                virheet.append(nimi)

        if oikein_lkm == 4:
            st.success("🏆 MAHTAVAA! Ratkaisit sukututkijan logiikkapähkinän täydellisesti!")
            st.balloons()
        else:
            st.error(f"Sait oikein {oikein_lkm} / 4 henkilöä.")
            if virheet:
                st.warning(f"Tarkista seuraavien henkilöiden tiedot: {', '.join(virheet)}")

