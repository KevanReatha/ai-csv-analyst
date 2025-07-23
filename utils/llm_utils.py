import requests

def ask_ollama_summary(df):
    csv_preview = df.head(10).to_csv(index=False)

    prompt = f"""
You are a helpful data analyst. Analyze this CSV sample and write a short summary.
Mention:
- What the columns represent
- Any patterns, outliers, or interesting stats
- Anything worth investigating

Here is the data:
{csv_preview}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result.get("response", "No response from Ollama.")