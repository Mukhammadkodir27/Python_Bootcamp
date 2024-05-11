# --- Introduction to Modules ---

#! importing one method from module
# * from module_example import introduce

# introduce("Kadir", "Abdusalomov")

#! importing multiple methods from module
# * from module_example import information, conclude, introduce

# introduce("Kadir", "Abdusalomov")
# information()
# conclude()

#! accessing through dot operator
import module_example

module_example.introduce("Kadir", "Abdusalomov")
module_example.information()
module_example.conclude()
