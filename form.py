from replit import db
from person import Person

year, courses, interests, pref = None, None, None, None
question, state = 1, False


async def get_user_data(message, start=False):
    prompt = "Hi {0.author}, I will ask a few questions to make a profile for you. Please follow the answer format given in the question.\n"

    question_1 = "Enter your current year of study (1, 2, 3, 4, or 5)."
    question_2 = "Enter the course codes for up to 5 of your current classes (e.g., COMP-2310, COMP-2140)."
    question_3 = "Enter up to 5 keywords that describe your interests (e.g., python, fintech, ai, etc.)."
    question_4 = "Enter a number between 1 and 5 for the degree of a match, where 5 is a perfect match."

    global question, year, courses, interests, pref, state
    
    if start:
        state = start
    
    if question == 1 and state:
        await message.author.send(prompt.format(message))
        await message.author.send(question_1)
        question = 2
    
    elif question == 2:
        year = message.content[0]
        await message.author.send(question_2)
        question = 3
    
    elif question == 3:
        courses = message.content
        await message.author.send(question_3)
        question = 4
    
    elif question == 4:
        interests = message.content
        await message.author.send(question_4)
        question = 5
    
    elif question == 5:
        pref = message.content
    
        # Insert user into database
        name = f"{message.author.name}#{message.author.discriminator}"
        person = Person(name, year, courses, interests, pref)
        db[person.user] = str(person)
        # print(year, courses, interests, pref)
        question, state = 1, False  # Reset the sequence
        await message.author.send("Thank you for the information")
        return