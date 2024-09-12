import keyboard
import pyautogui
import time
import math

def press_backspace(n):
    # Ensure there's a small delay to allow you to focus on a field where backspace should work
    #time.sleep(5)  # Delay for 5 seconds
    pyautogui.press('backspace', presses=n)


def write_text(text):
    # Ensure there's a small delay to allow you to focus on the input area
    #time.sleep(5)  # Delay for 5 seconds
    pyautogui.write(text, interval=0.05)  # Writes the text with a small delay between key presses

 
buffer = ''
def on_key_press(event):
    global buffer
    # This function is called every time a key press is captured
    buffer += event.name  # Append the pressed key's name to the buffer
    #print(buffer)  # Print the current state of the buffer
    try:
        buffer = buffer[buffer.rfind('=') :] 
    except ValueError:
        pass
    
    if len(buffer) > 10:  # Limit buffer length to 10 characters
        buffer = buffer[1:]  # Remove the oldest character to maintain buffer size
        
    if '=' in buffer:
        #print(buffer)
        try:
            # find index of = and slice after =
            temp_buffer = buffer[buffer.rfind('=') + 1:]  # Slice after
            # now find // in buffer and slice before /
            temp_buffer = buffer[ 1:buffer.index('/')]
            print('temp', temp_buffer)
            ft, inches = temp_buffer.split('\'')
            ft = float(ft)
            inches = float(inches)
            mm =  (ft * 304.8) + (inches * 25.4)
            mm =round(mm,2)
            press_backspace(len(temp_buffer)+2)
            write_text(str(mm) +' mm')

            
        except ValueError:
            pass
# Hook only to key press events
keyboard.on_press(on_key_press)

# Print a message and block the program so it doesn't exit
print("Listening to keyboard... Press Ctrl+C to stop.")
keyboard.wait()
