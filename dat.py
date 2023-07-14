import pandas as pd
import random as rd


class Word:
    def __init__(self):
        try:
            dat = pd.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            dat = pd.read_csv("data/french_words.csv")
        finally:
            self.dat_list = dat.to_dict("records")
            self.current_word = {}

    def generate_word(self):
        self.current_word = rd.choice(self.dat_list)
        return self.current_word["French"]

    def return_meaning(self):
        return self.current_word["English"]

    def remove_word(self):
        self.dat_list.remove(self.current_word)
        data = pd.DataFrame(self.dat_list)
        data.to_csv("data/words_to_learn.csv", index=False)
