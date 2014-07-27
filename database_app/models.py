from django.db import models


class tmn(models.Model):
    structure_id = models.CharField(max_length=20, name='Structure')
    metal_id = models.CharField(max_length=4, name='Metal')
    lattice_constant = models.FloatField(name='Lattice_Constant')
    bulk_modulus = models.FloatField(name='Bulk_Modulus', null=True, blank=True)
    elastic_c11 = models.FloatField(name='C11_elastic_constant', null=True, blank=True)
    elastic_c12 = models.FloatField(name='C12_elastic_constant', null=True, blank=True)
    elastic_c44 = models.FloatField(name='C44_elastic_constant', null=True, blank=True)
    e_n = models.FloatField(name='e_n', null=True, blank=True)
    nu = models.FloatField(name='nu', null=True, blank=True)
    k = models.FloatField(name='k', null=True, blank=True)
    cauchy_pressure = models.FloatField(name='Cauchy_pressure', null=True, blank=True)
    vickers_hardness = models.FloatField(name='Vickers_hardness', null=True, blank=True)
    is_exp = models.BooleanField(name='Experimental')
    is_stable = models.BooleanField(name='Stable')
    is_with_spin = models.BooleanField(name='Is_with_spin')
    potential = models.CharField(max_length=20, name = 'Potential')
    wave_func = models.CharField(max_length=20, name = 'Wave_function')
    code_package = models.CharField(max_length=20, name = 'Code_Package')
    reference_doi = models.CharField(max_length=200, name = 'Reference_DOI')
    comment = models.CharField(max_length=200, name = 'Comment')
    verified = models.BooleanField(name='Verified')


class Contributions(models.Model):
    c_name = models.CharField(max_length=100, name='Name')
    c_university = models.CharField(max_length=100, name='University')
    c_contact = models.CharField(max_length=200, name='Contact')