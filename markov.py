from PIL import Image

REL_PATH = "C:/Users/User/Desktop/CC/Markov1/images/"

def main():

    im = Image.open(REL_PATH + "lakers.png")
    im.rotate(45).show()

    return








if __name__ == "__main__": 
    main() 