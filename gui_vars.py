import tkinter as tk

# Initialize the root Tkinter instance
root = tk.Tk()

# Hide the root window
root.withdraw()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Initialize StringVar and other Tkinter variables
var1_kAE = tk.StringVar(value="")
var2_kAE = tk.StringVar(value="")
var3_kAE = tk.StringVar(value="")
var1_kEP = tk.StringVar(value="")
var2_kEP = tk.StringVar(value="")
var3_kEP = tk.StringVar(value="")
var1_kPM = tk.StringVar(value="")
var2_kPM = tk.StringVar(value="")
var3_kPM = tk.StringVar(value="")
var4_kPM = tk.StringVar(value="")
var1_kAA = tk.StringVar(value="")
var2_kAA = tk.StringVar(value="")
var3_kAA = tk.StringVar(value="")
var1_rf = tk.StringVar(value="")
var2_rf = tk.StringVar(value="")
var_r1 = tk.StringVar(value="")
var_r2 = tk.StringVar(value="")
var_r3 = tk.StringVar(value="")
var_r4 = tk.StringVar(value="")

position_x1 = screen_width/10.3783
position_y1 = screen_height/7.4482
position_x2 = screen_width/8.1702
position_y2 = screen_height/7.4482
position_x3 = screen_width/6.7368
position_y3 = screen_height/7.4482
position_x4 = screen_width/5.7313
position_y4 = screen_height/7.4482
position_x5 = screen_width/4.9870
position_y5 = screen_height/7.4482
position_x_l = screen_width/8.1702

check_var = tk.IntVar() 

Instr_Cache = []