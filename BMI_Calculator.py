from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from queue import Queue
from threading import Thread
from urllib.request import urlopen
import webbrowser
import math
from Module6 import BMI_database


# Element 1. Define an application class :
class MY_BMI_Calculator():
    def __init__(self,master):

#Element 2. Change the application title and fix the application window size:
        master.title('BMI Calculator')
        master.resizable(False,False)
#Element 6: Add a new attribute body status and the urls to the class
        self.body_status =' '
        self.the_urls = ["https://en.wikipedia.org/wiki/Body_mass_index", "https://youtu.be/tqHInpEcwpE"]
#Element 3. Configure the application title font size and style:
        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
#Element 4. Create a first frame to contain logo and title:
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()
#Element5. Insert an image and create two labels, one is for header another is for BMI instruction and put them into first frame:
        self.img = PhotoImage(file = 'workout-logo_1.png')
        ttk.Label(self.header_frame,image = self.img).grid(row = 0, column = 0, rowspan =2)
        ttk.Label(self.header_frame, text = 'BMI Calculator', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.header_frame, wraplength = 300,
        text = ("BMI is a person's weight divided by his or her height in meters squared."
                "The National Institutes of Health (NIH) now defines normal weight, overweight, and obesity "
                "according to BMI rather than the traditional height/weight charts.")).grid(row = 1, column = 1)
#Element 7. Create the second frame:
        self.frame_content_upper = ttk.Frame(master)
        self.frame_content_upper.pack()
#Element 8. Create labels for inputs: weight label, height in feet label, height in inch label and age label. Put them in to the frame and grid format.
        ttk.Label(self.frame_content_upper, text = 'Weight* : (lbs)').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content_upper, text = 'Height* :').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content_upper, text = 'ft.').grid(row = 1, column = 2, sticky = 'sw')
        ttk.Label(self.frame_content_upper, text = 'in.').grid(row = 1, column = 4, sticky = 'sw')
        ttk.Label(self.frame_content_upper, text = 'Gender:').grid(row = 2, column = 0, sticky = 'sw')
#Element 9. Create a gender variable to store gender choices from two radio buttons:
        self.gender = StringVar()
        ttk.Radiobutton(self.frame_content_upper,variable =self.gender, text = "Male" ,value = "Male").grid(row = 3, column = 0,padx = 5 )
        ttk.Radiobutton(self.frame_content_upper,variable =self.gender, text = "Female" ,value = "Female").grid(row = 3, column = 1,padx = 5)
#Element 10. Create a variable to store age information,  an age combobox and a label for age combobox:
        ttk.Label(self.frame_content_upper, text = 'Age:').grid(row = 4, column = 0, padx = 5, sticky = 'sw')
        self.age = StringVar()
        age_combobox = ttk.Combobox(self.frame_content_upper,textvariable = self.age, width = 12,
                                      values = ('1', '2', '3', '4', '5', '6',
                                             '7', '8', '9', '10', '11','12',
                                             '13', '14', '15', '16','17','18',
                                             '19', '20', '21', '22', '23', '24',
                                             '25', '26', '27', '28', '29', '30',
                                             '32', '33', '34', '35', '36', '37',
                                             '38', '39', '40', '41', '42', '43',
                                             '44', '45', '46', '47', '48', '49',
                                             '50', '51', '52', '53', '54', '55',
                                             '56', '57', '58', '59', '60', '61',
                                             '62', '63', '64', '65', '66', '67',
                                             '68', '69', '70', '71', '72', '73',
                                             '74', '75', '76', '77', '78', '79',
                                             '80', '81', '82', '83', '84', '85',
                                             '86', '87', '88', '89', '90', '91',
                                             '92', '93', '94', '95', '96', '97',
                                             '98', '99', '100', '101', '102', '103',
                                             '104', '105', '106', '107', '108', '109','110'))\
                                      .grid(row = 5,column = 0,padx = 5, sticky = 'sw')

#Element 11. Create entries for weight and height and then use gird layout:
        self.entry_weight = ttk.Entry(self.frame_content_upper, width = 12, font = ('Arial', 10))
        self.entry_ft = ttk.Entry(self.frame_content_upper, width = 12, font = ('Arial', 10))
        self.entry_in = ttk.Entry(self.frame_content_upper, width = 12, font = ('Arial', 10))
        self.entry_weight.grid(row = 1, column = 0, padx = 5)
        self.entry_ft.grid(row = 1, column = 1, padx = 5)
        self.entry_in.grid(row = 1, column = 3, )
#Element 12. Create the third frame for name, email and comments information:
        self.frame_content_lower = ttk.Frame(master)
        self.frame_content_lower.pack()
#Element 13. Create name, email, comments label:
        ttk.Label(self.frame_content_lower, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content_lower, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content_lower, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
#Element 14. Create name, email entries and comments text:
        self.entry_name = ttk.Entry(self.frame_content_lower, width = 18, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content_lower, width = 18, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content_lower, width = 50, height = 10, font = ('Arial', 10))
        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
#Element 15. Create calculate and clear buttons and bind with calculate and clear functions:
        ttk.Button(self.frame_content_lower, text = 'Calculate',
                   command = self.calculate).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content_lower, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')
#Element 16. Create calculate function:
    def calculate(self):
#Element 21. Create a valid value exception: the weight,inches,and feet only can be integer number, otherwise will pup up a window warning users.
         try:
            BMI_database.insert(self)#Element 29: Add insert() method into calculate() function, so that after user click Calculate, the new user’s record will be stored into database:
            BMI_database.read_from_db()
            self.display_BMI_level()
            self.get_url()
            print('Name: {}'.format(self.entry_name.get()))
            print('Email: {}'.format(self.entry_email.get()))
            print('Age: {}'.format(self.age.get()))
            print('Gender: {}'.format(self.gender.get()))
            print('Weight: {}'.format(self.entry_weight.get())+ ' Lbs')
            print('Height: {}'.format(self.entry_ft.get())+ ' feets ' + format(self.entry_in.get())+ ' inchs' )
            print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
            int(self.entry_weight.get())
            int(self.entry_ft.get())
            int(self.entry_in.get())
            return(print('BMI:' + str(self.calculate_BMI())))
         except ValueError as e:
          print(e)
          messagebox.showinfo(title = 'BMI Calculator', message = 'BMI CANNOT be calculated by non integer number values for weight or height!')
         self.clear()
#Element 17: Define Clear function:
    def clear(self):
        self.entry_ft.delete(0, 'end')
        self.entry_in.delete(0, 'end')
        self.entry_weight.delete(0, 'end')
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')
#Element 18: Define calculate_BMI objec from Calculator class:
    def calculate_BMI(self):
        c = Calculator()
        return c.calculate(int(self.entry_ft.get()),int(self.entry_in.get()),int(self.entry_weight.get()))
#Element 22 Create a function can show BMI level as underweight, Normal weight, Overweight,Obesity and Nonsense
    def display_BMI_level(self):
        self.decimal_BMI = float(str(self.calculate_BMI()))
        more_info = ' Please see more info  from these websites.'

        if 0< self.decimal_BMI < 18.5:
            messagebox.showinfo(title = 'BMI Calculator',
                                message = 'Your BMI is '+ str(self.calculate_BMI())+ ' You are underweight!'
                                + more_info)
            self.body_status = 'Underweight'
        elif 18.5 <= self.decimal_BMI < 24.9:
            messagebox.showinfo(title = 'BMI Calculator',
                                message = 'Your BMI is '+ str(self.calculate_BMI())+ ' Congratulations! Your weight is normal!'
                                + more_info)
            self.body_status  = 'Normal Weight'
        elif 25 < self.decimal_BMI < 29.9:
            messagebox.showinfo(title = 'BMI Calculator',
                                message = 'Your BMI is '+ str(self.calculate_BMI())+ ' You are overweight!'
                                + more_info)
            self.body_status  = 'Overweight'
        elif 30 < self.decimal_BMI:
            messagebox.showinfo(title = 'BMI Calculator',
                                message = 'Your BMI is '+ str(self.calculate_BMI())+ ' Obese! Go to workout!'
                                + more_info)
            self.body_status  = 'Obesity'
        else:
            messagebox.showinfo(title = 'BMI Calculator',
                                message = 'Your BMI is '+ str(self.calculate_BMI())+ ' Are you okey?'
                                + more_info)
            self.body_status = 'Nonsense'
        return (print('Body Status: '+ self.body_status))
#Element 23: Create a function to read the webists
    def more_info(self,a_queue,a_url):
        a_queue.put(urlopen(a_url).read())
        webbrowser.open_new(a_url)
#Element 24: Create a Tread to open the webiste
    def get_url(self):
     the_queue = Queue()
     for url in self.the_urls:
        Thread(target= self.more_info, args=(the_queue, url)).start()

#Element 19: run the whole application with main loop
def main():
    root = Tk()
    feedback = MY_BMI_Calculator(root)
    root.mainloop()
#Element 20: Created a Calculator class
class Calculator():
    def calculate(self,feet,inches,weight):
        inches = feet * 12 + inches
        BMI_value= (weight * 703)/(math.pow(inches,2))
        return round(BMI_value,1)


if __name__ == "__main__": main()


