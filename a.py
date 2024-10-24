with open('Codingal (1).txt', 'w') as f:
    f.write("Hello world.")
f.close()

with open('Codingal (1).txt', 'r') as f:
    data = f.readlines()
    print("Words in the file are: ")
    for line in data:
        word = line.split()
        print(word)
f.close()