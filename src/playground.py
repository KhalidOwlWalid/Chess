
class Alia:

    def __init__(self, love):
        self.love = love
        self.tell_alia()

    def tell_alia(self):
        
        if self.love == "I love you":
            print(self.love)
        else:
            print("I cant tell you now")
        

if __name__ == '__main__':
    sentence = "Hi"
    Alia(sentence)