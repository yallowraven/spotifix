import os
import sys
import time
import keyboard
import psutil

def get_spotify_path():
    for process in psutil.process_iter(["name", "exe"]):
        if process.info["name"] and "spotify" in process.info["name"].lower():
            return process.info["exe"]
    return None

def restart_spotify(spotify_path):
    print("Restarting Spotify...")
    for process in psutil.process_iter(["name"]):
        if process.info["name"] and "spotify" in process.info["name"].lower():
            process.kill()

    if spotify_path:
        os.startfile(spotify_path)
    else:
        print("Spotify executable not found. Please start Spotify manually.")

def main():
    print("Listening for Ctrl+Shift+S key combination...")
    spotify_path = get_spotify_path()
    
    while True:
        if keyboard.is_pressed("ctrl+shift+s"):
            restart_spotify(spotify_path)

if __name__ == "__main__":
    main()
