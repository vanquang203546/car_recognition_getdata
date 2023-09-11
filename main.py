import os
from Modules.extract_frame import frame_per_second
from Modules.change_id_label import change_id_label
from Modules.remove_img import remove_img

def extract_frame_video(folder_video, type='img', frame_index=0, n=5):
    type = 'traffic_camera_test'
    frame_index = 0 #start index
    n = 5           #5frames/s
    for video in os.listdir(folder_video):
        path_video = os.path.join(folder_video, video)
        frame_index = frame_per_second(path_video, type, frame_index, n)
        frame_index += n
def count_objects(folder_label):
    obj = {}
    for label in os.listdir(folder_label):
        with open(os.path.join(folder_label, label), 'r', encoding='utf-8') as data:
            for text in data:
                id = text.split(' ',1)[0]
                obj[id]=obj.get(id, 0)+1
    print(obj)
def main():
    # folder_video = r"C:/Users/PC/OneDrive - Hanoi University of Science and Technology/Desktop/Video/video_test"
    # type='traffic_camera_test'
    # extract_frame_video(folder_video, type)

    # folder_label = r'C:\Users\PC\OneDrive - Hanoi University of Science and Technology\Desktop\New folder (2)\train\labels'
    # change_id_label(folder_label,label_id=0, label_idx=1)

    # path_folder_data=r'C:\Users\PC\OneDrive - Hanoi University of Science and Technology\Desktop\Car_recognitions\Honda CRV_abc\test'
    # extension_img='.jpg'
    # label_id=1
    # mode='copy'
    # remove_img(path_folder_data, extension_img=extension_img, label_id=label_id, mode=mode)

    # count_objects(r'Results_remove_imgs\run0\labels')
    # count_objects(r'C:\Users\PC\OneDrive - Hanoi University of Science and Technology\Desktop\Car_recognitions\traffic_camera\labels')
    pass
if __name__=='__main__':
    main()
    # pass