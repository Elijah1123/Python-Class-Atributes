class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC",
        "Production", "Legal", "Finance", "Sales",
        "General Management", "Research & Development",
        "Marketing", "Purchasing"
    ]

    def __init__(self, name="John Doe", job="Admin"):
        self.name = name
        self.job = job

    # Name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    # Job property
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")


p1 = Person("elijah mzalindu", "ITC")     
p2 = Person("", "Doctor")               
p3 = Person("mary jane", "Marketing")    

print(p1.name, p1.job)   