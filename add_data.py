def add_data() -> None:
    """
    function to add data points to the file if there is no pre filled in file provided
    :return: None
    """

    text: dict[str, str] = {"dimension": "input dimension size\n", "data": "input data number with spaces or stop\n"}
    # get number of variables
    text_dimension: str = ""

    while not text_dimension.isnumeric():
        text_dimension = input(text["dimension"])

    number_dimension: int = int(text_dimension)
    # main part of writing to file
    data: str = ""

    with open("data.csv", "w") as sheet:

        while data != "stop":
            data = input(text["data"]).strip()

            if not data:
                continue
            elif data == "stop":
                break
            else:
                sliced_data: [str] = data.split(" ")
                data_error: list[bool | str] = [False, "There is a non number"]

                if len(sliced_data) > number_dimension:
                    print("dimensional error")
                    continue

                for data_slice in sliced_data:
                    if not data_slice.isnumeric():
                        data_error[0] = True
                        print(data_error[1])
                        break

                if data_error[0] is True:
                    continue
                else:
                    if len(sliced_data) == number_dimension:
                        sheet.write(",".join(sliced_data) + "\n")
                    else:
                        sheet.write(",".join(sliced_data) + "," +
                                    ",".join(["0" for _ in range(number_dimension - len(sliced_data))]) + "\n")


def main():
    pass


if __name__ == "__main__":
    main()
