from file_classes import TxtFile

if __name__ == "__main__":
    document = TxtFile("file.txt")
    document.write("Hello", "World")
    document.append("", "Goodbye", "World")
    print(document.read())