import tkinter as tk
import pickle
import sklearn
import numpy as np
from tkinter import filedialog


class RegressionApp:

    def __init__(self):
        self.model = None

        self.window = tk.Tk()
        self.window.title("Regression App")
        self.window.geometry("400x300")

        # set window style
        self.window.configure(bg='black')
        self.window.option_add('*foreground', 'white')
        self.window.option_add('*background', 'black')
        self.window.option_add('*Font', 'Helvetica 12')
        self.window.option_add('*Label.Font', 'Helvetica 14 bold')

        # create input widgets
        self.input_label = tk.Label(self.window, text="Enter data:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.window)
        self.input_entry.pack()

        # create button to trigger prediction
        self.predict_button = tk.Button(self.window, text="Predict", command=self.predict)
        self.predict_button.pack()

        # create output widget
        self.output_label = tk.Label(self.window, text="")
        self.output_label.pack()

        # create button to browse for model file
        self.browse_button = tk.Button(self.window, text="Browse", command=self.browse_model_file)
        self.browse_button.pack()

    def browse_model_file(self):
        # open file dialog to select model file
        file_path = filedialog.askopenfilename()

        # load model from file
        with open(file_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self):
        if self.model is None:
            self.output_label.config(text="Please select a model file first.")
            return

        # get input data from widget
        input_data = self.input_entry.get()

        # преобразуем строку с данными в список значений
        input_data_list = input_data.split(',')

        # преобразуем список в массив numpy и изменяем его форму на 2D
        input_data_array = np.array(input_data_list).reshape(1, -1)

        # make prediction
        prediction = self.model.predict(input_data_array)

        # update output widget
        self.output_label.config(text="Prediction: {}".format(prediction))

    def run(self):
        self.window.mainloop()


# create app instance
app = RegressionApp()

# start the app
app.run()
