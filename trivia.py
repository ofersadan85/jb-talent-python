import csv


def save_question_row(question_row: list):
    with open("questions.csv", mode="a") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(question_row)

def get_question_row() -> list:
    question = input("Enter a question: ")
    answer = input("Enter a currect answer: ")
    row = [question, answer]
    while True:
        answer = input("Enter more answers: ")
        if answer == "quit":
            break
        row.append(answer)
    return row

def ask_questions() -> int:
    with open("questions.csv") as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            print(line[0])
            
            # index = 1
            # while index < len(line):
            #     print(line[index])
            #     index += 1

            # for index in range(1, len(line)):
            #     print(line[index])

            for index, answer in enumerate(line[1:]):
                print(index + 1, "=>", answer)
            user_answer = input("What is your answer? ")
            if user_answer == "1":
                print("Correct")
            else:
                print("Wrong!")
    return 0


# question_row = get_question_row()
# save_question_row(question_row)
