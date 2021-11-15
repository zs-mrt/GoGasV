import os
import time
import datetime
from numpy.core.numeric import NaN
import cv2
import numpy as np
import pandas as pd


RootPath = "Z:\Privat\GasVid\Videos\MOV_"
ExcelPath = "Z:\Privat\GasVid\GasVid_Logging_File.xlsx"
OutputFile = "Z:\Privat\GasVid\Frames"
file_name = "undef"

f = '%H:%M:%S'




class Video(object):
    def __init__(self) -> None:
        pass    

    def videoOpen(self, path) -> int:
        video = cv2.VideoCapture(path)
        if video.isOpened():
            frame_fps = video.get(5)
            num_frames = video.get(7)
            print("The fps of frames is %s" %(num_frames/frame_fps))
            return 1
        else:
            print("Error")
            return 0

    def ReadFile(self, path) -> str:
        df = pd.read_excel(io = path)
        for i in range(len(df)-3): #exclude the Notes
            row = df.iloc[i].values
            Distance = row[1]
            if Distance == 18.6 or Distance == 8.8:
                #according to the GasVid, we don't consider the video captured at distance 18.6 and 8.8
                continue
            else:
                Nr = row[0]
                ShootingTime = row[2]
                print(row[3])
                print(type(row[3]))
                #Time_L0 = time.mktime(time.strptime(row[3], f))
                #print(type(Time_L0))
                #print(Time_L0)
                #break
                Time_L1 = row[4]
                Position = row[5]
                VideoPath = RootPath + str(Nr) + ".mp4"
                status = self.videoOpen(VideoPath)
                #print(status)
 

    

class VideoToFrame:
    def __init__(self) -> None:
        pass
    def videoOpen(self, path) -> int:
        video = cv2.VideoCapture(path)
        if video.isOpened():
            print("Open")
            frame_fps = video.get(5)
            print("The fps of frames is %s" %(frame_fps))
            return 1
        else:
            print("Error")
            return 0


#for 3DCNN, the frames are need to be converted into subvideos.
class FrameToSubvideo:
    def __init__(self) -> None:
        pass
    #shape of frames is 320 x 240 x 1


def main():

    Vid = Video()
    Vid.ReadFile(ExcelPath)

if __name__ == "__main__":
    main()


