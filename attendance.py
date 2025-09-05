class AttendanceRegister:
    record = {}
    def mark_present(self, name):
        self.record[name]= "present"
    def mark_absent(self,name):
        self.record[name]="absent"
    def get_status(self, name):
        if name in self.record:
            return f"{name} is {self.record[name]}"
        else:
            return f"No record of {name}" 
    def show_register(self):
        return self.record
register = AttendanceRegister()

register.mark_present("john")
register.mark_absent("mimi")
check_status =register.get_status("john")
print(check_status)
check_status =register.get_status("tom")
print(check_status)
print(register.record)
finaly_register =register.show_register()
print(finaly_register)