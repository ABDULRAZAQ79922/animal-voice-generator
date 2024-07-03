import tkinter as tk
import pygame
import os
import random

pygame.mixer.init()

def my_play_random_animal_sound():
    my_animal_sounds = {
        'Cat': 'cat.wav',
        'Dog': 'dog.wav',
        'Cow': 'cow.wav',
        'Lion': 'lion.wav'
    }
    my_animal_name, my_sound_file = random.choice(list(my_animal_sounds.items()))
    my_animal_label.config(text=f"Playing: {my_animal_name}")
    pygame.mixer.music.load(os.path.join('animal_sounds', my_sound_file))
    pygame.mixer.music.play()

def my_stop_sound():
    pygame.mixer.music.stop()
    my_animal_label.config(text="")

my_root = tk.Tk()
my_root.title("Random Animal Voice Generator")

my_play_button = tk.Button(my_root, text="Play Random Animal Sound", command=my_play_random_animal_sound)
my_play_button.pack(pady=20)

my_stop_button = tk.Button(my_root, text="Stop Sound", command=my_stop_sound)
my_stop_button.pack(pady=20)

my_animal_label = tk.Label(my_root, text="")
my_animal_label.pack(pady=20)

my_root.mainloop()
