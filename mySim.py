"""

Space Station Simulation
Using SimPy and Tkinter


"""

import numpy as np
import simpy
from tkinter import *
import tkinter.scrolledtext as tkscrolled

HOUR = 60                                  # 60 minutes in a hour
SIM_YEAR = 1                               # How many years will continue to simulate
HUMAN_NUMBER = 5                           # How many humans are in the simulation
YEAR = 5                                 # 365 days in a year
DAY = 24 * HOUR                            # 24 hours in a day
MY_SIM_TIME = DAY*YEAR*SIM_YEAR            # Simulation works for a year
WORK_VARIANCE = 2                          # Variance of work time
MEAL_VARIANCE = 3                          # Variance of meal preparation
BREATH_VARIANCE = 1                        # Variance inhaling in a minute
WORK_TIME = 0.75 * HOUR                    # Average work time in minutes
BREAK_TIME = 0.25 * HOUR                   # Average break time between work times in minutes
WORK_NUMBER = 8                            # How many times they would work in a day
TOTAL_MEAL_TIME = 1.5 * HOUR               # Meal time in minutes
MEAL_READY_TIME = 0.5 * HOUR               # Meal preparations in minutes
RELAXATION_TIME = 3.5 * HOUR               # Relaxation time in minutes (Watch a movie or workout)
SLEEP_TIME = 8 * HOUR                      # Sleep time of every human
BREATH_NUMBER = 15                         # Average breath number of a human in a minute
OXYGEN_CONSUMPTION_SECOND = 2              # Average oxygen consumption of a human in a second
TOTAL_OXYGEN_CONSUMPTION = 0               # General oxygen consumption of the system
AVERAGE_WATER_WASTE = 350                  # Average water waste in liter
AVERAGE_CALORIE_REQUIREMENT = 2000         # Average calorie requirement for a human
CALORIE_VARIANCE = 100                     # Variance of required calories
TOTAL_CALORIE_CONSUMPTION = 0              # Total calorie consumption during the simulation
WATER_RECYCLE = 0.15                       # Rate of wasted water in recycling
WATER_VARIANCE = 50                        # Variance of consumption of water for a human in a day


class Human(object):

    def __init__(self, env, name):
        self.env = env
        self.name = name

    def food(self, number):
        calorie_requirement = int(np.random.normal(AVERAGE_CALORIE_REQUIREMENT, CALORIE_VARIANCE))
        temp = TOTAL_CALORIE_CONSUMPTION + calorie_requirement

        print("\tToday Subject consumed %d calorie"
              % calorie_requirement)

        temp2 = "\tToday Subject consumed %d calorie" % calorie_requirement
        changeText(text=str(temp2), number=number)

        globals().update(TOTAL_CALORIE_CONSUMPTION=int(temp))

    def oxygen(self, rate,  time, number):
        oxygen_consumption = int(np.random.normal(BREATH_NUMBER, BREATH_VARIANCE))
        output = oxygen_consumption / OXYGEN_CONSUMPTION_SECOND * time * rate

        print("Subject consumed %d grams oxygen"
              % output)
        temp = TOTAL_OXYGEN_CONSUMPTION + output

        globals().update(TOTAL_OXYGEN_CONSUMPTION=int(temp))

        temp2 = "Subject consumed %d grams oxygen" % output
        changeText(text=str(temp2), number=number)

    def water():
        water_consumption = int(np.random.normal(AVERAGE_WATER_WASTE, WATER_VARIANCE))
        output = water_consumption * WATER_RECYCLE

        water_waste = HUMAN_NUMBER * output * YEAR *SIM_YEAR
        print("Total water wasted by human %d" % water_waste)
        return "Total water wasted by human %d" % water_waste

    def waking_up(self, number):

        preparation_time = int(np.random.normal(MEAL_READY_TIME, MEAL_VARIANCE))
        meal_time = TOTAL_MEAL_TIME - preparation_time

        print("Subject spend %d minute for the meal preparation. So Subject have %d minutes to eat "
              % (preparation_time, meal_time))
        temp = "Subject spend %d minute for the meal preparation. So Subject have %d minutes to eat " % (preparation_time, meal_time)

        changeText(text=str(temp), number=number)

        Human.oxygen(self, 1, TOTAL_MEAL_TIME ,number)


        return TOTAL_MEAL_TIME

    def morning_work_hour_time(self, number):

        total_worktime = 0
        total_breaktime = 0

        for i in range(int(WORK_NUMBER/2)):

            work_time = int(np.random.normal(WORK_TIME, WORK_VARIANCE))
            break_time = HOUR - work_time
            print("This Subject should work %d minutes and break for %d minutes" % (work_time, break_time))
            total_worktime += work_time
            total_breaktime += break_time

        print("This Subject worked for %d minutes and breaks for %d minute in total before meal"
              % (total_worktime, total_breaktime))

        temp = "This Subject worked for %d minutes and breaks for %d minute in total before meal" % (total_worktime, total_breaktime)

        changeText(text=str(temp), number=number)

        time = (total_worktime + total_breaktime)
        Human.oxygen(self, 1.25, time, number)

        return time

    def lunch_time(self, number):

        preparation_time = int(np.random.normal(MEAL_READY_TIME, MEAL_VARIANCE))
        meal_time = TOTAL_MEAL_TIME - preparation_time

        print("Subject spend %d minute for the meal preparation. So they have %d minutes to eat "
              % (preparation_time, meal_time))

        temp = "Subject spend %d minute for the meal preparation. So they have %d minutes to eat " % (preparation_time, meal_time)

        changeText(text=str(temp), number=number)

        Human.oxygen(self, 1, TOTAL_MEAL_TIME, number)

        return TOTAL_MEAL_TIME

    def evening_work_hour_time(self, number):

        total_worktime = 0
        total_breaktime = 0

        for i in range(int(WORK_NUMBER/2)):

            work_time = int(np.random.normal(WORK_TIME, WORK_VARIANCE))
            break_time = HOUR - work_time
            print("This Subject should work %d minutes and break for %d minutes" % (work_time, break_time))
            total_worktime += work_time
            total_breaktime += break_time

        print("This Subject worked for %d minutes and breaks for %d minute in total before meal"
              % (total_worktime, total_breaktime))

        temp = "This Subject worked for %d minutes and breaks for %d minute in total before meal" % (total_worktime, total_breaktime)

        changeText(text=str(temp), number=number)


        time = (total_worktime + total_breaktime)

        Human.oxygen(self, 1.25, time,number)

        return time

    def dinner_time(self, number):

        preparation_time = int(np.random.normal(MEAL_READY_TIME, MEAL_VARIANCE))
        meal_time = TOTAL_MEAL_TIME - preparation_time

        print("Subject spend %d minute for the meal preparation. So Subject have %d minutes to eat "
              % (preparation_time, meal_time))

        temp = "Subject spend %d minute for the meal preparation. So Subject have %d minutes to eat " % (preparation_time, meal_time)

        changeText(text=str(temp), number=number)

        Human.oxygen(self, 1, TOTAL_MEAL_TIME, number)

        return TOTAL_MEAL_TIME

    def relax_time(self, number):

        Human.oxygen(self, 1, RELAXATION_TIME, number)

        return RELAXATION_TIME

    def sleep_time(self, number):

        Human.oxygen(self, 0.75, SLEEP_TIME, number)
        Human.food(self,number)
        return SLEEP_TIME

def setup():

    resources = []

    for number in range(HUMAN_NUMBER):

        multienv = simpy.Environment()
        simpy.Environment()
        human = Human(multienv, number)
        resources.append([multienv, human])

    return resources

def pro(env, human):
    old_time = env.now
    yield env.timeout(human.waking_up(human.name))
    new_time = env.now - old_time
    print("\n\tBreakfast end after %d minutes for human %d\n" % (new_time, human.name))
    temp = "\n\tBreakfast end after %d minutes for human %d\n" % (new_time, human.name)
    changeText(text=str(temp), number=human.name)


def pro2(env, human):
    old_time = env.now
    yield env.timeout(human.morning_work_hour_time(human.name))
    new_time = env.now - old_time
    print("\n\tWork time end after %d minutes for human %d\n" % (new_time, human.name))
    temp = ("\n\tWork time end after %d minutes for human %d\n" % (new_time, human.name))
    changeText(text=str(temp), number=human.name)



def pro3(env, human):
    old_time = env.now
    yield env.timeout(human.lunch_time(human.name))
    new_time = env.now - old_time
    print("\n\tLunch end after %d minutes for human %d\n" % (new_time, human.name))
    temp = "\n\tLunch end after %d minutes for human %d\n" % (new_time, human.name)
    changeText(text=str(temp), number=human.name)


def pro4(env, human):
    old_time = env.now
    yield env.timeout(human.evening_work_hour_time(human.name))
    new_time = env.now - old_time
    print("\n\tWork time end after %d minutes for human %d\n" % (new_time, human.name))
    temp = "\n\tWork time end after %d minutes for human %d\n" % (new_time, human.name)
    changeText(text=str(temp), number=human.name)


def pro5(env, human):
    old_time = env.now
    yield env.timeout(human.dinner_time(human.name))
    new_time = env.now - old_time
    print("\n\tDinner time end after %d minutes for human %d\n" % (new_time, human.name))
    temp = "\n\tDinner time end after %d minutes for human %d\n" % (new_time, human.name)
    changeText(text=str(temp), number=human.name)


def pro6(env, human):
    old_time = env.now
    yield env.timeout(human.relax_time(human.name))
    new_time = env.now - old_time
    print("\n\tRelaxatation time end after %d minutes for human %d\n" % (new_time, human.name))
    temp = "\n\tRelaxatation time end after %d minutes for human %d\n" % (new_time, human.name)
    changeText(text=str(temp), number=human.name)


def pro7(env, human):
    old_time = env.now
    yield env.timeout(human.sleep_time(human.name))
    new_time = env.now - old_time
    print("\n\tSleep time end after %d minutes for human %d\n" % (new_time, human.name))
    temp = "\n\tSleep time end after %d minutes for human %d\n" % (new_time, human.name)
    changeText(text=str(temp), number=human.name)



def start():
    results = []
    res = setup()
    print(SIM_YEAR)
    globals().update(MY_SIM_TIME = DAY * YEAR * SIM_YEAR)
    while res[0][0].now < MY_SIM_TIME:
        for i in res:
            i[0].process(pro(i[0], i[1]))
            i[0].run()

        for i in res:
            i[0].process(pro2(i[0], i[1]))
            i[0].run()

        for i in res:
            i[0].process(pro3(i[0], i[1]))
            i[0].run()

        for i in res:
            i[0].process(pro4(i[0], i[1]))
            i[0].run()

        for i in res:
            i[0].process(pro5(i[0], i[1]))
            i[0].run()

        for i in res:
            i[0].process(pro6(i[0], i[1]))
            i[0].run()

        for i in res:
            i[0].process(pro7(i[0], i[1]))
            i[0].run()
    results.append(Human.water())
    print("Total of oxygen consuption of system %d grams of oxygen" %TOTAL_OXYGEN_CONSUMPTION)
    print("To produce %d gram oxygen %d gram water should be electrolysed" % (TOTAL_OXYGEN_CONSUMPTION , ((TOTAL_OXYGEN_CONSUMPTION/1000) * 36) / 22.4))
    print("Total calorie requirement all space staion is %d calorie" %TOTAL_CALORIE_CONSUMPTION)

    results.append("Total of oxygen consuption of system %d grams of oxygen" %TOTAL_OXYGEN_CONSUMPTION)
    results.append("To produce %d gram oxygen %d gram water should be electrolysed" % (TOTAL_OXYGEN_CONSUMPTION , ((TOTAL_OXYGEN_CONSUMPTION/1000) * 36) / 22.4))
    results.append("Total calorie requirement all space staion is %d calorie" %TOTAL_CALORIE_CONSUMPTION)

    return results

# start()


TEXTBOX = []


def changeText(text, number):
    text = text + "\n"
    TEXTBOX[number].insert(INSERT, text)
    TEXTBOX[number].see(END)

def run():
    globals().update(HUMAN_NUMBER=int(human_number.get()))
    globals().update(SIM_YEAR=int(year_number.get()))

    mainBox = tkscrolled.ScrolledText(root, width=64, height=10)
    mainBox.config(font=("consolas", 10), undo=True, wrap='word')
    mainBox.grid(row=3, column=1)

    for i in range(HUMAN_NUMBER):
        temp = "Human %d" % i
        Textbox = tkscrolled.ScrolledText(mainBox, width=60, height=10)
        Textbox.config(font=("consolas", 10), undo=True, wrap='word')
        Textbox.see(END)
        Label(mainBox, text=temp).grid(row=(((int(i/4))+2)*2)-1, column=(i % 4))
        Textbox.grid(row=((int(i/4))+2)*2, column=(i % 4))
        TEXTBOX.append(Textbox)

    results = start()

    top = Toplevel()
    top.title("Results of Simulation")
    resultText = ""
    for i in range(len(results)) :
        resultText +=results[i]
        resultText += "\n"
    msg = Message(top, text=resultText)
    msg.config(width=500)
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()



root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

Label(root, text="Human Number").grid(row=0, column=0)
human_number = Scale(root, from_=1, to=20, orient=HORIZONTAL)
human_number.grid(row=0, column=1)

Label(root, text="Year").grid(row=1, column=0)
year_number = Scale(root, from_=1, to=10, orient=HORIZONTAL)
year_number.grid(row=1, column=1)

b = Button(root, text="Run Simulation", command=run)
b.grid(row=1, column=2)

root.mainloop()

