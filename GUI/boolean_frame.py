import time
from tkinter import LabelFrame, Label, Entry, messagebox, END
from tkinter.ttk import Style, Button

from Partie2.get_docs_by_boolean_model import get_docs_by_boolean_model


class BooleanFrame:

    def __init__(self, root, output):
        self.root = root
        self.output = output

    def create_boolean_frame(self):
        boolean_frame = LabelFrame(self.root, text='Boolean search engine', padx=10, pady=10)

        boolean_label_title = Label(boolean_frame, text='Research by boolean model')
        boolean_label_title.config(font=("poppins", 14))
        boolean_label_title.pack()

        boolean_label_sub_title = Label(boolean_frame, text='Enter your query')
        boolean_label_sub_title.config(font=("poppins", 10))
        boolean_label_sub_title.pack()

        boolean_query = Entry(boolean_frame, width=30)
        boolean_query.config(font=("poppins", 12))
        boolean_query.pack(padx=10, pady=10)

        Style().configure(style='TButton', font=('poppins', 10))
        Button(boolean_frame, text='Start search !', width=15,
               command=lambda: self.run_search_by_boolean_model(boolean_query, self.output)).pack()
        return boolean_frame

    @staticmethod
    def run_search_by_boolean_model(boolean_query, output):
        output.delete('1.0', END)
        query = boolean_query.get()
        if len(query) == 0:
            messagebox.showerror('error', 'please enter a valid query')
        else:
            output.insert(END, 'Search in process, please wait ...\n')
            start = time.time()
            results = get_docs_by_boolean_model(boolean_query.get())
            output.insert(END, 'Process complete. Time : ' + str(time.time() - start) + " seconds\n")
            if results == -1:
                messagebox.showerror('error', 'Query syntax invalid. PLease try again')
            else:
                if len(results) == 0:
                    output.insert(END, 'No results found\n')
                else:
                    output.insert(END, 'Total documents found : ' + str(len(results)) + '\n')
                    output.insert(END, 'List of pertinents documents\n')
                    for index in results:
                        output.insert(END, 'Document ' + str(index) + '\n')
