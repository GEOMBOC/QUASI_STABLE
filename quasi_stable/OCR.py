"""
USAGE:
    1- Create class instance from Image_Identifier.
    2- Select a frame and apply either the function "datetime" or "coordinates" to obtain the temporal or spatial coordinates associated with the image.
    3- Print or export the result by calling the class instance attribute you desire. 
    
NOTE: All images must be 
"""
from PIL import Image
import easyocr
import os 
import re

class Image_Identifier:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])
        self.coord = 'NA'
        self.time = 'NA'
        self.date = 'NA'
        self.id = 0
        self.objects = []
        
    def datetime(self,frame):
        """
        This function serves to obtain the temporal coordinates of the frame given.
        To do this, the function starts by cropping the image at the location that shows the time and date.
        It then applies easyocr to obtain the text. 
        
        INPUT: frame, image file path.
        OUTPUT: 
        
        All dates are exported in dd/mm/yy format.
        All times are exported in 24H format.
        """
        image = Image.open(frame)
        crop_rectangle = (0,120,100,200) 
        cropped_image = image.crop(crop_rectangle)
        cropped_image.save('processed_time_frame.png')
        temporal_coord = self.reader.readtext('processed_time_frame.png',paragraph=True)
        temp = re.sub(r'[\W+]','',temporal_coord[0][1]) # We remove all spaces and all non alpha-numeric characters.
        self.date = temp[0:2] + '/' + temp[3:5] + '/' + temp[6:8]
        self.time = temp[8:10] + ':' + temp[11:13] + ':' + temp[14:16]
        os.remove('processed_time_frame.png')
        
    def coordinates(self,frame):
        """
        This function serves to obtain the spatial coordinates of the frame given.
        To do this, the function starts by cropping the image at the location that shows the coordinates. 
        It then applies easyocr to obtain the text.
        
        INPUT: frame, image file path
        OUTPUT: 
        """
        image = Image.open(frame)
        crop_rectangle = (0,40,350,100)
        cropped_image = image.crop(crop_rectangle)
        cropped_image.save('processed_coord_frame.png')
        spatial_coord = self.reader.readtext('processed_coord_frame.png',paragraph=True)
        space = re.sub(r'[\W+]','',spatial_coord[0][1]) # We remove all spaces and all non alpha-numeric characters.
        self.coord = space[0:1]+ '°' + space[2:4] + '\'' + space[4:6] + '.' + space[6:8] + '" N | ' + space[9:11] + '°' + space[12:14] + '\'' + space[14:16] + '.' + space[16:18] + '" W'
        os.remove('processed_coord_frame.png')

# The following is a usage example. Follow steps  
FRAME = '0001.png' # Select image file (frame)
instance2 = Image_Identifier() # Initiate class instance
instance2.coordinates(FRAME) # Call coordinate function with image file as arg.
instance2.datetime(FRAME) # Call datetime function with image file as arg.
# Print the results and cross-validate. 
print('Date of frame: ',instance2.date,'- Time of frame: ',instance2.time,'- Spatial location of frame: ',instance2.coord)