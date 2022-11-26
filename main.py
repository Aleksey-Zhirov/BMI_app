from tkinter import *

root = Tk()
root.title('BMI app')
root.geometry('640x480')
root.resizable(width=False, height=False)


# Widgets
label_for_height = Label(
    text='Введите ваш рост (м.)',
    font=('Consolas', '18')
)
entry_for_height = Entry(
    width=18,
    font=('Consolas', '30'),
    justify=CENTER
)
label_for_weigth = Label(
    text='Введите ваш вес (кг.)',
    font=('Consolas', '18')
)
entry_for_weigth = Entry(
    width=18,
    font=('Consolas', '30'),
    justify=CENTER
)


def calculate():
    height = float(entry_for_height.get())
    weigth = float(entry_for_weigth.get())

    # bmi = weigth / (height **2)

    bmi = round(weigth / (height ** 2), 2)

    if bmi < 15.99:
        status = 'Выраженный дефицит массы тела'
    elif bmi > 16 and bmi < 18.49:
        status = 'Недостаточная масса тела'
    elif bmi > 18.5 and bmi < 24.99:
        status = 'Норма'
    elif bmi > 25 and bmi < 29.99:
        status = 'Предожтрение'
    elif bmi > 30 and bmi < 34.99:
        status = '1-ая степень ожирения'
    elif bmi > 35 and bmi < 39.99:
        status = '2-ая степень ожирения'
    else:
        status = '3-ая степень ожирения'

    result_label = Label(
        text=f'''
    Ваш ИМТ: {bmi} кг/м2\n
    Это {status}
        ''',
        font=('Consolas', '18')
    )
    result_label.pack()


submit_button = Button(
    text='Расчитать',
    font=('Consolas', '16'),
    command=calculate
)


# Placing widgets
label_for_height.pack()
entry_for_height.pack()
label_for_weigth.pack()
entry_for_weigth.pack()
submit_button.pack()


if __name__ == '__main__':
    root.mainloop()
