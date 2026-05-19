import streamlit as st
import requests



if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



st.set_page_config(
    page_title="FinSure",
    page_icon="🏦",
    layout="wide"
)



st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.stApp {
    background: linear-gradient(to right, #041226, #061933);
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: #07162d;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Logo */

.logo-text {
    font-size: 40px;
    font-weight: bold;
    color: #f5b61a;
    margin-bottom: 5px;
}

.subtitle {
    color: #9eb0c7;
    font-size: 15px;
    margin-bottom: 30px;
}

/* Hero */

.hero-card {
    background: rgba(9, 24, 52, 0.95);
    padding: 45px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 30px;
}

.hero-title {
    font-size: 52px;
    font-weight: 700;
    margin-bottom: 18px;
    color: white;
}

.hero-desc {
    color: #c8d2df;
    font-size: 19px;
    line-height: 1.7;
}

/* Response */

.response-box {
    background: rgba(9, 24, 52, 0.95);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-top: 25px;
}

/* Buttons */

.stButton > button {
    width: 100%;
    background: #f5b61a;
    color: #041226;
    font-size: 17px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 14px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: #ffcc4d;
    color: black;
}

/* Text Area */

textarea {
    border-radius: 15px !important;
    background-color: #081a38 !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.markdown(
        '<div class="logo-text">FinSure</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Secure Financial Intelligence Workspace</div>',
        unsafe_allow_html=True
    )

    st.markdown("## Conversation History")

    if st.button("Clear History", key="clear_history_btn"):
        st.session_state.chat_history = []
        st.rerun()

    if len(st.session_state.chat_history) == 0:
        st.info("No conversations yet.")

    else:

        for chat in reversed(st.session_state.chat_history):

            st.markdown(f"""
            <div style="
                background-color:#0B1F3A;
                padding:12px;
                border-radius:12px;
                margin-bottom:12px;
                border:1px solid rgba(255,255,255,0.08);
            ">

            <p style="color:white; font-size:14px;">
            <b>Q:</b> {chat['question'][:60]}
            </p>

            <p style="color:#CBD5E1; font-size:12px;">
            {chat['answer'][:80]}
            </p>

            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Secure Document Center")

    uploaded_file = st.file_uploader(
        "Upload Secure PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("Upload Document", key="upload_btn"):

            files = {
                "file": uploaded_file
            }

            response = requests.post(
                "https://finsure-rag-portal.onrender.com/upload",
                files=files
            )

            if response.status_code == 200:
                st.success("Document uploaded successfully")

            else:
                st.error("Upload failed")


st.markdown("""
<div class="hero-card">

<div class="hero-title">
Financial Intelligence Portal
</div>

<div class="hero-desc">

Access secure document insights, retrieve banking policy
information, and interact with enterprise-grade financial
knowledge systems using semantic search and intelligent retrieval.

</div>

</div>
""", unsafe_allow_html=True)



query = st.text_area(
    "Search Financial Documents",
    placeholder="Ask questions about uploaded banking documents...",
    height=150
)



if st.button("Generate Insight", key="generate_btn"):

    if query.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating financial insight..."):

            response = requests.post(
                "https://finsure-rag-portal.onrender.com/chat",
                params={"query": query}
            )

            if response.status_code == 200:

                result = response.json()

                answer = result["response"]

                st.markdown(
                    '<div class="response-box">',
                    unsafe_allow_html=True
                )

                st.success(answer)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

                st.session_state.chat_history.append({
                    "question": query,
                    "answer": answer
                })

            else:
                st.error(f"Backend Error: {response.text}")
