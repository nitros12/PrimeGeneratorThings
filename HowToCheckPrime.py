import math

class FuckThisFuckThat:
    def __init__(self, statement=None):
        self.statement = statement or "if {} % {}:"

    def _generate_nest(self, number):
        root = math.ceil(math.sqrt(number)) + 1
        base_condition = list()
        for i in range(2, root):
            base_condition.append(
                "{}{}".format("    "*(i), self.statement.format(number, i))
            )
        base_condition.append("{}{}".format("    "*max(root, 2), "raise Exception('Number {} is prime!')".format(number)))

        return base_condition

    def generate_range(self, complete_range):
        complete_list = list()

        if not isinstance(complete_range, range):
            complete_range = range(20)

        for i in complete_range:
            complete_list.append(
            "    {}if number == {}:\n{}".format(
            "el" if i else "", i, "\n".join(self._generate_nest(i))))

        return "\n\n".join(complete_list)


if __name__ == "__main__":
    this = FuckThisFuckThat()
    print("number = int(input('number:'))")
    print("try:")
    print(this.generate_range(range(1000)))
    print("except Exception as e:")
    print("    print(e)")
    print("else:")
    print("    print('Number was not prime')")
