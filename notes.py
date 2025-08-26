import tkinter as tk 
from tkinter import messagebox
import os

NOTES_FILE = "notes.txt"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]
    

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(f"{note} \n")


def refresh_listbox():
    listbox.delete(0, tk.END)
    for note in notes:
        print("\n")
        listbox.insert(tk.END, note)



def add_note():
    note = entry.get().strip()
    if note:
        notes.append(note)
        save_notes(notes)
        refresh_listbox()
        entry.delete(0, tk.END)
        messagebox.showinfo("Saved", "Note added successfully!")
    else:
        messagebox.showwarning("Empty", "Please type something before adding.")

def delete_note():
    try:
        selected_index = listbox.curselection()[0]
        note = notes.pop(selected_index)
        save_notes(notes)
        refresh_listbox()
        messagebox.showinfo("Deleted", f"Deletednote {note}")
    except IndexError:
        messagebox.showwarning("No Selection", "Please select a note to delete.")



#GUI Setup
root  = tk.Tk()
root.title("Notes App")
root.geometry("400x400")

notes = load_notes()

#Input field
entry = tk.Entry(root, width=30, font=('Aril', 12))
entry.pack(pady=10)

#Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Note", command=add_note)
add_btn.grid(row=0, column=1, padx=5)

del_btn = tk.Button(btn_frame, text="Del Note", command=delete_note)
del_btn.grid(row=0, column=2, padx=20)

#Notes list
listbox = tk.Listbox(root, width=40,height=15)
listbox.pack(pady=10)

refresh_listbox()

root.mainloop()

