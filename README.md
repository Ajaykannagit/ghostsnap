# 👻 GhostSnap

> *"Every picture has a dark side."*

**GhostSnap** is an AI-powered horror storytelling application that transforms ordinary photographs into eerie, folklore-inspired supernatural tales using multimodal computer vision, authentic cultural legends, and dynamic narrative generation.

---

## 🌟 Key Features

- 📸 **Multimodal Image Investigation**: Upload an image (or capture one live via camera) along with optional investigator notes, whispers, or scene context.
- 👁️ **Multi-Stage Visual Scene Analysis**: Objectively examines lighting, shadows, reflections, textures, and geometry to extract intriguing visual cues (with scientific/optical explanations for grounded realism).
- 📜 **Global Folklore & Legend Matching**: Correlates detected scene elements with a curated database of 25+ authentic legends (Tamil Nadu, Japan, Celtic, Latin America, Nordic, Slavic, and Cosmic lore).
- 🖋️ **Atmospheric Horror Generation**: Crafts immersive, multi-chapter horror narratives tailored to your chosen storytelling style and intensity level.
- ⚡ **Interactive Story Branching**:
  - 📖 Reveal Chapter 2 ("The Descent")
  - 🔀 Explore Alternate Endings
  - 🩸 Crank up the suspense with a Darker Climax
- 🎙️ **Voice Narration**: In-browser audio playback of the generated horror tale.
- 🎴 **Shareable Horror Card**: Generate exportable preview cards to share with friends.
- 📲 **WhatsApp Teaser Dispatch**: Send quick, punchy horror teasers straight to your phone using Twilio WhatsApp integration.
- 🔒 **Privacy-First Ghost Mode**: Fully stateless image processing — zero image or prompt data retention.

---

## 🛠️ Tech Stack

- **Frontend & UI**: [Streamlit](https://streamlit.io/)
- **AI & Vision Model**: [Google Gemini AI](https://aistudio.google.com/) (`gemini-2.5-flash` / `gemini-3.5-flash`)
- **Messaging**: [Twilio WhatsApp API](https://www.twilio.com/)
- **Image Processing**: [Pillow (PIL)](https://python-pillow.org/)

---

## 🚀 Quick Start (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/Ajaykannagit/ghostsnap.git
cd ghostsnap
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Secrets
Create a `.streamlit/secrets.toml` file in the project root:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"

# Optional: Twilio WhatsApp Integration
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_WHATSAPP_FROM = "+17372508034"
TWILIO_CONTENT_SID = "your_twilio_content_sid"
```

### 4. Run the Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## ☁️ Streamlit Cloud Deployment

1. Fork or push this repository to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Deploy a new app:
   - **Repository:** `Ajaykannagit/ghostsnap`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Go to **App Settings → Secrets** and paste your `secrets.toml` contents.
5. Click **Save** and launch! 🎉

---

## 📜 Disclaimer

GhostSnap is designed purely for creative, fictional storytelling and entertainment. All legends and stories are generated as works of fiction.
