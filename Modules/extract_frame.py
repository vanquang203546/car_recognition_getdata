import cv2
import os

def create_folder(*names):
    for name in names:
        try:
            os.mkdir(name)
        except:
            print("Already exist {}".format(name))
def create_folder_save(type, path_folder_save=r'Results_frames'):
    try:
        os.mkdir(os.path.join(path_folder_save, 'run0'))
        path_folder_save=os.path.join(path_folder_save, 'run0')
    except:
        id=max(int(i.split('run')[-1]) for i in os.listdir(path_folder_save) if 'run' in i)+1
        path_folder_save=os.path.join(path_folder_save, 'run' + str(id))
        os.mkdir(path_folder_save)
    path_images_save = os.path.join(path_folder_save, type)
    create_folder(path_images_save)
    return path_images_save

def frame_per_second(path_video=None, type=None, frame_index=1, n=3):
    path_folder_save = create_folder_save(type)
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
            cv2.imwrite(os.path.join(path_folder_save,file_save_frame), frame)
        frame_index += 1
    capture.release()
    return frame_index