class IOOperation(object):

    def read_file(self, file_path):
        with open(file_path) as f:
            content = f.readlines()

        content = [x.strip() for x in content]

        return content

    def write_in_file(self, filename, objects):
        file = open("./outputs/" + filename, "w")
        for object in objects:
            file.write(str(len(objects)) + ' - ' + object + '\n')