

def main():
    
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
    print(file_contents)
    print(len(file_contents.split()))

#def wordcount():
    #with open('./books/frankenstein.txt') as f:
     #   file_contents = f.read()
    #print(len(file_contents.split()))
main()