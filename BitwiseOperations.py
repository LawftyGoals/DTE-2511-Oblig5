from tkinter import *
from tkinter.ttk import Combobox

class BitwiseOperations:
    def __init__(self):
        
        window = Tk()
        window.title("Bitwise Operations")
        window.geometry("550x100")

        frame1 = Frame(window)
        frame1.pack(anchor="w")
        
        first_num_labl = Label(frame1, text="First number, range 0-255")
        first_num_labl.grid(row=0, column=0, sticky="w")

        self.first_num_var = StringVar()

        self.first_num_ent = Entry(frame1, width=3, text="0", textvariable=self.first_num_var)
        self.first_num_ent.grid(row=0,column=1)
        

        self.first_num_bit_lab = Label(frame1, text="00000000")
        self.first_num_bit_lab.grid(row=0,column=2)

        sec_num_labl = Label(frame1, text="Second number, range 0-255")
        sec_num_labl.grid(row=1, column=0, sticky="w")

        self.sec_num_var = StringVar()

        self.sec_num_ent = Entry(frame1, width=3, text="0", textvariable=self.sec_num_var)
        self.sec_num_ent.grid(row=1,column=1)
        

        self.sec_num_bit_lab = Label(frame1, text="00000000")
        self.sec_num_bit_lab.grid(row=1,column=2)

        yr_answer_lbl = Label(frame1, text="Your answer")
        yr_answer_lbl.grid(row=2,column=0, sticky="w")
        
        self.yr_answ_var = StringVar()
        self.yr_answer_ent = Entry(frame1, width=8, textvariable=self.yr_answ_var)
        self.yr_answer_ent.grid(row=2, column=2)

        self.comb_var = StringVar()
        combo_box = Combobox(frame1, textvariable = self.comb_var)
        combo_box['values'] = ["AND", "OR", "OCOMP", "XOR", "SHIFTLEFT", "SHIFTRIGHT"]
        combo_box.grid(row=2, column=3)

        answ_btn = Button(frame1, text="Check", command=self.check_answ)
        answ_btn.grid(row=2, column=4)
        
        self.cor_answer_lbl = Label(frame1, text="Correct answer")
        self.cor_answer_lbl.grid(row=3,column=0, sticky="w")
        
        self.cor_answ_lbl_res = Label(frame1, text="")
        self.cor_answ_lbl_res.grid(row=3,column=2)

        
        self.first_num_ent.bind("<FocusOut>", self.change_fn_bit_lab)
        self.sec_num_ent.bind("<FocusOut>", self.change_sn_bit_lab)

        self.first_num_ent.bind("<FocusIn>", self.clear_entry)
        self.sec_num_ent.bind("<FocusIn>", self.clear_entry)


        window.mainloop()

    def clear_entry(self, event):
        event.widget.delete(0,END)
        event.widget.config(bg="white")
        self.yr_answer_ent.config(bg="white")


    def change_fn_bit_lab(self, event):
        if self.first_num_var.get().isdigit():
            first_num_inp = int(self.first_num_var.get())
            self.first_num_bit_lab.config(text=format(first_num_inp, "08b"))
    
    def change_sn_bit_lab(self, event):
        if self.sec_num_var.get().isdigit():
            sec_num_inp = int(self.sec_num_var.get())
            self.sec_num_bit_lab.config(text=format(sec_num_inp, "08b"))
    
    def check_answ(self):
        res = ""
        if self.first_num_var.get().isdigit():
            if self.comb_var.get() == "AND":
                res = format(int(self.first_num_var.get()) & int(self.sec_num_var.get()), "08b")
            elif self.comb_var.get() == "OR":
                res = format(int(self.first_num_var.get()) | int(self.sec_num_var.get()), "08b")
            elif self.comb_var.get() == "OCOMP":
                res = format(~int(self.first_num_var.get()) & 255, "08b")
            elif self.comb_var.get() == "XOR":
                res = format(int(self.first_num_var.get()) ^ int(self.sec_num_var.get()), "08b")
            elif self.comb_var.get() == "SHIFTLEFT":
                res = format(int(self.first_num_var.get()) << 1 & 255, "08b")
            elif self.comb_var.get() == "SHIFTRIGHT":
                res = format(int(self.first_num_var.get()) >> 1 & 255, "08b")

            self.cor_answ_lbl_res.config(text=res)

            
            if self.yr_answ_var.get() == res:
                self.yr_answer_ent.config(bg="green")
            else:
                self.yr_answer_ent.config(bg="red")


BitwiseOperations()

