import os
import shutil

def fyle_copy_all(src, dst):
    print(f"Entering fyle_copy_all; Copying {src} to {dst}")
    if not os.path.exists(src):
        raise FileNotFoundError(src)
    try:
        """
        It should first delete all the contents of the
        destination directory (public) to ensure that the 
        copy is clean.
        """

        print(f"then ganna try creating the directory {dst}")
        if not os.path.exists(dst):
            print(f"Creating directory {dst}")
            os.makedirs(dst)
        else:
            print(f"Directory {dst} already exists")
            print(f"but i will doing rmtree on {dst}")
            shutil.rmtree(dst)

        for file in os.listdir(src):
            print(f"File {file} ...")
            if not os.path.isfile(os.path.join(src, file)):
                print(f"File {file} is directory, we need to go deeper")
                fyle_copy_all(os.path.join(src, file), os.path.join(dst, file))
            else:
               shutil.copyfile(os.path.join(src, file), os.path.join(dst, file))
               print(f"Copied {file} to {dst}")
    except Exception as e:
        print(e)


