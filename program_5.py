# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def course_info():
    courses = {}
    
    while True:
        course_id = input("Enter course ID (Or 'done' to finish): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter course name: ")
        courses[course_id] = course_name

    subject = input("Enter a subject to search for (e.g., 'COS'): ").upper()
    
    print(f"Courses with subject '{subject}':")
    found = False
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True
            
    if not found:
        print(f"Sorry, no courses found with that subject '{subject}'.")
course_info()