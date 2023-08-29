import os
from Modules.extract_frame import frame_per_second
from Modules.change_id_label import change_id_label
path = os.getcwd()
print(path)

def main():
    folder_video = r"C:/Users/PC/OneDrive - Hanoi University of Science and Technology/Desktop/Video/video_test"
    type = 'traffic_camera_test'
    frame_index = 0 #start index
    n = 5           #5frames/s
    # for video in os.listdir(folder_video):
    #     path_video = os.path.join(folder_video, video)
    #     frame_index = frame_per_second(path_video, type, frame_index, n)
    #     frame_index += n
    # os.chdir(path)

    folder_label = r'C:/Users/PC/OneDrive - Hanoi University of Science and Technology/Desktop/Extract_frames/data_test/labels'
    change_id_label(folder_label,label_id=1, label_idx=0)
    
if __name__=='__main__':
    # main()
    pass