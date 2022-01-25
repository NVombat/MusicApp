from .errors import AdminExistsError
from . import Admin_Auth


def generate_admin(name: str, email: str, pwd: str) -> None:
    try:
        Admin_Auth.insert_admin(name, email, pwd)
    except AdminExistsError as aee:
        print("Error: ", str(aee))


if __name__ == "__main__":
    print("Creating Admin...")

    name = input("Enter Admin Name: ")
    email = input("Enter Admin Email ID: ")
    pwd = input("Enter Admin Password: ")

    try:
        generate_admin(name, email, pwd)
    except Exception:
        print("Error Creating Admin... Try Again...")

    print("Admin Created Successfully...")
