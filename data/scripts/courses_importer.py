from importer import Importer

class Courses(Importer):

    def __init__(self, dump_file):
      self.table_name = "courses_t"
      self.dump_file = dump_file

    def import_data(self):
