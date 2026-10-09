"""
GhostSnap - WhatsApp Service Integration
Wraps Twilio messaging to send GhostSnap horror summaries to WhatsApp.
Includes automatic fallback between Twilio Content Templates and Direct Body Messaging.
"""

import json
from twilio.rest import Client as TwilioClient

def clean_whatsapp_text(text: str) -> str:
    """Sanitizes text for WhatsApp content payload."""
    if not text:
        return "No GhostSnap summary available."
    text = " ".join(text.split())
    return text[:1500] + "..." if len(text) > 1500 else text

def send_whatsapp_story(twilio_account_sid: str, twilio_auth_token: str, twilio_from: str, twilio_content_sid: str, to_number: str, user_name: str, summary: str):
    """
    Sends WhatsApp message via Twilio with automatic fallback to body text if ContentSid fails.
    """
    if not all([twilio_account_sid, twilio_auth_token, twilio_from]):
        return False, "Twilio WhatsApp credentials not fully configured in Streamlit secrets."
    
    try:
        client = TwilioClient(twilio_account_sid, twilio_auth_token)
        
        # Clean from & to phone numbers
        clean_from = twilio_from.strip().replace(" ", "")
        if not clean_from.startswith("whatsapp:"):
            clean_from = f"whatsapp:{clean_from}"
            
        clean_to = to_number.strip().replace(" ", "")
        if not clean_to.startswith("+") and not clean_to.startswith("whatsapp:"):
            clean_to = f"+{clean_to}"
        if not clean_to.startswith("whatsapp:"):
            clean_to = f"whatsapp:{clean_to}"

        cleaned_summary = clean_whatsapp_text(summary)
        name_str = user_name or "Investigator"

        # Twilio requires a Content Template (ContentSid) for WhatsApp messages
        if not twilio_content_sid or not twilio_content_sid.strip():
            return False, "TWILIO_CONTENT_SID is not configured. Please create a Content Template in Twilio Console (Messaging → Content Template Builder) and add the Content SID to your Streamlit secrets."

        content_vars = json.dumps(
            {"1": name_str, "2": cleaned_summary},
            ensure_ascii=False
        )
        message = client.messages.create(
            from_=clean_from,
            to=clean_to,
            content_sid=twilio_content_sid.strip(),
            content_variables=content_vars
        )
        return True, message.sid

    except Exception as e:
        return False, str(e)
