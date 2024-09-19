# import os
# import time
# import webbrowser

# # Function to open Notepad
# def open_notepad():
#     os.system("notepad")
#     speak("Notepad is now open.")

# # Function to open Calculator
# def open_calculator():
#     os.system("calc")
#     speak("Calculator is now open.")

# # Function to tell the time
# def tell_time():
#     current_time = time.strftime("%H:%M")
#     speak(f"The current time is {current_time}")

# # Function to search Google
# def search_google(query):
#     url = "https://www.google.com/search?q=" + query
#     webbrowser.open(url)
#     speak(f"Searching Google for {query}")

# # Text-to-Speech function
# def speak(text):
#     import pyttsx3
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# # Main Assistant Function
# def assistant():
#     speak("Hi, I'm your assistant!")
#     while True:
#         command = input("What do you want me to do? ").lower()

#         if "open notepad" in command:
#             open_notepad()
#         elif "open calculator" in command:
#             open_calculator()
#         elif "what time" in command:
#             tell_time()
#         elif "search" in command:
#             query = command.replace("search", "").strip()  # Extract search term
#             search_google(query)
#         elif "exit" in command:
#             speak("Goodbye!")
#             break
#         else:
#             speak("Sorry, I don't understand that command.")

# # Run the assistant
# assistant()



import os
import time
import webbrowser

# Function to open Notepad
def open_notepad():
    os.system("notepad")
    speak("Notepad is now open.")

# Function to open Calculator
def open_calculator():
    os.system("calc")
    speak("Calculator is now open.")

# Function to tell the time
def tell_time():
    current_time = time.strftime("%H:%M")
    speak(f"The current time is {current_time}")

# Function to search Google
def search_google(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    speak(f"Searching Google for {query}")

# Text-to-Speech function
def speak(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main Assistant Function
def assistant():
    speak("Hi, I'm your assistant!")
    while True:
        command = input("What do you want me to do? ").lower()

        # Check for variations of opening Notepad
        if "notepad" in command:
            open_notepad()
        # Check for variations of opening Calculator
        elif "calculator" in command or "calc" in command:
            open_calculator()
        # Check for telling the time
        elif "what time" in command:
            tell_time()
        # Check for Google search
        elif "search" in command:
            query = command.replace("search", "").strip()  # Extract search term
            if query:
                search_google(query)
            else:
                speak("Please provide something to search for.")
        # Exit command
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't understand that command.")

# Run the assistant
assistant()
