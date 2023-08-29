import cv2
import os

def change_folder(name = None):
    try:
        os.chdir(name)
    except:
        print("Don't exist, creating {}".format(name))
        os.mkdir(name)
        os.chdir(name)
def rescale(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    return cv2.resize(frame, (width, height), cv2.INTER_AREA)
def frame_per_second(path_video=None, type=None, frame_index=1, n=3):
    change_folder('Results_frames')
    change_folder(type)
    capture = cv2.VideoCapture(path_video)
    frame_rate = capture.get(cv2.CAP_PROP_FPS)
    frame_counts = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print('--------------------------------------------------')
    print('| Informations of Video:                         |')
    print('|   *Frame_rate:     {0:10.3f}                  |'.format(frame_rate))
    print('|   *Frame_counts:   {0:10.3f}                  |'.format(frame_counts))
    print('|   *Time videos:    {0:10.3f}                  |'.format(frame_counts/frame_rate))
    print('{0:-^50}'.format('-'))
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        if frame_index % int(frame_rate/n) == 0:
        # if (frame_index % n) == 0:
            file_save_frame = '{}_{}_{}.jpg'.format(type, 'frame', frame_index)
            cv2.imwrite(file_save_frame, frame)
        frame_index += 1
    capture.release()
    change_folder('../../Results_frames')
    return frame_index