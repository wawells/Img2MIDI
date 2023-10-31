import cv2

#get image
#image = input("Enter image path here: ")

image = cv2.imread('sunflower.jpg')

if image is None:
    print("Error loading image")
else:
    #image validation
    height, width, channels = image.shape
    
    if channels == 3:
        b, g, r = cv2.split(image)
        

    else:
        print("Image does not contain RGB values")
    