from database import engine, Base, SessionLocal

# импорт моделей 
from models.user import User
from models.profile import Profile
from models.course import Course
from models.student import Student

# создаём таблицы
Base.metadata.create_all(bind=engine)

# создаём сессию
db = SessionLocal()

print("База данных создана!")

# создаём пользователей
user1 = User(name="Aida", email="aida@mail.com")
user2 = User(name="Ali", email="ali@mail.com")

db.add_all([user1, user2])
db.commit()

# профиль (1:1)
profile1 = Profile(bio="Backend developer", user=user1)
db.add(profile1)
db.commit()

# курсы (1:N)
course1 = Course(title="Python", teacher=user1)
course2 = Course(title="Databases", teacher=user1)

db.add_all([course1, course2])
db.commit()

# студенты (N:N)
student1 = Student(name="Bek")
student2 = Student(name="Nura")

student1.courses.append(course1)
student2.courses.append(course1)
student2.courses.append(course2)

db.add_all([student1, student2])
db.commit()

print("Данные добавлены!")

print("\n--- QUERY ---")

# поиск по email
user = db.query(User).filter(User.email == "aida@mail.com").first()
print("Найден пользователь:", user.name)

# получить курсы пользователя
print("Курсы пользователя:", [c.title for c in user.courses])

# получить курсы студента
student = db.query(Student).filter(Student.name == "Nura").first()
print("Курсы студента:", [c.title for c in student.courses])

print("\n--- CRUD ---")

# UPDATE
user.name = "Aida Updated"
db.commit()
print("Обновили имя:", user.name)

# DELETE
user_to_delete = db.query(User).filter(User.name == "Ali").first()
db.delete(user_to_delete)
db.commit()
print("Пользователь Ali удалён")