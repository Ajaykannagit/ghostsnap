import google.generativeai as genai
key='AIzaSyC2mMUDUY3EKxnSXmiSxjCyUq7DbQtksZY'
genai.configure(api_key=key)
models = genai.list_models()
flash_models = [m.name for m in models if 'flash' in m.name]
print('Flash models:', flash_models)
