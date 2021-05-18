from django.test import TestCase
from django.db.utils import IntegrityError

from flairsou_api.models import Account, Book


class AccountTestCase(TestCase):
    def setUp(self):
        bookBDE = Book.objects.create(name="Comptes", entity=1)
        self.assets = Account.objects.create(
            name="Actifs", accountType=Account.AccountType.ASSET, book=bookBDE)

    def test_type_constraint(self):
        # on crée un sous-compte au compte actif
        # ceci doit fonctionner
        accountSG = Account.objects.create(name="SG", parent=self.assets)

        # on vérifie qu'on ne peut pas créer de compte de dépenses sous le
        # compte accountSG
        with self.assertRaises(IntegrityError):
            Account.objects.create(name="Pizzas",
                                   parent=accountSG,
                                   accountType=Account.AccountType.EXPENSE)
