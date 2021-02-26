import os

#devolve o último ficheiro editado na diretoria dos screenshots
def up(path):
    # return os.system("ls -t /home/" + user + "/Pictures  |  head -n1")

    name_list = os.listdir(path)
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)

    sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
    return sorted_filename_list[-1]#último elemtnos da lista, ficheiro mais recente

