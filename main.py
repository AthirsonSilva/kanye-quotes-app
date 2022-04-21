from tkinter import *
import requests


def get_quote():
    '''
    A Kanye West quotes generator

    This function when triggered through the click of the
    Kanye button, requests the Kanye Rest API to return a
    random Kanye West quote in JSON format
    '''

    response = requests.get(url='https://api.kanye.rest/')
    response.raise_for_status()
    
    data = response.json()
    quote = data['quote']
    canvas.itemconfig(quote_text, text=f'"{quote}"')
    # Write your code here.


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(
    file="/home/athirson/Programming/bootcamp/projects/kanye-quotes-app/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=(
    "Arial", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(
    file="/home/athirson/Programming/bootcamp/projects/kanye-quotes-app/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
