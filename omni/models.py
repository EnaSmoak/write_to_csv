from datetime import datetime as dt
from dataclasses import dataclass
import marshmallow_dataclass
from marshmallow import Schema, fields, validate


@dataclass
class SourceAccount:
    reference: str
    bene_name: str
    bank: str
    branch: str
    address: str
    country: str
    debit_acc_number: str
    currency: str
    city: str


@dataclass
class DestAccount:
    country: str
    currency: str


@dataclass
class TransferDetails:
    source: SourceAccount
    dest: DestAccount
    amount: float
    # amount: "{}, {}, {}".format(amount)
    activation_date: dt
    date: dt
    debit_reference: dt
    credit_reference: dt
    # activation_date: "{:%d-%m-%Y}".format(dt)
    # date: "{:%d-%m-%Y}".format(dt)


TransferDetailsSchema = marshmallow_dataclass.class_schema(TransferDetails)


class ResponseSchema(Schema):
    message = fields.String()
    errors = fields.Dict()


class CSVResponse(ResponseSchema):
    csv = fields.String(required=True)
