from tkinter import LabelFrame, Label, Text


class QueryResultFrame:
    results_output = None

    def __init__(self, root):
        self.root = root

    def create_output_frame(self):
        output_frame = LabelFrame(self.root, text='Results', padx=10, pady=10)
        output_frame_title = Label(output_frame, text='Query Results')
        output_frame_title.config(font=("poppins", 16))
        output_frame_title.pack()
        self.results_output = Text(output_frame, width=110, height=10)
        self.results_output.pack()
        return output_frame
