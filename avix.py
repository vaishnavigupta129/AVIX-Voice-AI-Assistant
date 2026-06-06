import os
import time
import asyncio  # Required for edge-tts
import speech_recognition as sr
import webbrowser  # Built-in library to open websites
from dotenv import load_dotenv  # Crucial for reading your .env file
import edge_tts  # Premium Microsoft Male Voice
import pygame  # Bulletproof audio player

# --- Google SDK Imports Ko Safe Order Mein Rakha Hai ---
from google import genai
from google.genai import types

# ==========================================
# 1. INITIALIZATION
# ==========================================

# Load environmental variables from the .env file
load_dotenv()

# Fetching API Key safely
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ Error: GEMINI_API_KEY environment variable not set in your .env file.")
    exit(1)     

# Initialize the Gemini Client with the safely fetched key
client = genai.Client(api_key=api_key)

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Premium Microsoft Male Voice Configuration
VOICE = "en-IN-PrabhatNeural" 

# Create the continuous AI chat session with AVIX personality
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are AVIX, a brilliant, witty, and loyal AI assistant. Keep your responses relatively concise, helpful, and always call the user 'Sir' or 'Boss'.",
        temperature=0.7,
    )
)

def speak(text):
    # Print the clean text to your command prompt
    print(f"AVIX: {text}")
    
    # Phonetic correction so it pronounces "AVIX" beautifully
    phonetic_text = text.replace("AVIX", "Aevix")
    audio_file = "avix_response.mp3"
    
    try:
        # Edge-TTS task execution
        communicate = edge_tts.Communicate(phonetic_text, VOICE)
        asyncio.run(communicate.save(audio_file))
        
        # Audio play karna cleanly
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # Keep python waiting until the speaker is done talking
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)
            
        # Unload the audio immediately so Windows releases the file lock
        pygame.mixer.music.unload()
        
        # Safe deletion
        if os.path.exists(audio_file):
            os.remove(audio_file)
            
    except Exception as e:
        print(f"❌ Audio playback failed: {e}")
        try:
            pygame.mixer.music.unload()
        except:
            pass

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Processing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        speak("I'm having trouble accessing my speech servers.")
        return None

# ==========================================
# 2. MAIN CORE LOOP
# ==========================================

if __name__ == "__main__":
    speak("Systems online. AVIX is at your service, Sir.")
    
    while True:
        user_input = listen()
        
        if not user_input:
            continue
            
        # Convert input to lowercase to make matching easier
        command = user_input.lower()
            
        # ------------------------------------------
        # SYSTEM COMMAND INTERCEPTS (Hardcoded Tasks)
        # ------------------------------------------
        if any(word in command for word in ["exit", "shutdown", "go to sleep", "goodbye"]):
            speak("Powering down systems. Goodbye, Sir.")
            break
            
        elif "open youtube" in command:
            speak("Opening YouTube right away, Sir.")
            webbrowser.open("https://www.youtube.com")
            continue  
            
        elif "open google" in command:
            speak("Opening Google, Sir.")
            webbrowser.open("https://www.google.com")
            continue

        elif "open instagram" in command:
            speak("Opening Instagram, Sir.")
            webbrowser.open("https://www.instagram.com/avigupta2803/")
            continue

        elif "open my linkedin profile" in command:
            speak("Opening your LinkedIn profile, Sir.")
            webbrowser.open("https://www.linkedin.com/in/vaishnavi-gupta-499412378/")
            continue

        elif "play songs" in command:
            speak("Playing songs, Sir.")
            webbrowser.open("https://www.youtube.com/live/y1vj6KvMUk0?si=vJIo0-66X-E0lkSJ")
            continue

        elif "open my github profile" in command:
            speak("Opening your GitHub profile, Sir.")
            webbrowser.open("https://github.com/vaishnavigupta129")
            continue

        elif "play cartoon" in command:
            speak("Playing cartoon, Sir.")
            webbrowser.open("https://youtu.be/UM9LJouVf3s?si=cpu-FDlsYTDczC2D")
            continue

        # ------------------------------------------
        # AI BRAIN (Casual Conversation / Questions)
        # ------------------------------------------
        try:
            
            time.sleep(1) 
            
            response = chat.send_message(user_input)
            speak(response.text)
            
            time.sleep(1)
            
        except Exception as e:
            print(f"\n❌ GEMINI API ERROR DETAILS: {e}\n")
            speak("I encountered an error processing that request, Sir.")