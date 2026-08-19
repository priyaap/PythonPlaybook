from pathlib import Path

def extract_data_file_path(fname):
    
    #fname = input("Enter file name: ")
    projectpath = str(Path(__file__).resolve().parent.parent.parent)
    filepath = projectpath + "/data/" + fname
    print(filepath)
    