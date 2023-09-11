import os
import shutil

def create_folder(*names):
    for name in names:
        try:
            os.mkdir(name)
        except:
            print("Already exist {}".format(name))
            # os.chdir(name)
def create_folder_save(path_folder_save=r'Results_remove_imgs'):
    try:
        os.mkdir(os.path.join(path_folder_save, 'run0'))
        path_folder_save=os.path.join(path_folder_save, 'run0')
    except:
        id=max(int(i.split('run')[-1]) for i in os.listdir(path_folder_save) if 'run' in i)+1
        path_folder_save=os.path.join(path_folder_save, 'run' + str(id))
        os.mkdir(path_folder_save)
    path_images_save = os.path.join(path_folder_save, 'images')
    path_labels_save = os.path.join(path_folder_save, 'labels')
    create_folder(path_images_save, path_labels_save)
    return (path_images_save, path_labels_save)
def remove_img(path_folder_data,path_folder_save=r'Results_remove_imgs', extension_img='.jpg', label_id=1, mode='copy'):
    path_imgs = os.path.join(path_folder_data, 'images')
    path_labels = os.path.join(path_folder_data,'labels')
    #get_file
    # list_imgs = [img for img in os.listdir(path_imgs) if ('.png' in img) or ('.jpg' in img)]
    list_labels = [label for label in os.listdir(path_labels) if ('.txt' in label)]
    #get_name
    # name_imgs = [name_img.split('.',1)[0] for name_img in list_imgs]
    # name_labels = [name_label.split('.',1)[0] for name_label in list_labels]
    #check
    label_success =[]
    for label in list_labels:
        path_label = os.path.join(path_labels, label)
        with open(path_label, 'r') as content_label:
            for text in content_label:
                if text.split(' ', 1)[0]==str(label_id):
                    label_success.append(label)
                    break
    #create folder save
    path_images_save, path_labels_save = create_folder_save(path_folder_save)
    #move file
    success=0
    for label_file in label_success:
        name_img = '.'.join(label_file.split('.')[:-1])+extension_img
        source_img_path = os.path.join(path_imgs, name_img)
        source_label_path = os.path.join(path_labels, label_file)
        if os.path.exists(source_img_path):
            if mode=='copy':
                shutil.copy(source_img_path, path_images_save)
                shutil.copy(source_label_path, path_labels_save)
            elif mode=='move':
                shutil.move(source_img_path, path_images_save)
                shutil.move(source_label_path, path_labels_save)
            else:
                print('Error arguments: mode')
                break
            success+=1
    print("Success:",success)