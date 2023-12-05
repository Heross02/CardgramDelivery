import os
import random
from tkinter import *
from PIL import Image, ImageTk

class EidCard(Tk):
    def __init__(self):
        super().__init__()
        self.title("Eid Mubarak!")

        current_dir = os.path.dirname(os.path.abspath(__file__))

        image_path = os.path.join(current_dir, "eid_al_adha_background.jpg")

        # Load the background image
        self.background_image = Image.open(image_path)
        self.background_image = self.background_image.resize((800, 600))  # Initial size
        self.background = ImageTk.PhotoImage(self.background_image)

        # Create a canvas to display the background image
        self.canvas = Canvas(self, width=800, height=600)
        self.canvas.create_image(0, 0, image=self.background, anchor='nw', tags="background")
        self.canvas.pack(fill=BOTH, expand=YES)

        # Add Happy Eid Al-Adha Amin text
        self.text = self.canvas.create_text(self.background.width() / 1.4, 100, text="Happy Eid Al-Adha\n Amin\n from CSE-350 class",
                                            font=("Arial", 40), fill="brown")

        # Load the sheep image
        sheep_image = Image.open("sheep.png")

        # Create a button to hide the sheep
        self.hide_sheep_button = Button(self, text="Hide Sheep", command=self.hide_sheep)
        self.hide_sheep_button.pack(side=LEFT, anchor=NW)

        # Create a button to reveal the sheep
        self.reveal_sheep_button = Button(self, text="Reveal Sheep", command=self.reveal_sheep, state=DISABLED)
        self.reveal_sheep_button.pack(side=LEFT, anchor=NW)

        # Create a button to toggle the star lights
        self.star_lights_button = Button(self, text="Toggle Star Lights", command=self.toggle_lights)
        self.star_lights_button.pack(side=LEFT, anchor=NW)

        # Create a sheep
        self.original_sheep = ImageTk.PhotoImage(sheep_image)
        sheep_width = self.original_sheep.width()
        sheep_height = self.original_sheep.height()
        self.sheep_sprite = self.canvas.create_image(800 - sheep_width // 2, 600 - sheep_height // 2, image=self.original_sheep)
        self.sheep = self.original_sheep  # Save reference to the original sheep image

        # Create star lights
        self.star_lights = []
        for _ in range(50):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            dx = random.choice([-1, 1]) * random.randint(1, 3)
            dy = random.choice([-1, 1]) * random.randint(1, 3)
            star = self.canvas.create_oval(x, y, x + 3, y + 3, fill='white', outline='gold')
            self.star_lights.append((star, dx, dy))

        self.is_light_on = True
        self.is_sheep_hidden = False
        self.flash_text()
        self.move_sheep()
        self.move_stars()

        # Call the function to generate the Eid template
        self.generate_eid_template()

        # Disable window resizing
        self.resizable(False, False)

    def hide_sheep(self):
        self.canvas.delete(self.sheep_sprite)
        self.hide_sheep_button.config(state=DISABLED)
        self.reveal_sheep_button.config(state=NORMAL)
        self.is_sheep_hidden = True

    def reveal_sheep(self):
        sheep_width = self.original_sheep.width()
        sheep_height = self.original_sheep.height()
        self.sheep_sprite = self.canvas.create_image(800 - sheep_width // 2, 600 - sheep_height // 2, image=self.sheep)
        self.hide_sheep_button.config(state=NORMAL)
        self.reveal_sheep_button.config(state=DISABLED)
        self.is_sheep_hidden = False

    def toggle_lights(self):
        if self.is_light_on:
            for star_info in self.star_lights:
                self.canvas.itemconfig(star_info[0], state='hidden')
            self.is_light_on = False
            self.star_lights_button.config(text="Show Star Lights")
        else:
            for star_info in self.star_lights:
                self.canvas.itemconfig(star_info[0], state='normal')
            self.is_light_on = True
            self.star_lights_button.config(text="Hide Star Lights")

    def move_sheep(self):
        if not self.is_sheep_hidden:
            # Sheep doesn't move in this version
            pass

        self.after(100, self.move_sheep)

    def move_stars(self):
        for i, star_info in enumerate(self.star_lights):
            star, dx, dy = star_info
            x1, y1, x2, y2 = self.canvas.coords(star)
            if x2 > 800 or x1 < 0:
                dx = -dx
            if y2 > 600 or y1 < 0:
                dy = -dy
            self.canvas.move(star, dx, dy)
            self.star_lights[i] = (star, dx, dy)
        self.after(50, self.move_stars)

    def flash_text(self):
        current_color = self.canvas.itemcget(self.text, 'fill')
        new_color = "brown" if current_color == "white" else "white"
        self.canvas.itemconfig(self.text, fill=new_color)
        self.after(500, self.flash_text)

    def generate_eid_template(self):
        print("Generating Eid template...")

        # Read content from a text file
        with open("eid_el-adha_template.txt", "r") as file:
            template_content = file.read()

        print("Eid template generated!")

    def run(self):
        # Run the Tkinter application
        self.mainloop()

def main():
    eid_card = EidCard()
    eid_card.mainloop()

# Only run the Tkinter application if this script is executed directly
if __name__ == "__main__":
    main()
