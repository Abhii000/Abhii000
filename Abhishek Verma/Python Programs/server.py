import socket
import random,os,time
from PIL import ImageTk, Image
import subprocess

import qrcode

batch_content = """
@echo off
FOR /F "tokens=2 delims=:" %%A in ('ipconfig ^| findstr /C:"IPv4 Address"') do set "ip=%%A"
set ip=%ip:~1%
echo %ip%

"""
file_name = "ip.bat"
# Open the file in write mode and write the batch content
with open(file_name, "w") as batch_file:
    batch_file.write(batch_content)
time.sleep(0.5)
batch_file_name = file_name
# Run the batch file using subprocess and capture the output
completed_process = subprocess.run(batch_file_name, text=True, capture_output=True)
# Get the captured standard output
output = completed_process.stdout
# Print the captured output
set_port=random.randrange(8000,9000)
server_ip=f'{output}:{set_port}/'
print(f'Your Server Host Url = {server_ip}')
print('Starting server:-')
print('\nScan this Qr-code to connect device')
time.sleep(1)
def create_qr_code1(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
if __name__ == "__main__":
    input_text = server_ip
    output_filename = 'localip'
    create_qr_code1(input_text, output_filename+'.jpg')
    time.sleep(0.2)
    current_directory = os.getcwd()
    image_filename = "{}.jpg".format(output_filename) 
    image_path = os.path.join(current_directory, image_filename)
    try:
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print("An error occurred:", e)
os.system('start cmd /K py -m http.server {}'.format(set_port))





















    

















