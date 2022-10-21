class Random:
    def __init__(self, k):
        self.k = k

    def print_value(self):
        return self.k

if __name__ == "__main__":
    r = Random(10)
    print(r.print_value())

