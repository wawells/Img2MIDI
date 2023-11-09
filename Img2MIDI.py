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
                    self.getMidi()
                else:
                    print("Image does not contain RGB Values")


    def getMidi(self):
        
           
        count = 0
        while count < len(self.b):
            
            #select instrument based on blue
            curPro = self.b[count]
            if (curPro > 1):
                progNum = (curPro - 1) / 2
                self.track.append(Message('program_change', program=progNum))

                #select velocity based on green
                curVel = self.g[count]
                if (curVel > 1):
                    velocity = (curVel - 1) / 2


                    #select note based on red
                    curNote = self.r[count]
                    if (curNote > 1):
                        note = (curNote - 1) / 2
                        self.track.append(Message("note_on", note = note, velocity = velocity, time = self.time))
                             
                        #increment time
                        self.time += random.randint(1,500)
                        self.track.append(Message("note_off", note = note, velocity = velocity, time = self.time))

        #generate file
        self.mid.save('result.mid')
                             
            

filename = "sunflower.jpg" #input("Enter image path here: ")
analyzer = Img2MIDI(filename)
analyzer.analyze()

