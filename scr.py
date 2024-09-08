import os
import argparse
import pyautogui
from pynput import keyboard
from datetime import datetime

def take_screenshot(base_output_file):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename, ext = os.path.splitext(base_output_file)

    output_file = f"{filename}_{timestamp}{ext}"
    screenshot = pyautogui.screenshot()
    screenshot.save(output_file)
    print(f'Screenshot saved to {output_file}')
   
   

def on_press(key):
    if key == keyboard.Key.esc:
            take_screenshot(output_file)
            print("Press 'Esc' again to take another screenshot.")

def main():
    global output_file

    parser = argparse.ArgumentParser(description='Take a screenshot and save it to a file.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to the output file for the screenshot.')


    args = parser.parse_args()
    global output_file
    output_file = args.output


    if not output_file or not os.path.splitext(output_file)[1]:
        print("Error: The output file must have a valid file extension.")
        return


    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_set = True


    with keyboard.Listener(on_press=on_press) as listener:
        print("Press 'Esc' to take a screenshot.")
        listener.join()

if __name__ == "__main__":
    main()

