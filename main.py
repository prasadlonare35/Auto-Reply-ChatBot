import pyautogui
import pyperclip
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

def is_last_message_from_prasad(chat_log):
    # Split the chat log into individual lines
    messages = chat_log.strip().split("\n")
    
    # Check if there are any messages in the log
    if not messages:
        return False
    
    # Get the last message
    last_message = messages[-1].strip()
    
    # Check if the last message contains "Prasad Lonare:"
    return "Prasad Lonare:" in last_message

def aiProcess(command):
    genai.configure(api_key=gemini_api_key)
    chat = genai.GenerativeModel("gemini-2.0-flash").start_chat()
        
    # Prepend context to the command
    context = """You are a person named Prasad who speaks english language. 
                You are from India and you are a college student. 
                You analyze chat history and roast and talk to people in a funny way. 
                Output should be the next chat response. 
                Respond in english language even if some one talking in other language and use emojis.
                don't talk in hindi, use proper english, reply in short messages and use emojis.
                Roast the sender so bad that they will never forgot it.
                Do not start like this [21:02, 12/6/2024] Rohan Das:,etc. 
                Following is the conversation :- """
    full_command = context + command
    try:
        response_chunks = chat.send_message(full_command, stream=True)
        response_text = ''.join(chunk.text for chunk in response_chunks if hasattr(chunk, 'text'))
        if not response_text.strip():
            return "Oops, couldn't generate a response. 😅"
        return response_text
    except ValueError as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong with the response. Don't use Hateful Speech you Fool 😵🤔"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""
    # return ''.join(chunk.text for chunk in chat.send_message(full_command, stream=True) if hasattr(chunk, 'text'))

# Step 1: Click on the icon at (695, 740)
pyautogui.click(695, 740)
time.sleep(1) 

while True:
    # Step 2: Drag from (481, 155) to (1310, 646) to select text
    pyautogui.moveTo(510, 172)
    pyautogui.mouseDown()  # Press and hold the left mouse button
    pyautogui.moveTo(1310, 646, duration=1)  # Drag to the target position
    pyautogui.mouseUp()  # Release the left mouse button

    # Step 3: Copy the selected text to the clipboard (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  
    pyautogui.click(500, 172)

    # Step 4: Get the text from the clipboard into a variable
    chatHistory = pyperclip.paste()
    
    # Check if the last message is NOT from "Prasad Lonare"
    if not is_last_message_from_prasad(chatHistory):
        print("Copied text:", chatHistory)
        response = aiProcess(chatHistory)
        pyperclip.copy(response)

        print(response)

        # Step 5: Click at (614, 679) to focus the input area
        pyautogui.click(614, 679)
        time.sleep(0.5) 
        
        # Step 6: Paste the response into the input area (Ctrl+V)
        pyautogui.hotkey('ctrl', 'v')

        # Step 7: Click at (1320, 688) to send or confirm
        pyautogui.click(1320, 688)
        time.sleep(10)
    else:
        print("Last message is from Prasad Lonare. Skipping reply.")
        time.sleep(10)
        continue
