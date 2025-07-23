# 📊 AI CSV Analyst (Local LLM with Ollama + Streamlit)

This app lets you upload a CSV file and receive **human-like insights** from a **local Large Language Model (LLM)** — completely offline and cost-free.

> ✅ Built with:  
> - 🧠 [Ollama](https://ollama.com) running [Mistral](https://ollama.com/library/mistral) (or any supported model)  
> - 🧾 `pandas` for CSV parsing  
> - 🖼️ `Streamlit` for a lightweight UI  

---

## 🎯 What it does

- 📂 Upload your CSV
- 🔍 Preview the data
- 🧠 Click "Generate Insight"
- ✍️ Your **local LLM** (e.g. Mistral) gives a summary like a data analyst:
  - Column explanations
  - Observed patterns
  - Outliers or data issues
  - Questions or next steps

---

## 🚀 Example Output

> In this simple CSV sample, we have four columns representing...  
> Sales for Widget A vary significantly across different regions...  
> It would be worth investigating:  
> - What factors contribute to the difference in sales across regions?  
> - Why is Product B not selling?...  
> *(Full response generated locally via Mistral)*

---

## 🛠️ How to run it locally

```bash
git clone https://github.com/kevantamom/ai-csv-analyst.git
cd ai-csv-analyst

# Use the correct Python version (e.g. via pyenv)
pip install -r requirements.txt

# Start your local LLM
ollama run mistral

# In another terminal, launch the app
streamlit run app.py