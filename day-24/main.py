# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("my_file.txt", mode="a") as file:
    file.write(input("write smth\n"))
with open("my_file.txt", mode="r") as file:
    content = file.read()
    print(content)
