import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="enter your root directory")

args = parser.parse_args()

if not args.path:
    print("Directory is not specified")
# else:
#     print(args.path)

os.chdir(args.path)
result = os.walk(".")
for root, dirs, files in result:
    for name in files:
        print(os.path.join(root, name))
    # for name in dirs:
    #     print(os.path.join(root, name))
