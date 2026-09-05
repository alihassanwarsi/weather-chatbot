import streamlit as st
from chatbot import ask_chatbot

st.set_page_config(
    page_title="SkyCast AI",
    page_icon="🌤",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_CSS = """
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #e2e8f0;
    }

    /* FIX: Hide only the header background/dots, NOT the whole header */
    header {background-color: rgba(0,0,0,0) !important;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;} 

    /* Chat Bubbles */
    .chat-bubble {
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin-bottom: 5px;
        display: inline-block;
        max-width: 80%;
        font-size: 1rem;
        line-height: 1.5;
        animation: fadeIn 0.3s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .user-bubble-container { text-align: right; width: 100%; margin-bottom: 15px; }
    .user-bubble {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border-bottom-right-radius: 4px;
    }
    
    .bot-bubble-container { text-align: left; width: 100%; margin-bottom: 15px; }
    .bot-bubble {
        background: #334155;
        color: #f1f5f9;
        border-bottom-left-radius: 4px;
        border: 1px solid #475569;
    }

    /* Modern Title */
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(to right, #60a5fa, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 2rem;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4052/4052984.png", width=80)
    st.markdown("### SkyCast AI")
    st.markdown("I'm your intelligent weather assistant.")
    st.markdown("---")
    st.markdown("**Example queries:**")
    st.caption("• What's the weather in Tokyo?")
    st.caption("• Is it raining in London?")
    st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown('<div class="main-title">SkyCast AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Personal AI Weather Meteorologist</div>', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble-container"><div class="chat-bubble user-bubble">{msg["content"]}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble-container"><div class="chat-bubble bot-bubble">{msg["content"]}</div></div>', unsafe_allow_html=True)

if prompt := st.chat_input("Ask about the weather..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble-container"><div class="chat-bubble user-bubble">{prompt}</div></div>', unsafe_allow_html=True)

    with st.spinner("Analyzing weather data..."):
        try:
            response_text = ask_chatbot(prompt)
            response_text = response_text.replace("```html", "").replace("```", "").strip()
        except Exception as e:
            response_text = f"⚠️ Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.markdown(f'<div class="bot-bubble-container"><div class="chat-bubble bot-bubble">{response_text}</div></div>', unsafe_allow_html=True)

    st.rerun()
