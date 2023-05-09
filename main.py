from tkinter import *
from tkinter import messagebox, ttk
import sqlite3

class System:

    def __init__(self, root):
        self.root = root

        self.condition = True
        
        # DATA ENTRY FRAME
        self.data_entry_frame = LabelFrame(self.root, text = ' STUDENT DATA ', fg = '#ffffff', bg = '#636e72', font = ('helvetica', 10, 'bold'), bd = 5, relief = GROOVE)
        self.data_entry_frame.place(x = 0, y = 0, width = 405, height = 330)

        # LABELS INSIDE THE DATA ENTRY FRAME
        Label(self.data_entry_frame, text = 'Name: ', width = 20, bg = '#b2bec3', font = ('helvetica', 10, 'bold'), bd = 3, relief = GROOVE).grid(row = 0, column = 0, ipadx = 10, ipady = 10)
        Label(self.data_entry_frame, text = 'Registration Number: ', width = 20, bg = '#b2bec3', font = ('helvetica', 10, 'bold'), bd = 3, relief = GROOVE).grid(row = 1, column = 0, ipadx = 10, ipady = 10)    
        Label(self.data_entry_frame, text = 'Branch: ', width = 20, bg = '#b2bec3', font = ('helvetica', 10, 'bold'), bd = 3, relief = GROOVE).grid(row = 2, column = 0, ipadx = 10, ipady = 10)   
        Label(self.data_entry_frame, text = 'Gender: ', width = 20, bg = '#b2bec3', font = ('helvetica', 10, 'bold'), bd = 3, relief = GROOVE).grid(row = 3, column = 0, ipadx = 10, ipady = 10)      
        Label(self.data_entry_frame, text = 'Age: ', width = 20, bg = '#b2bec3', font = ('helvetica', 10, 'bold'), bd = 3, relief = GROOVE).grid(row = 4, column = 0, ipadx = 10, ipady = 10)        
        Label(self.data_entry_frame, text = 'Contact Number: ', width = 20, bg = '#b2bec3', font = ('helvetica', 10, 'bold'), bd = 3, relief = GROOVE).grid(row = 5, column = 0, ipadx = 10, ipady = 10)
        Label(self.data_entry_frame, text = 'E-mail: ', width = 20, bg = '#b2bec3', font = ('helvetica', 10, 'bold'), bd = 3, relief = GROOVE).grid(row = 6, column = 0, ipadx = 10, ipady = 10)

        # ENTRY SPACES INSIDE THE DATA ENTRY FRAME
        self.name_entry = Entry(self.data_entry_frame, width = 25, font = ('helvetica', 10), bd = 3, relief = GROOVE, justify = 'center')
        self.name_entry.grid(row = 0, column = 1, ipadx = 11, ipady = 10)

        self.regno_entry = Entry(self.data_entry_frame, width = 25, font = ('helvetica', 10), bd = 3, relief = GROOVE, justify = 'center')
        self.regno_entry.grid(row = 1, column = 1, ipadx = 11, ipady = 10)

        self.branch_entry = Entry(self.data_entry_frame, width = 25, font = ('helvetica', 10), bd = 3, relief = GROOVE, justify = 'center')
        self.branch_entry.grid(row = 2, column = 1, ipadx = 11, ipady = 10)

        self.gender_entry = Entry(self.data_entry_frame, width = 25, font = ('helvetica', 10), bd = 3, relief = GROOVE, justify = 'center')
        self.gender_entry.grid(row = 3, column = 1, ipadx = 11, ipady = 10)

        self.age_entry = Entry(self.data_entry_frame, width = 25, font = ('helvetica', 10), bd = 3, relief = GROOVE, justify = 'center')
        self.age_entry.grid(row = 4, column = 1, ipadx = 11, ipady = 10)

        self.contact_entry = Entry(self.data_entry_frame, width = 25, font = ('helvetica', 10), bd = 3, relief = GROOVE, justify = 'center')
        self.contact_entry.grid(row = 5, column = 1, ipadx = 11, ipady = 10)

        self.email_entry = Entry(self.data_entry_frame, width = 25, font = ('helvetica', 10), bd = 3, relief = GROOVE, justify = 'center')
        self.email_entry.grid(row = 6, column = 1, ipadx = 11, ipady = 10)

        # BUTTONS FRAME
        self.button_frame = LabelFrame(self.root, text = ' CONTROL BUTTONS ', fg = '#ffffff', bg = '#636e72', font = ('helvetica', 10, 'bold'), bd = 5, relief = GROOVE)
        self.button_frame.place(x = 405, y = 0, width = 195, height = 330)
        
        # BUTTON PLACEMENT
        Button(self.button_frame, text = 'SAVE RECORD', fg = '#ffffff', bg = '#2d3436', font = ('helvetica', 10, 'bold'), bd = 3, width = 18, command = self.save_record).grid(row = 0, column = 0, ipadx = 10, ipady = 8, padx = (4, 5), pady = (2, 2))
        Button(self.button_frame, text = 'UPDATE RECORD', fg = '#ffffff', bg = '#2d3436', font = ('helvetica', 10, 'bold'), bd = 3, width = 18, command = self.update_record).grid(row = 1, column = 0, ipadx = 10, ipady = 8, padx = (4, 5), pady = (2, 2))
        Button(self.button_frame, text = 'DELETE RECORD', fg = '#ffffff', bg = '#2d3436', font = ('helvetica', 10, 'bold'), bd = 3, width = 18, command = self.delete_record).grid(row = 2, column = 0, ipadx = 10, ipady = 8, padx = (4, 5), pady = (2, 2))
        Button(self.button_frame, text = 'CLEAR ENTRY SPACES', fg = '#ffffff', bg = '#2d3436', font = ('helvetica', 10, 'bold'), bd = 3, width = 18, command = self.clear_spaces).grid(row = 3, column = 0, ipadx = 10, ipady = 8, padx = (4, 5), pady = (2, 2))

        # SEARCH BAR
        self.searchbar = Entry(self.button_frame, text = 'Search', font = ('helvetica', 10), bd = 2, width = 22, justify = 'center')
        self.searchbar.grid(row = 4, column = 0, ipadx = 5, ipady = 5, pady = (18, 5))

        self.search_button = Button(self.button_frame, text = 'SEARCH', fg = '#ffffff', bg = '#2d3436', font = ('helvetica', 10, 'bold'), bd = 3, width = 18, command = self.search_record)
        self.search_button.grid(row = 5, column = 0, ipadx = 10, ipady = 8, padx = (4, 5), pady = (2, 2))
        
        # RECORDS VIEW AND SCROLLBAR
        records_scrollbar = Scrollbar(self.root, orient = VERTICAL, bg = '#2d3436', bd = 0)
        columns = ('Name', 'Reg. No.', 'Branch', 'Gender', 'Age', 'Contact No.', 'Email')
        self.student_records = ttk.Treeview(self.root, column = columns, yscrollcommand = records_scrollbar.set)
        records_scrollbar.place(x = 585, y = 330, height = 255)
        records_scrollbar.config(command = self.student_records.yview)

        # TREEVIEW HEADINGS
        self.student_records.heading('Name', text = 'Name')
        self.student_records.heading('Reg. No.', text = 'Reg. No.')
        self.student_records.heading('Branch', text = 'Branch')
        self.student_records.heading('Gender', text = 'Gender')
        self.student_records.heading('Age', text = 'Age')
        self.student_records.heading('Contact No.', text = 'Contact No.')
        self.student_records.heading('Email', text = 'Email')

        self.student_records['show'] = 'headings'

        # TREEVIEW COLUMN WIDTH ADJUSTMENT
        self.student_records.column('Name', width = 25, anchor = 'center')
        self.student_records.column('Reg. No.', width = 10, anchor = 'center')
        self.student_records.column('Branch', width = 20, anchor = 'center')
        self.student_records.column('Gender', width = 5, anchor = 'center')
        self.student_records.column('Age', width = 5, anchor = 'center')
        self.student_records.column('Contact No.', width = 20, anchor = 'center')
        self.student_records.column('Email', width = 10, anchor = 'center')
        
        # TREEVIEW PLACEMENT
        self.student_records.bind("<ButtonRelease-1>", self.get_cursor)

        self.student_records.place(x = 0, y = 330, width = 584, height = 255)

        self.get_data()

    
    # CLEAR ALL SPACE BUTTON FUNCTION
    def clear_spaces(self):
        self.name_entry.delete(0, END)
        self.regno_entry.delete(0, END)
        self.branch_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.searchbar.delete(0, END)

    # GET CURSOR FUNCTION
    def get_cursor(self, event):
        cursor_row = self.student_records.focus()
        contents = self.student_records.item(cursor_row)
        rows = contents['values']

        self.clear_spaces()
        self.name_entry.insert(0, rows[0])
        self.regno_entry.insert(0, rows[1])
        self.branch_entry.insert(0, rows[2])
        self.gender_entry.insert(0, rows[3])
        self.age_entry.insert(0, rows[4])
        self.contact_entry.insert(0, rows[5])
        self.email_entry.insert(0, rows[6])
        self.searchbar.insert(0, rows[1])

    # GET DATA TO VIEW IN TREEVIEW FUNCTION
    def get_data(self):
        try:
            conn = sqlite3.connect('database\student_records.db')
            sqlite_select_query = """SELECT * from record"""
            cur = conn.cursor()
            cur.execute(sqlite_select_query)

            data = cur.fetchall()
            if len(data) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in data:
                    self.student_records.insert('', END, value = row)
            else:
                self.student_records.delete(*self.student_records.get_children())
            conn.close()
        except Exception:
            messagebox.showerror(title = 'Student Management System Alert', message = 'Trouble connecting to the database. Please try again later!')

    # SAVE RECORD FUNCTION
    def save_record(self):
        try:
            flag = 0
            conn = sqlite3.connect('database\student_records.db')
            sqlite_insert_query = """INSERT INTO record (name, regno, branch, gender, age, contact, email) VALUES (?,?,?,?,?,?,?)"""
            student_data = (self.name_entry.get(), self.regno_entry.get(), self.branch_entry.get(), self.gender_entry.get(), self.age_entry.get(), self.contact_entry.get(), self.email_entry.get())
            cur = conn.cursor()
            for i in range(len(student_data)):
                if student_data[i] == '' or student_data[i] == None:
                    flag = 1
            if flag == 0:
                cur.execute(sqlite_insert_query, student_data)
                conn.commit()
                messagebox.showinfo(title = 'Student Management System Alert', message = 'The student record was saved successfully')
            else:
                messagebox.showwarning(title = 'Student Management System Alert', message = 'Please fill all the details')
            conn.close()
            
            self.clear_spaces()
            self.get_data()
            
        except Exception:
            messagebox.showerror(title = 'Student Management System Alert', message = 'Trouble connecting to the database. Please try again later!')
   
    # SEARCH BUTTON FUNCTION
    def search_record(self):
        if self.condition:
            try:
                conn = sqlite3.connect('database\student_records.db')
                sqlite_search_query = """SELECT * from record where regno = ?"""
                cur = conn.cursor()
                cur.execute(sqlite_search_query, (self.searchbar.get(),))

                data = cur.fetchone()
                if len(data) != 0:
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert('', END, value = data)
                    self.condition = False
                    self.search_button['text'] = 'SHOW ALL'
                    self.clear_spaces()

                conn.close()
            except Exception:
                messagebox.showerror(title = 'Student Management System Alert', message = "The record you're looking for doesn't exist")
        else:
            self.condition = True
            self.search_button['text'] = 'SEARCH'
            self.get_data() 

    # DELETE RECORD FUNCTION
    def delete_record(self):
        try:
            conn = sqlite3.connect('database\student_records.db')
            sqlite_delete_query = """DELETE from record where regno = ?"""
            if self.searchbar.get():
                conn.execute(sqlite_delete_query, (self.searchbar.get(),))
                conn.commit()
                messagebox.showinfo(title = 'Student Management System Alert', message = 'The student record was removed successfully')
            else:
                messagebox.showwarning(title = 'Student Management System Alert', message = 'Select a record to delete')
            conn.close()
            self.clear_spaces()
            self.get_data()
        except Exception:
            messagebox.showerror(title = 'Student Management System Alert', message = "We're having trouble removing that record. Please try again later!")

    # UPDATE RECORD FUNCTION
    def update_record(self):
        try:
            conn = sqlite3.connect('database\student_records.db')
            sqlite_update_query = """UPDATE record set name = ?, regno = ?, branch = ?, gender = ?, age = ?, contact = ?, email = ? where regno = ?"""
            student_data = (self.name_entry.get(), self.regno_entry.get(), self.branch_entry.get(), self.gender_entry.get(), self.age_entry.get(), self.contact_entry.get(), self.email_entry.get(), self.searchbar.get())
            conn.execute(sqlite_update_query, student_data)
            conn.commit()
            messagebox.showinfo(title = 'Student Management System Alert', message = 'The student record was updated successfully')
            conn.close()
            self.clear_spaces()
            self.get_data()
        except Exception:
            messagebox.showerror(title = 'Student Management System Alert', message = "We're having trouble removing that record. Please try again later!")
        

root = Tk()
root.title('Student Management System')
root.geometry('600x585')
root.resizable(0, 0)
root.configure(bg = '#636e72')
root.iconbitmap("<FILE DIRECTORY FOR THE ICON")

System(root)

root.mainloop()