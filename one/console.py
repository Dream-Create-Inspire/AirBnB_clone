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

