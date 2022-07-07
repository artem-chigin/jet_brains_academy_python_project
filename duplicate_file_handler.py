import os
import argparse
import hashlib


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
        print("Wrong option")
        return sort_direction()


def calculate_hash(path_to_file_value):
    with open(path_to_file_value, "rb") as checked_file:
        hash_value = hashlib.md5()
        hash_value.update(checked_file.read())
        return hash_value.hexdigest()


# def print_result(value, *h):
#     for file_size in sorted(value.keys(), reverse=sort_direction()):
#         print(str(file_size) + " bytes")
#         for file in value[file_size]:
#             print(file, sep="\n")
#         print()


def check_for_duplicates():
    print("Check for duplicates?")
    answer = str(input())
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return check_for_duplicates()


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

    same_size_files = {s: p for s, p in path_and_size.items() if len(p) > 1}

    # print_result(same_size_files)

    direction_of_sorted = sort_direction()

    for byte in sorted(same_size_files.keys(), reverse=direction_of_sorted):
        print(str(byte) + " bytes")
        for file in same_size_files[byte]:
            print(file, sep="\n")
        print()

    files_with_hash_value = {}

    if check_for_duplicates():
        for _ in sorted(same_size_files.keys(), reverse=direction_of_sorted):
            files_with_hash_value[_] = files_with_hash_value.get(_, {})
            for file in same_size_files[_]:
                hash_value = calculate_hash(file)
                files_with_hash_value[_][hash_value] = files_with_hash_value[_].get(hash_value, []) + [file]

    duplicates = {size: {h: p for h, p in hash_and_path.items() if len(p) > 1} for size, hash_and_path in files_with_hash_value.items()}

    count = 1

    for byte in sorted(duplicates.keys(), reverse=direction_of_sorted):
        print(str(byte) + " bytes")
        for h_value in duplicates[byte]:
            print("Hash: " + h_value)
            for file in duplicates[byte][h_value]:
                print(str(count) + ". " + file, sep="\n")
                count += 1
        print()
