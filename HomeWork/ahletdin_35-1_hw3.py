class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__memory


    def __str__(self):
        return f'cpu: {self.cpu} memory: {self.memory}'


    def __gt__(self, other):
        return self.__cpu > other

    def __lt__(self, other):
        return self.__cpu < other

    def __ge__(self, other):
        return self.__cpu >= other

    def __le__(self, other):
        return self.__cpu <= other

    def __eq__(self, other):
        return self.__cpu == other

    def __ne__(self, other):
        return self.__cpu != other

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value


    def call(self, sim_card_number, call_to_number):
        return f"идет звонок на номер телефона-{call_to_number}" \
               f"с сим карты-{self.__sim_cards_list[sim_card_number]}"


    def __str__(self):
        return f'sim card list: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    def use_gps(self, location):
        return f"вы сейчас находитесь {location}"

    def __str__(self):
        return f'cpu: {self.cpu} memory: {self.memory} sim card list: {self.sim_cards_list}'


asus = Computer(23, 16)

iphone = Phone(['Beeline', 'O!'])

redmi = SmartPhone(650, 128,  ["Beeline", "o!", "MegaCom"])

huawei = SmartPhone(600, 32, ["Beeline", "o!", "MegaCom"])

print(redmi.use_gps("гум"))
print(asus.make_computations())
print(asus)
print(iphone)
print(redmi)
print(huawei)




