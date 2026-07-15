from services import get_ai_response
print("Sending request to AI...")
result = get_ai_response("Hello, are you working?")
print("AI Response:", result)