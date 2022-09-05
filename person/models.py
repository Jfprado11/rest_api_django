from django.db import models


class Person(models.Model):
    """
    Person model
    model to save as table in the database
        attributes:
        - document_type: a Enum which hace as options [CC, TI, NUIP, CE]
        - documet: a integer which specifies the number of the person
        - name: string that represents the name of the person
        - last_name: string that represents the lastname of the person
        - hobbie: a string description of what hobbie the person does
    """

    class DocumentType(models.TextChoices):
        CEDULA_CIUDANIDA = 'CC'
        TARJETA_IDENTIDAD = 'TI'
        REGISTO_CIVIL = 'NUIP'
        CEDULA_EXTRAJERA = 'CE'
        NN = 'NN'

    document_type = models.CharField(
        max_length=4,
        choices=DocumentType.choices,
        default=DocumentType.NN,
    )
    document = models.IntegerField(unique=True)
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    hobbie = models.CharField(max_length=200)
