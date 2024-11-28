def main():
    counts = {'p': 0}
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        text = file_contents.lower()
        #text.count()
        for char in text:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    print("--- Begin report of ", path, " ---")
    for key in counts:
        print("The '", key, "' character was found ", counts[key], " times")
    print("--- End report ---")

main()
