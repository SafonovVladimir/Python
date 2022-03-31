class Axe:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


if __name__ == '__main__':
    axe = Axe(x=5, y=18)
#
print(axe.x)
print(axe.y)

del axe
# print(axe.x)
# print(axe.y)
