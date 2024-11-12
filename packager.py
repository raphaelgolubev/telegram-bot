from pathlib import Path


def main():
    while True:
        break_flag = 'q'
        package_name = input(f'> Package name (enter "{break_flag}" to quit): ')
        
        if package_name != break_flag:
            package_path = Path(package_name)
            package_path.mkdir(exist_ok=True)

            package_path.joinpath('__init__.py').touch()

            print(f'Created package {package_path}')
        else:
            break


if __name__ == '__main__':
    main()
