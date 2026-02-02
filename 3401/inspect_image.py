
import cv2
import numpy as np
import os

file_path = 'assignment 1/pic3.png'

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    # Try looking for other files with '2' and 'png' in the name in assignment 1
    print("Searching for similar files in 'assignment 1'...")
    for f in os.listdir('assignment 1'):
        if '2' in f and 'png' in f:
            print(f"Found candidate: {f}")
            file_path = os.path.join('assignment 1', f)
            break
    else:
        exit(1)

print(f"Analyzing: {file_path}")

try:
    img = cv2.imread(file_path)
    if img is None:
        print("Error: Could not read image. It might be corrupted or not an image.")
    else:
        print(f"Dimensions: {img.shape}")
        print(f"Data type: {img.dtype}")
        
        # Check for channels
        if len(img.shape) == 3:
            print(f"Channels: {img.shape[2]} (Color)")
            # Split and analyze
            b, g, r = cv2.split(img)
            print(f"Blue - Min: {b.min()}, Max: {b.max()}, Mean: {b.mean():.2f}")
            print(f"Green - Min: {g.min()}, Max: {g.max()}, Mean: {g.mean():.2f}")
            print(f"Red - Min: {r.min()}, Max: {r.max()}, Mean: {r.mean():.2f}")
            
            # Convert to gray for brightness check
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            print("Channels: 1 (Grayscale)")
            gray = img
            
        print(f"Grayscale Min: {gray.min()}")
        print(f"Grayscale Max: {gray.max()}")
        print(f"Grayscale Mean: {gray.mean():.2f}")
        
        # Histogram analysis
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        # Check if concentrated in dark or bright
        dark_pixels = np.sum(hist[:50])
        bright_pixels = np.sum(hist[200:])
        total_pixels = gray.size
        
        print(f"Dark pixels (<50): {dark_pixels} ({dark_pixels/total_pixels*100:.2f}%)")
        print(f"Bright pixels (>200): {bright_pixels} ({bright_pixels/total_pixels*100:.2f}%)")
        
except Exception as e:
    print(f"An error occurred: {e}")
