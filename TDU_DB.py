#IMPORT RELEVANT MODULES:
import sqlite3 as sql
import pandas as pd
import tkinter as tk
#import tabulate as tbl
import pandastable as pt


#CREATE CONNECTION TO DATABASE AND CURSOR FUNCTION:
DB = 'C:/Users/steph/Documents/SQL/TDU_VEHICLES.db'
con = sql.connect(DB)
cur = con.cursor()

#FETCH TABLES IN DATABASE:
cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")

#CREATE LAUNCH FUNCTION:
def mm():
    root=tk.Tk()
    root.title('Test Drive Unlimited Database')
    app=main_menu(root)
    root.mainloop()

#CREATE MAIN MENU:   
class main_menu:
    def __init__(self, master):
        self.master=master
        self.frame=tk.Frame(self.master)
        self.frame.grid(row=0, column=0, sticky='news')
        self.btn_all_v=tk.Button(self.frame,
                             text='ALL VEHICLES',
                             command=self.button_all_v,
                             activeforeground='#ffffff', #White
                             activebackground='#9900ff', #Purple
                             bg='#cc80ff', #Lilac
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=0, column=0, columnspan=8, sticky='news')
        self.btn_all_c=tk.Button(self.frame,
                             text='ALL CARS',
                             command=self.button_all_c,
                             activeforeground='#ffffff', #White
                             activebackground='#00ff00', #Lime
                             bg='#80ff80', #Pale Lime
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=1, column=0, columnspan=4, sticky='ew')
        self.btn_all_b=tk.Button(self.frame,
                             text='ALL BIKES',
                             command=self.button_all_b,
                             activeforeground='#ffffff', #White
                             activebackground='#ffff00', #Yellow
                             bg='#ffff80', #Pale Yellow
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=1, column=4, columnspan=4, sticky='ew')
        self.btn_g=tk.Button(self.frame,
                             text='CLASS G',
                             command=self.button_g,
                             activeforeground='#ffffff', #White
                             activebackground='#0000ff', #Blue
                             bg='#8080ff', #Pale Blue
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=2, column=0)
        self.btn_f=tk.Button(self.frame,
                             text='CLASS F',
                             command=self.button_f,
                             activeforeground='#ffffff', #White
                             activebackground='#00ffcc', #Light Blue
                             bg='#80ffe5', #Pale Light Blue
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=2, column=1)
        self.btn_e=tk.Button(self.frame,
                             text='CLASS E',
                             command=self.button_e,
                             activeforeground='#ffffff', #White
                             activebackground='#00ff00', #Lime
                             bg='#80ff80', #Pale Lime
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=2, column=2)
        self.btn_d=tk.Button(self.frame,
                             text='CLASS D',
                             command=self.button_d,
                             activeforeground='#ffffff', #White
                             activebackground='#aaff00', #Green
                             bg='#d5ff80', #Pale Green
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=2, column=3, columnspan=2)
        self.btn_c=tk.Button(self.frame,
                             text='CLASS C',
                             command=self.button_c,
                             activeforeground='#ffffff', #White
                             activebackground='#ffff00', #Yellow
                             bg='#ffff80', #Pale Yellow
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=2, column=5)
        self.btn_b=tk.Button(self.frame,
                             text='CLASS B',
                             command=self.button_b,
                             activeforeground='#ffffff', #White
                             activebackground='#ff8000', #Orange
                             bg='#ffbf80', #Pale Orange
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=2, column=6)
        self.btn_a=tk.Button(self.frame,
                             text='CLASS A',
                             command=self.button_a,
                             activeforeground='#ffffff', #White
                             activebackground='#ff0000', #Red
                             bg='#ff8080', #Pink
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=2, column=7)
        self.btn_mb=tk.Button(self.frame,
                             text='CLASS MB',
                             command=self.button_mb,
                             activeforeground='#ffffff', #White
                             activebackground='#0000ff', #Blue
                             bg='#8080ff', #Pale Blue
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=3, column=0, columnspan=4, sticky='ew')
        self.btn_a=tk.Button(self.frame,
                             text='CLASS MA',
                             command=self.button_ma,
                             activeforeground='#ffffff', #White
                             activebackground='#ff0000', #Red
                             bg='#ff8080', #Pink
                             fg='#000000', #Black
                             cursor='hand2',
                             overrelief='raised',
                             font=('Ariel', 15, 'bold')
                             ).grid(row=3, column=4, columnspan=4, sticky='ew')
#DEFINE BUTTON FUNCTIONS:
    def button_all_v(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=ALL_V_screen(self.newWindow)
        
    def button_all_c(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=ALL_C_screen(self.newWindow)

    def button_all_b(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=ALL_B_screen(self.newWindow)
        
    def button_g(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=G_screen(self.newWindow)

    def button_f(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=F_screen(self.newWindow)

    def button_e(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=E_screen(self.newWindow)

    def button_d(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=D_screen(self.newWindow)

    def button_c(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=C_screen(self.newWindow)

    def button_b(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=B_screen(self.newWindow)

    def button_a(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=A_screen(self.newWindow)

    def button_mb(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=MB_screen(self.newWindow)

    def button_ma(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=MA_screen(self.newWindow)
#################################################################ALL VEHICLES SCREEN#############################################################        
#CREATE SCREEN FOR All VECHICLES:
class ALL_V_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('All Vehicles')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR ALL VEHICLES:
        self.all_v=pd.read_sql_query("SELECT * FROM 'All Vehicles'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_all_v=pt.Table(self.frame,
                            dataframe=self.all_v,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_all_v.show()
        self.tbl_all_v.hideRowHeader()
        self.tbl_all_v.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#cc80ff', #Lilac
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#9900ff', #Purple
                 'textcolor': '#ffffff', #White
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_all_v)
        self.tbl_all_v.editable=False
        self.tbl_all_v.setWrap()
        self.tbl_all_v.setFont()
        self.tbl_all_v.expandColumns(54.9)
        self.tbl_all_v.colheader.bgcolor='#9900ff', #Purple
        self.tbl_all_v.colheader.fgcolor='#ffffff', #White
        self.tbl_all_v.enable_menus=False
        self.tbl_all_v.handle_mouse_drag=True
        self.tbl_all_v.redraw()
        return
#################################################################ALL VEHICLES SCREEN#################################################################        
#################################################################ALL CARS SCREEN###########################################################        
#CREATE SCREEN FOR All Cars:
class ALL_C_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('All Cars')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR ALL CARS:
        self.all_c=pd.read_sql_query("SELECT * FROM 'All Cars'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_all_c=pt.Table(self.frame,
                            dataframe=self.all_c,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_all_c.show()
        self.tbl_all_c.hideRowHeader()
        self.tbl_all_c.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#80ff80', #Pale Lime
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#00ff00', #Lime
                 'textcolor': '#000000', #Black
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_all_c)
        self.tbl_all_c.editable=False
        self.tbl_all_c.setWrap()
        self.tbl_all_c.setFont()
        self.tbl_all_c.expandColumns(54.9)
        self.tbl_all_c.colheader.bgcolor='#00ff00', #Lime
        self.tbl_all_c.colheader.fgcolor='#000000', #Black
        self.tbl_all_c.enable_menus=False
        self.tbl_all_c.handle_mouse_drag=True
        self.tbl_all_c.redraw()
        return
#################################################################ALL CARS SCREEN###########################################################        
#################################################################ALL MOTORBIKES SCREEN###########################################################        
#CREATE SCREEN FOR All MOTORBIKES:
class ALL_B_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('All Motorbikes')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR ALL MOTORBIKES:
        self.all_b=pd.read_sql_query("SELECT * FROM 'All Bikes'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_all_b=pt.Table(self.frame,
                            dataframe=self.all_b,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_all_b.show()
        self.tbl_all_b.hideRowHeader()
        self.tbl_all_b.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#ffff80', #Pale Yellow
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#ffff00', #Yellow
                 'textcolor': '#000000', #Black
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_all_b)
        self.tbl_all_b.editable=False
        self.tbl_all_b.setWrap()
        self.tbl_all_b.setFont()
        self.tbl_all_b.expandColumns(66.7)
        self.tbl_all_b.colheader.bgcolor='#ffff00', #Yellow
        self.tbl_all_b.colheader.fgcolor='#000000', #Black
        self.tbl_all_b.enable_menus=False
        self.tbl_all_b.handle_mouse_drag=True
        self.tbl_all_b.bind('<MouseWheel>', self.disable)
        self.tbl_all_b.redraw()
        return
    
#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'
#################################################################ALL MOTORBIKES SCREEN###########################################################        
#################################################################G SCREEN#####################################################################        
#CREATE SCREEN FOR CLASS G VECHICLES:
class G_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('Class G')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS G VEHICLES:
        self.class_g=pd.read_sql_query("SELECT * FROM 'Class G'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_g=pt.Table(self.frame,'#ffffff', #White
                            dataframe=self.class_g,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_g.show()
        self.tbl_g.hideRowHeader()
        self.tbl_g.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#8080ff', #Pale Blue
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#0000ff', #Blue
                 'textcolor': '#ffffff', #White
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_g)
        self.tbl_g.editable=False
        self.tbl_g.setWrap()
        self.tbl_g.setFont()
        self.tbl_g.expandColumns(56.3)
        self.tbl_g.colheader.bgcolor='#0000ff', #Blue
        self.tbl_g.colheader.fgcolor='#ffffff', #White
        self.tbl_g.bind('<MouseWheel>', self.disable)
        self.tbl_g.enable_menus=False
        self.tbl_g.handle_mouse_drag=True
        self.tbl_g.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'   
#################################################################G SCREEN####################################################################### 
#################################################################F SCREEN#######################################################################
#CREATE SCREEN FOR CLASS F VECHICLES:
class F_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('Class F')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS F VEHICLES:
        self.class_f=pd.read_sql_query("SELECT * FROM 'Class F'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_f=pt.Table(self.frame,
                            dataframe=self.class_f,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_f.show()
        self.tbl_f.hideRowHeader()
        self.tbl_f.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#80ffe5', #Pale Light Blue
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#00ffcc', #Light Blue
                 'textcolor': '#000000', #Black
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_f)
        self.tbl_f.editable=False
        self.tbl_f.setWrap()
        self.tbl_f.setFont()
        self.tbl_f.expandColumns(67)
        self.tbl_f.colheader.bgcolor='#00ffcc', #Light Blue
        self.tbl_f.colheader.fgcolor='#000000', #Black
        self.tbl_f.bind('<MouseWheel>', self.disable)
        self.tbl_f.enable_menus=False
        self.tbl_f.handle_mouse_drag=True
        self.tbl_f.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'
#################################################################F SCREEN####################################################################### 
#################################################################E SCREEN####################################################################### 
#CREATE SCREEN FOR CLASS E VECHICLES:
class E_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('Class E')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS E VEHICLES:
        self.class_e=pd.read_sql_query("SELECT * FROM 'Class E'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_e=pt.Table(self.frame,
                            dataframe=self.class_e,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_e.show()
        self.tbl_e.hideRowHeader()
        self.tbl_e.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#80ff80', #Pale Lime
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#00ff00', #Lime
                 'textcolor': '#000000', #Black
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_e)
        self.tbl_e.editable=False
        self.tbl_e.setWrap()
        self.tbl_e.setFont()
        self.tbl_e.expandColumns(59.3)
        self.tbl_e.colheader.bgcolor='#00ff00', #Lime
        self.tbl_e.colheader.fgcolor='#000000', #Black
        self.tbl_e.bind('<MouseWheel>', self.disable)
        self.tbl_e.enable_menus=False
        self.tbl_e.handle_mouse_drag=True
        self.tbl_e.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'
#################################################################E SCREEN####################################################################### 
#################################################################D SCREEN####################################################################### 
#CREATE SCREEN FOR CLASS D VECHICLES:
class D_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('Class D')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS D VEHICLES:
        self.class_d=pd.read_sql_query("SELECT * FROM 'Class D'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_d=pt.Table(self.frame,
                            dataframe=self.class_d,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_d.show()
        self.tbl_d.hideRowHeader()
        self.tbl_d.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#d5ff80', #Pale Green
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#aaff00', #Green
                 'textcolor': '#000000', #Black
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_d)
        self.tbl_d.editable=False
        self.tbl_d.setWrap()
        self.tbl_d.setFont()
        self.tbl_d.expandColumns(57)
        self.tbl_d.colheader.bgcolor='#aaff00', #Green
        self.tbl_d.colheader.fgcolor='#000000', #Black
        self.tbl_d.bind('<MouseWheel>', self.disable)
        self.tbl_d.enable_menus=False
        self.tbl_d.handle_mouse_drag=True
        self.tbl_d.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'
#################################################################D SCREEN####################################################################### 
#################################################################C SCREEN####################################################################### 
#CREATE SCREEN FOR CLASS C VECHICLES:
class C_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('Class C')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS C VEHICLES:
        self.class_c=pd.read_sql_query("SELECT * FROM 'Class C'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_c=pt.Table(self.frame,
                            dataframe=self.class_c,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_c.show()
        self.tbl_c.hideRowHeader()
        self.tbl_c.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#ffff80', #Pale Yellow
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#ffff00', #Yellow
                 'textcolor': '#000000', #Black
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_c)
        self.tbl_c.editable=False
        self.tbl_c.setWrap()
        self.tbl_c.setFont()
        self.tbl_c.expandColumns(59.8)
        self.tbl_c.colheader.bgcolor='#ffff00', #Yellow
        self.tbl_c.colheader.fgcolor='#000000', #Black
        self.tbl_c.bind('<MouseWheel>', self.disable)
        self.tbl_c.enable_menus=False
        self.tbl_c.handle_mouse_drag=True
        self.tbl_c.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'
#################################################################C SCREEN####################################################################### 
#################################################################B SCREEN####################################################################### 
#CREATE SCREEN FOR CLASS B VECHICLES:
class B_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('Class B')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS B VEHICLES:
        self.class_b=pd.read_sql_query("SELECT * FROM 'Class B'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_b=pt.Table(self.frame,
                            dataframe=self.class_b,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_b.show()
        self.tbl_b.hideRowHeader()
        self.tbl_b.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#ffbf80', #Pale Orange
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#ff8000', #Orange
                 'textcolor': '#ffffff', #White
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_b)
        self.tbl_b.editable=False
        self.tbl_b.setWrap()
        self.tbl_b.setFont()
        self.tbl_b.expandColumns(59.8)
        self.tbl_b.colheader.bgcolor='#ff8000', #Orange
        self.tbl_b.colheader.fgcolor='#ffffff', #White
        self.tbl_b.bind('<MouseWheel>', self.disable)
        self.tbl_b.enable_menus=False
        self.tbl_b.handle_mouse_drag=True
        self.tbl_b.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'
#################################################################B SCREEN####################################################################### 
#################################################################A SCREEN####################################################################### 
#CREATE SCREEN FOR CLASS A VECHICLES:
class A_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('Class A')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS A VEHICLES:
        self.class_a=pd.read_sql_query("SELECT * FROM 'Class A'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_a=pt.Table(self.frame,
                            dataframe=self.class_a,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_a.show()
        self.tbl_a.hideRowHeader()
        self.tbl_a.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#ff8080', #Pink
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#ff0000', #Red
                 'textcolor': '#ffffff', #White
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_a)
        self.tbl_a.editable=False
        self.tbl_a.setWrap()
        self.tbl_a.setFont()
        self.tbl_a.expandColumns(62.8)
        self.tbl_a.colheader.bgcolor='#ff0000', #Red
        self.tbl_a.colheader.fgcolor='#ffffff', #White
        self.tbl_a.bind('<MouseWheel>', self.disable)
        self.tbl_a.enable_menus=False
        self.tbl_a.handle_mouse_drag=True
        self.tbl_a.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'
#################################################################A SCREEN####################################################################### 
#################################################################MB SCREEN####################################################################        
#CREATE SCREEN FOR CLASS MB VECHICLES:
class MB_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.geometry(f'{width}x{height}')
        self.master.title('Class MB')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS MB VEHICLES:
        self.class_mb=pd.read_sql_query("SELECT * FROM 'Class MB'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_mb=pt.Table(self.frame,
                            dataframe=self.class_mb,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_mb.show()
        self.tbl_mb.hideRowHeader()
        self.tbl_mb.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#8080ff', #Pale Blue
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#0000ff', #Blue
                 'textcolor': '#ffffff', #White
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_mb)
        self.tbl_mb.editable=False
        self.tbl_mb.setWrap()
        self.tbl_mb.setFont()
        self.tbl_mb.expandColumns(66.7)
        self.tbl_mb.colheader.bgcolor='#0000ff', #Blue
        self.tbl_mb.colheader.fgcolor='#ffffff', #White
        self.tbl_mb.bind('<MouseWheel>', self.disable)
        self.tbl_mb.enable_menus=False
        self.tbl_mb.handle_mouse_drag=True
        self.tbl_mb.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'   
#################################################################MB SCREEN###################################################################### 
#################################################################MA SCREEN###################################################################### 
#CREATE SCREEN FOR CLASS MA VECHICLES:
class MA_screen:
    def __init__(self, master):
        self.master=master
        width=self.master.winfo_screenwidth()
        height=self.master.winfo_screenheight()
        self.master.title('Class MA')
        self.frame=tk.Frame(self.master, width=width)
        self.frame.pack(fill='both', expand=True, side=tk.TOP)

#CREATE & FORMAT TABLE FOR CLASS A VEHICLES:
        self.class_ma=pd.read_sql_query("SELECT * FROM 'Class MA'", con)
        pd.set_option('display.max_columns', None)
        self.tbl_ma=pt.Table(self.frame,
                            dataframe=self.class_ma,
                            showtoolbar=False,
                            showstatusbar=False,
                            width=width,
                            height=height,
                            handle_mouse_drag=False
                            )     
        self.tbl_ma.show()
        self.tbl_ma.hideRowHeader()
        self.tbl_ma.zoomOut()
        options={'align': 'w',
                 'floatprecision': 0,
                 'thousandseparator': ',',
                 'cellbackgr': '#ff8080', #Pink
                 'font': 'Arial',
                 'fontsize': 10,
                 'fontstyle': 'bold',
                 'rowselectedcolor': '#ff0000', #Red
                 'textcolor': '#ffffff', #White
                 'handle_mouse_drag': False
                 }
        pt.config.apply_options(options, self.tbl_ma)
        self.tbl_ma.editable=False
        self.tbl_ma.setWrap()
        self.tbl_ma.setFont()
        self.tbl_ma.expandColumns(74.6)
        self.tbl_ma.colheader.bgcolor='#ff0000', #Red
        self.tbl_ma.colheader.fgcolor='#ffffff', #White
        self.tbl_ma.bind('<MouseWheel>', self.disable)
        self.tbl_ma.enable_menus=False
        self.tbl_ma.handle_mouse_drag=True
        self.tbl_ma.redraw()
        return

#DISABLE MOUSE WHEEL:
    def disable(self, event):
        return 'break'
#################################################################MA SCREEN###################################################################### 
#LAUNCH DATABASE:
if __name__ == '__main__':
    mm()

#CLOSE DATABASE CONNECTION:
con.close()
