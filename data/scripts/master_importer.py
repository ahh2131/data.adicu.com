from courses_importer import Courses
import argparse


def main():
    parser = argparse.ArgumentParser(description="""Reads a dump file and imports
            it to specified table""")
    parser.add_argument('table_name', help="""Table name - e.g. courses, housing,
            housing_amenities""")
    parser.add_argument('--create', action='store_true', help="""create the
            courses_v2_t table if it doesn't already exist""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            courses_v2_t table""")
    parser.add_argument('dump_file', help="""Name of dump file""")

    args = parser.parse_args()
    # create object for corresponding table based on args
    if (args.table_name == "courses"):
        table_object = Courses(args.dump_file)
    elif (args.table_name =="housing"):
        table_object == Housing(args.dump_file)

    if (args.create):
      table_object.create_table()
    elif(args.drop):
      table_object.create_table()
    else:
      table_object.import_data()

if __name__ == "__main__":
    main()
