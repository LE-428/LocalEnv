# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.environ['TEST_VARIABLE'] = 'hello-world'
    print(os.getenv('TEST_VARIABLE'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
