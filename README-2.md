---
title: Smart Invoice & Finance Assistant
sdk: streamlit
emoji: 📊
sdk_version: 1.44.1
---
# 💰 Smart Invoice & Finance Assistant (Powered by Gemini)
## 🚀 Live Demo
👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/Abiram348/Invoice_Reader_Budget_Categorizer)

---

## 📂 Features

✅ Upload `.pdf` invoices/statements  
✅ Extract clean transaction data  
✅ AI-generated spending summaries  
✅ Follow-up question-answering  
✅ No-code, privacy-first, fast  
✅ Works beautifully on mobile too!

---

## ⚙️ Tech Stack

| Tool           | Purpose                                             |
|----------------|---------------------------------------------------- |
| `Streamlit`    | UI framework                                        |
| `Gemini API`   | Google Generative AI (learnlm-1.5-pro-experimental) |
| `PyPDF2`       | Extracts text from PDF files                        |
| `Hugging Face` | Deployment + frontend hosting                       |

---

## 🛠️ How to Run Locally

git clone https://huggingface.co/spaces/Abiram348/Invoice_Reader_Budget_Categorizer
cd Invoice_Reader_Budget_Categorizer

# Create a virtual environment
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows

pip install -r requirements.txt

# Set your Gemini API key
export GOOGLE_API_KEY=your_api_key

# Run the app
streamlit run app.py