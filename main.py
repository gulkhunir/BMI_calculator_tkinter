import tkinter

window = tkinter.Tk()
window.title("BMI Calculator Tkinter")
window.minsize(width=300, height=150)


def calc_bmi():
    classification = ["Under Weight", "Normal", "Over Weight", "Obesity (Class I)", "Obesity (Class II)",
                      "Extreme Obesity"]

    w_input = wei_entry.get()
    h_input = hei_entry.get()
    if w_input == "" or h_input == "":
        result_label.config(text="Enter both weight and height")
    else:
        try:
            bmi = (float(w_input) / (float(h_input) / 100) ** 2)
            for i in range(len(classification)):
                if bmi < 18.5:
                    i = 0
                elif bmi < 24.9:
                    i = 1
                elif bmi < 29.9:
                    i = 2
                elif bmi < 34.9:
                    i = 3
                elif bmi < 39.9:
                    i = 4
                elif bmi > 40:
                    i = 5
            result_label.config(text=f"Your Bmi is {round(bmi,2)}. You are {classification[i]}!")
        except:
            result_label.config(text="Enter a valid number")


wei_label = tkinter.Label(text="Enter Your Weight (kg)")
wei_label.pack()
wei_entry = tkinter.Entry(width=10)
wei_entry.pack()
hei_label = tkinter.Label(text="Enter Your Height (cm)")
hei_label.pack()
hei_entry = tkinter.Entry(width=10)
hei_entry.pack()
calc_button = tkinter.Button(text="Calculate", command=calc_bmi)
calc_button.pack()
result_label = tkinter.Label()
result_label.pack()

window.mainloop()
