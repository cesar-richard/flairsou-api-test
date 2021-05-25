from django.db import models

from .timestamped import TimeStampedModel


class Reconciliation(TimeStampedModel):
    """
    Modèle de rapprochement.

    Attributes
    ----------

    account : ForeignKey
        Clé étrangère vers le compte à rapprocher

    date : DateField
        Date à laquelle le rapprochement est effectif (i.e. la date de fin de
        période indiquée sur le relevé de banque, 
        pas la date de saisie du rapprochement)

    solde : PositiveIntegerField
        Solde rapproché du compte à la date de fin de période, qui doit 
        correspondre à celui indiqué sur le relevé de banque.
    """
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    date = models.DateField("Date")
    solde = models.IntegerField("solde")

    def __str__(self):
        return "Reconciliation of account {} on {}".format(
            self.account, self.date)

    class Meta:
        constraints = []

        # on ne peut avoir qu'un rapprochement par date pour un compte
        constraints.append(
            models.UniqueConstraint(
                fields=['account', 'date'],
                name="%(app_label)s_%(class)s_one_reconc_per_date"))
