"""
GhostSnap - AI Engine Module
Provides robust, stateless image scene analysis and horror story generation using Gemini AI.
Uses google.generativeai for fast, reliable HTTP inference on Windows environments.
Includes automatic retry with backoff on 429 rate limit errors.
"""

import json
import re
import time
import os
from PIL import Image
import io

import google.generativeai as genai_sdk

from prompts import (
    VISUAL_ANALYSIS_PROMPT,
    STORY_GENERATION_PROMPT_TEMPLATE,
    CHAPTER_TWO_PROMPT_TEMPLATE,
    ALTERNATE_ENDING_PROMPT_TEMPLATE,
    DARKER_TWIST_PROMPT_TEMPLATE,
    WHATSAPP_SUMMARY_PROMPT_TEMPLATE
)

# Ordered list of valid Gemini flash model IDs. We prioritize the 3.5 flash model as requested.
MODEL_FALLBACKS = [
    "models/gemini-3.5-flash",
    "models/gemini-2.5-flash",
    "models/gemini-2.5-flash-lite",
]

MAX_RETRY_SECONDS = 65  # Maximum time to wait on a 429 before giving up


def get_genai_client(api_key: str):
    """Initializes the Gemini client."""
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing. Please enter your API key in the sidebar or secrets.toml.")
    
    genai_sdk.configure(api_key=api_key)
    return genai_sdk


def clean_json_response(raw_text: str) -> str:
    """Strips markdown code fences or extra text around raw JSON."""
    raw_text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw_text, re.DOTALL)
    if match:
        return match.group(1)
    
    start = raw_text.find('{')
    end = raw_text.rfind('}')
    if start != -1 and end != -1 and end > start:
        return raw_text[start:end+1]
    
    return raw_text


def prepare_image(image_input) -> Image.Image:
    """Normalizes image input into PIL Image."""
    if isinstance(image_input, bytes):
        image = Image.open(io.BytesIO(image_input))
    elif hasattr(image_input, "getvalue"):
        image = Image.open(io.BytesIO(image_input.getvalue()))
    elif isinstance(image_input, Image.Image):
        image = image_input
    else:
        raise ValueError("Unsupported image format.")
    
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    
    max_size = (1500, 1500)
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    return image


def _check_permission_error(err_str: str):
    """Fails fast if the error is an API key suspension or permission denial."""
    err_lower = err_str.lower()
    if "suspended" in err_lower or "permission_denied" in err_lower or "403" in err_lower or "api_key_invalid" in err_lower:
        raise PermissionError("Your Gemini API Key has been suspended or is invalid (HTTP 403). Please enter a valid key in the sidebar.")


def _parse_retry_delay(err_str: str, default: int = 15) -> int:
    """Extracts the retry delay in seconds from a 429 error message, or returns a default."""
    import re as _re
    match = _re.search(r"retry[^\d]*(\d+)", err_str.lower())
    if match:
        delay = int(match.group(1))
        return min(delay, MAX_RETRY_SECONDS)
    return default


def _is_rate_limit(err_str: str) -> bool:
    return "429" in err_str or "quota" in err_str.lower() or "rate" in err_str.lower()


def call_gemini_vision(client, image: Image.Image, prompt: str) -> str:
    """
    Executes a stateless vision call across available models.
    Automatically retries once on 429 rate-limit with the suggested delay.
    """
    last_error = None

    for model in MODEL_FALLBACKS:
        for attempt in range(2):  # max 2 attempts per model (initial + 1 retry)
            try:
                model_obj = client.GenerativeModel(model)
                response = model_obj.generate_content([prompt, image])
                if response and response.text:
                    return response.text
                break  # empty response — try next model
            except Exception as e:
                err_str = str(e)
                _check_permission_error(err_str)

                if _is_rate_limit(err_str) and attempt == 0:
                    delay = _parse_retry_delay(err_str, default=20)
                    time.sleep(delay)
                    continue  # retry same model after waiting
                else:
                    last_error = e
                    break  # move to next model

    raise RuntimeError(f"Failed to generate vision content after retries: {last_error}")


def call_gemini_text(client, prompt: str) -> str:
    """
    Executes a stateless text call across available models.
    Automatically retries once on 429 rate-limit with the suggested delay.
    """
    last_error = None

    for model in MODEL_FALLBACKS:
        for attempt in range(2):  # max 2 attempts per model (initial + 1 retry)
            try:
                model_obj = client.GenerativeModel(model)
                response = model_obj.generate_content(prompt)
                if response and response.text:
                    return response.text
                break  # empty response — try next model
            except Exception as e:
                err_str = str(e)
                _check_permission_error(err_str)

                if _is_rate_limit(err_str) and attempt == 0:
                    delay = _parse_retry_delay(err_str, default=20)
                    time.sleep(delay)
                    continue  # retry same model after waiting
                else:
                    last_error = e
                    break  # move to next model

    raise RuntimeError(f"Failed to generate text content after retries: {last_error}")


def analyze_image_scene(client, image_input) -> dict:
    """Stateless Step 2: Analyzes image visual elements."""
    image = prepare_image(image_input)
    raw_response = call_gemini_vision(client, image, VISUAL_ANALYSIS_PROMPT)
    cleaned = clean_json_response(raw_response)
    
    try:
        data = json.loads(cleaned)
    except Exception:
        data = {
            "neutral_description": raw_response[:300],
            "important_objects": ["Observed environment elements"],
            "interesting_details": ["Shadows", "Reflections", "Atmospheric lighting"],
            "ordinary_explanations": ["Natural shadow angles and perspective interplay"],
            "horror_themes": ["The Quiet Room", "Whispering Shadows"],
            "safety_note": "Visual observation completed. No supernatural entity detected."
        }
    
    data["safety_note"] = "Visual observation completed. Fictional analysis only — no supernatural entity detected."
    return data


def generate_horror_story(client, analysis_data: dict, style: str, intensity: str, folklore_data: dict = None) -> dict:
    """Stateless Step 3: Generates personalized horror story based on image analysis."""
    folklore_ctx = "None"
    if folklore_data:
        folklore_ctx = f"{folklore_data.get('name', '')} ({folklore_data.get('region', '')}): {folklore_data.get('traditional_belief', '')}"
    
    prompt = STORY_GENERATION_PROMPT_TEMPLATE.format(
        analysis_json=json.dumps(analysis_data, indent=2),
        style=style,
        intensity=intensity,
        folklore_context=folklore_ctx
    )
    
    raw_response = call_gemini_text(client, prompt)
    cleaned = clean_json_response(raw_response)
    
    try:
        story_json = json.loads(cleaned)
    except Exception:
        story_json = {
            "title": "Shadows of the Forgotten Room",
            "atmospheric_intro": "The air grows thin as twilight touches the edges of the photograph.",
            "visual_clues_used": analysis_data.get("interesting_details", ["Atmospheric shadow"]),
            "supernatural_legend": "Local whispers tell of an echo that never leaves this exact spot.",
            "rising_suspense": "As you gaze closer, the shadow seems to hold a posture that wasn't there before.",
            "plot_twist": "The realization dawns—it wasn't standing in front of the lens, but right behind you.",
            "chilling_final_sentence": "Every picture has a dark side.",
            "full_narrative": raw_response
        }
    
    return story_json


def generate_chapter_two(client, title: str, previous_narrative: str, style: str, intensity: str) -> dict:
    """Generates Chapter 2 continuation."""
    prompt = CHAPTER_TWO_PROMPT_TEMPLATE.format(
        title=title,
        previous_narrative=previous_narrative[:1000],
        style=style,
        intensity=intensity
    )
    raw = call_gemini_text(client, prompt)
    try:
        return json.loads(clean_json_response(raw))
    except Exception:
        return {
            "chapter_title": "Chapter 2: The Unseen Presence",
            "chapter_narrative": raw,
            "cliffhanger": "The darkness outside the frame began to move."
        }


def generate_alternate_ending(client, title: str, previous_narrative: str) -> dict:
    """Generates an alternate ending."""
    prompt = ALTERNATE_ENDING_PROMPT_TEMPLATE.format(
        title=title,
        previous_narrative=previous_narrative[:1000]
    )
    raw = call_gemini_text(client, prompt)
    try:
        return json.loads(clean_json_response(raw))
    except Exception:
        return {
            "alternate_title": "Alternate Ending: The Silent Mirage",
            "alternate_narrative": raw,
            "chilling_final_sentence": "It was never a legend—it was a warning."
        }


def generate_darker_twist(client, title: str, previous_narrative: str) -> dict:
    """Generates a darker twist ending."""
    prompt = DARKER_TWIST_PROMPT_TEMPLATE.format(
        title=title,
        previous_narrative=previous_narrative[:1000]
    )
    raw = call_gemini_text(client, prompt)
    try:
        return json.loads(clean_json_response(raw))
    except Exception:
        return {
            "darker_title": "Darker Twist: Abyss",
            "darker_narrative": raw,
            "chilling_final_sentence": "Some photographs should never be taken."
        }


def generate_whatsapp_summary(client, story: dict, visual_detail: str) -> str:
    """Generates a WhatsApp-friendly short summary."""
    prompt = WHATSAPP_SUMMARY_PROMPT_TEMPLATE.format(
        title=story.get("title", "GhostSnap Tale"),
        visual_detail=visual_detail,
        chilling_quote=story.get("chilling_final_sentence", "Every picture has a dark side."),
    )
    return call_gemini_text(client, prompt)
