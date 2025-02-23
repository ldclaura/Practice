import requests

# question_data = [
#     # {
#     #     "category": "Science: Computers",
#     #     "type": "boolean",
#     #     "difficulty": "medium",
#     #     "question": "The HTML5 standard was published in 2014.",
#     #     "correct_answer": "True",
#     #     "incorrect_answers": [
#     #         "False"
#     #     ]
#     # },
#     # {
#     #     "category": "Science: Computers",
#     #     "type": "boolean",
#     #     "difficulty": "medium",
#     #     "question": "The first computer bug was formed by faulty wires.",
#     #     "correct_answer": "False",
#     #     "incorrect_answers": [
#     #         "True"
#     #     ]
#     # },
# ]
anime_trivia_api = "https://opentdb.com/api.php?amount=10&category=31&type=boolean"
random_trivia_api = "https://opentdb.com/api.php?amount=10&type=boolean"


def get_quote(api):
    response = requests.get(url=api)
    # response.raise_for_status() #raise an error if the request fails
    questions = response.json()
    for _ in questions:
        if _ != "response_code":
            return questions[_]
        #for some fuckin reason I can't just return questions["results"], it gives me a keyerror?
        #since it's only response_code and results, i just made it so if it's not response_code it'll return results.
        #this works


question_data = get_quote(random_trivia_api)