# __name__ is a string, the name of the current file

if __name__ == '__main__':      # if no one imported me, do this
    print(f'Hello from {__name__}!')

x = 100

y = [10, 20, 30]


def hello(name):
    return f'Hello, {name}!'


if __name__ == '__main__':  # if no one imported me, do this
    print(f'Goodbye from {__name__}!')
