from Parsers.nginxparser import nginxparser


class Site:

    def __init__(self, path):
        self.path = path
        file = open(path)
        self.config = nginxparser.load(file)
        file.close()

    def find(self, search, current_item=None):
        if current_item is None:
            current_item = self.config

        for item in current_item:
            if isinstance(item, list):
                result = self.find(search, current_item=item)
                if result:
                    return result
            elif item == search:
                return current_item

    def set(self, key, value):
        item = self.find(key)
        if item:
            item[1] = value

    def get(self, key):
        item = self.find(key)
        if item:
            return item[1]

    def save(self):
        file = open(self.path, "w")
        nginxparser.dump(self.config, file)
        file.close()
