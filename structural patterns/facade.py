from abc import ABC

class Drive(ABC):
    def add_folder(self, name: str) -> None:
        self.memory[name] = dict()

    def delete_folder(self, name: str) -> None:
        if name in self.memory:
            del self.memory[name]


class Drive_C(Drive):
    memory = dict()

    def add_folder(self, name: str) -> None:
        # self.memory[name] = dict()
        super().add_folder(name)

    def delete_folder(self, name: str) -> None:
        super().delete_folder(name)
    
    def scan_drive(self, name: str) -> dict:
        result = {'length': 0, 'files': []}

        for file in list(self.memory.keys()):
            if file == name:
                result['files'].append(file)
                result['length'] += 1

        return result


class Drive_D(Drive):
    memory = dict()

    def add_folder(self, name: str) -> None:
        super().add_folder(name)

    def delete_folder(self, name: str) -> None:
        super().delete_folder(name)
    
    def scan_drive(self, name: str) -> dict:
        result = {'length': 0, 'files': []}

        for file in list(self.memory.keys()):
            if file == name:
                result['files'].append(file)
                result['length'] += 1

        return result


class Windows_System(ABC):
    def __init__(self, drive_c: Drive_C, driver_d: Drive_D) -> None:
        self.Drive_C = drive_c
        self.Drive_D = driver_d

    def search_file(self, name: str) -> dict:
        result1 = self.Drive_C.scan_drive(name)
        result2 = self.Drive_D.scan_drive(name)

        return {'Drive C': result1, 'Drive D': result2}


    def clear_system(self) -> None:
        for key in list(self.Drive_C.memory.keys()):
            del self.Drive_C.memory[key]

        for key in list(self.Drive_D.memory.keys()):
            del self.Drive_D.memory[key]



if __name__ == '__main__':
    drive_C = Drive_C()
    drive_D = Drive_D()

    drive_C.add_folder('operation torch')
    drive_D.add_folder('operation overload')

    windows_system = Windows_System(drive_C, drive_D)
    search = windows_system.search_file('operation overload')
    print(search)

    windows_system.clear_system()
    search = windows_system.search_file('operation overload')
    print(search)