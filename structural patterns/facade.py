from abc import ABC

class Drive(ABC):
    memory = dict()

    def add_folder(self, name: str) -> None:
        self.memory[name] = dict()

    def delete_folder(self, name: str) -> None:
        if name in self.memory:
            del self.memory[name]


class Drive_C(Drive):
    def add_folder(self, name: str) -> None:
        self.memory[name] = dict()

    def delete_folder(self, name: str) -> None:
        if name in self.memory:
            del self.memory[name]


class Drive_D(Drive):
    def add_folder(self, name: str) -> None:
        self.memory[name] = dict()

    def delete_folder(self, name: str) -> None:
        if name in self.memory:
            del self.memory[name]


class Windows_System(ABC):
    def __init__(self, drive_c: Drive_C, driver_d: Drive_D) -> None:
        self.Drive_C = drive_c
        self.Drive_D = driver_d

    def search_file(self, name: str) -> dict:
        result = { 'result': 0, 'files': list() }

        for file_name, file in self.Drive_C.memory.items():
            if file_name == name:
                result['files'].append(file)

        for file_name, file in self.Drive_D.memory.items():
            if file_name == name:
                result['files'].append(file)

        return result


    def clear_system(self) -> None:
        for key in self.Drive_D.keys():
            del self.Drive_D[key]



if __name__ == '__main__':
    drive_C = Drive_C()
    drive_D = Drive_D()

    drive_C.add_folder('operation torch')
    drive_D.add_folder('operation overload')

    windows_system = Windows_System(drive_C, drive_D)
    search = windows_system.search_file('operation overload')
    print(search)

    windows_system.clear_system()