import tkinter as tk


def run():
    root.mainloop()

def hide_buttons():
    frm_buttons.config(bg=color)
    frm_buttons.pack_forget()


color = "#AED6F1"

root = tk.Tk()
root.title("SmartKey")
root.geometry("600x800")

top_frame = tk.Frame(
    root, 
    bg= color,
    bd=2,
    height=100,
    width=560,
    highlightcolor= "gray",
    relief=tk.RAISED
    )
top_frame.pack_propagate(0)
top_frame.pack(side="top", padx=20,pady=20)

btn_bell = tk.Button(
top_frame,
text="Pozvoni",
command= "ide_mid"
)
btn_bell.config(width=15, height=5)
btn_bell.pack(side="left",padx=5)

btn_lock = tk.Button(
top_frame,
text="Otključaj",
)
btn_lock.config(width=15, height=5)
btn_lock.pack(side="right",padx=5)

mid_frame = tk.Frame(
    root, 
    bg= color,
    bd=2,
    height=340,
    width=560,
    highlightcolor= "gray",
    relief = tk.RAISED
)
mid_frame.pack_propagate(0)
mid_frame.pack(pady=20)

frm_buttons = tk .Frame(
    mid_frame,
    bd=2,
    height= 300,
    width= 250,
    )

frm_buttons.pack_propagate(0)
frm_buttons.pack(padx=10, pady=10, side="left")



frm_status = tk .Frame(
    mid_frame,
    bd=2,
    height= 300,
    width= 250,
    )

frm_status.pack_propagate(0)
frm_status.pack(padx=10, pady=10, side="right")










bot_frame = tk.Frame(
    root, 
    bd= 2,
    bg= color,
    height=240,
    width=560,
    highlightcolor= "gray",
    relief = tk.RAISED
)
bot_frame.pack_propagate(0)
bot_frame.pack(pady=20)



