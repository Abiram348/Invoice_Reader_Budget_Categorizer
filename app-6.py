import streamlit as st
import google.generativeai as genai
import os
import tempfile
from PyPDF2 import PdfReader

# 🔐 Gemini API Key from environment (set this on Hugging Face Spaces)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("learnlm-1.5-pro-experimental")

# 🧾 Streamlit App Settings
st.set_page_config(page_title="Smart Invoice Assistant", layout="centered", page_icon="📑")
st.title("📑 Smart Invoice & Finance Assistant")

st.markdown("""
Welcome! Upload a PDF invoice or statement (like Paytm, Amazon, etc.)  
Gemini will extract key financial insights, and you can also ask it any question about your document.
""")

# 📂 Upload PDF
pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

extracted_text = None
temp_file_path = None

# Extract Text from PDF
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

# 💡 Financial Analysis Prompt Template
def generate_insight_prompt(text):
    return f"""
You are a financial assistant. Analyze the following transaction data and generate insights:
{text}

Your response should include:
- A summary of the financial activity
- Key transaction patterns
- Estimated total spend
- Category-wise breakdown (if possible)
- Notable vendors or amounts
- Suggestions to improve financial behavior
"""

# 🧠 Ask Gemini with Context
def ask_gemini_about_invoice(query, original_text):
    prompt = f"""
The user uploaded a financial statement PDF. Here's the content:

{original_text}

Now, answer this specific query: "{query}"
"""
    response = model.generate_content(prompt)
    return response.text

# 🚀 Handle Upload + Analysis
if pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf.read())
        temp_file_path = tmp.name

    # Extract Text
    with st.spinner("Extracting content from PDF..."):
        extracted_text = extract_text(temp_file_path)

    if extracted_text:
        st.success("✅ PDF content extracted successfully!")
        with st.expander("📜 View Extracted Text (optional)"):
            st.text(extracted_text[:3000])  # Limit preview

        # Run Initial Insight
        if st.button("📊 Generate Financial Insight"):
            with st.spinner("Generating insights with Gemini..."):
                initial_prompt = generate_insight_prompt(extracted_text)
                response = model.generate_content(initial_prompt)
                st.subheader("🔍 Financial Insights")
                st.write(response.text)

        # Query section
        st.markdown("---")
        user_query = st.text_input("💬 Ask a question about this document")

        if st.button("❓ Ask Gemini"):
            if user_query:
                with st.spinner("Gemini is thinking..."):
                    result = ask_gemini_about_invoice(user_query, extracted_text)
                    st.write(result)
            else:
                st.warning("Please enter a question.")

    else:
        st.error("⚠️ Could not extract text from this PDF. Make sure it’s not a scanned image.")