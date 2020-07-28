import requests
import sys
import bs4


def get_lottery_results():
    resp = requests.get("https://ketqua.net")
    tree = bs4.BeautifulSoup(resp.text, features="html.parser")
    table = tree.find("table", attrs={"id": "result_tab_mb"}).find("tbody")
    awards = []
    for line in table.find_all("tr"):
        td = line.find_all("td")
        if len(td) > 1:
            for i in range(len(td)):
                awards.append(td[i].text)
    return awards


def get_print_lots():
    for i in get_lottery_results():
        if get_lottery_results[i] == isdigit():
            return get_lottery_results[i]


def check_lots(input_lot):
    won = 0
    for i in input_lot:
        for j in get_lottery_results():
            if i[:] == j[-2:]:
                won += 1
    if won == 0:
        print('Good luck for the next time!')
        print(get_lottery_results())
    else:
        print("You won {} time".format(won))


def main():
    if len(sys.argv) < 2:
        print('please input an INTEGER with the format:'
              'python(3) ketqua.py [Integer]')
    else:
        input_lot = sys.argv[1:]
        check_lots(input_lot)


if __name__ == "__main__":
    main()
