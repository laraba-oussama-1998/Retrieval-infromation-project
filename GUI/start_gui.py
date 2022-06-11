from tkinter import *
from GUI.boolean_frame import BooleanFrame
from GUI.output_frame import QueryResultFrame
from GUI.performance_frame import PerformanceFrame
from GUI.vectorial_frame import VectorFrame



def start_gui():

    # Initialize main window
    root = Tk()
    root.title('RI Project')
    root.geometry("1000x600")
    root.state("zoomed")

    # Output frame
    output = QueryResultFrame(root)
    output_frame = output.create_output_frame()

    # Performance frame
    perf = PerformanceFrame(root)
    performance_frame = perf.create_performance_frame()

    # Boolean frame
    boolean_frame = BooleanFrame(root, output.results_output).create_boolean_frame()

    # Vector frame
    vector_frame = VectorFrame(root, output.results_output).create_vector_frame()

    # Position frames on main window
    boolean_frame.place(x=20, y=0)
    vector_frame.place(x=20, y=200)
    output_frame.place(x=425, y=0)
    performance_frame.place(x=425, y=275)

    # Display window
    root.mainloop()




