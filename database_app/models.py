from django.db import models
import django_filters


class tmn(models.Model):
    structure_id = models.CharField(max_length=20, name='Structure')
    metal_id = models.CharField(max_length=4, name='Metal')
    lattice_constant = models.FloatField(name='Lattice_Constant')
    bulk_modulus = models.FloatField(name='Bulk_Modulus', null=True, blank=True)
    elastic_c11 = models.FloatField(name='C11_elastic_constant', null=True, blank=True)
    elastic_c12 = models.FloatField(name='C12_elastic_constant', null=True, blank=True)
    elastic_c44 = models.FloatField(name='C44_elastic_constant', null=True, blank=True)
    is_exp = models.BooleanField(name='Experimental')
    is_stable = models.BooleanField(name='Stable')
    is_with_spin = models.BooleanField(name='Is_with_spin')
    potential = models.CharField(max_length=20, name = 'Potential')
    wave_func = models.CharField(max_length=20, name = 'Wave_function')
    code_package = models.CharField(max_length=20, name = 'Code_Package')
    reference_doi = models.CharField(max_length=200, name = 'Reference_DOI')
    link = models.CharField(max_length=200, name = 'Link')
    verified = models.BooleanField(name='Verified')

class AuthUser(models.Model):
    username = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=256)
    add_auth = models.BooleanField()
    delete_auth = models.BooleanField()
