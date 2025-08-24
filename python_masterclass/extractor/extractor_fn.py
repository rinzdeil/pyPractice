import zipfile

def extract(input_path, dir_path):
    with zipfile.ZipFile(input_path, 'r') as zip_ref:
        zip_ref.extractall(dir_path)

if __name__ == '__main__':
    extract()