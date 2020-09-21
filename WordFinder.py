# Import python modules for GUI
import tkinter
import tkinter.messagebox
from collections import Counter

# Module Constants
SCORES = {'A': 1, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1,
          'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10,
          'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4,  'V': 4, 'Y': 4,
          'X': 8, 'Z': 10}

class WordFinder(tkinter.Tk):

    def __init__(self, listofwords, *args, **kwargs):
        # Initialise parent clas
        tkinter.Tk.__init__(self, *args, **kwargs)

        # Store values
        self.listofwords = listofwords

        # Setup main window
        self.title('Scrabble Solver - Fola Adebanjo 18/19')

        # Create widget/buttons
        input_rack_label = tkinter.Label(self, text='Enter your rack')
        
        self.input_rack_entry = tkinter.Entry(self)
        
        input_rack_button = tkinter.Button(self, text='Enter', command=self.search)
        
        quit_button = tkinter.Button(self, text='Quit', command=self.quit)
        
        self.valid_list = tkinter.Listbox(self, width=40, font='Courier')

        # Place widgets/buttons
        input_rack_label.grid(row=0, column=0, sticky=tkinter.W)
        self.input_rack_entry.grid(row=1, column=0, sticky=tkinter.W)
        
        input_rack_button.grid(row=1, column=1, sticky=tkinter.W)
        
        quit_button.grid(row=1, column=2, sticky=tkinter.W)
        
        self.valid_list.grid(row=2, columnspan=3, sticky=tkinter.W)

       # Points Table - Displays each Tile and it's point value
        self.letterPoints1 = tkinter.Label(self, text="A\nB\nC\nD\nE\nF\nG\nH\nI", font="Courier 10 bold")
        self.letterPoints1.grid(row=2, column=5)

        self.letterPoints2 = tkinter.Label(self,text="1 point\n3 points\n3 points\n2 points \n1 points\n4 points\n2 points\n4 points\n1 point", font="Courier 10 bold")
        self.letterPoints2.grid(row=2, column=6)

        self.letterPoints3 = tkinter.Label(self, text="J\nK\nL\nM\nN\nO\nP\nQ\nR", font="Courier 10 bold") 
        self.letterPoints3.grid(row=2, column=7)

        self.letterPoints4 = tkinter.Label(self, text="8 points\n5 points\n1 point\n3 points\n1 point\n1 point\n3 points\n10 points\n1 point", font="Courier 10 bold")
        self.letterPoints4.grid(row=2, column=8)

        self.letterPoints5 = tkinter.Label(self, text="S\nT\nU\nV\nW\nX\nY\nZ\nBlank", font="Courier 10 bold")
        self.letterPoints5.grid(row=2, column=9)

        self.letterPoints6 = tkinter.Label(self, text="1 point\n1 point\n1 point\n4 points\n4 points\n8 points\n4 points\n10 points\n0 points", font="Courier 10 bold")
        self.letterPoints6.grid(row=2, column=10)

    def run(self):
        # Enter event loop
        self.mainloop()

    def error(self):
        # Throw and error message dialog
        tkinter.messagebox.showinfo('You have entered too many letters!')

    def search(self):
        # Cleanup up valid list
        self.valid_list.delete(0, tkinter.END)
        
        # Get data of entry, and make them lower case
        input_rack = self.input_rack_entry.get().lower()
        
        # Check length of data
        if len(input_rack) <= 8:
            return self.find_valid_words(input_rack)
        self.error()

    def find_valid_words(self, input_rack):
        # Produce a dictionary for accepted words and its point total
        valid = {}
        
        input_rack_chars = Counter(input_rack)
        
        for word in self.listofwords:
            word_chars = Counter(word)
            if word_chars == word_chars & input_rack_chars:
                valid[word] = sum(SCORES[letter.upper()] for letter in word)

        # Sort the results and insert them into the list box
        if valid:
            for word, score in sorted(valid.items(), key=lambda v: v[1], reverse=True):
                self.valid_list.insert(tkinter.END, '{:<10} {}'.format(word, score))
        else:
            self.valid_list.insert(tkinter.END, 'No results found.')

if __name__ == '__main__':
    # Open dictionary file and scan for words
    with open('dictionary.dat', 'r') as file:
        all_words = [word for word in file.read().split()]
        
    # Create instance and call run method
    WordFinder(all_words).run()
