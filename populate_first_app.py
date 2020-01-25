import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Creatly.settings')
import django

django.setup()

from faker import Faker
from users.models import User

fakegen = Faker()


def add_user(N=5):
    for entry in range(N):
        fake_uname = fakegen.name()
        fake_upassword = fakegen.name()
        fake_ucountry = fakegen.country()
        fake_ucity = fakegen.city()
        fake_ustreetAddress = fakegen.address()
        fake_fname = fakegen.name()
        fake_lname = fakegen.name()
        fake_umembership = fakegen.name()

        usr = User.objects.get_or_create(uname=fake_uname, upassword=fake_upassword, ucountry=fake_ucountry,
                                         ucity=fake_ucity, ustreetAddress=fake_ustreetAddress, ufname=fake_fname,
                                         ulname=fake_lname, umembership=fake_umembership)[0]


if __name__ == '__main__':
    print('populating script')
    add_user(20)
    print("Populating Complete!")
