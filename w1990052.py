# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1990052
# Date: 22/11/2023 
from graphics import *

student_data = []
student_data_display = []

def student_credits():
    try:
        credits_pass = int(input("\nPlease enter your credits at pass: "))
        if credits_pass not in (0, 20, 40, 60, 80, 100, 120):
            print("Out of range")
            return student_credits()
        
        credits_defer = int(input("Please enter your credits at defer: "))
        if credits_defer not in (0, 20, 40, 60, 80, 100, 120):
            print("Out of range")
            return student_credits()
        
        credits_fail = int(input("Please enter your credits at fail: "))
        if credits_fail not in (0, 20, 40, 60, 80, 100, 120):
            print("Out of range")
            return student_credits()

        credits_total = credits_pass + credits_defer + credits_fail
        if credits_total != 120:
            print("Total incorrect")
            return student_credits()
        
        return credits_pass, credits_defer, credits_fail
                
    except ValueError:
        print("Integer required")
        return student_credits()

def progression_outcome(credits_pass, credits_defer, credits_fail):
    if credits_pass == 120:
        print("Progress")
        outcome_progress = "Progress"
        return outcome_progress
    
    elif credits_pass == 100 and (credits_defer or credits_fail == 20):
        print("Progress (module trailer)")
        outcome_trailer = "Progress (module trailer)"
        return outcome_trailer
    
    elif credits_pass <= 80 and (not credits_fail >= 80):
        print("Do not Progress – module retriever")
        outcome_retriever = "Module retriever"
        return outcome_retriever
    
    else:
        print("Exclude")
        outcome_exclude = "Exclude"
        return outcome_exclude

def count_outcomes(student_data):
    count_progress = student_data.count('Progress')
    count_trailer = student_data.count('Progress (module trailer)')
    count_retriever = student_data.count('Module retriever')
    count_exclude = student_data.count('Exclude')
    count_total = count_progress + count_trailer + count_retriever + count_exclude

    return count_progress, count_trailer, count_retriever, count_exclude, count_total

def progression_outcome_graph():
    win = GraphWin("Progression Outcome Graph", 1000, 600)
    win.setBackground("white")
    histogram_title = Text(Point(225,50), "Histogram results")
    histogram_title.setStyle("bold")
    histogram_title.setSize(20)
    histogram_title.draw(win)
    
    x_axis = Line(Point(100,500), Point(900,500))
    x_axis.draw(win)
    x_axis_label = Text(Point(500,570), "Progression Outcomes")
    x_axis_label.setStyle("bold")
    x_axis_label.setSize(15)
    x_axis_label.draw(win)
    
    count_progress, count_trailer, count_retriever, count_exclude, count_total = count_outcomes(student_data)
    
    progress_bar = Rectangle(Point(150,500), Point(250, 500 - (count_progress * 20)))
    progress_bar.setFill("green")
    progress_bar.draw(win)
    trailer_bar = Rectangle(Point(350,500), Point(450, 500 - (count_trailer * 20)))
    trailer_bar.setFill("green2")
    trailer_bar.draw(win)
    retriever_bar = Rectangle(Point(550,500), Point(650, 500 - (count_retriever * 20)))
    retriever_bar.setFill("yellow")
    retriever_bar.draw(win)
    exclude_bar = Rectangle(Point(750,500), Point(850, 500 - (count_exclude * 20)))
    exclude_bar.setFill("red")
    exclude_bar.draw(win)
    
    count_progress_counter = Text(Point(200, 500 - (count_progress * 20) - 20), count_progress)
    count_progress_counter.draw(win)
    count_trailer_counter = Text(Point(400, 500 - (count_trailer * 20) - 20), count_trailer)
    count_trailer_counter.draw(win)
    count_retriever_counter = Text(Point(600, 500 - (count_retriever * 20) - 20), count_retriever)
    count_retriever_counter.draw(win)
    count_exclude_counter = Text(Point(800, 500 - (count_exclude * 20) - 20), count_exclude)
    count_exclude_counter.draw(win)

    count_total_display = Text(Point(850, 50), str(count_total) + " outcomes in total")
    count_total_display.draw(win)
    
    count_progress_label = Text(Point(200, 520), "Progress")
    count_progress_label.draw(win)
    count_trailer_label = Text(Point(400, 520), "Trailer")
    count_trailer_label.draw(win)
    count_retriever_label = Text(Point(600, 520), "Retriever")
    count_retriever_label.draw(win)
    count_exclude_label = Text(Point(800, 520), "Exclude")
    count_exclude_label.draw(win)
    
    return count_progress, count_trailer, count_retriever, count_exclude

def display_list():
    print("\nPart 2:")
    for item in student_data_display:
        print(*item)

def write_txtfile():
    with open('Progression outcomes.txt', 'w') as txtfile:
        txtfile.write("Part 3:\n")
        for item in student_data_display:
            txtfile.write(' '.join(map(str, item)) + '\n')

def read_txtfile():
    with open('Progression outcomes.txt', 'r') as txtfile:
        open_txtfile = txtfile.read()
        print(open_txtfile)

def main():
    credits_pass, credits_defer, credits_fail = student_credits()
    outcome = progression_outcome(credits_pass, credits_defer, credits_fail)
    student_data.append(outcome)
    student_data_display.append((outcome, '-' , *(credits_pass, credits_defer, credits_fail)))
    count_outcomes(student_data)

while True:
    main()
    user_continue = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
    user_continue.lower()
    if user_continue == 'y':
        continue
    elif user_continue == 'q':
        break
    
progression_outcome_graph()
display_list()
write_txtfile()
read_txtfile()
