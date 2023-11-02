import cv2, mido, random

from mido import MidiFile, MidiTrack, Message

class Img2MIDI:

    def __init__(self, filename):
        self.filename = filename
        self.mid = MidiFile()
        self.track = MidiTrack()
        self.mid.tracks.append(self.track)
        self.time = 0


    def analyze(self):
        if len(self.filename) == 0:
            print("Error in filename")
        else:
            image = cv2.imread(self.filename)
            if image is None:
                print("Error loading image")
            else:
                height, width, channels = image.shape

                #image validation
                if channels == 3:
                    self.b, self.g, self.r = cv2.split(image)
                    self.valid = True
                    print(f'Image is {width}px by {height}px')
                else:
                    print("Image does not contain RGB Values")


    def getMidi(self):
        if self.valid:
            #select instrument based on blue (B)
            port = mido.open_output("Output port 1")
            progNum = GET INSTRUMENT HERE FROM BLUE ARRAY

            #select velocity based on blue values(B)
            velocity = GET VELOCITY HERE FROM BLUE VALUES

            #select note based on green (G)
            noteOn = Message("note_on", note = #note here#)
                             
            #increment time
            self.time += random.randint(1,500)
            noteOff = Message("note_off", note = #same note here)
                             
            

filename = input("Enter image path here: ")
analyzer = Img2MIDI(filename)
analyzer.analyse()