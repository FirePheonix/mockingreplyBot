import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    api_key = "ENTER_YOUR_API_KEY_HERE"
)

def is_last_message_from_sender(chat_log, sender_name="Tejas Singh Bhati"): ##enter the saved contact name here
    # Split the chat log into individual messages, that too with the one with /2024 on it
    messages = chat_log.strip().split("/2024] ")[-1]
    #ensure if tejas singh bhati is written on it
    if sender_name in messages:
        return True 
    return False


pyautogui.click(1061, 1036)
time.sleep(1)



pyautogui.moveTo(764, 312)




while True:
    time.sleep(0.5) #added a 6 seconds time gap because we don't want the code checking after every 1 second.
    #changed to 0.5 to show demo :)

    pyautogui.mouseDown()
    time.sleep(0.5)
    
    pyautogui.moveTo(1836, 893, duration=0.5)  # Adds smooth dragging effect
    pyautogui.mouseUp()

    
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(746,287)

    # Short pause to ensure the text has been copied
    time.sleep(0.5)

    # Retrieve copied text from clipboard using pyperclip
    chat_history = pyperclip.paste()

    # Output the copied text to confirm it's stored in the variable
    print("Copied Text:", chat_history)

    if is_last_message_from_sender(chat_history):
        
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named Shubham, living in India. You’re fluent in English and Hindi, and you’re a coder. You are rude, sarcastic, and humorous. You love making fun of your friend in a playful way, with short replies that are blunt and often mocking. Make sure to keep replies as brief as the friend’s message."},
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )

        response = completion.choices[0].message.content
        print(response)



        pyperclip.copy(response)

        pyautogui.click(1100,960)
        time.sleep(1) #wait for 0.5 seconds to make sure that 
        #previous command is executed well

        pyautogui.hotkey('ctrl','v')
        time.sleep(1) #wait for 1 second to ensure the 
        #paste command is completed

        pyautogui.press('enter')