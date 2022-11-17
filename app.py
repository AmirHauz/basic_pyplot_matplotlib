import matplotlib.pyplot as plt


def visualization(ls):
    plt.plot(ls)
    plt.ylabel('some numbers')
    plt.show()


if __name__ == "__main__":
    visualization([1, 3, 2, 4])
