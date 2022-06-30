from typing import List

class FileSystem:

    def __init__(self):
        self.file_system_dict = {}
        self.file_system_dict['/'] = ['dir', []]

    def ls(self, path: str) -> List[str]:
        if path in self.file_system_dict:
            if self.file_system_dict[path][0] == 'dir':
                return sorted(self.file_system_dict[path][1])
            else:
                return [path[path.rfind('/') + 1:]]
        else:
            return []

    def mkdir(self, path: str) -> None:
        mother_dir = ''
        path = path + '/'
        for idx_ in range(0, len(path), 1):
            if path[idx_] == '/':
                if idx_ != 0 and path[:idx_] not in self.file_system_dict:
                    folder_name = path[:idx_][len(mother_dir) + 1:]
                    self.file_system_dict[path[:idx_]] = ['dir', []]
                    if mother_dir == '':
                        mother_dir += '/'
                    self.file_system_dict[mother_dir][1].append(folder_name)
                mother_dir = path[:idx_]

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath in self.file_system_dict:
            self.file_system_dict[filePath][1] += content
        else:
            mother_folder = filePath[:filePath.rfind('/')]
            file_name = filePath[len(mother_folder) + 1:]
            if mother_folder not in self.file_system_dict:
                self.mkdir(mother_folder)

            self.file_system_dict[filePath] = ['file', content]
            if mother_folder == '':
                mother_folder += '/'
            self.file_system_dict[mother_folder][1].append(file_name)

    def readContentFromFile(self, filePath: str) -> str:
        if filePath in self.file_system_dict:
            return self.file_system_dict[filePath][1]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)