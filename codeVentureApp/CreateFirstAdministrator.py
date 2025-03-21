from users.Administrator import Administrator
from SystemStorage import SystemStorage

# Create a SystemStorage object
system_storage = SystemStorage()

# Define the admin's information
admin_username = "admin5"
admin_password = "admin5"
admin_firstname = "Admin Firstname123456"
admin_lastname = "Admin Lastname123456"
admin_role = "Admin"  # Make sure the role is "Admin"
security_question = "Your favorite color?"  # Choose an appropriate security question
security_answer = "Blue"  # Provide the answer to the security question

    # Create an Administrator instance
admin = Administrator(admin_username, admin_password, admin_firstname, admin_lastname, security_question,
                          security_answer)

    # Insert the admin's data into the User_Data table
system_storage.insert_user_data(admin, security_question, security_answer)
system_storage.get_user(admin_username, admin_password)
    # Commit the changes
system_storage.connection.close()
    ######################################################################################
storage = SystemStorage()
user = storage.get_user(admin_username, admin_password)
print(user)
print(user.get_username(), user.get_password(), user.get_firstname(), user.get_lastname(), user.get_role())