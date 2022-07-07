import os
import argparse
import hashlib

msg_sort_direction = ("""Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:""")
msg_duplicates = ("Check for duplicates?", "Wrong option")
msg_delete_files = ("Delete files?", "Wrong option")


def sort_direction():
    print(msg_sort_direction)
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
        hash_val = hashlib.md5()
        hash_val.update(checked_file.read())
        return hash_val.hexdigest()


# def print_result(value, *h):
#     for file_size in sorted(value.keys(), reverse=sort_direction()):
#         print(str(file_size) + " bytes")
#         for file in value[file_size]:
#             print(file, sep="\n")
#         print()


def choose_yes_or_no(value1, value2, msg):
    msg_intro, msg_outro = msg
    print(msg_intro)
    answer = str(input())
    if answer == value1:
        return True
    elif answer == value2:
        return False
    else:
        print(msg_outro)
        return choose_yes_or_no(value1, value2, msg)


def delete_input_check():
    print("Enter file numbers to delete:")
    numbers_of_files = str(input()).split()
    if any(map(lambda x: not x.isdigit(), numbers_of_files)) or not numbers_of_files:
        print("Wrong format")
        return delete_input_check()
    else:
        return numbers_of_files


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

    if choose_yes_or_no("yes", "no", msg_duplicates):
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
            for i in range(len(duplicates[byte][h_value])):
                duplicates[byte][h_value][i] = (str(count), duplicates[byte][h_value][i])
                print(*duplicates[byte][h_value][i], sep=". ")
                count += 1
        print()

    if choose_yes_or_no("yes", "no", msg_delete_files):
        files_to_delete = set(delete_input_check())

        deleted_files_size = 0
        for bite in duplicates.keys():
            for h_and_path in duplicates[bite]:
                for f in range(len(duplicates[bite][h_and_path])):
                    file_number, path = duplicates[bite][h_and_path][f]
                    # print(file_number, p)
                    if file_number in files_to_delete:
                        deleted_files_size += bite
                        os.remove(path)

        print("Total freed up space:", deleted_files_size)
