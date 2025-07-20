import streamlit as st
from PIL import Image
import piexif
import folium
import pandas as pd
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

st.title("🖼️ Application EXIF & Voyages")

uploaded_file = st.file_uploader("📤 Choisissez une image JPEG", type=["jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image originale", use_container_width=True)

    if "exif" in image.info:
        exif_dict = piexif.load(image.info["exif"])
    else:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    st.subheader("📌 Modifier les coordonnées GPS")
    lat = st.number_input("Latitude", value=48.8566)
    lng = st.number_input("Longitude", value=2.3522)

    def dms_to_rational(number):
        from fractions import Fraction
        degrees = int(number)
        minutes_float = (number - degrees) * 60
        minutes = int(minutes_float)
        seconds = (minutes_float - minutes) * 60
        return [
            (degrees, 1),
            (minutes, 1),
            (int(seconds * 100), 100)]


    gps_ifd = {
        piexif.GPSIFD.GPSLatitudeRef: b'N' if lat >= 0 else b'S',
        piexif.GPSIFD.GPSLatitude: dms_to_rational(abs(lat)),
        piexif.GPSIFD.GPSLongitudeRef: b'E' if lng >= 0 else b'W',
        piexif.GPSIFD.GPSLongitude: dms_to_rational(abs(lng)),
    }

    if st.button("✅ Enregistrer les nouvelles coordonnées dans l'image"):
        exif_dict["GPS"] = gps_ifd
        exif_bytes = piexif.dump(exif_dict)
        image.save("data/photo_exif.jpg", "jpeg", exif=exif_bytes)
        st.success("EXIF modifiées et image sauvegardée dans data/photo_exif.jpg")

    st.subheader("🗺️ Carte avec les coordonnées GPS")
    map_gps = folium.Map(location=[lat, lng], zoom_start=10)
    folium.Marker([lat, lng], popup="Image géolocalisée ici").add_to(map_gps)
    st_folium(map_gps, width=700)

st.subheader("🌍 Mes voyages (ou rêves)")
df = pd.read_csv("assets/lieux.csv")
map_voyages = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=2)
for i, row in df.iterrows():
    folium.Marker([row["latitude"], row["longitude"]], popup=row["lieu"]).add_to(map_voyages)
folium.PolyLine(df[["latitude", "longitude"]].values, color="blue").add_to(map_voyages)
st_folium(map_voyages, width=700)