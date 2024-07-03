from PIL import Image
import pytesseract
import re
import csv
import os
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Extract flashcards from images.")
parser.add_argument('folder_path', type=str, help='Path to the folder containing image files.')
parser.add_argument('output_file', type=str, help='Path where the TSV output file will be saved.')
args = parser.parse_args()

# Configure pytesseract to use the path where Tesseract-OCR is installed
pytesseract.pytesseract.tesseract_cmd = r'D:\Programs\Tesseract\tesseract.exe'

# Initialize the list to store all flashcards
all_flashcards = []

# Process each image in the folder
for filename in os.listdir(args.folder_path):
    if filename.endswith('.jpg'):  # Check if the file is a JPG image
        img_path = os.path.join(args.folder_path, filename)
        img = Image.open(img_path)
        img = img.convert('L')  # Convert to grayscale
        text = pytesseract.image_to_string(img, lang='rus+eng', config='--psm 6')

        entries = text.strip().split('\n\n')
        for entry in entries:
            normalized_entry = ' '.join(entry.split())
            match = re.match(r"^(.*?)\s+to\s+(.*)$", normalized_entry)
            if match:
                russian = match.group(1)
                english = 'to ' + match.group(2)
            else:
                parts = normalized_entry.split(maxsplit=1)
                if len(parts) > 1:
                    russian, english = parts[0], parts[1]
                else:
                    continue

            all_flashcards.append((english, russian))

# Writing all results to a single CSV file
with open(args.output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_ALL)
    writer.writerow(['English', 'Russian'])  # Header is optional but recommended
    for card in all_flashcards:
        writer.writerow(card)

print(f"Flashcards exported to {args.output_file}")
