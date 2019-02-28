class IOOperation(object):

    def read_file(self, file_path):
        with open(file_path) as f:
            content = f.readlines()

        content = [ x.replace("\n", "").split(" ") for x in content]

        return (int)(content[0][0]), content[1:]

    def write_in_file(self, filename, objects):
        file = open("./outputs/" + filename, "w")
        file.write(str(len(objects)) + '\n')
        for object in objects:
            file.write(object.__str__() + '\n')