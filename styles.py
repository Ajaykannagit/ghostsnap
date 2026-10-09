"""
GhostSnap - Cinematic Styling & UI Component Extensions
Provides custom CSS, dark horror aesthetic, animation keyframes, card renderers, and audio narration scripts.
"""

def inject_ghostsnap_styles():
    """Returns CSS string for injection into Streamlit."""
    return """
    <style>
    /* Global Theme & Reset */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background-color: #07070a !important;
        background-image: 
            radial-gradient(circle at 50% 0%, rgba(124, 58, 237, 0.12) 0%, transparent 60%),
            radial-gradient(circle at 100% 100%, rgba(220, 38, 38, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 0% 50%, rgba(15, 23, 42, 0.5) 0%, transparent 70%);
        color: #e2e8f0 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Headers & Typography */
    h1, h2, h3, .ghost-title {
        font-family: 'Cinzel', serif !important;
        letter-spacing: 1px;
    }
    
    .ghost-main-title {
        font-family: 'Cinzel', serif !important;
        font-size: 3.2rem !important;
        font-weight: 900 !important;
        text-align: center;
        background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 40%, #7c3aed 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 35px rgba(124, 58, 237, 0.4);
        margin-bottom: 0px !important;
    }
    
    .ghost-tagline {
        text-align: center;
        font-family: 'Cinzel', serif;
        font-size: 1.25rem;
        color: #a855f7;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: -5px;
        margin-bottom: 25px;
        text-shadow: 0 0 15px rgba(168, 85, 247, 0.5);
    }
    
    /* Privacy Badge */
    .privacy-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background: rgba(124, 58, 237, 0.15);
        border: 1px solid rgba(124, 58, 237, 0.4);
        border-radius: 20px;
        padding: 6px 16px;
        font-size: 0.85rem;
        color: #c084fc;
        box-shadow: 0 0 15px rgba(124, 58, 237, 0.2);
        margin: 0 auto 20px auto;
    }
    
    /* Custom Card Containers */
    .ghost-card {
        background: rgba(18, 18, 28, 0.75);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(124, 58, 237, 0.25);
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    
    .ghost-card:hover {
        border-color: rgba(168, 85, 247, 0.45);
        box-shadow: 0 12px 35px rgba(124, 58, 237, 0.25);
    }
    
    .ghost-section-header {
        font-family: 'Cinzel', serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #f1f5f9;
        border-bottom: 1px solid rgba(124, 58, 237, 0.3);
        padding-bottom: 8px;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Section Highlights */
    .sees-highlight {
        color: #38bdf8;
    }
    .folklore-highlight {
        color: #f59e0b;
    }
    .story-highlight {
        color: #c084fc;
    }
    
    /* Multi-stage Scan Loader */
    .scan-container {
        text-align: center;
        padding: 30px;
        background: rgba(15, 15, 25, 0.9);
        border: 1px solid rgba(124, 58, 237, 0.4);
        border-radius: 16px;
        box-shadow: 0 0 40px rgba(124, 58, 237, 0.3);
    }
    
    .scan-pulse-icon {
        font-size: 3rem;
        animation: ghostPulse 2s infinite ease-in-out;
    }
    
    @keyframes ghostPulse {
        0% { transform: scale(1); opacity: 0.7; filter: drop-shadow(0 0 10px rgba(124,58,237,0.5)); }
        50% { transform: scale(1.15); opacity: 1; filter: drop-shadow(0 0 25px rgba(168,85,247,0.9)); }
        100% { transform: scale(1); opacity: 0.7; filter: drop-shadow(0 0 10px rgba(124,58,237,0.5)); }
    }
    
    .scan-step-text {
        font-family: 'Cinzel', serif;
        font-size: 1.2rem;
        color: #e2e8f0;
        margin-top: 15px;
        letter-spacing: 1px;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 50%, #7c3aed 100%) !important;
        color: #ffffff !important;
        font-family: 'Cinzel', serif !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        border: 1px solid rgba(168, 85, 247, 0.5) !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #6d28d9 0%, #7c3aed 50%, #8b5cf6 100%) !important;
        box-shadow: 0 6px 25px rgba(168, 85, 247, 0.6) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Form inputs & Selectboxes */
    .stSelectbox label, .stTextInput label, .stFileUploader label {
        color: #cbd5e1 !important;
        font-family: 'Cinzel', serif !important;
    }
    
    /* Hide Streamlit default branding footer */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """


def render_shareable_card_html(story_title: str, visual_detail: str, chilling_quote: str, intensity: str) -> str:
    """Generates an HTML preview card for social sharing or image export."""
    return f"""
    <div style="
        background: linear-gradient(135deg, #09090e 0%, #170d2c 50%, #0d0714 100%);
        border: 2px solid rgba(168, 85, 247, 0.6);
        border-radius: 16px;
        padding: 30px;
        color: #f1f5f9;
        font-family: 'Cinzel', serif;
        box-shadow: 0 15px 40px rgba(0,0,0,0.8), 0 0 30px rgba(124,58,237,0.3);
        margin: 20px 0;
        text-align: center;
        position: relative;
        overflow: hidden;
    ">
        <div style="position: absolute; top: -20px; right: -20px; font-size: 8rem; opacity: 0.05; user-select: none;">👻</div>
        <div style="font-size: 0.85rem; color: #a855f7; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px;">👻 GHOSTSNAP INVESTIGATION CARD</div>
        <h2 style="font-size: 1.8rem; margin: 10px 0; color: #ffffff; text-shadow: 0 0 20px rgba(168,85,247,0.5);">{story_title}</h2>
        <div style="font-size: 0.95rem; color: #cbd5e1; margin-bottom: 20px; font-family: 'Inter', sans-serif;">
            <strong>Inspired Detail:</strong> {visual_detail} | <strong>Intensity:</strong> {intensity}
        </div>
        <div style="
            background: rgba(0, 0, 0, 0.4);
            border-left: 3px solid #dc2626;
            padding: 15px;
            font-style: italic;
            color: #fda4af;
            font-size: 1.1rem;
            margin: 15px 0;
            border-radius: 4px;
        ">
            "{chilling_quote}"
        </div>
        <div style="font-size: 0.8rem; color: #94a3b8; margin-top: 25px; letter-spacing: 2px;">
            GHOSTSNAP • EVERY PICTURE HAS A DARK SIDE
        </div>
    </div>
    """


def render_audio_narration_player(text_content: str):
    """
    Renders an inline Web Speech API SpeechSynthesis audio player in Streamlit.
    """
    escaped_text = text_content.replace('"', '\\"').replace('\n', ' ')
    return f"""
    <div style="margin: 15px 0; padding: 12px; background: rgba(30, 27, 75, 0.4); border: 1px solid rgba(124, 58, 237, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
        <span style="font-family: 'Cinzel', serif; font-size: 0.95rem; color: #c084fc;">🔊 Voice Narration:</span>
        <div>
            <button onclick="speakText()" style="background: #6d28d9; color: white; border: none; padding: 6px 14px; border-radius: 6px; cursor: pointer; font-family: sans-serif; font-size: 0.85rem; margin-right: 6px;">Play Narration 🎙️</button>
            <button onclick="stopText()" style="background: #334155; color: white; border: none; padding: 6px 14px; border-radius: 6px; cursor: pointer; font-family: sans-serif; font-size: 0.85rem;">Stop ⏹️</button>
        </div>
    </div>
    
    <script>
    function speakText() {{
        window.speechSynthesis.cancel();
        const msg = new SpeechSynthesisUtterance("{escaped_text}");
        msg.rate = 0.9;
        msg.pitch = 0.8;
        window.speechSynthesis.speak(msg);
    }}
    function stopText() {{
        window.speechSynthesis.cancel();
    }}
    </script>
    """
