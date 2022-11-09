"""Utilities for course registration.

Author: CS 149 Instructors and Alex Sizov
Version: NOV/9/2022
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 9.1


class Section:
    """The Section class represents one section of a course.

    Attributes:
        course_code (str): The course identifier, e.g. 'CS 149'
        section_number (int): The number of this section
        capacity (int): The maximum number of students for this section
        enrolled (int): The number of students enrolled in this section

    """

    def __init__(self, course_code, section_number, capacity):
        """Initialize a new empty Section.

        Args:
            course_code (str): The course identifier, e.g. 'CS 149'
            section_number (int): The number for this section
            capacity (int): The maximum number of students for this section

        """
        self.course_code = course_code
        self.section_number = section_number
        self.capacity = capacity
        self.enrolled = 0

    def add_students(self, num_students):
        """Add some students to this section.

        If the number of students provided exceeds the remining
        capacity then no students will be added and an error message
        will be printed.

        Args:
            num_students (int): The number of students to add

        """
        seats_remaining = self.capacity - self.enrolled
        if num_students > seats_remaining:
            print("Error: not enough seats!")
        else:
            self.enrolled += num_students

    def __str__(self):
        """Create a string representation of this Section.

        NOTE: The method name __str__ has a special meaning in
        Python. This method determines what will happen when we
        convert a Section object to a string.  This will be covered in
        section 10.2.

        Returns:
            string: A string representation of this Section

        """
        result = f"{self.course_code} {self.section_number:04}"
        result += f" ({self.enrolled}/{self.capacity})"
        return result


def create_sections(course_code, section_size, total_students):
    """Create a list of Section objects adequate for all students.

    This function will generate a list of Section objects numbered
    sequentially starting at 1. The last section may not be completely
    full if If the section size doesn't divide evenly into the total
    number of students.

    Args:
        course_code (str): The course identifier, e.g. 'CS 149'
        section_size (int): The capacity for each section
        total_students (int): The total number of students that need a seat

    Returns:
        list: A list of section objects adequate to seat all students

    """
    c_list = []
    s_num = 1
    c_students = total_students
    while (c_students > 0):
        d = min(section_size, c_students)
        ns = Section(course_code, s_num, section_size)
        ns.add_students(d)
        c_list.append(ns)
        c_students -= d
        s_num += 1
    return c_list


if __name__ == "__main__":

    # Execution example:
    sections = create_sections("CS 149", 30, 100)
    for section in sections:
        print(section)
