import os


class FileWrapper:
    def __init__(self, filename):
        self.filename = filename
        self.posts = []
        self.generate_list()

    def generate_list(self):
        if os.path.isfile(self.filename):
            with open(self.filename, "r") as f:
                self.posts = f.read()
                self.posts = self.posts.split("\n")
                self.posts = list(filter(None, self.posts))

    def write_file(self):
        with open(self.filename, "w") as f:
            for post_id in self.posts:
                f.write(post_id + "\n")
