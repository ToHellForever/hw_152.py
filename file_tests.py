from file_classes import TxtFile
from file_classes import JsonFile
from file_classes import CsvFile

if __name__ == "__main__":
    document = TxtFile("file.txt")
    document.write("Hello", "World")
    document.append("", "Goodbye", "World")
    print(document.read())
    
    
if __name__ == "__main__":
    document = JsonFile("file.json")
    document.write({"name": "John", "age": 30})
    document.append({"city": "New York"})
    print(document.read())
    

if __name__ == "__main__":
    document = CsvFile("file.csv")
    document.write([{"name": "John", "age": 30}, {"name": "Alice", "age": 25}])
    document.append([{"name": "Bob", "age": 35}])
    print(document.read())