import openai

openai.api_key = "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"

try:
    # Attempt a simple test API call
    response = openai.models.list()

    if response:
        print("API key is valid.")
    else:
        print("API key is invalid.")

except Exception as e:
    print(f"API key is invalid: {e}")