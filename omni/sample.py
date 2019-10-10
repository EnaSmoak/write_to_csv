from datetime import datetime as dt
from . import models

TRANSFER = models.TransferDetails(
    source=models.SourceAccount(
        reference="001TT6789210",
        bene_name="EnterpriseGH",
        bank="GH020100",
        branch="020101",
        debit_acc_number="012345548787454",
        currency="GHS",
        address="High Street, Ground floor, Accra 12345",
        country="GHANA",
        city="Accra"


    ),
    dest=models.DestAccount(
        country="GHANA",
        currency="GHS"

    ),
    amount=100000,
    activation_date="{:%d%m%Y}".format(dt.now()),
    date="{:%d%m%Y}".format(dt.now()),
    debit_reference="{:%^B%Y}".format(dt.now()) + " " + "PAYMENT",
    credit_reference="{:%^B%Y}".format(dt.now()) + " " + "PAYMENT"

)
