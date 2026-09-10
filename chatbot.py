def chatbot():
    print("Chatbot: Hello! I am a simple chatbot.")
    print("Chatbot: You can say hello, how are you, or bye.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi!")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Chatbot: My name is Simple Chatbot.")

        elif user == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
