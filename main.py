import tkinter

window = tkinter.Tk()
window.title("BMI Calculator Tkinter")
window.minsize(width=300, height=150)


def calc_bmi():
    w_input = int(wei_entry.get())
    h_input = int(hei_entry.get())
    bmi = w_input / (h_input * h_input/10000)
    classification = ["Under Weight", "Normal", "Over Weight", "Obesity (Class I)", "Obesity (Class II)",
                      "Extreme Obesity"]

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
    sonuc_label.config(text=("Your Bmi is " + '{:.2f}'.format(bmi) + ". You are " + classification[i]))


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
sonuc_label = tkinter.Label()
sonuc_label.pack()

window.mainloop()
