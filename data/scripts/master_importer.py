from courses_importer import Courses
import argparse


def main():
    parser = argparse.ArgumentParser(description="""Reads a dump file and imports
            it to specified table""")
    parser.add_argument('table_name', help="""Table name -- courses, housing,
            housing_amenities""")
    parser.add_argument('dump_file', help="""Name of dump file""")

    args = parser.parse_args()
    # create object for corresponding table based on args
    if (args.table_name == "courses")
        table_object = Courses(args.dump_file)
    elif (args.table_name =="housing")
        table_object == Housing(args.dump_file)


        load_data(args.dump_file)

if __name__ == "__main__":
    main()
