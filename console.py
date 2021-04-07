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

member4 = Member('Jessica', 'Drew', 'Premium', 'Inactive')
member_repository.save(member4)

member5 = Member('Steve', 'Rodgers', 'Standard', 'Active')
member_repository.save(member5)

member6 = Member('Linda', 'Danvers', 'Premium', 'Active')
member_repository.save(member6)

member7 = Member('Clark', 'Kent', 'Standard', 'Inctive')
member_repository.save(member7)

member8 = Member('James', 'Howlett', 'Premium', 'Active')
member_repository.save(member8)

member9 = Member('Barry', 'Allen', 'Standard', 'Active')
member_repository.save(member9)

member10 = Member('Alan', 'Scott', 'Premium', 'Active')
member_repository.save(member10)



gymsession1 = Gymsession('Les Mills : Body Pump', 'A full body weights workout.', 'Strength', 'Moderate', 'Monday', '05/04/21', '13.00', 45, 'Standard', 'Gym 1', 4.50, 10, 'Lonnie Machin')
gymsession_repository.save(gymsession1)

gymsession2 = Gymsession('Les Mills : Body Combat', 'High energy martial arts inspired workout.', 'Cardio', 'Advanced', 'Wednesday', '07/04/21', '15.00', 60, 'Standard', 'Gym 2', 4.50, 10, 'Selina Kyle')
gymsession_repository.save(gymsession2)

gymsession3 = Gymsession('Les Mills : Body Balance', 'A Yoga based class that will improve your mind, your body and your life', 'Flexibility', 'Beginner', 'Friday', '09/04/21', '11.00', 90, 'Premium', 'Gym 2', 4.50, 15, 'Selina Kyle')
gymsession_repository.save(gymsession3)

gymsession4 = Gymsession('Les Mills : Core', 'Ultimte core workout for incredible core strength and sports performance.', 'Strength', 'Moderate', 'Friday', '09/04/21', '9.00', 60, 'Premium', 'Gym 2', 4.50, 10, 'Lillian Rose')
gymsession_repository.save(gymsession4)

gymsession5 = Gymsession('Les Mills : Body Attack', 'High energy fitness class with moves that cater for total beginners.', 'Flexibility', 'Beginner', 'Wednesday', '07/04/21', '11.00', 45, 'Premium', 'Gym 1', 4.50, 10, 'Lillian Rose')
gymsession_repository.save(gymsession5)

gymsession6 = Gymsession('Les Mills : Body RPM', 'Indoor cycling class, set to the rhythm of motivating music.', 'Cardio', 'Moderate', 'Monday', '05/04/21', '13.00', 45, 'Premium', 'Gym 1', 4.50, 5, 'Lillian Rose')
gymsession_repository.save(gymsession6)





booking1 = Booking(member1, gymsession1)
booking_repository.save(booking1, member1, gymsession1)

booking2 = Booking(member1, gymsession2, True)
booking_repository.save(booking2, member1, gymsession2)

booking3 = Booking(member1, gymsession3, True)
booking_repository.save(booking3, member1, gymsession3)

booking4 = Booking(member2, gymsession2)
booking_repository.save(booking4, member2, gymsession2)

booking5 = Booking(member2, gymsession1, True)
booking_repository.save(booking5, member2, gymsession1)

booking6 = Booking(member3, gymsession2, True)
booking_repository.save(booking6, member3, gymsession2)

booking7 = Booking(member3, gymsession4, True)
booking_repository.save(booking7, member3, gymsession4)

booking8 = Booking(member4, gymsession4, True)
booking_repository.save(booking8, member4, gymsession4)

booking9 = Booking(member5, gymsession4, True)
booking_repository.save(booking9, member5, gymsession4)

booking10 = Booking(member6, gymsession4, True)
booking_repository.save(booking10, member6, gymsession4)

booking11 = Booking(member6, gymsession6, True)
booking_repository.save(booking11, member6, gymsession6)

pdb.set_trace()