import time
from tkinter import LabelFrame, Label, Entry, ttk, StringVar, END, messagebox
from tkinter.ttk import Style, Button

from Partie4.get_docs_by_vector_model import VectorSearch


class VectorFrame:

    def __init__(self, root, output):
        self.root = root
        self.output = output

    def create_vector_frame(self):
        vector_frame = LabelFrame(self.root, text='Vector search engine', padx=10, pady=10)
        vector_frame_title = Label(vector_frame, text='Research by vector model')
        vector_frame_title.config(font=("poppins", 14))
        vector_frame_title.pack()

        vector_frame_sub_title = Label(vector_frame, text='Enter your query')
        vector_frame_sub_title.config(font=("poppins", 10))
        vector_frame_sub_title.pack()

        query = Entry(vector_frame, width=30)
        query.config(font=("poppins", 12))
        query.pack(padx=10, pady=10)

        Style().configure('Wild.TRadiobutton', font=("poppins", 10))
        radio_button_frame = LabelFrame(vector_frame, padx=10, pady=10)
        vector_method = StringVar()
        vector_method.set('')
        radio_button_frame = LabelFrame(vector_frame, padx=10, pady=10)
        ttk.Radiobutton(radio_button_frame, variable=vector_method, value='dot', text="Inner product",
                        style='Wild.TRadiobutton').grid(row=0, column=0)
        ttk.Radiobutton(radio_button_frame, variable=vector_method, value='cos', text="Cosine",
                        style='Wild.TRadiobutton').grid(row=0, column=1)
        ttk.Radiobutton(radio_button_frame, variable=vector_method, value='dice', text="Dice coefficient",
                        style='Wild.TRadiobutton').grid(row=1, column=0)
        ttk.Radiobutton(radio_button_frame, variable=vector_method, value='jaccard',
                        text="Jaccard similarity coefficient",
                        style='Wild.TRadiobutton').grid(row=1, column=1)
        radio_button_frame.pack()

        style = Style()
        style.configure(style='TButton', font=('poppins', 10))
        boolean_button = Button(vector_frame, text='Start search !',
                                command=lambda: self.run_search_by_vector_model(query.get(), vector_method.get()),
                                width=15).pack(padx=5, pady=5)

        return vector_frame

    def run_search_by_vector_model(self, query, vector_method):
        vector_search = VectorSearch()
        self.output.delete('1.0', END)
        if len(query) == 0:
            messagebox.showerror('error', 'please enter a valid query')
        if vector_method == '':
            messagebox.showerror('error', 'Please select a search method')
        else:
            self.output.insert(END, 'Search in process, please wait ...\n')
            start = time.time()
            results = vector_search.get_docs_by_vector_model(query, vector_method, threshold=0, size=None)
            self.output.insert(END, 'Process complete. Time : ' + str(time.time() - start) + " seconds\n")
            self.output.insert(END, 'Total documents found : ' + str(len(results)) + '\n')
            self.output.insert(END, 'List of pertinents documents\n')
            for index in results:
                self.output.insert(END, 'Document ' + str(index[0]) + '\n')
