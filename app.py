# app.py

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="AI Web Scraper", layout="wide")
st.title("🕷️ AI Web Scraper")
st.markdown("Enter a URL and extract all paragraph text from it.")

url = st.text_input("🔗 Enter URL", "https://example.com")

if st.button("Scrape"):
    if not url.startswith("http"):
        st.warning("Please enter a valid URL (starting with http or https)")
    else:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = [p.text.strip() for p in soup.find_all("p") if p.text.strip()]
            
            if paragraphs:
                df = pd.DataFrame(paragraphs, columns=["Paragraph Text"])
                st.success(f"✅ Found {len(paragraphs)} paragraphs")
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No paragraph text found on the page.")
        except Exception as e:
            st.error(f"Error: {e}")
# app.py

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="AI Web Scraper", layout="wide")
st.title("🕷️ AI Web Scraper")
st.markdown("Enter a URL and extract all paragraph text from it.")

url = st.text_input("🔗 Enter URL", "https://example.com")

if st.button("Scrape"):
    if not url.startswith("http"):
        st.warning("Please enter a valid URL (starting with http or https)")
    else:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = [p.text.strip() for p in soup.find_all("p") if p.text.strip()]
            
            if paragraphs:
                df = pd.DataFrame(paragraphs, columns=["Paragraph Text"])
                st.success(f"✅ Found {len(paragraphs)} paragraphs")
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No paragraph text found on the page.")
        except Exception as e:
            st.error(f"Error: {e}")
