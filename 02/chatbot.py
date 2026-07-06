from ki_werkstatt_ollama_api_example import OllamaApi

def chatbot():
    model_name = "gemma3:12b"
    chat_context = [
        {"role": "system", "content": "Du bist ein HTW-Chatbot. Sei freundlich und direkt."},
        # {"role": "user", "content": -question from the user-}
        # {"role": "model", "content": -response from the model-}
        # ... more entries
    ]
    chat_result = OllamaApi.chat(chat_context, model=model_name)
    print("Willkommen beim HTW Chatbot! Geben Sie 'quit' ein, um das Programm zu beenden.")
    
    while True:
        user_input = input("Sie: ")
        if user_input.lower() == "quit":
            print("Programm beendet.")
            break
        else:
            chat_context.append({"role": "user","content": user_input})
            response = OllamaApi.chat(chat_context, model=model_name)
            print(f"Bot: {response.get('result')}")
            chat_context.append({"role": "model","content": str(response.get('result'))})

            
if __name__ == "__main__":
    chatbot()
