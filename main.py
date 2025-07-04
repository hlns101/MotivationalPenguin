'''
Credit to: Fabio Musanni for showing how to play a GIF file in python tkinter guis
https://youtu.be/KQ0Dddn6sag?si=eCaTK3A41iv7682e

Credit to GeeksForGeeks for Tkinter tutorials
https://www.geeksforgeeks.org/python/python-tkinter-tutorial/

'''


import tkinter as tk

from random import randint

from PIL import Image, ImageTk


class MyApp(tk.Frame):
    def __init__(self, root):
        super().__init__(
            root,
            # light blue bg
            bg='#DAF0F7'
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=0)

        self.create_widgets()

    def create_widgets(self):

        self.label_gif = tk.Label(
            self.main_frame,
            anchor=tk.CENTER,
            bg='WHITE',
            border=0,
            highlightthickness=0
        )
        self.label_gif.grid(column=0, row=0)

        self.gif_frames = self._get_frames('penguin.gif')

        root.after(100, self._play_gif, self.label_gif, self.gif_frames)

        def get_random_quote():
            random_quote = randint(0, quotes.__len__())
            return random_quote

        def button_clicked():
            quote_num = get_random_quote()
            text_var.set(quotes[quote_num-1])
            label.config(textvariable=text_var)

        button = tk.Button(root, text='Click here!',
                           anchor=tk.CENTER,
                           justify="center",
                           width=13,
                           height=3,
                           cursor="hand2",
                           font=("Arial", 10),
                           command=button_clicked,
                           )
        button.pack(padx=0, pady=25)
    def _get_frames(self, img):
        with Image.open(img) as gif:
            index = 0
            frames = []
            while True:
                try:
                    gif.seek(index)
                    frame = ImageTk.PhotoImage(gif)
                    frames.append(frame)
                except EOFError:
                    break

                index += 1

            return frames

    def _play_gif(self, label, frames):

        total_delay = 50
        delay_frames = 100
        for frame in frames:
            root.after(total_delay, self._next_frame, frame, label, frames)
            total_delay += delay_frames
        root.after(total_delay, self._next_frame, frame, label, frames, True)

    def _next_frame(self, frame, label, frames, restart=False):
        if restart:
            root.after(1, self._play_gif, label, frames)
            return

        label.config(
            image=frame
        )

root=tk.Tk()
root.title('Motivational Penguin')
root.geometry('600x500')
root.resizable(width=False, height=False)
root.configure(bg='#DAF0F7')

quotes = ["Keep the beat going!",
          "Every second counts!",
          "Just make it exist first, you can make it good later",
          "Starting is the hardest step",
          "The journey of a thousand miles begins with one step.",
          "The key to success is failure",
          "You'll get through this like you always do",
          "Nothing is impossible, the word itself says ‘I’m possible",
          "Complimenting yourself is so rewarding!",
          "Never underestimate the value of being just who you are",
          "Be wise. Be safe. Be aware",
          "Even when life is so unfair, dont give up.",
          "The best solution to a problem is usually the easiest one",
          "The extraordinary is in what we do, not who we are",
          "That which is lost can be found again",
          "True victory is to give all of yourself, without regret.",
          "Tough times don't last, tough people do",
          "Trust the process",
          "Work hard in silence, let your success be the noise.",
          "Hard work beats talent when talent doesnt work hard",
          "I believe a miracle will happen and a chance will come",
          "The best views comes from the hardest climbs",
          "Dont struggle alone anymore",
          "Remember, you deserve to be here."

          ]

text_var = tk.StringVar()
text_var.set("")

# quote label
label = tk.Label(root, textvariable=text_var,
                 anchor=tk.CENTER,
                 height=5,
                 width=150,
                 font=("Arial", 15, "bold"),
                 bg='#DAF0F7',
                 padx=10,
                 pady=2,
                 )
label.pack()

my_app_instance = MyApp(root)

root.mainloop()
