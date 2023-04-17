import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
markdown = """
Web App URL: <https://akshatpunia26-sat-stapp-streamlit-app-xnc761.streamlit.app/>

GitHub Repository: <https://github.com/akshatpunia26/sat_stapp>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Indian Subcontinent Geospatial Analysis")

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
