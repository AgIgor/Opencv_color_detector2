import json

class Leds:
    def __init__(self, pos, color):
        self.__pos = pos
        self.__color = color
        self.data = {
            "start": self.__pos,
            "stop": self.__pos + 1,
            "col": [self.__color]
        }


def send_data(led_inicial, led_final, colors):
    list_json = []
    b, g, r = colors
    # print(r, g, b)
    # for i in range(led_inicial, led_final):
    #     list_json.append(Leds(i, [r, g, b]).data)
    # j = json.dumps({"seg": list_json})
    j = json.dumps({"seg": Leds([5, 11], [r, g, b]).data})
    print(j)
    # with open("teste.json", "w") as f:
    #     f.write(j)
    # return j



# if __name__ == '__main__':
    # print(send_data())
    # send_data()
