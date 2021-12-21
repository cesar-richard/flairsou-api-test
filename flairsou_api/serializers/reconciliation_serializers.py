from .flairsou_serializers import FlairsouModelSerializer
from flairsou_api.models import Reconciliation, Account

from datetime import datetime


class ReconciliationSerializer(FlairsouModelSerializer):
    """
    Serializer pour les rapprochements
    """
    class Meta:
        model = Reconciliation
        fields = ['pk', 'account', 'date', 'balance']

    def check_date_after_last_reconc(self, account: Account,
                                     date: datetime.date) -> None:
        """
        Vérifie que la date passée pour le rapprochement est bien postérieure à
        celle du dernier rapprochement effectué sur le compte
        """
        last_reconc = account.last_reconciliation
        if last_reconc is not None:
            if date < last_reconc.date:
                raise self.ValidationError({
                    'date':
                    "La date doit être "
                    "postérieure au dernier rapprochement"
                })

    def check_balance_valid(self, account: Account, date: datetime.date,
                            balance: int) -> None:
        """
        Vérifie que le solde passé das le rapprochement est bien le même
        que le solde du compte à la même date
        """
        if balance != account.balance_at_date(date):
            raise self.ValidationError(
                {'balance': "Le solde du rapprochement n'est "
                 "pas correct"})

    def check_account_nonvirtual(self, account: Account) -> None:
        """
        Vérifie que le compte rapproché est bien non virtuel
        """
        if account.virtual:
            raise self.ValidationError(
                {'account': "Un compte virtuel ne peut pas "
                 "être rapproché"})

    def validate(self, data):
        """
        Valide l'enregistrement du rapprochement
        """
        account = data['account']
        date = data['date']
        balance = data['balance']

        # vérifie que le compte n'est pas virtuel (on ne rapproche pas un
        # compte virtuel)
        self.check_account_nonvirtual(account)

        # vérifie que la date est bien postérieure au dernier rapprochement
        self.check_date_after_last_reconc(account, date)

        # vérifie que le solde est valide
        self.check_balance_valid(account, date, balance)

        return data
