#import modules
from tkinter import * #GUI interface
import csv            #csv file handeling

#main program
def validateUser():
    def authenticate():
        filename = "UserCredentials.csv" 
        fields = [] 
        row = []
        flag = 0
        with open(filename, 'r') as csvfile: 
            csvreader = csv.reader(csvfile)
            for row in csvreader: 
                if (row[3]==E1.get() and row[4]==E2.get()):
                    flag = 1
                    break
            
            if(flag==1):
                valid.destroy()

                from welcomePage import welcomePage
                
                f = open('currentuserCache',"w")
                f.write(str(row))
                f.close()

                
                
                
                welcomePage()
                                
            else:
                L3 = Label(valid, text = "Invalid credentials")
                L3.grid(row = 4, column = 0)
            
                
                
    valid = Tk()
    valid.title("ADINA")
    L1 = Label(valid, text = "User Name")
    L1.grid(row = 0, column = 0)
    E1 = Entry(valid)
    E1.grid(row = 0, column = 1)
    L2 = Label(valid, text = "password")
    L2.grid(row = 1, column = 0)
    E2 = Entry(valid)
    E2.grid(row = 1, column = 1)
    MyButton1 = Button(valid, text="Submit", width=10, command = authenticate)
    MyButton1.grid(row=2, column=1)
    valid.mainloop()
    


