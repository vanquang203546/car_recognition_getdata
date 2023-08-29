import os

def create_folder(name = None):
    try:
        os.mkdir(name)
    except:
        print("Already exist {}".format(name))
        # os.chdir(name)
def change_id_label(folder_label,path_save_label='Results_labels/labels',label_id=0, label_idx=1, mode='a'):
    create_folder(path_save_label)
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