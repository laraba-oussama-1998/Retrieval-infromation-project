




import json
from threading import Thread
from tkinter import LabelFrame, Label, Text, END, Scrollbar, RIGHT, Y, ttk, StringVar, messagebox, DISABLED
from tkinter.ttk import Style, Button
import time

from Partie4.get_docs_by_vector_model import VectorSearch


class PerformanceFrame:
    performance_output = None
    performance_method = None
    start_button = None
    evaluation_button = None

    def __init__(self, root):
        self.root = root

    def create_performance_frame(self):
        comparison_frame = LabelFrame(self.root, text='Query tests', padx=10, pady=10)
        comparison_frame_title = Label(comparison_frame, text='Query Precision / Recoil')
        comparison_frame_title.config(font=("poppins", 16))
        comparison_frame_title.pack()

        self.performance_method = StringVar()
        self.performance_method.set('')
        radio_button_frame = LabelFrame(comparison_frame, padx=5, pady=5, borderwidth=0)
        ttk.Radiobutton(radio_button_frame, variable=self.performance_method, value='dot', text="Inner product",
                        style='Wild.TRadiobutton').grid(row=0, column=0)
        ttk.Radiobutton(radio_button_frame, variable=self.performance_method, value='cos', text="Cosine",
                        style='Wild.TRadiobutton').grid(row=0, column=1)
        ttk.Radiobutton(radio_button_frame, variable=self.performance_method, value='dice', text="Dice coefficient",
                        style='Wild.TRadiobutton').grid(row=0, column=2)
        ttk.Radiobutton(radio_button_frame, variable=self.performance_method, value='jaccard',
                        text="Jaccard similarity coefficient",
                        style='Wild.TRadiobutton').grid(row=0, column=3)

        radio_button_frame.pack()
        scroll = Scrollbar(comparison_frame)
        scroll.pack(side=RIGHT, fill=Y)
        self.performance_output = Text(comparison_frame, width=110, height=11, yscrollcommand=scroll.set)
        self.performance_output.config(font=("poppins", 10))
        self.performance_output.tag_configure("tag", foreground="#0288d1")
        self.performance_output.pack()

        buttons = LabelFrame(comparison_frame, padx=2, pady=2)
        buttons.pack()

        Style().configure(style='TButton', font=('poppins', 10))
        Style().layout('TButton')
        self.start_button = Button(buttons, text='Start performance test !',
                                   command=self.performance)
        self.evaluation_button = Button(buttons, text='Start evaluation test !', command=self.evaluation)
        self.start_button.grid(row=0, column=0, padx=10)
        self.evaluation_button.grid(row=0, column=1, padx=10)

        return comparison_frame

    def evaluation(self):
        t1 = Thread(target=self.start_evaluation_test)
        t1.start()

    def start_evaluation_test(self):
        method = self.performance_method.get()

        if method == '':
            messagebox.showerror('error', 'Please select a search method')
        else:
            test_queries = json.load(open('query_meta.json', encoding='UTF-8'))
            size = len(test_queries)
            vector_search = VectorSearch()
            count = 0
            data = {}
            start = 0

            for (index, query) in list(test_queries.items())[0:64]:

                start = time.time()
                # Print data
                
                self.performance_output.insert(END, 'Query Index : ', "tag")
                self.performance_output.insert(END, index + "\n")
                self.performance_output.insert(END, 'Query Text : ', "tag")
                self.performance_output.insert(END, query['query'] + "\n")
                self.performance_output.insert(END, 'Finding optimal parameters for this query, please wait ...\n', "tag")

                # for each query, determine it's best threshold and size
                search_docs = vector_search.get_docs_by_vector_model(query['query'], method=method, threshold=0, size=None)

                # max threshold
                max_threshold = search_docs[0][1]
                

                nb_pertinent_in_result = 0
                lst = [doc for doc, w in search_docs]
                for doc in query['docs']:
                    if doc in lst:
                        nb_pertinent_in_result += 1

                max_size = len(search_docs)
                
                k = 0
                if nb_pertinent_in_result > max_size:
                    min_size = max_size
                else:
                    min_size = nb_pertinent_in_result

                k = min_size


                try:
                    precision = (nb_pertinent_in_result / len(search_docs))
                    recall = (nb_pertinent_in_result / len(query['docs']))
                    f_score = 2 * ((precision * recall) / (precision + recall))
                    data = {
                        'precision': precision,
                        'recall': recall,
                        'f_score': f_score,
                        'threshold': 0,
                        'size': len(search_docs)
                    }
                except ZeroDivisionError:
                    pass

                threshold = 0.05
                max_size=100
                while threshold <= max_threshold:

                    min_size = 0

                    while min_size <= max_size:

                        search_docs = vector_search.get_docs_by_vector_model(query['query'], method='cos', threshold=threshold,
                                                                             size=min_size)
                        nb_pertinent_in_result = 0
                        lst = [doc for doc, w in search_docs]
                        for doc in query['docs']:
                            if doc in lst:
                                nb_pertinent_in_result += 1

                        try:
                            #print(min_size)
                            #print(threshold)
                            precision = (nb_pertinent_in_result / len(search_docs))
                            recall = (nb_pertinent_in_result / len(query['docs']))
                            f_score = 2 * ((precision * recall) / (precision + recall))
                            if data['f_score'] < f_score:
                                data = {
                                    'precision': precision,
                                    'recall': recall,
                                    'f_score': f_score,
                                    'threshold': threshold,
                                    'size': min_size
                                }
                        except ZeroDivisionError:
                            pass

                        min_size += int(max_size*1/100)
                    threshold += .05

                self.performance_output.insert(END, 'Process finished. Time : ', "tag")
                self.performance_output.insert(END, str(time.time()-start) + " sec\n")
                self.performance_output.insert(END, 'f_score : ', "tag")
                self.performance_output.insert(END, str(data['f_score']) + '\n')
                self.performance_output.insert(END, 'new recall : ', "tag")
                self.performance_output.insert(END, str(data['recall'] * 100) + '%\n')
                self.performance_output.insert(END, 'new precision : ', "tag")
                self.performance_output.insert(END, str(data['precision'] * 100) + '%\n')
                self.performance_output.insert(END, 'threshold : ', "tag")
                self.performance_output.insert(END, str(data['threshold']) + '\n')
                self.performance_output.insert(END, 'size : ', "tag")
                self.performance_output.insert(END, str(data['size']) + '\n')
                self.performance_output.insert(END, '_______________________________________________________ \n\n')
            

    def performance(self):
        t1 = Thread(target=self.start_performance_test)
        t1.start()


    def start_performance_test(self):

        method = self.performance_method.get()
        vector_search = VectorSearch()

        if method == '':
            messagebox.showerror('error', 'Please select a search method')
        else:

            # Disable button
            self.start_button.configure(state='disabled')

            # Clear output
            self.performance_output.delete('1.0', END)

            test_queries = json.load(open('query_meta.json', encoding='UTF-8'))
            for (index, query) in test_queries.items():
                doc_ranking = {}
                rank = 1
                if len(query['docs']) > 0:
                    search_docs = vector_search.get_docs_by_vector_model(query['query'], method=method, threshold=0, size=None)
                    nb_pertinent_in_result = 0
                    for doc, weight in search_docs:
                        if doc in query['docs']:
                            nb_pertinent_in_result += 1
                            doc_ranking[doc] = rank
                        rank += 1

                    precision = (nb_pertinent_in_result / len(search_docs)) * 100
                    recoil = (nb_pertinent_in_result / len(query['docs'])) * 100

                    self.performance_output.insert(END, 'Query Index : ', "tag")
                    self.performance_output.insert(END, index + "\n")
                    self.performance_output.insert(END, 'Query Text : ', "tag")
                    self.performance_output.insert(END, query['query'] + "\n")
                    self.performance_output.insert(END, 'Total documents retrieved : ', "tag")
                    self.performance_output.insert(END, str(len(search_docs)) + '\n')
                    self.performance_output.insert(END, 'Total pertinent documents retrieved : ', "tag")
                    self.performance_output.insert(END,
                                                   str(nb_pertinent_in_result) + '/' + str(len(query['docs'])) + '\n')
                    f_score=2 * ((precision * recoil) / (precision + recoil))
                    self.performance_output.insert(END, 'f_score : ', "tag")
                    self.performance_output.insert(END, "%.2f" % f_score + '%\n')
                    self.performance_output.insert(END, 'Precision : ', "tag")
                    self.performance_output.insert(END, "%.2f" % precision + "%  ")
                    self.performance_output.insert(END, 'Recall : ', "tag")
                    self.performance_output.insert(END, '%.2f' % recoil + " %\n")
                    self.performance_output.insert(END, 'Pertinent documents ranking : \n', "tag")

                    for doc_index, rank in doc_ranking.items():
                        self.performance_output.insert(END, 'Document index : ', "tag")
                        self.performance_output.insert(END, doc_index + "  ")
                        self.performance_output.insert(END, 'Document rank : ', "tag")
                        self.performance_output.insert(END,  str(rank) + '\n')

                    self.performance_output.insert(END, '_______________________________________________________ \n\n')

            # Show some statistical information

            # Enable button again
            self.start_button.configure(state='enable')
