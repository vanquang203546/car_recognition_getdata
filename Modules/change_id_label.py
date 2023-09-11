import os

def create_folder(*names):
    for name in names:
        try:
            os.mkdir(name)
        except:
            print("Already exist {}".format(name))
            # os.chdir(name)
def create_folder_save(path_folder_save=r'Results_labels'):
    try:
        os.mkdir(os.path.join(path_folder_save, 'run0'))
        path_folder_save=os.path.join(path_folder_save, 'run0')
    except:
        id=max(int(i.split('run')[-1]) for i in os.listdir(path_folder_save) if 'run' in i)+1
        path_folder_save=os.path.join(path_folder_save, 'run' + str(id))
        os.mkdir(path_folder_save)
    path_labels_save = os.path.join(path_folder_save, 'labels')
    create_folder(path_labels_save)
    return path_labels_save
def change_id_label(folder_label,path_save_label='Results_labels',label_id=0, label_idx=1, mode='a'):
    path_save_label = create_folder_save(path_save_label)
    success_label = 0
    for label in os.listdir(folder_label):
        with open(os.path.join(folder_label, label), 'r') as label_file:
            success = False
            for text in label_file:
                if text.split()[0] == str(label_id):
                    with open(os.path.join(path_save_label, label), mode) as save_file:
                        save_file.write(str(label_idx) + ' ' + text.split(' ', 1)[1])
                        success = True
            if success:
                success_label += 1
    print(success_label)