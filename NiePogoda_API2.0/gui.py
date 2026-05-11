import sys
from logger_config import setup_logging
setup_logging()
import logging
logger = logging.getLogger(__name__)
import tkinter as tk
from tkinter import filedialog
from main import callback
logger.info('Program started')
def folder_choice(names, extensions):
    folder = filedialog.askdirectory(
        title='select folder',
        initialdir='C:/Users'
    )
    n, e = callback(folder)
    names.config(text=n)
    extensions.config(text=e)
try:
    window = tk.Tk()
    window.title('The Ultra-Mega-Super-Extraordinary Perspicacious & Panoptical Quiddity-Quantifier: An Ineffable Multi-Dimensional File-Summation Apparatus for the Most Fastidious & Erudite Computational Connoisseurs')
    window.geometry('1300x600+100+50')
    logger.info('Window created')

    button = tk.Button(window, text='Select folder', command=lambda:folder_choice(names, extensions))
    button.pack()
    label = tk.Label(window, text='Names of files:')
    label.pack(pady=20)
    names = tk.Label(window, text='')
    names.pack()
    label2 = tk.Label(window, text='Extensions:')
    label2.pack(pady=20)
    extensions = tk.Label(window, text='')
    extensions.pack()
    window.mainloop()
except TypeError as e:
    logger.error('Error has crashed the program')
    sys.exit()