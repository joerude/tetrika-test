def index_of_first_zero(array: str) -> int:
    first_zero = array.find("0")
    return first_zero - 1


if __name__ == "__main__":
    print(index_of_first_zero("111111111110000000000000000"))
    print(index_of_first_zero("3333322222111111111110000000000000000"))
    print(index_of_first_zero("6666663333322222111111111110000000000000000"))
