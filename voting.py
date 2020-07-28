import sys
import requests


def get_top_question(N, label):
    params = {
        "order": "desc",
        "sort": "votes",
        "tagged": label,
        "pagesize": N,
        "site": "stackoverflow.com",
    }
    resp = requests.get("https://api.stackexchange.com/2.2/questions", params=params)
    return resp.json()


def get_top_answer(N, label):
    try:
        params = {
            "order": "desc",
            "sort": "votes",
            "pagesize": 1,
            "site": "stackoverflow.com",
        }
        for i in range(int(N)):
            title = get_top_question(N, label).get("items")[i].get("title")
            question_id = get_top_question(N, label).get("items")[i].get("question_id")
            resp_answer = requests.get(
                "https://api.stackexchange.com/2.2/questions/{}/answers".format(
                    question_id
                ),
                params=params,
            ).json()
            answer_id = resp_answer.get("items")[0].get("answer_id")
            print("label{}: {}".format(i, title))
            print(
                "link{}: /https://stackoverflow.com/questions/{}".format(i, answer_id)
            )
    except IndexError:
        print("input another question")


def main():
    try:
        if len(sys.argv) != 3:
            print(
                "input 2 arguments by the way: number of questions and question label"
            )
            sys.exit()
        N = int(sys.argv[1])
        label = sys.argv[2]
        if N <= 0:
            print("input number > 0")
        get_top_answer(N, label)
    except ValueError:
        print("input with N is a number!")


if __name__ == "__main__":
    main()
