from pyo import *
import random

# Initialize the server
s = Server().boot()

# Start the server
s.start()

# Function to generate a random frequency in the musical scale
def random_frequency():
    scale = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
    return random.choice(scale)

# Oscillator for generating sound waves
osc = Sine(freq=random_frequency(), mul=0.5)

# Create an envelope to control the amplitude of the sound
env = Adsr(attack=0.01, decay=0.2, sustain=0.5, release=0.3, dur=1, mul=osc)

# Apply the envelope to the oscillator
env.play()

# Start the graphical user interface (GUI)
s.gui(locals())
