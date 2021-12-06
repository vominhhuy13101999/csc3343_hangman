def new_text_file(filename, content):
    """Create a new text file and add content to it"""
    file = open(filename, "w")
    file.write(content)
    file.close()
    print('File {} created, {} bytes'.format(filename, len(content)))
    if __name__ == "__main__":
        filename = sys.argv[1]
        content = sys.argv[2]
        new_text_file(filename, content)
