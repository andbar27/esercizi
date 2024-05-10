from Admin import Admin, Privileges

privileges = Privileges(["ciao","bella"])
a1 = Admin("Alessandro", "Gini", 27, privileges)
a1.privileges.show_privileges()