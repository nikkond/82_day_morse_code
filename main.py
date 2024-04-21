import tkinter as tk

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            raise ValueError(f"Invalid symbol '{char}' entered. Only alphanumeric characters and spaces are allowed.")
    return morse_code.strip()  # Remove trailing space


def morse_to_text(morse_code):
    text = ''
    morse_code_list = morse_code.split(' ')
    for code in morse_code_list:
        for char, morse in morse_code_dict.items():
            if code == morse:
                text += char
                break
        else:
            if code != '':
                raise ValueError(f"Invalid Morse code '{code}' entered.")
    return text


def toggle_converter_mode():
    global mode
    if mode == "Text to Morse":
        mode = "Morse to Text"
        convert_button.config(text="Convert to Text")
        input_text_area.delete(1.0, tk.END)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Here will be a Text")
    else:
        mode = "Text to Morse"
        convert_button.config(text="Convert to Morse")
        input_text_area.delete(1.0, tk.END)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Here will be a Morse code")
    update_output_hint()


def update_output_hint():
    global mode
    if mode == "Text to Morse":
        output_text.config(state=tk.NORMAL)  # Enable the widget
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Here will be a Morse code")
        output_text.config(state=tk.DISABLED)  # Disable the widget again
    else:
        output_text.config(state=tk.NORMAL)  # Enable the widget
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Here will be a Text")
        output_text.config(state=tk.DISABLED)  # Disable the widget again


def convert():
    if mode == "Text to Morse":
        input_text = input_text_area.get("1.0", tk.END).strip()  # Get text from the whole widget
        try:
            morse_code = text_to_morse(input_text)
            output_text.config(state=tk.NORMAL)  # Enable the widget
            output_text.delete(1.0, tk.END)  # Clear previous content
            output_text.insert(tk.END, morse_code)
            output_text.config(state=tk.DISABLED)  # Disable the widget again
        except ValueError as e:
            output_text.config(state=tk.NORMAL)  # Enable the widget
            output_text.delete(1.0, tk.END)  # Clear previous content
            output_text.insert(tk.END, str(e), "error")  # Insert error message with tag "error"
            output_text.config(state=tk.DISABLED)  # Disable the widget again
    else:
        morse_code = input_text_area.get("1.0", tk.END).strip()  # Get text from the whole widget
        try:
            text = morse_to_text(morse_code)
            output_text.config(state=tk.NORMAL)  # Enable the widget
            output_text.delete(1.0, tk.END)  # Clear previous content
            output_text.insert(tk.END, text)
            output_text.config(state=tk.DISABLED)  # Disable the widget again
        except ValueError as e:
            output_text.config(state=tk.NORMAL)  # Enable the widget
            output_text.delete(1.0, tk.END)  # Clear previous content
            output_text.insert(tk.END, str(e), "error")  # Insert error message with tag "error"
            output_text.config(state=tk.DISABLED)  # Disable the widget again


# Create the main window
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("400x400")

# Configure row and column weights for adaptive resizing
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create input frame with vertical scrollbar
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")
input_frame.grid_columnconfigure(0, weight=1)
input_frame.pack_propagate(False)  # Prevent resizing to fit contents

input_text_scrollbar = tk.Scrollbar(input_frame)
input_text_scrollbar.pack(side="right", fill="y")

input_text_area = tk.Text(input_frame, wrap="word", yscrollcommand=input_text_scrollbar.set)
input_text_area.pack(side="left", fill="both", expand=True)

input_text_scrollbar.config(command=input_text_area.yview)

# Create convert button
convert_button = tk.Button(root, text="Convert to Morse", command=convert)
convert_button.grid(row=1, column=0, pady=5, padx=5)

# Create change mode button
change_button = tk.Button(root, text="Change", command=toggle_converter_mode)
change_button.grid(row=1, column=1, pady=5, padx=5)

# Create output frame with vertical scrollbar
output_frame = tk.Frame(root)
output_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")
output_frame.grid_columnconfigure(0, weight=1)
output_frame.pack_propagate(False)  # Prevent resizing to fit contents

output_scrollbar = tk.Scrollbar(output_frame)
output_scrollbar.pack(side="right", fill="y")

output_text = tk.Text(output_frame, wrap="word", yscrollcommand=output_scrollbar.set)
output_text.pack(side="left", fill="both", expand=True)

output_scrollbar.config(command=output_text.yview)

# Set default text and configure color and opacity
mode = "Text to Morse"  # Initial mode
update_output_hint()
output_text.tag_config("error", foreground="red")
output_text.config(fg="gray", state=tk.DISABLED)

# Set focus on the input text area
input_text_area.focus_set()

root.mainloop()
