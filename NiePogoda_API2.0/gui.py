import sys
from pathlib import Path
from logger_config import setup_logging
setup_logging()
import logging
logger = logging.getLogger(__name__)
import tkinter as tk
from tkinter import filedialog
from main import callback
from save import save_result
logger.info('Program started')
def folder_choice(names, extensions, info_label):
    folder = filedialog.askdirectory(
        title='select folder',
        initialdir='C:/'
    )
    n, e = callback(folder, info_label)
    if n or e == None:
        raise TypeError('Error in chosed a folder')
    names.config(text=n)
    extensions.config(text=e)

def dowland_results(name, extension, save_label):
    if name == None or extension == None:
        save_label.config(text='You have to get results at first to dowland.')
    else:
        sciezka = filedialog.asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Plik tekstowy', '*.txt'), ('Plik JSON','*.json')],
            initialdir=Path.home() / 'Downloads',
            title='Zapisz plik',
            initialfile='namesANDextensions'
        )
        save_result(sciezka, name, extension, save_label)

try:
    window = tk.Tk()
    window.title('The Ultra-Mega-Super-Extraordinary Perspicacious & Panoptical Quiddity-Quantifier: An Ineffable Multi-Dimensional File-Summation Apparatus for the Most Fastidious & Erudite Computational Connoisseurs')
    window.geometry('1300x600+100+50')
    logger.info('Window created')

    button = tk.Button(window, text='Select folder', command=lambda:folder_choice(names, extensions, info_label))
    button.pack()
    label = tk.Label(window, text='Names of files:')
    label.pack(pady=20)
    names = tk.Label(window, text='')
    names.pack()
    label2 = tk.Label(window, text='Extensions:')
    label2.pack(pady=20)
    extensions = tk.Label(window, text='')
    extensions.pack()

    dowland = tk.Button(window, text='Dowland results', command=lambda:dowland_results(names.cget('text'), extensions.cget('text'), info_label))
    dowland.pack(pady=20)
    info_label = tk.Label(window, text='')
    info_label.pack()

    window.mainloop()
except TypeError as e:
    logger.error(f'Error {e} has crashed the program')
    sys.exit()