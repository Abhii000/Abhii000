import os

folder=input('paste folder location here ')

def open_parent_cmd_with_http_server():
    try:
        # Open a new command prompt process and run 'python -m http.server' command
        os.system('start cmd /k python -m http.server ')
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    open_parent_cmd_with_http_server()
