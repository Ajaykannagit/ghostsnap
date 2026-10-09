"""
GhostSnap - Main Streamlit Application
"Every picture has a dark side."

AI-powered horror storytelling application that transforms ordinary photographs into eerie,
folklore-inspired supernatural stories with visual analysis, authentic legend matching,
and a privacy-first stateless architecture.
"""

import time
import os
import streamlit as st
from PIL import Image

from ai_engine import (
    get_genai_client,
    analyze_image_scene,
    generate_horror_story,
    generate_chapter_two,
    generate_alternate_ending,
    generate_darker_twist,
    generate_whatsapp_summary
)
from folklore_db import find_matching_folklore
from whatsapp_service import send_whatsapp_story
from styles import (
    inject_ghostsnap_styles,
    render_shareable_card_html,
    render_audio_narration_player
)

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="GhostSnap 👻 - Every Picture Has a Dark Side",
    page_icon="👻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom CSS Styles
st.markdown(inject_ghostsnap_styles(), unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Session State Initialization
# -----------------------------------------------------------------------------
def init_session():
    """Initializes clean session state variables."""
    if "analysis" not in st.session_state:
        st.session_state.analysis = None
    if "story" not in st.session_state:
        st.session_state.story = None
    if "folklore" not in st.session_state:
        st.session_state.folklore = None
    if "chapter_two" not in st.session_state:
        st.session_state.chapter_two = None
    if "alternate_ending" not in st.session_state:
        st.session_state.alternate_ending = None
    if "darker_twist" not in st.session_state:
        st.session_state.darker_twist = None
    if "active_image_bytes" not in st.session_state:
        st.session_state.active_image_bytes = None
    if "whatsapp_summary" not in st.session_state:
        st.session_state.whatsapp_summary = None
    if "error_message" not in st.session_state:
        st.session_state.error_message = None

def reset_session():
    """Wipes all active investigation state for Privacy-First Ghost Mode."""
    st.session_state.analysis = None
    st.session_state.story = None
    st.session_state.folklore = None
    st.session_state.chapter_two = None
    st.session_state.alternate_ending = None
    st.session_state.darker_twist = None
    st.session_state.active_image_bytes = None
    st.session_state.whatsapp_summary = None
    st.session_state.error_message = None
    st.rerun()

init_session()

# -----------------------------------------------------------------------------
# Sidebar: Settings, API Keys & Privacy Controls
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 👻 GhostSnap Controls")
    st.markdown("---")
    
    # API Key Configuration
    secrets_key = ""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            secrets_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
    
    user_api_key = st.text_input(
        "🔑 Gemini API Key",
        value=secrets_key,
        type="password",
        help="Enter your Gemini API key. Obtained from Google AI Studio (a valid, active key is required)."
    )
    
    api_key = user_api_key.strip()
    
    st.markdown("### 🎭 Story Controls")
    story_style = st.selectbox(
        "Storytelling Style",
        [
            "Psychological horror",
            "Paranormal mystery",
            "Haunted location",
            "Cursed object",
            "Urban legend",
            "Folklore-inspired horror",
            "Cosmic or supernatural horror",
            "Short horror story",
            "Deep, cinematic long-form story"
        ],
        index=0
    )
    
    horror_intensity = st.select_slider(
        "Horror Intensity",
        options=["Mild 🌙", "Creepy 🕷️", "Terrifying 🩸", "Nightmare 👁️"],
        value="Creepy 🕷️"
    )
    
    folklore_region = st.selectbox(
        "Folklore Region Focus",
        ["All Cultures 🌏", "Tamil Nadu & South India 🏹", "Japan ⛩️", "North India 🪔", "Europe 🏰", "Latin America 🕯️", "Cosmic / Weird Lore 🌌"]
    )
    
    st.markdown("---")
    st.markdown("### 🔒 Privacy-First Ghost Mode")
    st.caption("Each image submission is processed independently. No session data is saved permanently.")
    if st.button("🔄 Forget Everything / New Snap", width="stretch"):
        reset_session()
        
    st.markdown("---")
    st.caption("GhostSnap v2.0 • Pure Fictional Entertainment")

# -----------------------------------------------------------------------------
# Main Hero Section
# -----------------------------------------------------------------------------
col_h1, col_h2, col_h3 = st.columns([1, 8, 1])
with col_h2:
    st.markdown("<h1 class='ghost-main-title'>GhostSnap 👻</h1>", unsafe_allow_html=True)
    st.markdown("<div class='ghost-tagline'>Every picture has a dark side.</div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center;'><div class='privacy-badge'>🔒 <span>Ghost Mode Active: Zero-Retention Session</span></div></div>",
        unsafe_allow_html=True
    )

# Display persistent error banner if set
if st.session_state.error_message:
    st.error(st.session_state.error_message)

# -----------------------------------------------------------------------------
# Step 1: Image Capture & Upload Section
# -----------------------------------------------------------------------------
if st.session_state.story is None:
    st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
    st.markdown("<div class='ghost-section-header'>📸 Step 1: Submit an Image for Investigation</div>", unsafe_allow_html=True)
    st.write("Upload a photograph of any ordinary room, building, window, corridor, staircase, or shadow. GhostSnap will analyze its visual geometry and reveal its fictional legend.")
    
    input_method = st.radio("Choose Input Method", ["File Upload / Drag & Drop", "Device Camera"], horizontal=True)
    
    uploaded_file = None
    if input_method == "File Upload / Drag & Drop":
        uploaded_file = st.file_uploader(
            "Select or drop an image (JPG, JPEG, PNG, WEBP)",
            type=["jpg", "jpeg", "png", "webp"],
            help="Maximum file size 15MB"
        )
    else:
        uploaded_file = st.camera_input("Capture a picture with your camera")
    
    if uploaded_file is not None:
        file_bytes = uploaded_file.getvalue()
        
        if len(file_bytes) > 15 * 1024 * 1024:
            st.error("⚠️ File size exceeds 15MB. Please upload a smaller photo.")
        else:
            col_img1, col_img2 = st.columns([1, 2])
            with col_img1:
                st.image(file_bytes, caption="Uploaded Investigation Photo", width="stretch")
            with col_img2:
                st.success("✅ Image loaded and validated!")
                st.info("Click below to begin multi-stage visual analysis and horror story generation.")
                
                if st.button("👁️ Begin Your Investigation", width="stretch"):
                    st.session_state.error_message = None
                    if not api_key:
                        st.session_state.error_message = "🔑 Please provide a valid Gemini API Key in the sidebar to continue."
                        st.rerun()
                    else:
                        st.session_state.active_image_bytes = file_bytes
                        
                        try:
                            client = get_genai_client(api_key)
                        except Exception as err:
                            st.session_state.error_message = f"🔑 Failed to initialize Gemini AI: {err}"
                            st.rerun()
                        
                        scan_placeholder = st.empty()
                        stages = [
                            ("🌌 Entering the scene...", 0.4),
                            ("👁️ Examining the shadows and visual details...", 0.5),
                            ("📜 Consulting the folklore archives...", 0.4),
                            ("🖋️ Writing your nightmare...", 0.6)
                        ]
                        
                        for text_step, sleep_dur in stages:
                            scan_placeholder.markdown(f"""
                            <div class='scan-container'>
                                <div class='scan-pulse-icon'>👻</div>
                                <div class='scan-step-text'>{text_step}</div>
                            </div>
                            """, unsafe_allow_html=True)
                            time.sleep(sleep_dur)
                        
                        try:
                            # 1. Visual analysis
                            analysis_data = analyze_image_scene(client, file_bytes)
                            st.session_state.analysis = analysis_data
                            
                            # 2. Folklore matching
                            region_clean = folklore_region.split()[0]
                            folklore_match = find_matching_folklore(
                                analysis_data.get("interesting_details", []),
                                region_filter=region_clean
                            )
                            st.session_state.folklore = folklore_match
                            
                            # 3. Horror story generation
                            intensity_clean = horror_intensity.split()[0]
                            story_data = generate_horror_story(
                                client,
                                analysis_data,
                                style=story_style,
                                intensity=intensity_clean,
                                folklore_data=folklore_match
                            )
                            st.session_state.story = story_data
                            scan_placeholder.empty()
                            st.rerun()
                        except PermissionError as perm_err:
                            scan_placeholder.empty()
                            st.session_state.error_message = f"⚠️ {perm_err}"
                            st.rerun()
                        except Exception as analysis_err:
                            scan_placeholder.empty()
                            st.session_state.error_message = f"⚠️ Investigation failed during AI analysis: {analysis_err}"
                            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Presentation Interface: 3-Section Story & Interactive Exploration
# -----------------------------------------------------------------------------
else:
    story = st.session_state.story
    analysis = st.session_state.analysis
    folklore = st.session_state.folklore
    
    top_col1, top_col2 = st.columns([3, 1])
    with top_col1:
        st.markdown(f"## 📖 {story.get('title', 'GhostSnap Horror Story')}")
    with top_col2:
        if st.button("📸 New Investigation", width="stretch"):
            reset_session()
    
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
        st.markdown("<div class='ghost-section-header'>📷 Investigated Photo</div>", unsafe_allow_html=True)
        if st.session_state.active_image_bytes:
            st.image(st.session_state.active_image_bytes, width="stretch")
        
        st.markdown("<br><strong>Investigation Specs:</strong>", unsafe_allow_html=True)
        st.caption(f"🎭 **Style:** {story_style}")
        st.caption(f"⚡ **Intensity:** {horror_intensity}")
        st.caption(f"🌏 **Folklore Focus:** {folklore_region}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section 1: WHAT THE AI SEES
        st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
        st.markdown("<div class='ghost-section-header sees-highlight'>👁️ SECTION 1: WHAT THE AI SEES</div>", unsafe_allow_html=True)
        st.write(f"**Neutral Description:** {analysis.get('neutral_description', '')}")
        
        st.write("**Key Objects:** " + ", ".join(analysis.get("important_objects", [])))
        st.write("**Intriguing Details:** " + ", ".join(analysis.get("interesting_details", [])))
        
        with st.expander("🔍 Reality Check (Ordinary Explanations)"):
            st.write("Below are natural scientific or optical explanations for the observed shapes:")
            for item in analysis.get("ordinary_explanations", []):
                st.write(f"• {item}")
        
        st.caption(f"🛡️ *{analysis.get('safety_note', '')}*")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section 2: WHAT FOLKLORE SAYS
        st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
        st.markdown("<div class='ghost-section-header folklore-highlight'>📜 SECTION 2: WHAT FOLKLORE SAYS</div>", unsafe_allow_html=True)
        if folklore:
            st.markdown(f"### {folklore.get('name', '')}")
            st.write(f"**Cultural Origin:** {folklore.get('cultural_origin', '')}")
            st.write(f"**Traditional Legend:** {folklore.get('traditional_belief', '')}")
            st.write(f"**Source / Reference:** *{folklore.get('credible_source', '')}*")
            st.info(f"💡 **Legend Connection:** {folklore.get('inspiration', '')}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        # Section 3: THE GHOSTSNAP STORY
        st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
        st.markdown("<div class='ghost-section-header story-highlight'>👻 SECTION 3: THE GHOSTSNAP STORY</div>", unsafe_allow_html=True)
        
        st.markdown(f"*{story.get('atmospheric_intro', '')}*")
        st.markdown("---")
        
        st.markdown("### 🔍 Inspired Visual Details")
        for clue in story.get("visual_clues_used", []):
            st.markdown(f"• *{clue}*")
            
        st.markdown("---")
        st.markdown("### 🩸 The Narrative")
        st.write(story.get("full_narrative", ""))
        
        st.markdown("---")
        st.markdown(f"<div style='border-left: 3px solid #dc2626; padding-left: 12px; font-style: italic; color: #fda4af; font-size: 1.15rem; margin: 15px 0;'>\"{story.get('chilling_final_sentence', '')}\"</div>", unsafe_allow_html=True)
        
        st.components.v1.html(
            render_audio_narration_player(story.get("full_narrative", "")),
            height=80
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.session_state.chapter_two:
            ch2 = st.session_state.chapter_two
            st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='ghost-section-header story-highlight'>📖 {ch2.get('chapter_title', 'Chapter 2')}</div>", unsafe_allow_html=True)
            st.write(ch2.get("chapter_narrative", ""))
            st.markdown(f"*{ch2.get('cliffhanger', '')}*")
            st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.alternate_ending:
            alt = st.session_state.alternate_ending
            st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='ghost-section-header story-highlight'>🔀 {alt.get('alternate_title', 'Alternate Ending')}</div>", unsafe_allow_html=True)
            st.write(alt.get("alternate_narrative", ""))
            st.markdown(f"*{alt.get('chilling_final_sentence', '')}*")
            st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.darker_twist:
            dark = st.session_state.darker_twist
            st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='ghost-section-header story-highlight'>🩸 {dark.get('darker_title', 'Darker Twist')}</div>", unsafe_allow_html=True)
            st.write(dark.get("darker_narrative", ""))
            st.markdown(f"*{dark.get('chilling_final_sentence', '')}*")
            st.markdown("</div>", unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # Step 5: Interactive Storytelling Options
        # ---------------------------------------------------------------------
        st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
        st.markdown("<div class='ghost-section-header'>⚡ Interactive Story Branching</div>", unsafe_allow_html=True)
        
        bcol1, bcol2, bcol3 = st.columns(3)
        
        with bcol1:
            if st.button("📖 Reveal Next Chapter", width="stretch"):
                with st.spinner("Writing Chapter 2..."):
                    try:
                        client = get_genai_client(api_key)
                        ch2_data = generate_chapter_two(
                            client,
                            title=story.get("title", ""),
                            previous_narrative=story.get("full_narrative", ""),
                            style=story_style,
                            intensity=horror_intensity
                        )
                        st.session_state.chapter_two = ch2_data
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
                    
        with bcol2:
            if st.button("🔀 Alternate Ending", width="stretch"):
                with st.spinner("Generating Alternate Ending..."):
                    try:
                        client = get_genai_client(api_key)
                        alt_data = generate_alternate_ending(
                            client,
                            title=story.get("title", ""),
                            previous_narrative=story.get("full_narrative", "")
                        )
                        st.session_state.alternate_ending = alt_data
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
                    
        with bcol3:
            if st.button("🩸 Make It Darker", width="stretch"):
                with st.spinner("Generating Darker Climax..."):
                    try:
                        client = get_genai_client(api_key)
                        dark_data = generate_darker_twist(
                            client,
                            title=story.get("title", ""),
                            previous_narrative=story.get("full_narrative", "")
                        )
                        st.session_state.darker_twist = dark_data
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
        st.markdown("</div>", unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # Additional Features: Shareable Card & WhatsApp Teaser
        # ---------------------------------------------------------------------
        st.markdown("<div class='ghost-card'>", unsafe_allow_html=True)
        st.markdown("<div class='ghost-section-header'>🎴 Shareable Horror Card & WhatsApp</div>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🎴 Horror Card", "📲 Send to WhatsApp"])
        
        with tab1:
            visual_detail_str = story.get("visual_clues_used", ["Atmospheric scene detail"])[0]
            card_html = render_shareable_card_html(
                story_title=story.get("title", "GhostSnap Tale"),
                visual_detail=visual_detail_str,
                chilling_quote=story.get("chilling_final_sentence", "Every picture has a dark side."),
                intensity=horror_intensity
            )
            st.markdown(card_html, unsafe_allow_html=True)
            st.caption("You can screenshot this card to share your GhostSnap experience!")
            
        with tab2:
            st.write("Send a short GhostSnap teaser summary straight to your phone via WhatsApp.")
            st.info("📋 **Note:** Your phone number must first be registered with the Twilio WhatsApp Sandbox. Text `join <sandbox-word>` to **+1 737 250 8034** on WhatsApp to opt in.")

            try:
                tw_sid = st.secrets.get("TWILIO_ACCOUNT_SID", "")
                tw_token = st.secrets.get("TWILIO_AUTH_TOKEN", "")
                tw_from = st.secrets.get("TWILIO_WHATSAPP_FROM", "")
                tw_csid = st.secrets.get("TWILIO_CONTENT_SID", "")
            except Exception:
                tw_sid = tw_token = tw_from = tw_csid = ""
            
            with st.form("whatsapp_form"):
                user_name = st.text_input("Your Name", value="Investigator")
                wa_number = st.text_input("WhatsApp Number (with country code)", placeholder="+1234567890")
                wa_submitted = st.form_submit_button("📤 Send Teaser via WhatsApp")
                
                if wa_submitted:
                    if not wa_number.strip():
                        st.warning("Please enter a WhatsApp number.")
                    else:
                        with st.spinner("Formatting teaser and sending..."):
                            try:
                                client = get_genai_client(api_key)
                                summary_text = generate_whatsapp_summary(
                                    client,
                                    story,
                                    visual_detail_str
                                )
                                success, info = send_whatsapp_story(
                                    twilio_account_sid=tw_sid,
                                    twilio_auth_token=tw_token,
                                    twilio_from=tw_from,
                                    twilio_content_sid=tw_csid,
                                    to_number=wa_number,
                                    user_name=user_name,
                                    summary=summary_text
                                )
                                if success:
                                    st.success("📲 Teaser sent! Check your WhatsApp.")
                                else:
                                    st.error(f"Could not send WhatsApp message: {info}")
                            except Exception as e:
                                st.error(f"Error: {e}")
        st.markdown("</div>", unsafe_allow_html=True)
