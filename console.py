import pdb

from models.member import Member
from models.gymsession import Gymsession
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymsession_repository as gymsession_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
gymsession_repository.delete_all()
booking_repository.delete_all()


member1 = Member('Diana', 'Prince', 'Premium', 'Active')
member_repository.save(member1)

member2 = Member('Bruce', 'Wayne', 'Premium', 'Inactive')
member_repository.save(member2)

member3 = Member('Peter', 'Parker', 'Standard', 'Active')
member_repository.save(member3)



gymsession1 = Gymsession('Les Mills - Body Pump', 'A full body weights workout.', 'Strength', 'Moderate', 'Monday', '05/04/21', '13.00', 45, 'Peak', 'Gym 1', 4.50, 10, 'Lonnie Machin')
gymsession_repository.save(gymsession1)

gymsession2 = Gymsession('Les Mills - Body Combat', 'High energy martial arts inspired workout.', 'Cardio', 'Advanced', 'Wednesday', '07/04/21', '15.00', 60, 'Off Peak', 'Gym 2', 4.50, 10, 'Selina Kyle')
gymsession_repository.save(gymsession2)

gymsession3 = Gymsession('Les Mills - Body Balance', 'A Yoga based class that will improve your mind, your body and your life', 'Flexibility', 'Beginner', 'Friday', '09/04/21', '11.00', 90, 'Peak', 'Gym 2', 4.50, 15, 'Selina Kyle')
gymsession_repository.save(gymsession3)



# booking1 = Booking(member1, gymsession3)
# booking_repository.save(booking1)

# booking2 = Booking(member2, gymsession1, True)
# booking_repository.save(booking2)

# booking3 = Booking(member2, gymsession3, True)
# booking_repository.save(booking3)


pdb.set_trace()