import csv
import tempfile
from typing import List
from datetime import datetime as dt
from io import StringIO
# import hug
from marshmallow import fields
from . import models
from . import sample

# *source* refers to details with "beneficiary" at the beginning in template
# *bank* refers to details with "bank" at the beginning in the template
# instrument date is transfer.date
# debit and credit reference format = JANUARY 2014  PAYMENT


def gen_instr(transfers: List[models.TransferDetails]):
    with open("test_data.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(
            ["H", "CORPORATE", "H2HPAY",
                "", "", "{:%d%m%Y}".format(dt.now()), "SALARYJAN2019"]
        )
        for transfer in transfers:
            csvwriter.writerow(
                ["D", transfer.source.reference]
                + [""] * 2
                + [transfer.source.bene_name]
                + [""] * 3
                + [
                    transfer.source.bank,
                    transfer.source.branch,
                    "", "",
                    transfer.dest.country,
                    transfer.source.debit_acc_number,
                    transfer.source.currency,
                    "",
                    transfer.source.address,
                    transfer.source.country,
                    "",
                    transfer.source.city,
                ]
                + [""] * 22
                + [transfer.source.debit_acc_number, transfer.dest.currency]
                + [""] * 3
                + [transfer.amount, "", transfer.activation_date, transfer.date]
                + [""] * 9
                + [transfer.debit_reference,
                   "",
                   transfer.credit_reference]
                + [""] * 7
            )
        csvwriter.writerow(
            ["T", len(transfers), sum(t.amount for t in transfers), "", ""]
        )
        csvwriter.writerow(
            ["", "", "", "", ""]
        )
        csvwriter.writerow(
            ["", "", "", "", ""]
        )
        csvwriter.writerow(
            ["H", "CLIENT CODE", "H2HPAY",
                "", "", "Payment Date", "PIR Reference"]
        )
        csvwriter.writerow(
            ["D", "Instrument Reference"]
            + [""] * 2
            + ["Name of Beneficiary"]
            + [""] * 3
            + [
                "Beneficiary Bank",
                "Beneficiary Branch",
                "", "",
                    "Bank Country",
                    "Beneficiary Account Number",
                    "Beneficiary Account Currency",
                    "",
                    "Beneficiary Address",
                    "Beneficiary Country",
                    "",
                    "Beneficiary City",
            ]
            + [""] * 22
            + ["Debit Account Number", "Payment Currency"]
            + [""] * 3
            + ["Payment Amount", "", "Acctivation Date", "Instrument Date"]
            + [""] * 9
            + ["Debit Reference",
               "",
               "Credit Reference"]
            + [""] * 7
        )
        csvwriter.writerow(
            ["T", len(transfers), sum(t.amount for t in transfers), "", ""]
        )


# @hug.post("/transactiondetails")
# def transactiondetails(
# transfers: hug.types.MarshmallowInputSchema(models.TransferDetailsSchema(many=True))
# ) -> models.CSVResponse():

# return {"csv": gen_instr([sample.TRANSFER])}
