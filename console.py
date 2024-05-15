#!/usr/bin/env python3
"""
This is a command interpreter for managing User objects.
"""

import cmd
import uuid
from datetime import datetime


class User:
    """Class representing a User."""

    def __init__(self, email, first_name, last_name):
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[User] ({self.id}) {self.__dict__}"


class UserCommand(cmd.Cmd):
    """Command interpreter for User management."""

    prompt = '(airbnb) '
    users = {}

    def do_create(self, arg):
        """Create a new User instance."""
        args = arg.split()
        if len(args) != 3:
            print("** usage: create <email> <first_name> <last_name> **")
            return
        user = User(*args)
        self.users[user.id] = user
        print(user.id)

    def do_show(self, arg):
        """Show the details of a User instance by ID."""
        args = arg.split()
        if len(args) != 1:
            print("** usage: show <user_id> **")
            return
        user_id = args[0]
        user = self.users.get(user_id)
        if user:
            print(user)
        else:
            print("** no such user **")

    def do_destroy(self, arg):
        """Delete a User instance by ID."""
        args = arg.split()
        if len(args) != 1:
            print("** usage: destroy <user_id> **")
            return
        user_id = args[0]
        if user_id in self.users:
            del self.users[user_id]
            print("** user deleted **")
        else:
            print("** no such user **")

    def do_all(self, arg):
        """Display all User instances."""
        if arg:
            print("** usage: all **")
            return
        for user in self.users.values():
            print(user)

    def do_update(self, arg):
        """Update attributes of a User instance by ID."""
        args = arg.split()
        if len(args) != 3:
            print("** usage: update <user_id> <attribute_name> <attribute_value> **")
            return
        user_id, attr_name, attr_value = args
        user = self.users.get(user_id)
        if user:
            if hasattr(user, attr_name):
                setattr(user, attr_name, attr_value)
                user.updated_at = datetime.now()
                print("** user updated **")
            else:
                print("** no such attribute **")
        else:
            print("** no such user **")

    def do_quit(self, arg):
        """Quit the command interpreter."""
        print("** exiting **")
        return True

    def do_EOF(self, arg):
        """Handle EOF to quit the command interpreter."""
        print("** exiting **")
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    UserCommand().cmdloop()

