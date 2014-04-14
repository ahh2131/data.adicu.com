from importer import Importer
import json

class Courses(Importer):

    def __init__(self, dump_file):
      self.table_name = "courses_t"
      self.dump_file = dump_file
      self.schema = [
          ("Course", "varchar(32) primary key"),
          ("CourseFull", "varchar(32)"),
          ("PrefixName", "varchar(32)"),
          ("DivisionCode", "varchar(32)"),
          ("DivisionName", "varchar(64)"),
          ("SchoolCode", "varchar(32)"),
          ("SchoolName", "varchar(64)"),
          ("DepartmentCode", "varchar(32)"),
          ("DepartmentName", "varchar(64)"),
          ("SubtermCode", "varchar(32)"),
          ("SubtermName", "varchar(64)"),
          ("EnrollmentStatus", "varchar(32)"),
          ("NumFixedUnits", "int"),
          ("MinUnits", "int"),
          ("MaxUnits", "int"),
          ("CourseTitle", "varchar(64)"),
          ("CourseSubtitle", "varchar(64)"),
          ("Approval", "varchar(32)"),
          ("BulletinFlags", "varchar(32)"),
          ("ClassNotes", "varchar(64)"),
          ("PrefixLongname", "varchar(32)"),
          ("Description", "text")
      ]

    def import_data(self):
      query = create_query(self)
      send_query(query)

    def create_query(self):
      return 0
