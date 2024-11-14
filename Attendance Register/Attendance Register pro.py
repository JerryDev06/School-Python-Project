# GOD PLEASE HELP ME TO FINISH THIS PROJECT !!!!! :)
import mysql.connector as ms                #ms is used to call mysql.connector
import tkinter
from tkinter import *
import tkinter.messagebox as messagebox
from datetime import *
from tabulate import tabulate
from PIL import Image, ImageTk
database="attendance"        #Change this accordingly
password="02101625"       #Change this according to your mysql password
connector = ms.connect(
        host="localhost",
        user="root",
        password=password,
        database=database
    )
cursor = connector.cursor()
cursor.execute("SHOW TABLES LIKE 'password'")  # to check weather table exist or not
table_exists = cursor.fetchone() is not None
if table_exists:  # not the first time for second time
    cursor.execute("SHOW TABLES LIKE 'student_details'")  # to check weather table exist or not
    table_exists = cursor.fetchone() is not None
    if table_exists:
        welcome = Tk()  # creating win welcome to show at the begaining
        welcome.configure(bg="black")
        welcome.title("welcome")
        welcome.geometry("800x600")
        welcome.iconbitmap("Reeds.ico")
        screen_width = welcome.winfo_screenwidth()
        screen_height = welcome.winfo_screenheight()
        bg_image = Image.open("voif.jpg")
        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
        background_image = ImageTk.PhotoImage(bg_image)
        canvas = Canvas(welcome, width=screen_width, height=screen_height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=NW, image=background_image)
        def admin():
            welcome.destroy()
            def geting():  # win asking password window
                global pword  # pword user input
                if enterpasswordbox.get() == "":
                    messagebox.showwarning('Missing information', 'Please Enter the Password.')
                else:
                    pword = enterpasswordbox.get()
                    passwin.destroy()
            passwin = Tk()  # win to enter password
            passwin.configure(bg="black")  # bg colour
            passwin.title("login")
            passwin.geometry("800x600")
            passwin.iconbitmap("Reeds.ico")
            screen_width = passwin.winfo_screenwidth()
            screen_height = passwin.winfo_screenheight()
            bg_image = Image.open("voif.jpg")
            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
            background_image = ImageTk.PhotoImage(bg_image)
            canvas = Canvas(passwin, width=screen_width, height=screen_height)
            canvas.pack()
            canvas.create_image(0, 0, anchor=NW, image=background_image)
            passwordlabel = Label(passwin, text="Enter password", font=("Arial", 30), fg="white", bg="black",
                                  justify="center", padx=10, pady=10)
            passwordlabel.place(relx=0.5, rely=0.4, anchor=CENTER)  # password using place
            enterpasswordbox = Entry(passwin, show="*", width=30)  # Entrty box to ask password
            enterpasswordbox.place(relx=0.5, rely=0.5, anchor=CENTER)
            loginpasswordButton = Button(passwin, text="login", font=("Arial", 15), fg="white", bg="black",
                                         command=geting, width=6, height=1)
            loginpasswordButton.place(relx=0.5, rely=0.6,anchor=CENTER)  # login password button
            passwin.mainloop()
            cursor.execute("select password from password where designation='admin'")
            passadmin=cursor.fetchone()[0]
            if pword == '':
                messagebox.showwarning('Missing information', 'Please Enter the Password.')
            else:
                if passadmin == pword:
                    def restart():
                        def summary():
                            def yearsumm():
                                summary.destroy()
                                date_column_query = """
                                        SELECT COLUMN_NAME 
                                        FROM INFORMATION_SCHEMA.COLUMNS 
                                        WHERE TABLE_NAME = 'student_details' 
                                        AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                    """
                                cursor.execute(date_column_query)
                                date_columns = [column[0] for column in cursor.fetchall()]

                                # Prepare a dictionary to store student details and attendance counts
                                student_details = {}

                                # Query to fetch student details and attendance for each date column
                                for date_column in date_columns:
                                    # Use backticks to reference the date columns
                                    query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A')"
                                    cursor.execute(query)
                                    attendance_data = cursor.fetchall()

                                    for row in attendance_data:
                                        admission_no, roll_number, name, gender, attendance_value = row

                                        if name not in student_details:
                                            student_details[name] = {'Admission No': admission_no,
                                                                     'Roll No': roll_number, 'Gender': gender,
                                                                     'Present': 0, 'Absent': 0}

                                        if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                            student_details[name]['Present'] += 1
                                        elif attendance_value == 'A':
                                            student_details[name]['Absent'] += 1
                                # Sort the student details by the number of days present in descending order
                                sorted_student_details = sorted(student_details.items(), key=lambda x: x[1]['Present'],
                                                                reverse=True)

                                # Prepare data for tabulate
                                table_data = []
                                for name, details in sorted_student_details:
                                    table_data.append(
                                        [details['Admission No'], details['Roll No'], details['Gender'], name,
                                         details['Present'], details['Absent']])

                                # Create a Tkinter window
                                root = Tk()
                                root.title("Attendance Summary")
                                root.geometry("800x600")
                                root.iconbitmap("Reeds.ico")
                                # Create a canvas with a vertical scrollbar
                                canvas = Canvas(root)
                                canvas.pack(side="left", fill="both", expand=True)

                                # Create a vertical scrollbar
                                scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                scrollbar.pack(side="right", fill="y")

                                canvas.configure(yscrollcommand=scrollbar.set)

                                # Convert tabulated data to a string with visually formatted table using "pretty" format
                                headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present', 'Days Absent']
                                attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                # Create a label to display the tabulated attendance summary inside the canvas
                                label = Label(canvas, text=attendance_table, justify="left", font=("Courier", 10))
                                canvas.create_window((0, 0), window=label, anchor="nw")

                                # Configure canvas scrolling region
                                canvas.config(scrollregion=canvas.bbox("all"))

                                # Start the Tkinter main loop
                                root.mainloop()
                            def monthsumm():
                                def Jan():
                                    month.destroy()
                                    monthn = 1
                                    date_column_query = """
                                                                                SELECT COLUMN_NAME 
                                                                                FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                WHERE TABLE_NAME = 'student_details' 
                                                                                AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                            """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")
                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Feb():
                                    month.destroy()
                                    monthn = 2
                                    date_column_query = """
                                                            SELECT COLUMN_NAME 
                                                            FROM INFORMATION_SCHEMA.COLUMNS 
                                                            WHERE TABLE_NAME = 'student_details' 
                                                            AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")
                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Mar():
                                    month.destroy()
                                    monthn = 3
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Apr():
                                    month.destroy()
                                    monthn = 4
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")
                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def May():
                                    month.destroy()
                                    monthn = 5
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")
                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Jun():
                                    month.destroy()
                                    monthn = 6
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Jul():
                                    month.destroy()
                                    monthn = 7
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Aug():
                                    month.destroy()
                                    monthn = 8
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Sep():
                                    month.destroy()
                                    monthn = 9
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Oct():
                                    month.destroy()
                                    monthn = 10
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Nov():
                                    month.destroy()
                                    monthn = 11
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Dec():
                                    month.destroy()
                                    monthn = 12
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                summary.destroy()
                                month = Tk()
                                month.configure(bg="black")  # bg colour
                                month.title("Month Summary")
                                month.geometry("800x600")
                                month.iconbitmap("Reeds.ico")
                                screen_width = month.winfo_screenwidth()
                                screen_height = month.winfo_screenheight()
                                bg_image = Image.open("voif.jpg")
                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                background_image = ImageTk.PhotoImage(bg_image)
                                canvas1 = Canvas(month, width=screen_width, height=screen_height)
                                canvas1.pack()
                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                monthlabel = Label(month, text="Select A Month For Summary", font=("Arial", 30), fg="white",
                                                   bg="black",justify="center", padx=10, pady=10)
                                monthlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
                                janButton = Button(month, text="Jan --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Jan, width=10, height=1)
                                janButton.place(relx=0.35, rely=0.5, anchor=CENTER)
                                FebButton = Button(month, text="Feb --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Feb, width=10, height=1)
                                FebButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                                MarButton = Button(month, text="Mar --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Mar, width=10, height=1)
                                MarButton.place(relx=0.65, rely=0.5, anchor=CENTER)
                                AprButton = Button(month, text="Apr --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Apr, width=10, height=1)
                                AprButton.place(relx=0.35, rely=0.6, anchor=CENTER)
                                MayButton = Button(month, text="May --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=May, width=10, height=1)
                                MayButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                JunButton = Button(month, text="Jun --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Jun, width=10, height=1)
                                JunButton.place(relx=0.65, rely=0.6, anchor=CENTER)
                                JulButton = Button(month, text="Jul --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Jul, width=10, height=1)
                                JulButton.place(relx=0.35, rely=0.7, anchor=CENTER)
                                AugButton = Button(month, text="Aug --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Aug, width=10, height=1)
                                AugButton.place(relx=0.5, rely=0.7, anchor=CENTER)
                                SepButton = Button(month, text="Sep --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Sep, width=10, height=1)
                                SepButton.place(relx=0.65, rely=0.7, anchor=CENTER)
                                OctButton = Button(month, text="Oct --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Oct, width=10, height=1)
                                OctButton.place(relx=0.35, rely=0.8, anchor=CENTER)
                                NovButton = Button(month, text="Nov --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Nov, width=10, height=1)
                                NovButton.place(relx=0.5, rely=0.8, anchor=CENTER)
                                DecButton = Button(month, text="Dec --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Dec, width=10, height=1)
                                DecButton.place(relx=0.65, rely=0.8, anchor=CENTER)
                                month.mainloop()

                            admenu.destroy()
                            summary = Tk()
                            summary.configure(bg="black")  # bg colour
                            summary.title("Summary")
                            summary.geometry("800x600")
                            summary.iconbitmap("Reeds.ico")
                            screen_width = summary.winfo_screenwidth()
                            screen_height = summary.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(summary, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            summarylabel = Label(summary, text="Summary", font=("Arial", 30), fg="white", bg="black",
                                                 justify="center", padx=10, pady=10)
                            summarylabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                            monthsummButton = Button(summary, text="Summary Of The Month --→", font=("Arial", 15),
                                                     fg="white",
                                                     bg="black", command=monthsumm, width=25, height=1)
                            monthsummButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                            yearsummButton = Button(summary, text="Summary Of The Year --→", font=("Arial", 15),
                                                    fg="white", bg="black",
                                                    command=yearsumm, width=25, height=1)
                            yearsummButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                            summary.mainloop()
                            restart()
                        def addstudent():
                            admenu.destroy()
                            gender = ""

                            def justforfun():
                                saved.destroy()
                                restart()

                            def M():  # for geting value from male
                                nonlocal gender
                                gender = "M"
                                text = "selected " + gender
                                genderlabelconfirm = Label(stuinfo, text=text, font=("Arial", 15), fg="white",
                                                           bg="black",
                                                           justify="center", padx=10, pady=10)
                                genderlabelconfirm.place(relx=0.88, rely=0.6, anchor=CENTER)

                            def F():  # for getting value from female
                                nonlocal gender
                                gender = "F"
                                text = "selected " + gender
                                genderlabelconfirm = Label(stuinfo, text=text, font=("Arial", 15), fg="white",
                                                           bg="black",
                                                           justify="center", padx=10, pady=10)
                                genderlabelconfirm.place(relx=0.88, rely=0.6, anchor=CENTER)

                            def get():  # getting value of the student
                                if stuname.get() == '' or sturollno.get() == '' or stuadmissionno.get() == '':
                                    messagebox.showwarning('Missing information',
                                                           'Please enter all the required details.')
                                elif gender == "":
                                    messagebox.showwarning('Missing information', 'Select a gender option.')
                                else:
                                    sqlroll = "select name from student_details where roll_number=%s"
                                    valuesroll = (sturollno.get(),)
                                    cursor.execute(sqlroll, valuesroll)
                                    resultroll = cursor.fetchone()
                                    checkroll = resultroll is not None
                                    sqladm = "select name from student_details where admission_no=%s"
                                    valuesadm = (stuadmissionno.get(),)
                                    cursor.execute(sqladm, valuesadm)
                                    resultadm = cursor.fetchone()
                                    checkadm = resultadm is not None
                                    if checkroll:
                                        messagebox.showwarning("Already Exist",
                                                               "Student " + resultroll[0] + " Has The Same Roll Number")
                                    elif checkadm:
                                        messagebox.showwarning("Already Exist",
                                                               "Student " + resultadm[
                                                                   0] + " Has The Same Admission Number")
                                    else:
                                        global rollno
                                        global saved
                                        name = stuname.get()
                                        rollno = sturollno.get()
                                        # Gender already stores the gender
                                        admissionno = stuadmissionno.get()
                                        cursor.execute(
                                            "INSERT INTO student_details (name, roll_number, admission_no, Gender) VALUES (%s, %s, %s, %s)",
                                            (name, rollno, admissionno, gender))
                                        connector.commit()
                                        stuinfo.destroy()
                                        saved = Tk()  # to create win
                                        saved.iconbitmap("Reeds.ico")
                                        saved.configure(bg="black")  # bg colour
                                        saved.title("login")
                                        saved.geometry("800x600")
                                        saved.iconbitmap("Reeds.ico")
                                        screen_width = saved.winfo_screenwidth()
                                        screen_height = saved.winfo_screenheight()
                                        bg_image = Image.open("voif.jpg")
                                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                        background_image = ImageTk.PhotoImage(bg_image)
                                        canvas1 = Canvas(saved, width=screen_width, height=screen_height)
                                        canvas1.pack()
                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                        textnew = "Student Details Saved"
                                        savedLabel = Label(saved, text=(textnew), font=("Arial", 30), fg="white"
                                                           , bg="black", justify="center", padx=10, pady=10)
                                        savedLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                                        savedbutton = Button(saved, text="Done --→", font=("Arial", 15), fg="white",
                                                             bg="black",
                                                             command=justforfun, width=20, height=1)
                                        savedbutton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                        saved.mainloop()

                            stuinfo = Tk()  # creating win welcome to show at the begaining
                            stuinfo.configure(bg="black")
                            stuinfo.title("welcome")
                            stuinfo.geometry("800x600")
                            stuinfo.iconbitmap("Reeds.ico")
                            screen_width = stuinfo.winfo_screenwidth()
                            screen_height = stuinfo.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(stuinfo, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            GI = Label(stuinfo, text="Enter the information of the student ", font=("Arial", 30),
                                       fg="white", bg="black", justify="center", padx=10, pady=10)
                            GI.place(relx=0.5, rely=0.2, anchor=CENTER)  # gi is thee general info

                            namelabel = Label(stuinfo, text="Name ", font=("Arial", 15),
                                              fg="white", bg="black", justify="center", padx=10, pady=10)
                            namelabel.place(relx=0.3, rely=0.4, anchor=CENTER)
                            stuname = Entry(stuinfo, width=25)
                            stuname.place(relx=0.7, rely=0.4, anchor=CENTER)
                            rollnolabel = Label(stuinfo, text="Roll Number ", font=("Arial", 15),
                                                fg="white", bg="black", justify="center", padx=10, pady=10)
                            rollnolabel.place(relx=0.3, rely=0.5, anchor=CENTER)
                            sturollno = Entry(stuinfo, width=25)
                            sturollno.place(relx=0.7, rely=0.5, anchor=CENTER)

                            genderlabel = Label(stuinfo, text="Gender ", font=("Arial", 15),
                                                fg="white", bg="black", justify="center", padx=10, pady=10)
                            genderlabel.place(relx=0.3, rely=0.6, anchor=CENTER)
                            genderButtonM = Button(stuinfo, text="M", font=("Arial", 10), fg="black",
                                                   bg="white", command=M, width=5, height=1, relief="raised")
                            genderButtonM.place(relx=0.65, rely=0.6, anchor=CENTER)
                            genderlabelor = Label(stuinfo, text="or", font=("Arial", 10),
                                                  fg="white", bg="black", justify="center", padx=10, pady=10)
                            genderlabelor.place(relx=0.7, rely=0.6, anchor=CENTER)
                            genderButtonF = Button(stuinfo, text="F", font=("Arial", 10), fg="black",
                                                   bg="white", command=F, width=5, height=1, relief="raised")
                            genderButtonF.place(relx=0.75, rely=0.6, anchor=CENTER)

                            admissionnolabel = Label(stuinfo, text="Admission Number ", font=("Arial", 15),
                                                     fg="white", bg="black", justify="center", padx=10, pady=10)
                            admissionnolabel.place(relx=0.3, rely=0.7, anchor=CENTER)
                            stuadmissionno = Entry(stuinfo, width=25)
                            stuadmissionno.place(relx=0.7, rely=0.7, anchor=CENTER)

                            Nextstudent = Button(stuinfo, text="Submit Detail Of The Student --→", font=("Arial", 15),
                                                 fg="white",
                                                 bg="black", command=get, width=35, height=1)
                            Nextstudent.place(relx=0.5, rely=0.8, anchor=CENTER)
                            stuinfo.mainloop()

                        def removestudent():
                            def windes():
                                done.destroy()
                                restart()

                            def removecomm():
                                rollno = enterrollbox.get()
                                if rollno == "":
                                    messagebox.showwarning('Missing information', 'Please enter the Roll Number.')
                                else:
                                    cursor.execute("SELECT * FROM student_details WHERE roll_number = %s", (rollno,))
                                    result = cursor.fetchone()
                                    if result is None:
                                        missinglabel = Label(remove,
                                                             text="Student With Roll No " + rollno + " Not Found",
                                                             font=("Arial", 15), fg="red", bg="black",
                                                             justify="center", padx=10, pady=10)
                                        missinglabel.place(relx=0.5, rely=0.7, anchor=CENTER)
                                    else:
                                        def sure():
                                            global done
                                            confirm.destroy()
                                            delete_query = "DELETE FROM student_details WHERE roll_number = %s"
                                            cursor.execute(delete_query, (rollno,))
                                            connector.commit()
                                            done = Tk()  # to create win
                                            done.configure(bg="black")  # bg colour
                                            done.title("Remove Student")
                                            done.geometry("800x600")
                                            done.iconbitmap("Reeds.ico")
                                            screen_width = done.winfo_screenwidth()
                                            screen_height = done.winfo_screenheight()
                                            bg_image = Image.open("voif.jpg")
                                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                            background_image = ImageTk.PhotoImage(bg_image)
                                            canvas1 = Canvas(done, width=screen_width, height=screen_height)
                                            canvas1.pack()
                                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                            successlabel = Label(done, text="Student Romoved Successfully ",
                                                                 font=("Arial", 30), fg="white",
                                                                 bg="black", justify="center", padx=10, pady=10)
                                            successlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                            doneButton = Button(done, text="Done", font=("Arial", 15), fg="white",
                                                                bg="black",
                                                                command=windes, width=6, height=1)
                                            doneButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                            done.mainloop()
                                            connector.commit()

                                        remove.destroy()
                                        confirm = Tk()  # to create win
                                        confirm.configure(bg="black")  # bg colour
                                        confirm.title("Remove Student")
                                        confirm.geometry("800x600")
                                        confirm.iconbitmap("Reeds.ico")
                                        screen_width = confirm.winfo_screenwidth()
                                        screen_height = confirm.winfo_screenheight()
                                        bg_image = Image.open("voif.jpg")
                                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                        background_image = ImageTk.PhotoImage(bg_image)
                                        canvas1 = Canvas(confirm, width=screen_width, height=screen_height)
                                        canvas1.pack()
                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                        sql = "select name from student_details where roll_number=%s"  # display std name
                                        value = (rollno,)
                                        cursor.execute(sql, value)
                                        result = cursor.fetchone()
                                        removelabel2 = Label(confirm, text="Are You Sure To", font=("Arial", 30),
                                                             fg="white", bg="black", justify="center", padx=10, pady=10)
                                        removelabel2.place(relx=0.5, rely=0.4, anchor=CENTER)
                                        removelabel1 = Label(confirm, text="remove " + result[0] + " ?",
                                                             font=("Arial", 30),
                                                             fg="white", bg="black", justify="center", padx=10, pady=10)
                                        removelabel1.place(relx=0.5, rely=0.5, anchor=CENTER)
                                        sureButton = Button(confirm, text="Submit --→", font=("Arial", 15), fg="white",
                                                            bg="black", command=sure, width=10, height=1)
                                        sureButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                        confirm.mainloop()

                            admenu.destroy()
                            remove = Tk()  # to create win
                            remove.configure(bg="black")  # bg colour
                            remove.title("Remove Student")
                            remove.geometry("800x600")
                            remove.iconbitmap("Reeds.ico")
                            screen_width = remove.winfo_screenwidth()
                            screen_height = remove.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(remove, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            removelabel = Label(remove, text="Enter The Roll Number Of The Student", font=("Arial", 30),
                                                fg="white", bg="black",
                                                justify="center", padx=10, pady=10)
                            removelabel.place(relx=0.5, rely=0.4, anchor=CENTER)

                            enterrollbox = Entry(remove, width=30)
                            enterrollbox.place(relx=0.5, rely=0.5, anchor=CENTER)
                            removeButton = Button(remove, text="Confirm --→", font=("Arial", 15), fg="white",
                                                  bg="black",
                                                  command=removecomm, width=10, height=1)
                            removeButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                            remove.mainloop()

                        def edit():
                            def editfn():
                                rollno = enterrollbox.get()
                                if rollno == "":
                                    messagebox.showwarning('Missing information', 'Please enter the Roll Number.')
                                else:
                                    cursor.execute("SELECT * FROM student_details WHERE roll_number = %s", (rollno,))
                                    result = cursor.fetchone()
                                    if result is None:
                                        missinglabel = Label(edit, text="Student With Roll No " + rollno + " Not Found",
                                                             font=("Arial", 15), fg="red", bg="black",
                                                             justify="center", padx=10, pady=10)
                                        missinglabel.place(relx=0.5, rely=0.7, anchor=CENTER)
                                    else:
                                        def rollnum():
                                            def getroll():
                                                rollnum = enterrollbox.get()
                                                if rollnum == "":
                                                    messagebox.showwarning('Missing information',
                                                                           'Please enter the Roll Number.')
                                                else:
                                                    sqlroll = "select name from student_details where roll_number=%s"
                                                    valuesroll = (enterrollbox.get(),)
                                                    cursor.execute(sqlroll, valuesroll)
                                                    resultroll = cursor.fetchone()
                                                    checkroll = resultroll is not None
                                                    if checkroll:
                                                        messagebox.showwarning("Already Exist",
                                                                               "Student " + resultroll[
                                                                                   0] + " Has The Same Roll Number")
                                                    else:
                                                        def updated1():
                                                            updatedroll.destroy()
                                                            restart()

                                                        roll.destroy()
                                                        sql = "UPDATE student_details SET roll_number = %s WHERE roll_number = %s"
                                                        values = (rollnum, rollno)
                                                        cursor.execute(sql, values)
                                                        connector.commit()
                                                        updatedroll = Tk()  # to create win
                                                        updatedroll.configure(bg="black")  # bg colour
                                                        updatedroll.title("Updated Roll Number")
                                                        updatedroll.geometry("800x600")
                                                        updatedroll.iconbitmap("Reeds.ico")
                                                        screen_width = updatedroll.winfo_screenwidth()
                                                        screen_height = updatedroll.winfo_screenheight()
                                                        bg_image = Image.open("voif.jpg")
                                                        bg_image = bg_image.resize((screen_width, screen_height),
                                                                                   Image.BICUBIC)
                                                        background_image = ImageTk.PhotoImage(bg_image)
                                                        canvas1 = Canvas(updatedroll, width=screen_width,
                                                                         height=screen_height)
                                                        canvas1.pack()
                                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                                        rolllabel = Label(updatedroll,
                                                                          text="Updated The New Roll Number",
                                                                          font=("Arial", 30),
                                                                          fg="white", bg="black", justify="center",
                                                                          padx=10, pady=10)
                                                        rolllabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                                        updatedrollButton = Button(updatedroll, text="Done --→",
                                                                                   font=("Arial", 15),
                                                                                   fg="white", bg="black",
                                                                                   command=updated1, width=10, height=1)
                                                        updatedrollButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                                        updatedroll.mainloop()

                                            choose.destroy()
                                            roll = Tk()  # to create win
                                            roll.configure(bg="black")  # bg colour
                                            roll.title("Roll Number")
                                            roll.geometry("800x600")
                                            roll.iconbitmap("Reeds.ico")
                                            screen_width = roll.winfo_screenwidth()
                                            screen_height = roll.winfo_screenheight()
                                            bg_image = Image.open("voif.jpg")
                                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                            background_image = ImageTk.PhotoImage(bg_image)
                                            canvas1 = Canvas(roll, width=screen_width, height=screen_height)
                                            canvas1.pack()
                                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                            sql = "select name from student_details where roll_number=%s"  # display std name
                                            value = (rollno,)
                                            cursor.execute(sql, value)
                                            result = cursor.fetchone()
                                            rolllabel1 = Label(roll, text="Of " + result[0], font=("Arial", 30),
                                                               fg="white", bg="black", justify="center", padx=10,
                                                               pady=10)
                                            rolllabel1.place(relx=0.5, rely=0.5, anchor=CENTER)
                                            rolllabel = Label(roll, text="Enter The New Roll Number",
                                                              font=("Arial", 30),
                                                              fg="white",
                                                              bg="black", justify="center", padx=10, pady=10)
                                            rolllabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                            enterrollbox = Entry(roll, width=30)
                                            enterrollbox.place(relx=0.5, rely=0.6, anchor=CENTER)
                                            submitrollButton = Button(roll, text="Submit --→", font=("Arial", 15),
                                                                      fg="white",
                                                                      bg="black", command=getroll, width=10, height=1)
                                            submitrollButton.place(relx=0.5, rely=0.7, anchor=CENTER)

                                        def admission():
                                            def getadm():
                                                admnum = enteradmissionbox.get()
                                                if admnum == "":
                                                    messagebox.showwarning('Missing information',
                                                                           'Please enter the Admission Number.')
                                                else:
                                                    sqladm = "select name from student_details where admission_no=%s"
                                                    valuesadm = (enteradmissionbox.get(),)
                                                    cursor.execute(sqladm, valuesadm)
                                                    resultadm = cursor.fetchone()
                                                    checkadm = resultadm is not None
                                                    if checkadm:
                                                        messagebox.showwarning("Already Exist",
                                                                               "Student " + resultadm[0] +
                                                                               " Has The Same Admission Number")
                                                    else:
                                                        def updated1():
                                                            updatedadm.destroy()
                                                            restart()

                                                        admissionwin.destroy()
                                                        sql = "UPDATE student_details SET admission_no = %s WHERE roll_number = %s"
                                                        values = (admnum, rollno)
                                                        cursor.execute(sql, values)
                                                        connector.commit()
                                                        updatedadm = Tk()  # to create win
                                                        updatedadm.configure(bg="black")  # bg colour
                                                        updatedadm.title("Updated Admission Number")
                                                        updatedadm.geometry("800x600")
                                                        updatedadm.iconbitmap("Reeds.ico")
                                                        screen_width = updatedadm.winfo_screenwidth()
                                                        screen_height = updatedadm.winfo_screenheight()
                                                        bg_image = Image.open("voif.jpg")
                                                        bg_image = bg_image.resize((screen_width, screen_height),
                                                                                   Image.BICUBIC)
                                                        background_image = ImageTk.PhotoImage(bg_image)
                                                        canvas1 = Canvas(updatedadm, width=screen_width,
                                                                         height=screen_height)
                                                        canvas1.pack()
                                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                                        admlabel = Label(updatedadm,
                                                                         text="Updated The New Admission Number",
                                                                         font=("Arial", 30),
                                                                         fg="white", bg="black", justify="center",
                                                                         padx=10, pady=10)
                                                        admlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                                        updatedadmButton = Button(updatedadm, text="Done --→",
                                                                                  font=("Arial", 15),
                                                                                  fg="white", bg="black",
                                                                                  command=updated1, width=10,
                                                                                  height=1)
                                                        updatedadmButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                                        updatedadm.mainloop()

                                            choose.destroy()
                                            admissionwin = Tk()  # to create win
                                            admissionwin.configure(bg="black")  # bg colour
                                            admissionwin.title("Roll Number")
                                            admissionwin.geometry("800x600")
                                            admissionwin.iconbitmap("Reeds.ico")
                                            screen_width = admissionwin.winfo_screenwidth()
                                            screen_height = admissionwin.winfo_screenheight()
                                            bg_image = Image.open("voif.jpg")
                                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                            background_image = ImageTk.PhotoImage(bg_image)
                                            canvas1 = Canvas(admissionwin, width=screen_width, height=screen_height)
                                            canvas1.pack()
                                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                            sql = "select name from student_details where roll_number=%s"  # display std name
                                            value = (rollno,)
                                            cursor.execute(sql, value)
                                            result = cursor.fetchone()
                                            rolllabel1 = Label(admissionwin, text="Of " + result[0], font=("Arial", 30),
                                                               fg="white", bg="black", justify="center", padx=10,
                                                               pady=10)
                                            rolllabel1.place(relx=0.5, rely=0.5, anchor=CENTER)
                                            rolllabel = Label(admissionwin, text="Enter The New Admission Number",
                                                              font=("Arial", 30),
                                                              fg="white", bg="black", justify="center", padx=10,
                                                              pady=10)
                                            rolllabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                            enteradmissionbox = Entry(admissionwin, width=30)
                                            enteradmissionbox.place(relx=0.5, rely=0.6, anchor=CENTER)
                                            submitadButton = Button(admissionwin, text="Submit --→", font=("Arial", 15),
                                                                    fg="white",
                                                                    bg="black", command=getadm, width=10, height=1)
                                            submitadButton.place(relx=0.5, rely=0.7, anchor=CENTER)
                                            admissionwin.mainloop()

                                        def name():
                                            def getname():
                                                name = enternamebox.get()
                                                if name == "":
                                                    messagebox.showwarning('Missing information',
                                                                           'Please enter the Name.')
                                                else:
                                                    def updated1():
                                                        updatedname.destroy()
                                                        restart()

                                                    namewin.destroy()
                                                    sql = "UPDATE student_details SET name = %s WHERE roll_number = %s"
                                                    values = (name, rollno)
                                                    cursor.execute(sql, values)
                                                    connector.commit()
                                                    updatedname = Tk()  # to create win
                                                    updatedname.configure(bg="black")  # bg colour
                                                    updatedname.title("Updated Name")
                                                    updatedname.geometry("800x600")
                                                    updatedname.iconbitmap("Reeds.ico")
                                                    screen_width = updatedname.winfo_screenwidth()
                                                    screen_height = updatedname.winfo_screenheight()
                                                    bg_image = Image.open("voif.jpg")
                                                    bg_image = bg_image.resize((screen_width, screen_height),
                                                                               Image.BICUBIC)
                                                    background_image = ImageTk.PhotoImage(bg_image)
                                                    canvas1 = Canvas(updatedname, width=screen_width, height=screen_height)
                                                    canvas1.pack()
                                                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                                    admlabel = Label(updatedname, text="Updated The New Name",
                                                                     font=("Arial", 30),
                                                                     fg="white", bg="black", justify="center", padx=10,
                                                                     pady=10)
                                                    admlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                                    updatedadmButton = Button(updatedname, text="Done --→",
                                                                              font=("Arial", 15),
                                                                              fg="white", bg="black", command=updated1,
                                                                              width=10,
                                                                              height=1)
                                                    updatedadmButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                                    updatedname.mainloop()

                                            choose.destroy()
                                            namewin = Tk()  # to create win
                                            namewin.configure(bg="black")  # bg colour
                                            namewin.title("Name")
                                            namewin.geometry("800x600")
                                            namewin.iconbitmap("Reeds.ico")
                                            screen_width = namewin.winfo_screenwidth()
                                            screen_height = namewin.winfo_screenheight()
                                            bg_image = Image.open("voif.jpg")
                                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                            background_image = ImageTk.PhotoImage(bg_image)
                                            canvas1 = Canvas(namewin, width=screen_width, height=screen_height)
                                            canvas1.pack()
                                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                            sql = "select name from student_details where roll_number=%s"  # display std name
                                            value = (rollno,)
                                            cursor.execute(sql, value)
                                            result = cursor.fetchone()
                                            namelabel1 = Label(namewin, text="Of " + result[0], font=("Arial", 30),
                                                               fg="white", bg="black", justify="center", padx=10,
                                                               pady=10)
                                            namelabel1.place(relx=0.5, rely=0.5, anchor=CENTER)
                                            namelabel = Label(namewin, text="Enter The New Name", font=("Arial", 30),
                                                              fg="white", bg="black", justify="center", padx=10,
                                                              pady=10)
                                            namelabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                            enternamebox = Entry(namewin, width=30)
                                            enternamebox.place(relx=0.5, rely=0.6, anchor=CENTER)
                                            submitnameButton = Button(namewin, text="Submit --→", font=("Arial", 15),
                                                                      fg="white",
                                                                      bg="black", command=getname, width=10, height=1)
                                            submitnameButton.place(relx=0.5, rely=0.7, anchor=CENTER)
                                            namewin.mainloop()

                                        def genderchange():
                                            gender = ""

                                            def M():  # for geting value from male
                                                nonlocal gender
                                                gender = "M"
                                                text = "selected " + gender
                                                genderlabelconfirm = Label(genderwin, text=text, font=("Arial", 15),
                                                                           fg="white",
                                                                           bg="black",
                                                                           justify="center", padx=10, pady=10)
                                                genderlabelconfirm.place(relx=0.75, rely=0.6, anchor=CENTER)

                                            def F():  # for getting value from female
                                                nonlocal gender
                                                gender = "F"
                                                text = "selected " + gender
                                                genderlabelconfirm = Label(genderwin, text=text, font=("Arial", 15),
                                                                           fg="white",
                                                                           bg="black",
                                                                           justify="center", padx=10, pady=10)
                                                genderlabelconfirm.place(relx=0.75, rely=0.6, anchor=CENTER)

                                            def getgen():
                                                if gender == "":
                                                    messagebox.showwarning('Missing information',
                                                                           'Please Select a Gender.')
                                                else:
                                                    def updated1():
                                                        updatedgen.destroy()
                                                        restart()

                                                    genderwin.destroy()
                                                    sql = "UPDATE student_details SET Gender = %s WHERE roll_number = %s"
                                                    values = (gender, rollno)
                                                    cursor.execute(sql, values)
                                                    connector.commit()
                                                    updatedgen = Tk()  # to create win
                                                    updatedgen.configure(bg="black")  # bg colour
                                                    updatedgen.title("Updated Gender")
                                                    updatedgen.geometry("800x600")
                                                    updatedgen.iconbitmap("Reeds.ico")
                                                    screen_width = updatedgen.winfo_screenwidth()
                                                    screen_height = updatedgen.winfo_screenheight()
                                                    bg_image = Image.open("voif.jpg")
                                                    bg_image = bg_image.resize((screen_width, screen_height),
                                                                               Image.BICUBIC)
                                                    background_image = ImageTk.PhotoImage(bg_image)
                                                    canvas1 = Canvas(updatedgen, width=screen_width, height=screen_height)
                                                    canvas1.pack()
                                                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                                    genlabel = Label(updatedgen, text="Updated The Gender",
                                                                     font=("Arial", 30),
                                                                     fg="white", bg="black", justify="center", padx=10,
                                                                     pady=10)
                                                    genlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                                    updatedgenButton = Button(updatedgen, text="Done --→",
                                                                              font=("Arial", 15),
                                                                              fg="white", bg="black", command=updated1,
                                                                              width=10,
                                                                              height=1)
                                                    updatedgenButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                                    updatedgen.mainloop()

                                            choose.destroy()
                                            genderwin = Tk()  # to create win
                                            genderwin.configure(bg="black")  # bg colour
                                            genderwin.title("Gender")
                                            genderwin.geometry("800x600")
                                            genderwin.iconbitmap("Reeds.ico")
                                            screen_width = genderwin.winfo_screenwidth()
                                            screen_height = genderwin.winfo_screenheight()
                                            bg_image = Image.open("voif.jpg")
                                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                            background_image = ImageTk.PhotoImage(bg_image)
                                            canvas1 = Canvas(genderwin, width=screen_width, height=screen_height)
                                            canvas1.pack()
                                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                            sql = "select name from student_details where roll_number=%s"  # display std name
                                            value = (rollno,)
                                            cursor.execute(sql, value)
                                            result = cursor.fetchone()
                                            namelabel1 = Label(genderwin, text="Of " + result[0], font=("Arial", 30),
                                                               fg="white", bg="black", justify="center", padx=10,
                                                               pady=10)
                                            namelabel1.place(relx=0.5, rely=0.5, anchor=CENTER)
                                            namelabel = Label(genderwin, text="Select The Gender", font=("Arial", 30),
                                                              fg="white", bg="black", justify="center", padx=10,
                                                              pady=10)
                                            namelabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                            genderButtonM = Button(genderwin, text="M", font=("Arial", 10), fg="black",
                                                                   bg="white", command=M, width=5, height=1,
                                                                   relief="raised")
                                            genderButtonM.place(relx=0.4, rely=0.6, anchor=CENTER)
                                            genderlabelor = Label(genderwin, text="or", font=("Arial", 10),
                                                                  fg="white", bg="black", justify="center", padx=10,
                                                                  pady=10)
                                            genderlabelor.place(relx=0.5, rely=0.6, anchor=CENTER)
                                            genderButtonF = Button(genderwin, text="F", font=("Arial", 10), fg="black",
                                                                   bg="white", command=F, width=5, height=1,
                                                                   relief="raised")
                                            genderButtonF.place(relx=0.6, rely=0.6, anchor=CENTER)
                                            submitgenderButton = Button(genderwin, text="Submit --→",
                                                                        font=("Arial", 15), fg="white",
                                                                        bg="black", command=getgen, width=10, height=1)
                                            submitgenderButton.place(relx=0.5, rely=0.7, anchor=CENTER)
                                            genderwin.mainloop()

                                        edit.destroy()
                                        choose = Tk()  # to create win
                                        choose.configure(bg="black")  # bg colour
                                        choose.title("Select")
                                        choose.geometry("800x600")
                                        choose.iconbitmap("Reeds.ico")
                                        screen_width = choose.winfo_screenwidth()
                                        screen_height = choose.winfo_screenheight()
                                        bg_image = Image.open("voif.jpg")
                                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                        background_image = ImageTk.PhotoImage(bg_image)
                                        canvas1 = Canvas(choose, width=screen_width, height=screen_height)
                                        canvas1.pack()
                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                        selectlabel = Label(choose, text="What You Want To Edit ", font=("Arial", 30),
                                                            fg="white",
                                                            bg="black", justify="center", padx=10, pady=10)
                                        sql = "select name from student_details where roll_number=%s"  # display std name
                                        value = (rollno,)
                                        cursor.execute(sql, value)
                                        result = cursor.fetchone()
                                        rolllabel1 = Label(choose, text="for " + result[0], font=("Arial", 30),
                                                           fg="white", bg="black", justify="center", padx=10, pady=10)
                                        rolllabel1.place(relx=0.5, rely=0.3, anchor=CENTER)
                                        selectlabel.place(relx=0.5, rely=0.2, anchor=CENTER)
                                        rollnoButton = Button(choose, text="Roll Number --→", font=("Arial", 15),
                                                              fg="white",
                                                              bg="black", command=rollnum, width=20, height=1)
                                        rollnoButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                                        admissionnoButton = Button(choose, text="Admission Number --→",
                                                                   font=("Arial", 15), fg="white",
                                                                   bg="black", command=admission, width=20, height=1)
                                        admissionnoButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                        nameButton = Button(choose, text="Name --→", font=("Arial", 15), fg="white",
                                                            bg="black", command=name, width=20, height=1)
                                        nameButton.place(relx=0.5, rely=0.7, anchor=CENTER)
                                        genderButton = Button(choose, text="Gender --→", font=("Arial", 15), fg="white",
                                                              bg="black", command=genderchange, width=20, height=1)
                                        genderButton.place(relx=0.5, rely=0.8, anchor=CENTER)
                                        choose.mainloop()

                            admenu.destroy()
                            edit = Tk()  # to create win
                            edit.configure(bg="black")  # bg colour
                            edit.title("Edit Student")
                            edit.geometry("800x600")
                            edit.iconbitmap("Reeds.ico")
                            screen_width = edit.winfo_screenwidth()
                            screen_height = edit.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(edit, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            editlabel = Label(edit, text="Enter the Roll Number Of The Student", font=("Arial", 30),
                                              fg="white",
                                              bg="black", justify="center", padx=10, pady=10)
                            editlabel.place(relx=0.5, rely=0.4, anchor=CENTER)

                            enterrollbox = Entry(edit, width=30)
                            enterrollbox.place(relx=0.5, rely=0.5, anchor=CENTER)
                            editButton = Button(edit, text="Confirm --→", font=("Arial", 15), fg="white", bg="black",
                                                command=editfn, width=10, height=1)
                            editButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                            edit.mainloop()
                        def attendance():
                            admenu.destroy()
                            def viewatt():
                                atmenu.destroy()
                                sql = "SELECT * FROM student_details order by roll_number"
                                cursor.execute(sql)
                                rows = cursor.fetchall()
                                table = tabulate(rows, headers=cursor.column_names, tablefmt="grid")

                                def exit_fullscreen():
                                    window.attributes('-fullscreen', False)

                                def close_window():
                                    window.destroy()
                                    restart()
                                window = Tk()
                                window.title("Attendance Table")
                                window.geometry("800x600")
                                window.iconbitmap("Reeds.ico")
                                window.attributes('-fullscreen', True)

                                # Create a button to exit fullscreen
                                exit_button = Button(window, text="Exit Fullscreen", command=exit_fullscreen)
                                exit_button.pack()

                                # Create a button to close the window
                                close_button = Button(window, text="Close", command=close_window)
                                close_button.pack()

                                frame = Frame(window)
                                frame.pack(fill="both", expand=True)

                                canvas = Canvas(frame)
                                canvas.pack(side="left", fill="both", expand=True)

                                # Create a vertical scrollbar
                                scrollbar_y = Scrollbar(frame, command=canvas.yview)
                                scrollbar_y.pack(side="right", fill="y")
                                canvas.configure(yscrollcommand=scrollbar_y.set)

                                # Create a horizontal scrollbar
                                scrollbar_x = Scrollbar(window, orient="horizontal", command=canvas.xview)
                                scrollbar_x.pack(side="bottom", fill="x")
                                canvas.configure(xscrollcommand=scrollbar_x.set)

                                # Create an inner frame and attach it to the canvas
                                frame_inner = Frame(canvas)
                                canvas.create_window((0, 0), window=frame_inner, anchor="nw",
                                                     width=window.winfo_width(), height=window.winfo_height())

                                # Create a text widget
                                text_box = Text(frame_inner, width=80, height=20)
                                text_box.pack(fill="both", expand=True)

                                # Insert table data into the text widget
                                text_box.insert("end", table)

                                # Update the canvas scroll region when the window is resized
                                canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

                                # Configure the frame to prevent unwanted padding
                                frame.grid_propagate(False)
                                frame_inner.grid_propagate(False)

                                # Configure window grid
                                window.grid_rowconfigure(0, weight=1)
                                window.grid_columnconfigure(0, weight=1)

                                # Prevent unwanted padding in the Text widget
                                text_box.config(wrap="none")

                                # Start the Tkinter main loop
                                window.mainloop()

                            def spcatt():
                                atmenu.destroy()
                                def submit():
                                    if enterdaybox.get() == "" or enteryearbox.get() == "" or entermonthbox.get() == "":
                                        messagebox.showwarning('Missing information', 'Please enter the Details.')
                                    else:
                                        day = enterdaybox.get()
                                        month = entermonthbox.get()
                                        year = enteryearbox.get()
                                        date = f"{day}-{month}-{year}"

                                        # Check if the column exists in the table
                                        check_column_query = f"DESCRIBE student_details `{date}`"
                                        cursor.execute(check_column_query)
                                        column_info = cursor.fetchone()
                                        if column_info is not None:
                                            # Column exists, fetch the attendance data
                                            sql = f"SELECT name, roll_number, admission_no, gender, `{date}` FROM student_details"
                                            cursor.execute(sql)
                                            attendance_data = cursor.fetchall()
                                            if len(attendance_data) == 0 or attendance_data[0][-1] is None:
                                                messagebox.showwarning('Not Found',
                                                                       'No attendance was recorded on this day.')
                                            else:
                                                spcatten.destroy()
                                                # Display attendance report in tkinter window
                                                window = Tk()
                                                window.title("Attendance Report")
                                                window.geometry("800x600")
                                                window.iconbitmap("Reeds.ico")
                                                text_box = Text(window, width=80, height=20)
                                                text_box.pack(side="left", fill="both", expand=True)
                                                scrollbar = Scrollbar(window)
                                                scrollbar.pack(side="right", fill="y")
                                                scrollbar.config(command=text_box.yview)
                                                text_box.config(yscrollcommand=scrollbar.set)
                                                table_headers = ["Name", "Roll Number", "Admission Number", "Gender",
                                                                 date]
                                                table_data = [list(row) for row in attendance_data]
                                                table = tabulate(table_data, headers=table_headers, tablefmt="pretty")
                                                text_box.insert("end", table)
                                                window.mainloop()
                                        else:
                                            messagebox.showwarning('Not Found',
                                                                   'No attendance column found for this date.')


                                spcatten = Tk()  # to create win
                                spcatten.configure(bg="black")  # bg colour
                                spcatten.title("Specific Date Attendance")
                                spcatten.geometry("800x600")
                                spcatten.iconbitmap("Reeds.ico")
                                screen_width = spcatten.winfo_screenwidth()
                                screen_height = spcatten.winfo_screenheight()
                                bg_image = Image.open("voif.jpg")
                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                background_image = ImageTk.PhotoImage(bg_image)
                                canvas1 = Canvas(spcatten, width=screen_width, height=screen_height)
                                canvas1.pack()
                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                spcattenlabel = Label(spcatten, text="Enter The Date", font=("Arial", 30), fg="white",
                                                      bg="black",
                                                      justify="center", padx=10, pady=10)
                                spcattenlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                daylabel = Label(spcatten, text="Day(DD)", font=("Arial", 15), fg="white", bg="black",
                                                 justify="center", padx=10, pady=10)
                                daylabel.place(relx=0.3, rely=0.5, anchor=CENTER)
                                monthlabel = Label(spcatten, text="Month(MM)", font=("Arial", 15), fg="white",
                                                   bg="black",
                                                   justify="center", padx=10, pady=10)
                                monthlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                                yearlabel = Label(spcatten, text="Year(YYYY)", font=("Arial", 15), fg="white",
                                                  bg="black",
                                                  justify="center", padx=10, pady=10)
                                yearlabel.place(relx=0.7, rely=0.5, anchor=CENTER)
                                enterdaybox = Entry(spcatten, width=5)
                                enterdaybox.place(relx=0.3, rely=0.6, anchor=CENTER)
                                entermonthbox = Entry(spcatten, width=5)
                                entermonthbox.place(relx=0.5, rely=0.6, anchor=CENTER)
                                enteryearbox = Entry(spcatten, width=6)
                                enteryearbox.place(relx=0.7, rely=0.6, anchor=CENTER)
                                SubmitButton = Button(spcatten, text="Submit --→", font=("Arial", 15), fg="white",
                                                      bg="black",command=submit, width=15, height=1)
                                SubmitButton.place(relx=0.5, rely=0.7, anchor=CENTER)

                                spcatten.mainloop()
                                restart()
                            atmenu = Tk()  # win to enter password
                            atmenu.configure(bg="black")  # bg colour
                            atmenu.title("login")
                            atmenu.geometry("800x600")  # Control
                            atmenu.iconbitmap("Reeds.ico")
                            screen_width = atmenu.winfo_screenwidth()
                            screen_height = atmenu.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(atmenu, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            welcomelabel = Label(atmenu, text="Attendance !!", font=("Arial", 30), fg="white",
                                                 bg="black",justify="center", padx=10, pady=10)
                            welcomelabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                            attButton = Button(atmenu, text="Attendance Record --→", font=("Arial", 15), fg="white",
                                                  bg="black",command=viewatt, width=30, height=1)
                            attButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                            viewButton = Button(atmenu, text="View Specific Date Attendance --→", font=("Arial", 15),
                                                     fg="white",bg="black",command=spcatt, width=30, height=1)
                            viewButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                            atmenu.mainloop()
                        def change():
                            admenu.destroy()
                            def geting():  # win asking password window
                                global pword  # pword user input
                                if enterpasswordbox.get() == "":
                                    messagebox.showwarning('Missing information', 'Please Enter the Password.')
                                else:
                                    pword = enterpasswordbox.get()
                                    passwin.destroy()
                            passwin = Tk()  # win to enter password
                            passwin.configure(bg="black")  # bg colour
                            passwin.title("login")
                            passwin.geometry("800x600")
                            passwin.iconbitmap("Reeds.ico")
                            screen_width = passwin.winfo_screenwidth()
                            screen_height = passwin.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(passwin, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            passwordlabel = Label(passwin, text="Admin! Enter password for Conformation", font=("Arial", 30), fg="white",
                                                  bg="black",justify="center", padx=10, pady=10)
                            passwordlabel.place(relx=0.5, rely=0.4, anchor=CENTER)  # password using place
                            enterpasswordbox = Entry(passwin, show="*", width=30)  # Entrty box to ask password
                            enterpasswordbox.place(relx=0.5, rely=0.5, anchor=CENTER)
                            loginpasswordButton = Button(passwin, text="login", font=("Arial", 15), fg="white",
                                                         bg="black",
                                                         command=geting, width=6, height=1)
                            loginpasswordButton.place(relx=0.5, rely=0.6, anchor=CENTER)  # login password button
                            passwin.mainloop()
                            cursor.execute("select password from password where designation='admin'")
                            passadmin = cursor.fetchone()[0]
                            if pword == '':
                                messagebox.showwarning('Missing information', 'Please Enter the Password.')
                            else:
                                if passadmin == pword:
                                    def adm():
                                        def confirm():
                                            np=enterpasswordbox.get()
                                            if np =='':
                                                messagebox.showwarning('Missing information',
                                                                       'Please Enter the Password.')
                                            else:
                                                def ok():
                                                    confermenu.destroy()
                                                    def chumma():   # Tamilan da
                                                        conmenu.destroy()
                                                    sql="UPDATE password SET password = %s WHERE designation = 'admin'"
                                                    update_values = (np,)
                                                    cursor.execute(sql, update_values)
                                                    connector.commit()
                                                    conmenu = Tk()  # win to enter password
                                                    conmenu.configure(bg="black")  # bg colour
                                                    conmenu.title("login")
                                                    conmenu.geometry("800x600")
                                                    conmenu.iconbitmap("Reeds.ico")
                                                    screen_width = conmenu.winfo_screenwidth()
                                                    screen_height = conmenu.winfo_screenheight()
                                                    bg_image = Image.open("voif.jpg")
                                                    bg_image = bg_image.resize((screen_width, screen_height),
                                                                               Image.BICUBIC)
                                                    background_image = ImageTk.PhotoImage(bg_image)
                                                    canvas1 = Canvas(conmenu, width=screen_width, height=screen_height)
                                                    canvas1.pack()
                                                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                                    welcomelabel = Label(conmenu, text="Password Changed Successfully",
                                                                         font=("Arial", 30),fg="white", bg="black", justify="center", padx=10,
                                                                         pady=10)
                                                    welcomelabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                                    loginpasswordButton = Button(conmenu, text="Done --→", font=("Arial", 15),
                                                                                 fg="white", bg="black",
                                                                                 command=chumma, width=15, height=1)
                                                    loginpasswordButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                                                    conmenu.mainloop()
                                                pmenu.destroy()
                                                confermenu = Tk()  # win to enter password
                                                confermenu.configure(bg="black")  # bg colour
                                                confermenu.title("login")
                                                confermenu.geometry("800x600")
                                                confermenu.iconbitmap("Reeds.ico")
                                                screen_width = confermenu.winfo_screenwidth()
                                                screen_height = confermenu.winfo_screenheight()
                                                bg_image = Image.open("voif.jpg")
                                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                                background_image = ImageTk.PhotoImage(bg_image)
                                                canvas1 = Canvas(confermenu, width=screen_width, height=screen_height)
                                                canvas1.pack()
                                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                                welcomelabel = Label(confermenu, text="Confirm Password",
                                                                     font=("Arial", 30), fg="white", bg="black",
                                                                     justify="center", padx=10,
                                                                     pady=10)
                                                welcomelabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                                loginpasswordButton = Button(confermenu, text="Confirm --→",
                                                                             font=("Arial", 15),
                                                                             fg="white", bg="black",
                                                                             command=ok, width=15, height=1)
                                                loginpasswordButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                                                confermenu.mainloop()
                                        cmenu.destroy()
                                        pmenu = Tk()  # win to enter password
                                        pmenu.configure(bg="black")  # bg colour
                                        pmenu.title("login")
                                        pmenu.geometry("800x600")
                                        pmenu.iconbitmap("Reeds.ico")
                                        screen_width = pmenu.winfo_screenwidth()
                                        screen_height = pmenu.winfo_screenheight()
                                        bg_image = Image.open("voif.jpg")
                                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                        background_image = ImageTk.PhotoImage(bg_image)
                                        canvas1 = Canvas(pmenu, width=screen_width, height=screen_height)
                                        canvas1.pack()
                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                        welcomelabel = Label(pmenu, text="Set Your New Password", font=("Arial", 30),
                                                             fg="white",bg="black", justify="center", padx=10, pady=10)
                                        welcomelabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                        enterpasswordbox = Entry(pmenu, width=30)
                                        enterpasswordbox.place(relx=0.5, rely=0.5, anchor=CENTER)
                                        loginpasswordButton = Button(pmenu, text="Continue --→", font=("Arial", 15),fg="white", bg="black",
                                                                     command=confirm, width=15,height=1)
                                        loginpasswordButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                        pmenu.mainloop()
                                    def ct():
                                        def confirm():
                                            np=enterpasswordbox.get()
                                            if np =='':
                                                messagebox.showwarning('Missing information',
                                                                       'Please Enter the Password.')
                                            else:
                                                def ok():
                                                    confermenu.destroy()
                                                    def chumma():   # Tamilan da
                                                        conmenu.destroy()
                                                    sql="UPDATE password SET password = %s WHERE designation = 'Class Teacher'"
                                                    update_values = (np,)
                                                    cursor.execute(sql, update_values)
                                                    connector.commit()
                                                    conmenu = Tk()  # win to enter password
                                                    conmenu.configure(bg="black")  # bg colour
                                                    conmenu.title("login")
                                                    conmenu.geometry("800x600")
                                                    conmenu.iconbitmap("Reeds.ico")
                                                    screen_width = conmenu.winfo_screenwidth()
                                                    screen_height = conmenu.winfo_screenheight()
                                                    bg_image = Image.open("voif.jpg")
                                                    bg_image = bg_image.resize((screen_width, screen_height),
                                                                               Image.BICUBIC)
                                                    background_image = ImageTk.PhotoImage(bg_image)
                                                    canvas1 = Canvas(conmenu, width=screen_width, height=screen_height)
                                                    canvas1.pack()
                                                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                                    welcomelabel = Label(conmenu, text="Password Changed Successfully",
                                                                         font=("Arial", 30),fg="white", bg="black", justify="center", padx=10,
                                                                         pady=10)
                                                    welcomelabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                                    loginpasswordButton = Button(conmenu, text="Done --→", font=("Arial", 15),
                                                                                 fg="white", bg="black",
                                                                                 command=chumma, width=15, height=1)
                                                    loginpasswordButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                                                    conmenu.mainloop()
                                                pmenu.destroy()
                                                confermenu = Tk()  # win to enter password
                                                confermenu.configure(bg="black")  # bg colour
                                                confermenu.title("login")
                                                confermenu.geometry("800x600")
                                                confermenu.iconbitmap("Reeds.ico")
                                                screen_width = confermenu.winfo_screenwidth()
                                                screen_height = confermenu.winfo_screenheight()
                                                bg_image = Image.open("voif.jpg")
                                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                                background_image = ImageTk.PhotoImage(bg_image)
                                                canvas1 = Canvas(confermenu, width=screen_width, height=screen_height)
                                                canvas1.pack()
                                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                                welcomelabel = Label(confermenu, text="Confirm Password",
                                                                     font=("Arial", 30), fg="white", bg="black",
                                                                     justify="center", padx=10,
                                                                     pady=10)
                                                welcomelabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                                loginpasswordButton = Button(confermenu, text="Confirm --→",
                                                                             font=("Arial", 15),
                                                                             fg="white", bg="black",
                                                                             command=ok, width=15, height=1)
                                                loginpasswordButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                                                confermenu.mainloop()
                                        cmenu.destroy()
                                        pmenu = Tk()  # win to enter password
                                        pmenu.configure(bg="black")  # bg colour
                                        pmenu.title("login")
                                        pmenu.geometry("800x600")
                                        pmenu.iconbitmap("Reeds.ico")
                                        screen_width = pmenu.winfo_screenwidth()
                                        screen_height = pmenu.winfo_screenheight()
                                        bg_image = Image.open("voif.jpg")
                                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                        background_image = ImageTk.PhotoImage(bg_image)
                                        canvas1 = Canvas(pmenu, width=screen_width, height=screen_height)
                                        canvas1.pack()
                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                        welcomelabel = Label(pmenu, text="Set A New Password For", font=("Arial", 30),
                                                             fg="white",bg="black", justify="center", padx=10, pady=10)
                                        welcomelabel.place(relx=0.5, rely=0.3, anchor=CENTER)
                                        welcome1label = Label(pmenu, text="The Class Teacher", font=("Arial", 30),
                                                             fg="white", bg="black", justify="center", padx=10, pady=10)
                                        welcome1label.place(relx=0.5, rely=0.4, anchor=CENTER)
                                        enterpasswordbox = Entry(pmenu, width=30)
                                        enterpasswordbox.place(relx=0.5, rely=0.5, anchor=CENTER)
                                        loginpasswordButton = Button(pmenu, text="Continue --→", font=("Arial", 15),fg="white", bg="black",
                                                                     command=confirm, width=15,height=1)
                                        loginpasswordButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                        pmenu.mainloop()
                                    cmenu = Tk()  # win to enter password
                                    cmenu.configure(bg="black")  # bg colour
                                    cmenu.title("login")
                                    cmenu.geometry("800x600")
                                    cmenu.iconbitmap("Reeds.ico")
                                    screen_width = cmenu.winfo_screenwidth()
                                    screen_height = (cmenu.winfo_screenheight())
                                    bg_image = Image.open("voif.jpg")
                                    bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                    background_image = ImageTk.PhotoImage(bg_image)
                                    canvas1 = Canvas(cmenu, width=screen_width, height=screen_height)
                                    canvas1.pack()
                                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                    welcomelabel = Label(cmenu, text="Change Password For !!", font=("Arial", 30), fg="white",
                                                         bg="black",justify="center", padx=10, pady=10)
                                    welcomelabel.place(relx=0.5, rely=0.3, anchor=CENTER)
                                    addstuButton = Button(cmenu, text="Admin --→", font=("Arial", 15),
                                                          fg="white",bg="black",command=adm, width=30, height=1)
                                    addstuButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                                    removestuButton = Button(cmenu, text="Class Teacher --→", font=("Arial", 15),
                                                             fg="white",bg="black",command=ct, width=30, height=1)
                                    removestuButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                    cmenu.mainloop()
                                else:
                                    messagebox.showwarning('Password Incorrect',
                                                           'Incorrect Password.')
                            restart()
                        admenu = Tk()                 # win to enter password
                        admenu.configure(bg="black")  # bg colour
                        admenu.title("login")
                        admenu.geometry("800x600")
                        admenu.iconbitmap("Reeds.ico")
                        screen_width = admenu.winfo_screenwidth()
                        screen_height = admenu.winfo_screenheight()
                        bg_image = Image.open("voif.jpg")
                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                        background_image = ImageTk.PhotoImage(bg_image)
                        canvas1 = Canvas(admenu, width=screen_width, height=screen_height)
                        canvas1.pack()
                        canvas1.create_image(0, 0, anchor=NW, image=background_image)                        #Control
                        welcomelabel = Label(admenu, text="Welcome Back !!", font=("Arial", 30), fg="white", bg="black",
                                         justify="center", padx=10, pady=10)
                        welcomelabel.place(relx=0.5, rely=0.2, anchor=CENTER)
                        addstuButton = Button(admenu, text="Add a Student --→", font=("Arial", 15), fg="white",
                                          bg="black",
                                          command=addstudent, width=30, height=1)
                        addstuButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                        removestuButton = Button(admenu, text="Remove a Student --→", font=("Arial", 15), fg="white",
                                             bg="black",
                                             command=removestudent, width=30, height=1)
                        removestuButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                        Editstubutton = Button(admenu, text="Edit Student Detail --→", font=("Arial", 15), fg="white",
                                           bg="black",
                                           command=edit, width=30, height=1)
                        Editstubutton.place(relx=0.5, rely=0.7, anchor=CENTER)
                        AttendanceButton = Button(admenu, text="Attendance Record --→", font=("Arial", 15), fg="white",
                                              bg="black",command=attendance, width=30, height=1)
                        AttendanceButton.place(relx=0.5, rely=0.4, anchor=CENTER)
                        summarybutton = Button(admenu, text="Summary --→", font=("Arial", 15), fg="white", bg="black",
                                           command=summary, width=30, height=1)
                        summarybutton.place(relx=0.5, rely=0.8, anchor=CENTER)
                        changebutton = Button(admenu, text="Change Password --→", font=("Arial", 15), fg="white", bg="black",
                                               command=change, width=30, height=1)
                        changebutton.place(relx=0.5, rely=0.9, anchor=CENTER)
                        admenu.mainloop()
                    restart()
                else:
                    messagebox.showwarning('Password Incorrect', 'Incorrect Password Restart The program.')
        def classt():
            welcome.destroy()
            def geting():  # win asking password window
                global pword  # pword user input
                if enterpasswordbox.get() == "":
                    messagebox.showwarning('Missing information', 'Please Enter the Password.')
                else:
                    pword = enterpasswordbox.get()
                    passwin.destroy()
            passwin = Tk()  # win to enter password
            passwin.configure(bg="black")  # bg colour
            passwin.title("login")
            passwin.geometry("800x600")
            passwin.iconbitmap("Reeds.ico")
            screen_width = passwin.winfo_screenwidth()
            screen_height = passwin.winfo_screenheight()
            bg_image = Image.open("voif.jpg")
            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
            background_image = ImageTk.PhotoImage(bg_image)
            canvas1 = Canvas(passwin, width=screen_width, height=screen_height)
            canvas1.pack()
            canvas1.create_image(0, 0, anchor=NW, image=background_image)
            passwordlabel = Label(passwin, text="Enter password", font=("Arial", 30), fg="white", bg="black",
                                  justify="center", padx=10, pady=10)
            passwordlabel.place(relx=0.5, rely=0.4, anchor=CENTER)  # password using place
            enterpasswordbox = Entry(passwin, show="*", width=30)  # Entrty box to ask password
            enterpasswordbox.place(relx=0.5, rely=0.5, anchor=CENTER)
            loginpasswordButton = Button(passwin, text="login", font=("Arial", 15), fg="white", bg="black",
                                         command=geting, width=6, height=1)
            loginpasswordButton.place(relx=0.5, rely=0.6,anchor=CENTER)  # login password button
            passwin.mainloop()
            cursor.execute("select password from password where designation='Class Teacher'")
            passadmin=cursor.fetchone()[0]
            if pword=='':
                messagebox.showwarning('Missing information', 'Please Enter the Password.')
            else:
                if passadmin == pword:
                    def restart():              #Control
                        def attendance():
                            ctmenu.destroy()
                            def editatt():
                                def newatt():
                                    roll = enterrollbox.get()
                                    sql = "select name from student_details where roll_number=%s"
                                    value = (roll,)
                                    cursor.execute(sql, value)
                                    result = cursor.fetchall()
                                    if roll == "":
                                        messagebox.showwarning('Missing information', 'Please enter the Roll Number.')
                                    elif not result:
                                        messagebox.showwarning('Not Found',
                                                               'Student with rool number ' + roll + " Not Found")
                                    else:
                                        status = ""
                                        editatt.destroy()

                                        def present():
                                            nonlocal status
                                            status = "P"
                                            text = "selected Present (P)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def absent():
                                            nonlocal status
                                            status = "A"
                                            text = "selected Absent (A)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def fp():
                                            nonlocal status
                                            status = "FP"
                                            text = "selected forenoon (FP)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def ap():
                                            nonlocal status
                                            status = "AP"
                                            text = "selected afternoon (AP)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def od():
                                            nonlocal status
                                            status = "OD"
                                            text = "selected on duty (OD)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def end():
                                            if status == "":
                                                messagebox.showwarning('Missing information',
                                                                       'Select a Attendance Report.')
                                            else:
                                                takeatt.destroy()
                                                insert_query = "UPDATE student_details SET `{}` = %s WHERE name = %s".format(
                                                    today)
                                                values = (status, result[0][0])
                                                cursor.execute(insert_query, values)
                                                connector.commit()

                                        takeatt = Tk()  # to create win
                                        takeatt.configure(bg="black")  # bg colour
                                        takeatt.title("New Attendance")
                                        takeatt.geometry("800x600")
                                        takeatt.iconbitmap("Reeds.ico")
                                        screen_width = takeatt.winfo_screenwidth()
                                        screen_height = takeatt.winfo_screenheight()
                                        bg_image = Image.open("voif.jpg")
                                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                        background_image = ImageTk.PhotoImage(bg_image)
                                        canvas1 = Canvas(takeatt, width=screen_width, height=screen_height)
                                        canvas1.pack()
                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                        stuattlabel = Label(takeatt, text="Student " + result[0][0],
                                                            font=("Arial", 30), fg="white", bg="black",
                                                            justify="center", padx=10, pady=10)
                                        stuattlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                        presentButton = Button(takeatt, text="Present", font=("Arial", 15), fg="white",
                                                               bg="black",
                                                               command=present, width=10, height=1)
                                        presentButton.place(relx=0.4, rely=0.5, anchor=CENTER)
                                        orlabel = Label(takeatt, text=",", font=("Arial", 30), fg="white", bg="black",
                                                        justify="center", padx=10, pady=10)
                                        orlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                                        absentButton = Button(takeatt, text="Absent", font=("Arial", 15), fg="white",
                                                              bg="black",
                                                              command=absent, width=10, height=1)
                                        absentButton.place(relx=0.6, rely=0.5, anchor=CENTER)
                                        orlabel3 = Label(takeatt, text=",", font=("Arial", 30), fg="white", bg="black",
                                                         justify="center", padx=10, pady=10)
                                        orlabel3.place(relx=0.7, rely=0.5, anchor=CENTER)
                                        ForeButton = Button(takeatt, text="ForeNoon", font=("Arial", 15), fg="white",
                                                            bg="black",
                                                            command=fp, width=10, height=1)
                                        ForeButton.place(relx=0.4, rely=0.6, anchor=CENTER)
                                        orlabel2 = Label(takeatt, text=",", font=("Arial", 30), fg="white", bg="black",
                                                         justify="center", padx=10, pady=10)
                                        orlabel2.place(relx=0.5, rely=0.6, anchor=CENTER)
                                        AfterButton = Button(takeatt, text="AfterNoon", font=("Arial", 15), fg="white",
                                                             bg="black",
                                                             command=ap, width=10, height=1)
                                        AfterButton.place(relx=0.6, rely=0.6, anchor=CENTER)
                                        orlabel4 = Label(takeatt, text=",", font=("Arial", 30), fg="white", bg="black",
                                                         justify="center", padx=10, pady=10)
                                        orlabel4.place(relx=0.7, rely=0.6, anchor=CENTER)
                                        odButton = Button(takeatt, text="On Duty", font=("Arial", 15), fg="white",
                                                          bg="black",
                                                          command=od, width=10, height=1)
                                        odButton.place(relx=0.4, rely=0.7, anchor=CENTER)
                                        nextstuButton = Button(takeatt, text="Done --→", font=("Arial", 15),
                                                               fg="white",
                                                               bg="black",
                                                               command=end, width=20, height=1)
                                        nextstuButton.place(relx=0.5, rely=0.8, anchor=CENTER)
                                        takeatt.mainloop()

                                atmenu.destroy()
                                today = date.today().strftime("%d-%m-%Y")
                                editatt = Tk()  # to create win
                                editatt.configure(bg="black")  # bg colour
                                editatt.title("Edit Attendance")
                                editatt.geometry("800x600")
                                editatt.iconbitmap("Reeds.ico")
                                screen_width = editatt.winfo_screenwidth()
                                screen_height = editatt.winfo_screenheight()
                                bg_image = Image.open("voif.jpg")
                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                background_image = ImageTk.PhotoImage(bg_image)
                                canvas1 = Canvas(editatt, width=screen_width, height=screen_height)
                                canvas1.pack()
                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                enterrolllabel = Label(editatt, text="Enter The roll number of the student",
                                                       font=("Arial", 30), fg="white", bg="black",
                                                       justify="center", padx=10, pady=10)
                                enterrolllabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                enterrollbox = Entry(editatt, width=30)
                                enterrollbox.place(relx=0.5, rely=0.5, anchor=CENTER)
                                rollButton = Button(editatt, text="Submit --→", font=("Arial", 15), fg="white",
                                                    bg="black",
                                                    command=newatt, width=15, height=1)
                                rollButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                editatt.mainloop()
                                restart()
                            def takeatt():
                                sql = "select name from student_details"
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                loopend = len(result)
                                loopstart = 0
                                today = date.today().strftime("%d-%m-%Y")

                                check_column_query = f"SHOW COLUMNS FROM student_details LIKE '{today}'"
                                cursor.execute(check_column_query)
                                existing_columns = [column[0] for column in cursor.fetchall()]

                                column_exists = today in existing_columns
                                if column_exists:
                                    messagebox.showinfo('Attendance Taken',
                                                        'Attendance has already been taken for today To change go to edit attendance opction.')
                                    atmenu.destroy()
                                else:
                                    atmenu.destroy()
                                    alter_table_query = "ALTER TABLE student_details ADD COLUMN `{}` VARCHAR(10) DEFAULT 'Newbie'".format(
                                        today)
                                    cursor.execute(alter_table_query)

                                    while loopstart < loopend:
                                        status = ""

                                        def present():
                                            nonlocal status
                                            status = "P"
                                            text = "selected Present (P)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def absent():
                                            nonlocal status
                                            status = "A"
                                            text = "selected Absent (A)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def fp():
                                            nonlocal status
                                            status = "FP"
                                            text = "selected forenoon (FP)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def ap():
                                            nonlocal status
                                            status = "AP"
                                            text = "selected afternoon (AP)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def od():
                                            nonlocal status
                                            status = "OD"
                                            text = "selected on duty (OD)"
                                            attlabelconfirm = Label(takeatt, text=text, font=("Arial", 15), fg="white",
                                                                    bg="black",
                                                                    justify="center", padx=10, pady=10)
                                            attlabelconfirm.place(relx=0.68, rely=0.7, anchor=CENTER)

                                        def end():
                                            if status == "":
                                                messagebox.showwarning('Missing information',
                                                                       'Select a Attendance Report.')
                                            else:
                                                takeatt.destroy()
                                                insert_query = "UPDATE student_details SET `{}` = %s WHERE name = %s".format(
                                                    today)
                                                values = (status, result[loopstart][0])
                                                cursor.execute(insert_query, values)
                                                connector.commit()

                                        takeatt = Tk()  # to create win
                                        takeatt.configure(bg="black")  # bg colour
                                        takeatt.title("login")
                                        takeatt.geometry("800x600")
                                        takeatt.iconbitmap("Reeds.ico")
                                        screen_width = takeatt.winfo_screenwidth()
                                        screen_height = takeatt.winfo_screenheight()
                                        bg_image = Image.open("voif.jpg")
                                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                        background_image = ImageTk.PhotoImage(bg_image)
                                        canvas1 = Canvas(takeatt, width=screen_width, height=screen_height)
                                        canvas1.pack()
                                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                        stuattlabel = Label(takeatt, text="Student " + str(result[loopstart][0]),
                                                            font=("Arial", 30), fg="white", bg="black",
                                                            justify="center", padx=10, pady=10)
                                        stuattlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                        presentButton = Button(takeatt, text="Present", font=("Arial", 15), fg="white",
                                                               bg="black",
                                                               command=present, width=10, height=1)
                                        presentButton.place(relx=0.4, rely=0.5, anchor=CENTER)
                                        orlabel = Label(takeatt, text=",", font=("Arial", 30), fg="white", bg="black",
                                                        justify="center", padx=10, pady=10)
                                        orlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                                        absentButton = Button(takeatt, text="Absent", font=("Arial", 15), fg="white",
                                                              bg="black",
                                                              command=absent, width=10, height=1)
                                        absentButton.place(relx=0.6, rely=0.5, anchor=CENTER)
                                        orlabel3 = Label(takeatt, text=",", font=("Arial", 30), fg="white", bg="black",
                                                         justify="center", padx=10, pady=10)
                                        orlabel3.place(relx=0.7, rely=0.5, anchor=CENTER)
                                        ForeButton = Button(takeatt, text="ForeNoon", font=("Arial", 15), fg="white",
                                                            bg="black",
                                                            command=fp, width=10, height=1)
                                        ForeButton.place(relx=0.4, rely=0.6, anchor=CENTER)
                                        orlabel2 = Label(takeatt, text=",", font=("Arial", 30), fg="white", bg="black",
                                                         justify="center", padx=10, pady=10)
                                        orlabel2.place(relx=0.5, rely=0.6, anchor=CENTER)
                                        AfterButton = Button(takeatt, text="AfterNoon", font=("Arial", 15), fg="white",
                                                             bg="black",
                                                             command=ap, width=10, height=1)
                                        AfterButton.place(relx=0.6, rely=0.6, anchor=CENTER)
                                        orlabel4 = Label(takeatt, text=",", font=("Arial", 30), fg="white", bg="black",
                                                         justify="center", padx=10, pady=10)
                                        orlabel4.place(relx=0.7, rely=0.6, anchor=CENTER)
                                        odButton = Button(takeatt, text="On Duty", font=("Arial", 15), fg="white",
                                                          bg="black",
                                                          command=od, width=10, height=1)
                                        odButton.place(relx=0.4, rely=0.7, anchor=CENTER)
                                        nextstuButton = Button(takeatt, text="Next Student --→", font=("Arial", 15),
                                                               fg="white", bg="black",
                                                               command=end, width=20, height=1)
                                        nextstuButton.place(relx=0.5, rely=0.8, anchor=CENTER)
                                        takeatt.mainloop()
                                        loopstart += 1
                                restart()
                            def viewatt():
                                atmenu.destroy()
                                sql = "SELECT * FROM student_details order by roll_number"
                                cursor.execute(sql)
                                rows = cursor.fetchall()
                                table = tabulate(rows, headers=cursor.column_names, tablefmt="grid")

                                def exit_fullscreen():
                                    window.attributes('-fullscreen', False)

                                def close_window():
                                    window.destroy()
                                    restart()

                                window = Tk()
                                window.title("Attendance Table")
                                window.geometry("800x600")
                                window.iconbitmap("Reeds.ico")
                                window.attributes('-fullscreen', True)

                                # Create a button to exit fullscreen
                                exit_button = Button(window, text="Exit Fullscreen", command=exit_fullscreen)
                                exit_button.pack()

                                # Create a button to close the window
                                close_button = Button(window, text="Close", command=close_window)
                                close_button.pack()

                                frame = Frame(window)
                                frame.pack(fill="both", expand=True)

                                canvas = Canvas(frame)
                                canvas.pack(side="left", fill="both", expand=True)

                                # Create a vertical scrollbar
                                scrollbar_y = Scrollbar(frame, command=canvas.yview)
                                scrollbar_y.pack(side="right", fill="y")
                                canvas.configure(yscrollcommand=scrollbar_y.set)

                                # Create a horizontal scrollbar
                                scrollbar_x = Scrollbar(window, orient="horizontal", command=canvas.xview)
                                scrollbar_x.pack(side="bottom", fill="x")
                                canvas.configure(xscrollcommand=scrollbar_x.set)

                                # Create an inner frame and attach it to the canvas
                                frame_inner = Frame(canvas)
                                canvas.create_window((0, 0), window=frame_inner, anchor="nw",
                                                     width=window.winfo_width(), height=window.winfo_height())

                                # Create a text widget
                                text_box = Text(frame_inner, width=80, height=20)
                                text_box.pack(fill="both", expand=True)

                                # Insert table data into the text widget
                                text_box.insert("end", table)

                                # Update the canvas scroll region when the window is resized
                                canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

                                # Configure the frame to prevent unwanted padding
                                frame.grid_propagate(False)
                                frame_inner.grid_propagate(False)

                                # Configure window grid
                                window.grid_rowconfigure(0, weight=1)
                                window.grid_columnconfigure(0, weight=1)

                                # Prevent unwanted padding in the Text widget
                                text_box.config(wrap="none")

                                # Start the Tkinter main loop
                                window.mainloop()
                            def spcatt():
                                atmenu.destroy()
                                def submit():
                                    if enterdaybox.get() == "" or enteryearbox.get() == "" or entermonthbox.get() == "":
                                        messagebox.showwarning('Missing information', 'Please enter the Details.')
                                    else:
                                        day = enterdaybox.get()
                                        month = entermonthbox.get()
                                        year = enteryearbox.get()
                                        date = f"{day}-{month}-{year}"

                                        # Check if the column exists in the table
                                        check_column_query = f"DESCRIBE student_details `{date}`"
                                        cursor.execute(check_column_query)
                                        column_info = cursor.fetchone()
                                        if column_info is not None:
                                            # Column exists, fetch the attendance data
                                            sql = f"SELECT name, roll_number, admission_no, gender, `{date}` FROM student_details"
                                            cursor.execute(sql)
                                            attendance_data = cursor.fetchall()
                                            if len(attendance_data) == 0 or attendance_data[0][-1] is None:
                                                messagebox.showwarning('Not Found',
                                                                       'No attendance was recorded on this day.')
                                            else:
                                                spcatten.destroy()
                                                # Display attendance report in tkinter window
                                                window = Tk()
                                                window.title("Attendance Report")
                                                window.geometry("800x600")
                                                window.iconbitmap("Reeds.ico")
                                                text_box = Text(window, width=80, height=20)
                                                text_box.pack(side="left", fill="both", expand=True)
                                                scrollbar = Scrollbar(window)
                                                scrollbar.pack(side="right", fill="y")
                                                scrollbar.config(command=text_box.yview)
                                                text_box.config(yscrollcommand=scrollbar.set)
                                                table_headers = ["Name", "Roll Number", "Admission Number", "Gender",
                                                                 date]
                                                table_data = [list(row) for row in attendance_data]
                                                table = tabulate(table_data, headers=table_headers, tablefmt="pretty")
                                                text_box.insert("end", table)
                                                window.mainloop()
                                        else:
                                            messagebox.showwarning('Not Found',
                                                                   'No attendance column found for this date.')


                                spcatten = Tk()  # to create win
                                spcatten.configure(bg="black")  # bg colour
                                spcatten.title("Specific Date Attendance")
                                spcatten.geometry("800x600")
                                spcatten.iconbitmap("Reeds.ico")
                                screen_width = spcatten.winfo_screenwidth()
                                screen_height = spcatten.winfo_screenheight()
                                bg_image = Image.open("voif.jpg")
                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                background_image = ImageTk.PhotoImage(bg_image)
                                canvas1 = Canvas(spcatten, width=screen_width, height=screen_height)
                                canvas1.pack()
                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                spcattenlabel = Label(spcatten, text="Enter The Date", font=("Arial", 30), fg="white",
                                                      bg="black",
                                                      justify="center", padx=10, pady=10)
                                spcattenlabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                                daylabel = Label(spcatten, text="Day(DD)", font=("Arial", 15), fg="white", bg="black",
                                                 justify="center", padx=10, pady=10)
                                daylabel.place(relx=0.3, rely=0.5, anchor=CENTER)
                                monthlabel = Label(spcatten, text="Month(MM)", font=("Arial", 15), fg="white",
                                                   bg="black",
                                                   justify="center", padx=10, pady=10)
                                monthlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                                yearlabel = Label(spcatten, text="Year(YYYY)", font=("Arial", 15), fg="white",
                                                  bg="black",
                                                  justify="center", padx=10, pady=10)
                                yearlabel.place(relx=0.7, rely=0.5, anchor=CENTER)
                                enterdaybox = Entry(spcatten, width=5)
                                enterdaybox.place(relx=0.3, rely=0.6, anchor=CENTER)
                                entermonthbox = Entry(spcatten, width=5)
                                entermonthbox.place(relx=0.5, rely=0.6, anchor=CENTER)
                                enteryearbox = Entry(spcatten, width=6)
                                enteryearbox.place(relx=0.7, rely=0.6, anchor=CENTER)
                                SubmitButton = Button(spcatten, text="Submit --→", font=("Arial", 15), fg="white",
                                                      bg="black",command=submit, width=15, height=1)
                                SubmitButton.place(relx=0.5, rely=0.7, anchor=CENTER)

                                spcatten.mainloop()
                                restart()
                            atmenu = Tk()  # win to enter password
                            atmenu.configure(bg="black")  # bg colour
                            atmenu.title("login")
                            atmenu.geometry("800x600")  # Control
                            atmenu.iconbitmap("Reeds.ico")
                            screen_width = atmenu.winfo_screenwidth()
                            screen_height = atmenu.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(atmenu, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            welcomelabel = Label(atmenu, text="Attendance !!", font=("Arial", 30), fg="white",
                                                 bg="black",justify="center", padx=10, pady=10)
                            welcomelabel.place(relx=0.5, rely=0.3, anchor=CENTER)
                            tattButton = Button(atmenu, text="Take Attendance --→", font=("Arial", 15), fg="white",
                                                bg="black", command=takeatt, width=30, height=1)
                            tattButton.place(relx=0.5, rely=0.4, anchor=CENTER)
                            eattButton = Button(atmenu, text="Edit Attendance --→", font=("Arial", 15), fg="white",
                                                bg="black", command=editatt, width=30, height=1)
                            eattButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                            attButton = Button(atmenu, text="View Attendance --→", font=("Arial", 15), fg="white",
                                                  bg="black",command=viewatt, width=30, height=1)
                            attButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                            viewButton = Button(atmenu, text="View Specific Date Attendance --→", font=("Arial", 15),
                                                     fg="white",bg="black",command=spcatt, width=30, height=1)
                            viewButton.place(relx=0.5, rely=0.7, anchor=CENTER)
                            atmenu.mainloop()
                        def summary():
                            def yearsumm():
                                summary.destroy()
                                date_column_query = """
                                                                        SELECT COLUMN_NAME 
                                                                        FROM INFORMATION_SCHEMA.COLUMNS 
                                                                        WHERE TABLE_NAME = 'student_details' 
                                                                        AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                    """
                                cursor.execute(date_column_query)
                                date_columns = [column[0] for column in cursor.fetchall()]

                                # Prepare a dictionary to store student details and attendance counts
                                student_details = {}

                                # Query to fetch student details and attendance for each date column
                                for date_column in date_columns:
                                    # Use backticks to reference the date columns
                                    query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A')"
                                    cursor.execute(query)
                                    attendance_data = cursor.fetchall()

                                    for row in attendance_data:
                                        admission_no, roll_number, name, gender, attendance_value = row

                                        if name not in student_details:
                                            student_details[name] = {'Admission No': admission_no,
                                                                     'Roll No': roll_number, 'Gender': gender,
                                                                     'Present': 0, 'Absent': 0}

                                        if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                            student_details[name]['Present'] += 1
                                        elif attendance_value == 'A':
                                            student_details[name]['Absent'] += 1
                                # Sort the student details by the number of days present in descending order
                                sorted_student_details = sorted(student_details.items(), key=lambda x: x[1]['Present'],
                                                                reverse=True)

                                # Prepare data for tabulate
                                table_data = []
                                for name, details in sorted_student_details:
                                    table_data.append(
                                        [details['Admission No'], details['Roll No'], details['Gender'], name,
                                         details['Present'], details['Absent']])

                                # Create a Tkinter window
                                root = Tk()
                                root.title("Attendance Summary")
                                root.geometry("800x600")
                                root.iconbitmap("Reeds.ico")

                                # Create a canvas with a vertical scrollbar
                                canvas = Canvas(root)
                                canvas.pack(side="left", fill="both", expand=True)

                                # Create a vertical scrollbar
                                scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                scrollbar.pack(side="right", fill="y")

                                canvas.configure(yscrollcommand=scrollbar.set)

                                # Convert tabulated data to a string with visually formatted table using "pretty" format
                                headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present', 'Days Absent']
                                attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                # Create a label to display the tabulated attendance summary inside the canvas
                                label = Label(canvas, text=attendance_table, justify="left", font=("Courier", 10))
                                canvas.create_window((0, 0), window=label, anchor="nw")

                                # Configure canvas scrolling region
                                canvas.config(scrollregion=canvas.bbox("all"))

                                # Start the Tkinter main loop
                                root.mainloop()

                            def monthsumm():
                                summary.destroy()
                                def Jan():
                                    month.destroy()
                                    monthn = 1
                                    date_column_query = """
                                                                                SELECT COLUMN_NAME 
                                                                                FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                WHERE TABLE_NAME = 'student_details' 
                                                                                AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                            """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Feb():
                                    month.destroy()
                                    monthn = 2
                                    date_column_query = """
                                                            SELECT COLUMN_NAME 
                                                            FROM INFORMATION_SCHEMA.COLUMNS 
                                                            WHERE TABLE_NAME = 'student_details' 
                                                            AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Mar():
                                    month.destroy()
                                    monthn = 3
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Apr():
                                    month.destroy()
                                    monthn = 4
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def May():
                                    month.destroy()
                                    monthn = 5
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Jun():
                                    month.destroy()
                                    monthn = 6
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Jul():
                                    month.destroy()
                                    monthn = 7
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Aug():
                                    month.destroy()
                                    monthn = 8
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Sep():
                                    month.destroy()
                                    monthn = 9
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Oct():
                                    month.destroy()
                                    monthn = 10
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Nov():
                                    month.destroy()
                                    monthn = 11
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                def Dec():
                                    month.destroy()
                                    monthn = 12
                                    date_column_query = """
                                                                                                                    SELECT COLUMN_NAME 
                                                                                                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                                                                                                    WHERE TABLE_NAME = 'student_details' 
                                                                                                                    AND COLUMN_NAME NOT IN ('admission_no', 'roll_number', 'name', 'Gender')
                                                                                                                """
                                    cursor.execute(date_column_query)
                                    date_columns = [column[0] for column in cursor.fetchall()]
                                    # Prepare a dictionary to store student details and attendance counts
                                    student_details = {}

                                    # Query to fetch student details and attendance for each date column
                                    for date_column in date_columns:
                                        # Use backticks to reference the date columns
                                        column_parts = date_column.split('-')
                                        month_part = column_parts[1]  # Extract the month part

                                        query = f"SELECT admission_no, roll_number, name, Gender, `{date_column}` FROM student_details WHERE `{date_column}` IN ('FP', 'AP', 'OD', 'P', 'A') AND {monthn} = {month_part}"
                                        cursor.execute(query)
                                        attendance_data = cursor.fetchall()
                                        for row in attendance_data:
                                            admission_no, roll_number, name, gender, attendance_value = row

                                            if name not in student_details:
                                                student_details[name] = {'Admission No': admission_no,
                                                                         'Roll No': roll_number, 'Gender': gender,
                                                                         'Present': 0, 'Absent': 0}

                                            if attendance_value in ['FP', 'AP', 'OD', 'P']:
                                                student_details[name]['Present'] += 1
                                            elif attendance_value == 'A':
                                                student_details[name]['Absent'] += 1
                                    # Sort the student details by the number of days present in descending order
                                    sorted_student_details = sorted(student_details.items(),
                                                                    key=lambda x: x[1]['Present'], reverse=True)

                                    # Prepare data for tabulate
                                    table_data = []
                                    for name, details in sorted_student_details:
                                        table_data.append(
                                            [details['Admission No'], details['Roll No'], details['Gender'], name,
                                             details['Present'], details['Absent']])

                                    # Create a Tkinter window
                                    root = Tk()
                                    root.title(f"Attendance Summary for Month {monthn}")
                                    root.geometry("800x600")
                                    root.iconbitmap("Reeds.ico")

                                    # Create a canvas with a vertical scrollbar
                                    canvas = Canvas(root)
                                    canvas.pack(side="left", fill="both", expand=True)

                                    # Create a vertical scrollbar
                                    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
                                    scrollbar.pack(side="right", fill="y")

                                    canvas.configure(yscrollcommand=scrollbar.set)

                                    # Convert tabulated data to a string with visually formatted table using "pretty" format
                                    headers = ['Admission No', 'Roll No', 'Gender', 'Name', 'Days Present',
                                               'Days Absent']
                                    attendance_table = tabulate(table_data, headers=headers, tablefmt='pretty')

                                    # Create a label to display the tabulated attendance summary inside the canvas
                                    label = Label(canvas, text=attendance_table, justify="left",
                                                  font=("Courier", 10))
                                    canvas.create_window((0, 0), window=label, anchor="nw")

                                    # Configure canvas scrolling region
                                    canvas.config(scrollregion=canvas.bbox("all"))

                                    # Start the Tkinter main loop
                                    root.mainloop()
                                month = Tk()
                                month.configure(bg="black")  # bg colour
                                month.title("Month Summary")
                                month.geometry("800x600")
                                month.iconbitmap("Reeds.ico")
                                screen_width = month.winfo_screenwidth()
                                screen_height = month.winfo_screenheight()
                                bg_image = Image.open("voif.jpg")
                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                background_image = ImageTk.PhotoImage(bg_image)
                                canvas1 = Canvas(month, width=screen_width, height=screen_height)
                                canvas1.pack()
                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                monthlabel = Label(month, text="Select A Month For Summary", font=("Arial", 30), fg="white",
                                                   bg="black",justify="center", padx=10, pady=10)
                                monthlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
                                janButton = Button(month, text="Jan --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Jan, width=10, height=1)
                                janButton.place(relx=0.35, rely=0.5, anchor=CENTER)
                                FebButton = Button(month, text="Feb --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Feb, width=10, height=1)
                                FebButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                                MarButton = Button(month, text="Mar --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Mar, width=10, height=1)
                                MarButton.place(relx=0.65, rely=0.5, anchor=CENTER)
                                AprButton = Button(month, text="Apr --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Apr, width=10, height=1)
                                AprButton.place(relx=0.35, rely=0.6, anchor=CENTER)
                                MayButton = Button(month, text="May --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=May, width=10, height=1)
                                MayButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                JunButton = Button(month, text="Jun --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Jun, width=10, height=1)
                                JunButton.place(relx=0.65, rely=0.6, anchor=CENTER)
                                JulButton = Button(month, text="Jul --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Jul, width=10, height=1)
                                JulButton.place(relx=0.35, rely=0.7, anchor=CENTER)
                                AugButton = Button(month, text="Aug --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Aug, width=10, height=1)
                                AugButton.place(relx=0.5, rely=0.7, anchor=CENTER)
                                SepButton = Button(month, text="Sep --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Sep, width=10, height=1)
                                SepButton.place(relx=0.65, rely=0.7, anchor=CENTER)
                                OctButton = Button(month, text="Oct --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Oct, width=10, height=1)
                                OctButton.place(relx=0.35, rely=0.8, anchor=CENTER)
                                NovButton = Button(month, text="Nov --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Nov, width=10, height=1)
                                NovButton.place(relx=0.5, rely=0.8, anchor=CENTER)
                                DecButton = Button(month, text="Dec --→", font=("Arial", 15),
                                                         fg="white",
                                                         bg="black", command=Dec, width=10, height=1)
                                DecButton.place(relx=0.65, rely=0.8, anchor=CENTER)
                                month.mainloop()

                            ctmenu.destroy()
                            summary = Tk()
                            summary.configure(bg="black")  # bg colour
                            summary.title("Summary")
                            summary.geometry("800x600")
                            summary.iconbitmap("Reeds.ico")
                            screen_width = summary.winfo_screenwidth()
                            screen_height = summary.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(summary, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            summarylabel = Label(summary, text="Summary", font=("Arial", 30), fg="white", bg="black",
                                                 justify="center", padx=10, pady=10)
                            summarylabel.place(relx=0.5, rely=0.4, anchor=CENTER)
                            monthsummButton = Button(summary, text="Summary Of The Month --→", font=("Arial", 15),
                                                     fg="white",
                                                     bg="black", command=monthsumm, width=25, height=1)
                            monthsummButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                            yearsummButton = Button(summary, text="Summary Of The Year --→", font=("Arial", 15),
                                                    fg="white", bg="black",
                                                    command=yearsumm, width=25, height=1)
                            yearsummButton.place(relx=0.5, rely=0.6, anchor=CENTER)
                            summary.mainloop()
                            restart()
                        ctmenu = Tk()  # win to enter password
                        ctmenu.configure(bg="black")  # bg colour
                        ctmenu.title("login")
                        ctmenu.geometry("800x600")  # Control
                        ctmenu.iconbitmap("Reeds.ico")
                        screen_width = ctmenu.winfo_screenwidth()
                        screen_height = ctmenu.winfo_screenheight()
                        bg_image = Image.open("voif.jpg")
                        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                        background_image = ImageTk.PhotoImage(bg_image)
                        canvas1 = Canvas(ctmenu, width=screen_width, height=screen_height)
                        canvas1.pack()
                        canvas1.create_image(0, 0, anchor=NW, image=background_image)
                        welcomelabel = Label(ctmenu, text="Welcome Back !!", font=("Arial", 30), fg="white", bg="black",
                                             justify="center", padx=10, pady=10)
                        welcomelabel.place(relx=0.5, rely=0.3, anchor=CENTER)
                        removestuButton = Button(ctmenu, text="Attendance --→", font=("Arial", 15), fg="white",
                                                 bg="black",
                                                 command=attendance, width=30, height=1)
                        removestuButton.place(relx=0.5, rely=0.5, anchor=CENTER)
                        Editstubutton = Button(ctmenu, text="Summary --→", font=("Arial", 15), fg="white",
                                               bg="black",
                                               command=summary, width=30, height=1)
                        Editstubutton.place(relx=0.5, rely=0.6, anchor=CENTER)
                        ctmenu.mainloop()

                    restart()
                else:
                    messagebox.showwarning('Password Incorrect', 'Incorrect Password Restart The program.')
        welcomelabel = Label(welcome, text="WELCOME !!!!", font=("Arial", 30), fg="white", bg="black",
                             justify="center", padx=10, pady=10)  # welcome lable
        welcomelabel.place(relx=0.5, rely=0.45, anchor=CENTER)  # welcome using place
        Letsget = Button(welcome, text="Administrator --→", font=("Arial", 15), fg="white", bg="black",
                         command=admin,
                         width=30, height=1)
        Letsget.place(relx=0.5, rely=0.55, anchor=CENTER)
        Letsget = Button(welcome, text="Class Teacher --→", font=("Arial", 15), fg="white", bg="black",
                         command=classt, width=30, height=1)
        Letsget.place(relx=0.5, rely=0.65, anchor=CENTER)
        welcome.mainloop()
    else:
        welcome = Tk()  # creating win welcome to show at the begaining
        welcome.configure(bg="black")
        welcome.title("welcome")
        welcome.geometry("800x600")
        welcome.iconbitmap("Reeds.ico")
        screen_width = welcome.winfo_screenwidth()
        screen_height = welcome.winfo_screenheight()
        bg_image = Image.open("voif.jpg")
        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
        background_image = ImageTk.PhotoImage(bg_image)
        canvas1 = Canvas(welcome, width=screen_width, height=screen_height)
        canvas1.pack()
        canvas1.create_image(0, 0, anchor=NW, image=background_image)
        def stdinfo():                  #for geting student info
            if studentsstrength.get() =="":
                messagebox.showwarning('Missing information', 'Please enter the Class Strength.')
            else:
                global intstrength
                global strength
                global gender
                strength=studentsstrength.get()
                noofstudents.destroy()
                intstrength=int(strength)
                loop=1
                while loop <= intstrength :         #inserting data
                    gender=""
                    def justforfun():
                        saved.destroy()
                    def M():        #for geting value from male
                        global gender
                        gender="M"
                        text="selected "+gender
                        genderlabelconfirm = Label(infoofstudent, text=text, font=("Arial", 15), fg="white", bg="black",
                                              justify="center", padx=10, pady=10)
                        genderlabelconfirm.place(relx=0.88, rely=0.6, anchor=CENTER)
                    def F():             #for getting value from female
                        global gender
                        gender="F"
                        text = "selected " + gender
                        genderlabelconfirm = Label(infoofstudent, text=text, font=("Arial", 15), fg="white", bg="black",
                                              justify="center", padx=10, pady=10)
                        genderlabelconfirm.place(relx=0.88, rely=0.6, anchor=CENTER)

                    def get():                  #getting value of the student
                        if stuname.get() == '' or sturollno.get() == '' or stuadmissionno.get() == '' :
                            messagebox.showwarning('Missing information', 'Please enter all the required details.')
                        elif gender== "":
                            messagebox.showwarning('Missing information', 'Select a gender option.')
                        else:
                            sqlroll = "select name from student_details where roll_number=%s"
                            valuesroll = (sturollno.get(),)
                            cursor.execute(sqlroll, valuesroll)
                            resultroll = cursor.fetchone()
                            checkroll = resultroll is not None
                            sqladm = "select name from student_details where admission_no=%s"
                            valuesadm = (stuadmissionno.get(),)
                            cursor.execute(sqladm, valuesadm)
                            resultadm = cursor.fetchone()
                            checkadm = resultadm is not None
                            if checkroll:
                                messagebox.showwarning("Already Exist",
                                                       "Student " + resultroll[0] + " Has The Same Roll Number")
                            elif checkadm:
                                messagebox.showwarning("Already Exist",
                                                       "Student " + resultadm[0] + " Has The Same Admission Number")
                            else:
                                global rollno
                                global saved
                                name=stuname.get()
                                rollno=sturollno.get()
                                #Gender already stores the gender
                                admissionno=stuadmissionno.get()
                                cursor.execute(
                                    "INSERT INTO student_details (name, roll_number, admission_no, Gender) VALUES (%s, %s, %s, %s)",
                                    (name, rollno, admissionno, gender))
                                connector.commit()
                                infoofstudent.destroy()
                                saved = Tk()  # to create win
                                saved.configure(bg="black")  # bg colour
                                saved.title("login")
                                saved.geometry("800x600")
                                saved.iconbitmap("Reeds.ico")
                                screen_width = saved.winfo_screenwidth()
                                screen_height = saved.winfo_screenheight()
                                bg_image = Image.open("voif.jpg")
                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                background_image = ImageTk.PhotoImage(bg_image)
                                canvas1 = Canvas(saved, width=screen_width, height=screen_height)
                                canvas1.pack()
                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                textnew="Student "+str(loop)+" Details Saved"
                                savedLabel=Label(saved, text=(textnew),font=("Arial", 30),fg="white"
                                             ,bg="black", justify="center",padx=10, pady=10)
                                savedLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                                savedbutton=Button(saved, text="Next Student --→",font=("Arial", 15),fg="white",bg="black",command=justforfun, width=20, height=1)
                                savedbutton.place(relx=0.5, rely=0.6, anchor=CENTER)
                                saved.mainloop()
                    cursor.execute("""
                        CREATE TABLE if not exists student_details (
                            admission_no VARCHAR(255) PRIMARY KEY,
                            roll_number VARCHAR(255) UNIQUE,
                            name VARCHAR(255),
                            Gender varchar(10)
                        )""")
                    infoofstudent=Tk()
                    infoofstudent.configure(bg="black")  # bg colour
                    infoofstudent.title("Information ")
                    infoofstudent.geometry("800x600")
                    infoofstudent.iconbitmap("Reeds.ico")
                    screen_width = infoofstudent.winfo_screenwidth()
                    screen_height = infoofstudent.winfo_screenheight()
                    bg_image = Image.open("voif.jpg")
                    bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                    background_image = ImageTk.PhotoImage(bg_image)
                    canvas1 = Canvas(infoofstudent, width=screen_width, height=screen_height)
                    canvas1.pack()
                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                    GI = Label(infoofstudent, text = "Enter the information of the student ", font = ("Arial",30),
                                          fg = "white", bg = "black", justify = "center", padx = 10, pady = 10)
                    GI.place(relx=0.5, rely=0.2, anchor=CENTER)     #gi is thee general info

                    namelabel=Label(infoofstudent, text="Name ",font=("Arial", 15),
                                    fg="white",bg="black", justify="center",padx=10, pady=10)
                    namelabel.place(relx=0.3, rely=0.4, anchor=CENTER)
                    stuname = Entry(infoofstudent, width=25)
                    stuname.place(relx=0.7, rely=0.4, anchor=CENTER)

                    rollnolabel=Label(infoofstudent, text="Roll Number ",font=("Arial", 15),
                                    fg="white",bg="black", justify="center",padx=10, pady=10)
                    rollnolabel.place(relx=0.3,rely=0.5,anchor=CENTER)
                    sturollno = Entry(infoofstudent, width=25)
                    sturollno.place(relx=0.7, rely=0.5, anchor=CENTER)

                    genderlabel=Label(infoofstudent, text="Gender ",font=("Arial", 15),
                                fg="white",bg="black", justify="center",padx=10, pady=10)
                    genderlabel.place(relx=0.3, rely=0.6, anchor=CENTER)
                    genderButtonM =Button(infoofstudent, text="M",font=("Arial", 10),fg="black",
                                     bg="white", command=M, width=5, height=1,relief="raised")
                    genderButtonM.place(relx=0.65, rely=0.6, anchor=CENTER)
                    genderlabelor = Label(infoofstudent, text="or", font=("Arial", 10),
                                     fg="white", bg="black", justify="center", padx=10, pady=10)
                    genderlabelor.place(relx=0.7, rely=0.6, anchor=CENTER)
                    genderButtonF = Button(infoofstudent, text="F", font=("Arial", 10), fg="black",
                                       bg="white", command=F, width=5, height=1, relief="raised")
                    genderButtonF.place(relx=0.75, rely=0.6, anchor=CENTER)

                    admissionnolabel=Label(infoofstudent, text="Admission Number ",font=("Arial", 15),
                                fg="white",bg="black", justify="center",padx=10, pady=10)
                    admissionnolabel.place(relx=0.3, rely=0.7, anchor=CENTER)
                    stuadmissionno=Entry(infoofstudent,width=25)
                    stuadmissionno.place(relx=0.7, rely=0.7, anchor=CENTER)

                    Nextstudent=Button(infoofstudent, text="Submit Detail Of The Student --→",font=("Arial", 15),fg="white",
                                   bg="black", command=get, width=35, height=1)
                    Nextstudent.place(relx=0.5, rely=0.8, anchor=CENTER)
                    infoofstudent.mainloop()
                    loop += 1
        def great():
            allset.destroy()
        def admin():
            welcome.destroy()
            def geting():  # win asking password window
                global pword  # pword user input
                if enterpasswordbox.get() == "":
                    messagebox.showwarning('Missing information', 'Please Enter the Password.')
                else:
                    pword = enterpasswordbox.get()
                    passwin.destroy()
            passwin = Tk()  # win to enter password
            passwin.configure(bg="black")  # bg colour
            passwin.title("login")
            passwin.geometry("800x600")
            passwin.iconbitmap("Reeds.ico")
            screen_width = passwin.winfo_screenwidth()
            screen_height = passwin.winfo_screenheight()
            bg_image = Image.open("voif.jpg")
            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
            background_image = ImageTk.PhotoImage(bg_image)
            canvas1 = Canvas(passwin, width=screen_width, height=screen_height)
            canvas1.pack()
            canvas1.create_image(0, 0, anchor=NW, image=background_image)
            passwordlabel = Label(passwin, text="Enter password", font=("Arial", 30), fg="white", bg="black",
                                  justify="center", padx=10, pady=10)
            passwordlabel.place(relx=0.5, rely=0.4, anchor=CENTER)  # password using place
            enterpasswordbox = Entry(passwin, show="*", width=30)  # Entrty box to ask password
            enterpasswordbox.place(relx=0.5, rely=0.5, anchor=CENTER)
            loginpasswordButton = Button(passwin, text="login", font=("Arial", 15), fg="white", bg="black",
                                         command=geting, width=6, height=1)
            loginpasswordButton.place(relx=0.5, rely=0.6,anchor=CENTER)  # login password button
            passwin.mainloop()
            cursor.execute("select password from password where designation='admin'")
            passadmin=cursor.fetchone()[0]
            if pword =='':
                messagebox.showwarning('Missing information', 'Please Enter the Password.')
            else:
                if passadmin == pword:
                    global noofstudents
                    global studentsstrength
                    global allset
                    noofstudents = Tk()
                    noofstudents.configure(bg="black")
                    noofstudents.title("Strength")
                    noofstudents.geometry("800x600")
                    noofstudents.iconbitmap("Reeds.ico")
                    screen_width = noofstudents.winfo_screenwidth()
                    screen_height = noofstudents.winfo_screenheight()
                    bg_image = Image.open("voif.jpg")
                    bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                    background_image = ImageTk.PhotoImage(bg_image)
                    canvas1 = Canvas(noofstudents, width=screen_width, height=screen_height)
                    canvas1.pack()
                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                    Strength = Label(noofstudents, text="Enter The Class Strength", font=("Arial", 30), fg="white",
                                     bg="black",
                                     justify="center", padx=10, pady=10)
                    Strength.place(relx=0.5, rely=0.4, anchor=CENTER)
                    studentsstrength = Entry(noofstudents, width=30)
                    studentsstrength.place(relx=0.5, rely=0.5, anchor=CENTER)
                    nextbutton = Button(noofstudents, text="Next --→", font=("Arial", 15), fg="white", bg="black",
                                        command=stdinfo, width=10, height=1)
                    nextbutton.place(relx=0.5, rely=0.6, anchor=CENTER)
                    noofstudents.mainloop()
                    allset = Tk()
                    allset.configure(bg="black")  # bg colour
                    allset.title("ALL SET !!")
                    allset.geometry("800x600")
                    allset.iconbitmap("Reeds.ico")
                    screen_width = allset.winfo_screenwidth()
                    screen_height = allset.winfo_screenheight()
                    bg_image = Image.open("voif.jpg")
                    bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                    background_image = ImageTk.PhotoImage(bg_image)
                    canvas1 = Canvas(allset, width=screen_width, height=screen_height)
                    canvas1.pack()
                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                    allsetlabel1 = Label(allset, text="You are all set", font=("Arial", 30), fg="white", bg="black",
                                         justify="center", padx=10, pady=10)
                    allsetlabel1.place(relx=0.5, rely=0.4, anchor=CENTER)
                    allsetlabel2 = Label(allset, text="Restart The Program To take Attendance", font=("Arial", 30),
                                         fg="white",
                                         bg="black",
                                         justify="center", padx=10, pady=10)
                    allsetlabel2.place(relx=0.5, rely=.5, anchor=CENTER)
                    donebutton = Button(allset, text="Done", font=("Arial", 15), fg="white", bg="black",
                                        command=great, width=10, height=1)
                    donebutton.place(relx=0.5, rely=0.6, anchor=CENTER)
                    allset.mainloop()
                else:
                    messagebox.showwarning('Password Incorrect', 'Incorrect Password Restart The program.')
        def classt():
            messagebox.showwarning('Insert Student Details', 'Please ask the admin to enter the student details.')
        welcomelabel = Label(welcome, text="WELCOME !!!!", font=("Arial", 30), fg="white", bg="black",
                             justify="center", padx=10, pady=10)  # welcome lable
        welcomelabel.place(relx=0.5, rely=0.45, anchor=CENTER)  # welcome using place
        Letsget = Button(welcome, text="Administrator --→", font=("Arial", 15), fg="white", bg="black",
                         command=admin,
                         width=30, height=1)
        Letsget.place(relx=0.5, rely=0.55, anchor=CENTER)
        Letsget = Button(welcome, text="Class Teacher --→", font=("Arial", 15), fg="white", bg="black",
                         command=classt,width=30, height=1)
        Letsget.place(relx=0.5, rely=0.65, anchor=CENTER)
        welcome.mainloop()
else:
    welcome = Tk()  # creating win welcome to show at the begaining
    welcome.configure(bg="black")
    welcome.title("welcome")
    welcome.geometry("800x600")
    welcome.iconbitmap("Reeds.ico")
    screen_width = welcome.winfo_screenwidth()
    screen_height = welcome.winfo_screenheight()
    bg_image = Image.open("voif.jpg")
    bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
    background_image = ImageTk.PhotoImage(bg_image)
    canvas1 = Canvas(welcome, width=screen_width, height=screen_height)
    canvas1.pack()
    canvas1.create_image(0, 0, anchor=NW, image=background_image)
    def letsgo():
        # Create the admin_info table
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS password ("
            "designation VARCHAR(255) NOT NULL,"
            "name VARCHAR(255) NOT NULL,"
            "mobileno VARCHAR(20) NOT NULL,"
            "password VARCHAR(255) NOT NULL)"
        )
        cursor.execute(create_table_query)
        def confirm():
            def ctp():
                def classt():
                    def teacher():
                        def classteach():
                            def close():
                                def des():
                                    closw.destroy()
                                su.destroy()
                                closw = Tk()
                                closw.configure(bg="black")
                                closw.title("welcome")
                                closw.geometry("800x600")
                                closw.iconbitmap("Reeds.ico")
                                screen_width = closw.winfo_screenwidth()
                                screen_height = closw.winfo_screenheight()
                                bg_image = Image.open("voif.jpg")
                                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                                background_image = ImageTk.PhotoImage(bg_image)
                                canvas1 = Canvas(closw, width=screen_width, height=screen_height)
                                canvas1.pack()
                                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                                welcomelabel = Label(closw, text="Restart the program to", font=("Arial", 30),
                                                     fg="white", bg="black", justify="center", padx=10, pady=10)
                                welcomelabel.place(relx=0.5, rely=0.45, anchor=CENTER)  # welcome using place
                                welcomelabel = Label(closw, text="Add Student Details", font=("Arial", 30),
                                                     fg="white", bg="black", justify="center", padx=10, pady=10)
                                welcomelabel.place(relx=0.5, rely=0.55, anchor=CENTER)  # welcome using place
                                Letsget = Button(closw, text="Done", font=("Arial", 15), fg="white", bg="black",
                                                 command=des, width=10, height=1)
                                Letsget.place(relx=0.5, rely=0.65, anchor=CENTER)
                                closw.mainloop()

                            confirmwint.destroy()
                            sql = "INSERT INTO password (designation, name, mobileno, password) VALUES (%s, %s, %s, %s)"
                            insert_values = ("Class Teacher", name, mob, pword)
                            cursor.execute(sql, insert_values)
                            connector.commit()
                            su = Tk()
                            su.configure(bg="black")
                            su.title("welcome")
                            su.geometry("800x600")
                            su.iconbitmap("Reeds.ico")
                            screen_width = su.winfo_screenwidth()
                            screen_height = su.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(su, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            welcomelabel = Label(su, text="Class Teacher information is", font=("Arial", 30),
                                                 fg="white",bg="black", justify="center", padx=10, pady=10)  # welcome lable
                            welcomelabel.place(relx=0.5, rely=0.45, anchor=CENTER)  # welcome using place
                            welcomelabel = Label(su, text="Added Successfully", font=("Arial", 30),
                                                 fg="white", bg="black", justify="center", padx=10,
                                                 pady=10)  # welcome lable
                            welcomelabel.place(relx=0.5, rely=0.55, anchor=CENTER)  # welcome using place
                            Letsget = Button(su, text="Next --→", font=("Arial", 15), fg="white", bg="black",
                                             command=close, width=10, height=1)
                            Letsget.place(relx=0.5, rely=0.65, anchor=CENTER)
                            su.mainloop()
                        pword = enterpasswordbox.get()
                        name = enternamebox.get()
                        mob = entermobbox.get()
                        select_query = "SELECT mobileno FROM password"
                        cursor.execute(select_query)
                        mobile_numbers = cursor.fetchall()
                        fetched_mobiles = [str(mobile[0]) for mobile in mobile_numbers]
                        if pword == name == mob == '':
                            messagebox.showwarning('Missing information', 'Please enter the Required information.')
                        elif mob in fetched_mobiles:
                            messagebox.showwarning('Mobile no Exist', 'Please enter you mobile number correctly.')
                        else:
                            ctpass.destroy()
                            confirmwint = Tk()  # creating win welcome to show at the begaining
                            confirmwint.configure(bg="black")
                            confirmwint.title("welcome")
                            confirmwint.geometry("800x600")
                            confirmwint.iconbitmap("Reeds.ico")
                            screen_width = confirmwint.winfo_screenwidth()
                            screen_height = confirmwint.winfo_screenheight()
                            bg_image = Image.open("voif.jpg")
                            bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                            background_image = ImageTk.PhotoImage(bg_image)
                            canvas1 = Canvas(confirmwint, width=screen_width, height=screen_height)
                            canvas1.pack()
                            canvas1.create_image(0, 0, anchor=NW, image=background_image)
                            welcomelabel = Label(confirmwint, text="confirm password and mob no", font=("Arial", 30),
                                                 fg="white", bg="black",
                                                 justify="center", padx=10, pady=10)  # welcome lable
                            welcomelabel.place(relx=0.5, rely=0.45, anchor=CENTER)  # welcome using place
                            Letsget = Button(confirmwint, text="Confirm --→", font=("Arial", 15), fg="white", bg="black",
                                             command=classteach, width=10, height=1)
                            Letsget.place(relx=0.5, rely=0.55, anchor=CENTER)
                            confirmwint.mainloop()
                    su.destroy()
                    ctpass = Tk()  # creating win welcome to show at the begaining
                    ctpass.configure(bg="black")
                    ctpass.title("welcome")
                    ctpass.geometry("800x600")
                    ctpass.iconbitmap("Reeds.ico")
                    screen_width = ctpass.winfo_screenwidth()
                    screen_height = ctpass.winfo_screenheight()
                    bg_image = Image.open("voif.jpg")
                    bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                    background_image = ImageTk.PhotoImage(bg_image)
                    canvas1 = Canvas(ctpass, width=screen_width, height=screen_height)
                    canvas1.pack()
                    canvas1.create_image(0, 0, anchor=NW, image=background_image)
                    welcomelabel = Label(ctpass, text="Admin Please Enter The Details", font=("Arial", 30), fg="white",
                                         bg="black",
                                         justify="center", padx=10, pady=10)  # welcome lable
                    welcomelabel.place(relx=0.5, rely=0.25, anchor=CENTER)  # welcome using place
                    welcomelabel = Label(ctpass, text="Of The Class Teacher", font=("Arial", 30), fg="white",
                                         bg="black",
                                         justify="center", padx=10, pady=10)  # welcome lable
                    welcomelabel.place(relx=0.5, rely=0.35, anchor=CENTER)  # welcome using place
                    welcomelabel = Label(ctpass, text="Name ", font=("Arial", 15), fg="white",
                                         bg="black", justify="center", padx=10, pady=10)  # welcome lable
                    welcomelabel.place(relx=0.3, rely=0.45, anchor=CENTER)  # welcome using place
                    enternamebox = Entry(ctpass, width=20)
                    enternamebox.place(relx=0.7, rely=0.45, anchor=CENTER)
                    welcomelabel = Label(ctpass, text="Mobile Number", font=("Arial", 15), fg="white",
                                         bg="black", justify="center", padx=10, pady=10)  # welcome lable
                    welcomelabel.place(relx=0.3, rely=0.55, anchor=CENTER)  # welcome using place
                    entermobbox = Entry(ctpass, width=20)
                    entermobbox.place(relx=0.7, rely=0.55, anchor=CENTER)
                    welcomelabel = Label(ctpass, text="Password", font=("Arial", 15), fg="white",
                                         bg="black", justify="center", padx=10, pady=10)  # welcome lable
                    welcomelabel.place(relx=0.3, rely=0.65, anchor=CENTER)  # welcome using place
                    enterpasswordbox = Entry(ctpass, width=20)
                    enterpasswordbox.place(relx=0.7, rely=0.65, anchor=CENTER)
                    Letsget = Button(ctpass, text="Next --→", font=("Arial", 15), fg="white", bg="black",
                                     command=teacher, width=10, height=1)
                    Letsget.place(relx=0.5, rely=0.75, anchor=CENTER)
                    ctpass.mainloop()
                confirmwin.destroy()
                sql="INSERT INTO password (designation, name, mobileno, password) VALUES (%s, %s, %s, %s)"
                insert_values = ("admin", name, mob, pword)
                cursor.execute(sql, insert_values)
                connector.commit()
                su=Tk()
                su.configure(bg="black")
                su.title("welcome")
                su.geometry("800x600")
                su.iconbitmap("Reeds.ico")
                screen_width = su.winfo_screenwidth()
                screen_height = su.winfo_screenheight()
                bg_image = Image.open("voif.jpg")
                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                background_image = ImageTk.PhotoImage(bg_image)
                canvas1 = Canvas(su, width=screen_width, height=screen_height)
                canvas1.pack()
                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                welcomelabel = Label(su, text="Your information is added successfully ", font=("Arial", 30), fg="white",
                                     bg="black",justify="center", padx=10, pady=10)  # welcome lable
                welcomelabel.place(relx=0.5, rely=0.45, anchor=CENTER)  # welcome using place
                Letsget = Button(su, text="Next --→", font=("Arial", 15), fg="white", bg="black",
                                 command=classt, width=10, height=1)
                Letsget.place(relx=0.5, rely=0.55, anchor=CENTER)
                su.mainloop()
            pword=enterpasswordbox.get()
            name=enternamebox.get()
            mob=entermobbox.get()
            if pword == name == mob == '':
                messagebox.showwarning('Missing information', 'Please enter the Required information.')
            else:
                adminpass.destroy()
                confirmwin = Tk()  # creating win welcome to show at the begaining
                confirmwin.configure(bg="black")
                confirmwin.title("welcome")
                confirmwin.geometry("800x600")
                confirmwin.iconbitmap("Reeds.ico")
                screen_width = confirmwin.winfo_screenwidth()
                screen_height = confirmwin.winfo_screenheight()
                bg_image = Image.open("voif.jpg")
                bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
                background_image = ImageTk.PhotoImage(bg_image)
                canvas1 = Canvas(confirmwin, width=screen_width, height=screen_height)
                canvas1.pack()
                canvas1.create_image(0, 0, anchor=NW, image=background_image)
                welcomelabel = Label(confirmwin, text="confirm password and mob no", font=("Arial", 30), fg="white", bg="black",
                                 justify="center", padx=10, pady=10)  # welcome lable
                welcomelabel.place(relx=0.5, rely=0.45, anchor=CENTER)  # welcome using place
                Letsget = Button(confirmwin, text="Confirm --→", font=("Arial", 15), fg="white", bg="black",
                             command=ctp,width=10, height=1)
                Letsget.place(relx=0.5, rely=0.55, anchor=CENTER)
                confirmwin.mainloop()
        welcome.destroy()
        adminpass = Tk()  # creating win welcome to show at the begaining
        adminpass.configure(bg="black")
        adminpass.title("welcome")
        adminpass.geometry("800x600")
        adminpass.iconbitmap("Reeds.ico")
        screen_width = adminpass.winfo_screenwidth()
        screen_height = adminpass.winfo_screenheight()
        bg_image = Image.open("voif.jpg")
        bg_image = bg_image.resize((screen_width, screen_height), Image.BICUBIC)
        background_image = ImageTk.PhotoImage(bg_image)
        canvas1 = Canvas(adminpass, width=screen_width, height=screen_height)
        canvas1.pack()
        canvas1.create_image(0, 0, anchor=NW, image=background_image)
        welcomelabel = Label(adminpass, text="Admin Please Enter Your Details", font=("Arial", 30), fg="white", bg="black",
                             justify="center", padx=10, pady=10)  # welcome lable
        welcomelabel.place(relx=0.5, rely=0.35, anchor=CENTER)  # welcome using place
        welcomelabel = Label(adminpass, text="Name ", font=("Arial", 15), fg="white",
                             bg="black",justify="center", padx=10, pady=10)  # welcome lable
        welcomelabel.place(relx=0.3, rely=0.45, anchor=CENTER)  # welcome using place
        enternamebox = Entry(adminpass, width=20)
        enternamebox.place(relx=0.7, rely=0.45, anchor=CENTER)
        welcomelabel = Label(adminpass, text="Mobile Number", font=("Arial", 15), fg="white",
                             bg="black",justify="center", padx=10, pady=10)  # welcome lable
        welcomelabel.place(relx=0.3, rely=0.55, anchor=CENTER)  # welcome using place
        entermobbox = Entry(adminpass, width=20)
        entermobbox.place(relx=0.7, rely=0.55, anchor=CENTER)
        welcomelabel = Label(adminpass, text="Password", font=("Arial", 15), fg="white",
                             bg="black",justify="center", padx=10, pady=10)  # welcome lable
        welcomelabel.place(relx=0.3, rely=0.65, anchor=CENTER)  # welcome using place
        enterpasswordbox = Entry(adminpass, width=20)
        enterpasswordbox.place(relx=0.7, rely=0.65, anchor=CENTER)
        Letsget = Button(adminpass, text="Next --→", font=("Arial", 15), fg="white", bg="black",
                         command=confirm,width=10, height=1)
        Letsget.place(relx=0.5, rely=0.75, anchor=CENTER)
        adminpass.mainloop()
    welcomelabel = Label(welcome, text="WELCOME !!!!", font=("Arial", 30), fg="white", bg="black",
                         justify="center", padx=10, pady=10)  # welcome lable
    welcomelabel.place(relx=0.5, rely=0.45, anchor=CENTER)  # welcome using place
    Letsget = Button(welcome, text="Let's Get Started --→", font=("Arial", 15), fg="white", bg="black", command=letsgo,
                     width=20, height=1)
    Letsget.place(relx=0.5, rely=0.55, anchor=CENTER)
    welcome.mainloop()
