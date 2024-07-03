# Flashcard-Maker
Converts an image of a vocabulary page from the New Penguin Russian Course into a CSV file which can be imported to Anki to create flashcards.

# Motivation
The New Penguin Russian Course requires memorising a list of vocabulary at the end of every chapter. Manually creating flashcards with Anki for this purpose becomes very tedious when typing in the foreign Cyrillic alphabet, especially in later chapters as the list sizes increase. This process is extremely time-consuming and not particularly beneficial for learning except as typing practice, I therefore decided to optimise this process.

# Installation

```bash
conda env create -f environment.yml
```

# Usage
The PDF of the book is available for free online. Alternatively, you can take a picture of the required page of the book.

Firstly, create separate JPG images of each row of the vocabulary list and save all of the images to the same folder. A CSV of all of the images compiled can then be created using:

```bash
python create_tsv.py <image_folder> <output_path>
```

This code transcribes the text and splits the vocabulary into the indivual entries. The russian and english are then separated for the back and front of the flashcards respectively. The output file can be imported to Anki Web to create flashcards.

# Limitations
The code makes many errors which need to be corrected manually. The CSV file could be corrected; however, I prefer to create the flashcards and then correct them, as I can use Anki on my phone which is easier to type in Cyrillic with. Despite the errors, using this code is still much faster than typing manually, at least for me. The errors can be split into the following types:

- The code splits the two sides of the flashcards by searching for the word "to" and if not present, makes the split after the first word. This method works 80-90% of the time, but ocassional corrections are necessary.

- The book includes stress markings above the vowel in a word which should be stressed. The code cannot recognise these so if wanted, must be added back. Furthermore, the stressses also regularly cause the code to mistake letters. Watch out particularly for "е" becoming "ё" and "o" becoming "б".

- The code also will make miscellaneous errors that need to be watched out for.

