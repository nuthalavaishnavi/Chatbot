from groq import Groq
client = Groq(api_key = "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")

print(" Chatbot (Groq Streaming): Type 'quit', 'exit', or 'bye' to stop\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in  ["quit", "exit", "bye"]:
        print("\n Chatbot: GoodBye!")
        break

    print(" Chatbot: ", end="", flush=True)

    stream = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful Chatbot."},
            {"role": "user", "content": user_input}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print()
