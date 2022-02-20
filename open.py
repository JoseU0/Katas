def main():
    # open("/path/to/mars.jpg")
    try:
        open('Módulo 10 - Manejo de errores\config.txt')
    # except FileNotFoundError:
    #     print("Couldn't find the config.txt file!")
    # except IsADirectoryError:
    #     print("Found config.txt but it is a directory, couldn't read it")

    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but it is a directory")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()