import os
import argparse


def sort_direction():
    print("""Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:""")
    option = int(input())
    if option == 1:
        return True
    elif option == 2:
        return False
    else:
        return sort_direction()


parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=None)
args = parser.parse_args()

if not args.path:
    print("Directory is not specified")
else:
    print("Enter file format:")
    file_format = str(input())

    root_path = os.walk(args.path, topdown=False)

    path_and_size = {}
    for root, dirs, files in root_path:
        for name in files:
            # print(os.path.join(root, name))
            path_to_file = os.path.join(root, name)
            size = os.path.getsize(path_to_file)
            if path_to_file.endswith(file_format):
                path_and_size[size] = path_and_size.get(size, []) + [path_to_file]
        # for name in dirs:
        #     print(os.path.join(root, name))

    result = {s: p for s, p in path_and_size.items() if len(p) > 1}

    for byte in sorted(result.keys(), reverse=sort_direction()):
        print(str(byte) + " bytes")
        for file in result[byte]:
            print(file, sep="\n")
        print()
