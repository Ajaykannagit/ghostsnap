import google.generativeai as genai
from ai_engine import get_genai_client, call_gemini_text, MODEL_FALLBACKS

key = 'AIzaSyC2mMUDUY3EKxnSXmiSxjCyUq7DbQtksZY'
client = get_genai_client(key)
print('Using fallback list:', MODEL_FALLBACKS)
try:
    result = call_gemini_text(client, 'Write a 3-word horror tagline.')
    print('Result:', result)
except Exception as e:
    print('Error during generation:', e)
