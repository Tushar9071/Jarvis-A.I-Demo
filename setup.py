import subprocess
import sys

if __name__ == "__main__":
    
    try:
        subprocess.Popen("pip install pyaudio") 
        subprocess.Popen("pip install speech_recognition")
        subprocess.Popen("pip install pyttsx3")
        subprocess.Popen("pip install opencv-python")
        subprocess.Popen("pip install pywhatkit")
    except Exception as e:
        print(f"Error occurred while installing dependencies: {e}")
        sys.exit()

    sys.exit()
