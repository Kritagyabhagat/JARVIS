import speech_recognition
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os
import openai

# Initialize the recognizer

# Initialize the speech engine

# Function to convert text to speech
def speak():
    engine.say()
    engine.runAndWait()

# Function to take the command from the user
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return None
    return query

# Function to access chat_gpt (Openai)
openai.api_key = 'xx-xxxxxx'    # xx-xxxxxx (write your own key of chat_gpt)

def ask_gpt(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=150
    )
    return response.choices[0].text.strip()

#  Function to open calculator
def open_calculator():
    speak("Opening calculator.")
    os.system('calc.exe')

#  Function to open notepad
def open_notepad():
    speak("Opening Notepad.")
    os.system('notepad.exe')

# function to operate web browser from selenium import webdriver
def open_browser():
    """Function to open Google in a web browser using Selenium."""
    speak("Opening web browser.")
    driver = webdriver.Chrome()  # Ensure that you have the appropriate WebDriver for your browser
    driver.get('http://www.google.com')
    
# function to fetch google
def fetch_google():
    """Function to fetch Google's homepage content."""
    speak("Fetching Google's homepage content.")
    response = requests.get('http://www.google.com')
    if response.status_code == 200:
        print("Google's homepage fetched successfully.")
    else:
        print("Failed to fetch the page.")
        
#function to open web view
def open_webview():
    """Function to open a web page in an embedded window."""
    speak("Opening web content in a window.")
    webview.create_window('Google', 'http://www.google.com')
    webview.start()

# Function to execute commands based on the query
def process_query(query):
    query = query.lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        return wikipedia

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'play music' in query:
        music_dir = 'D:\\Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randrange(1, 128)]))    # [random.randrange(Start, End)]

        exit()
        
    elif 'open spotify' in query:
        speak("Opening spotify")
        webbrowser.open("https://")
        
    elif 'gpt' in query:
        response = ask_gpt(query)
        speak(response)
        
    elif 'open calculator' in query:
        open_calculator()
    
    elif 'exit' in query:
        speak("Goodbye!, better see you next time.")
        exit()

    else:
        speak("I am not sure how to help with that.")

# Main function
def jarvis():
    speak("Hello, I am Jarvis. How can I assist you today?")
    
    while True:
        query = take_command()
        if query:
            process_query(query)
            
if __name__ == "__main__":
    jarvis()
