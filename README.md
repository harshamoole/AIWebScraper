# 🕷️ AI Web Scraper

A simple Python-based web scraper that extracts paragraph content from any public webpage and displays it using a clean Streamlit UI.

---

## 📌 Features
- Accepts a URL as input
- Uses BeautifulSoup to parse all paragraph `<p>` tags
- Displays content in a structured pandas DataFrame
- Runs entirely in a browser (thanks to Streamlit)

---

## 🔧 Tech Stack
- Python
- Streamlit
- BeautifulSoup
- pandas
- requests

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/harshamoole/AIWebScraper

# 2. Change into the project directory
cd AIWebScraper

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
