import openai
import pyttsx3
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up the text-to-speech engine
voice_engine = pyttsx3.init()
# Set the voice rate and volume
voice_engine.setProperty("rate", 200)
voice_engine.setProperty("volume", 1.0)

# Count the number of files
def num_files():
    num_file = len([f for f in os.listdir("D:\Programowanie\My Programs\AI_TextFile\Logs") if f.endswith(".txt")])
    return str(num_file)

# Set the directory log path
folder_path = "D:\Programowanie\My Programs\AI_TextFile\Logs"
file_name = "logConversation_" + num_files() + ".txt"
full_path = os.path.join(folder_path, file_name)

# Define a function to prompt the chatGPT API and get a response
def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# Define a function to handle user input and generate a response
def handle_user_input(input_text):
    # TODO: Add any necessary input pre-processing or validation here
    prompt = f"User: {input_text}\nChatbot:"
    return get_gpt_response(prompt)

# Define a function to start the chatbot
def start_chatbot():
    with open(full_path, "w") as file:
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                file.write(f"---END---")
                break
            elif user_input.lower() == "set volume":
                print("What volume from 0 - 1 do you want? ")
                new_volume = float(input())
                if new_volume >= 0 and new_volume <= 1:
                    voice_engine.setProperty("volume", new_volume)
                else:
                    print("Invalid volume value. Volume must be between 0 and 1.")
            else:
                response = handle_user_input(user_input)
                print("Chatbot: " + response)
                file.write(f"You: {user_input}\n")
                file.write(f"Chatbot: {response}\n")
                voice_engine.say(response)
                voice_engine.runAndWait()



# Start the chatbot
print("# If you want to change the volume of voice, type 'set volume'")
print("What is your question?")
start_chatbot()


""" Speech to text... """
""" Create the memory for this AI to remember the topic of the conversation """ 