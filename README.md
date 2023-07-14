# Flash-Card
A simple flashcard program to help learn a new language/concept
# main
The UI design by tkinter package, with features such as:
- Front of the card to learn the word in a specific language (French). After 3 seconds, the card will flip to the back.
- Back of the card with the corresponding word's English translation
- Check mark (✔) indicates that the user already knows the word. If so, the word will be removed from the list of words_to_learn
- Incorrect mark (X) indicates that the user guesses the word wrong. If so, the word will be remained in the library and pop up again
# dat
Contains the class Word that gives a random French word and its translation from a CSV file of 100 French words to learn.
Can change the input file to learn more words / a new language

