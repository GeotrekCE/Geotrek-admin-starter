# coding=utf-8
from __future__ import unicode_literals

from django.contrib.gis.geos import Point
from geotrek.common.parsers import *
from geotrek.tourism.models import *
from django.conf import settings

class TourinsoftParser61(TourInSoftParser):
    eid = 'eid'
    label = "TourinSoft Restauration 61"
    model = TouristicContent
    url = "http://wcf.tourinsoft.com/Syndication/cdt61/cd8d229b-cdb8-495e-a468-e2495563b060/Objects"

    constant_fields = {
        'published': True,
        'deleted': False,
    }

    fields = {
        'eid': 'SyndicObjectID',
        'name': 'SyndicObjectName',
        'description_teaser': 'DescriptionCommerciale',
        'geom': ('GmapLongitude', 'GmapLatitude'),
        'category': 'ObjectTypeName',
        'practical_info': (
            'LanguesParlees',
            'PeriodeOuverture',
            'PrestationsEquipements',
        ),
        'contact': ('MoyenDeCom', 'AdresseComplete'),
        'email': 'MoyenDeCom',
        'website': 'MoyenDeCom',
    }

    m2m_fields = {
        'type1': 'Classification',
        'type2': 'Classification2',
    }

    non_fields = {
        'attachments': 'Photos',
    }

    def filter_type1(self, src, val):
        instance, created = TouristicContentType1.objects.get_or_create(
            category_id=5,
            label=val
        )

        return [instance, ]

    def filter_type2(self, src, value):
        instances = []
        if value:
            values = value.split('#')
            if values:
                for value in values:
                    instance, created = TouristicContentType2.objects.get_or_create(
                        category_id=5,
                        label=value
                    )
                    instances.append(instance)
        return instances

    def filter_contact(self, src, val):
        infos = ""
        com, adresse = val

        if adresse:
            address_splitted = adresse.split('|')
            if address_splitted:
                infos += "<strong>Adresse :</strong><br/>"
                infos += "%s<br/>" % address_splitted[0]
                infos += "%s - %s<br/>" % (address_splitted[4], address_splitted[5])
                infos += "<br/>"
        if com:
            response_dict = {}
            values = com.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            tel = response_dict.get('Téléphone filaire', '')

            if tel:
                infos += "<strong>Téléphone :</strong><br/>"
                infos += "%s<br/>" % tel
                infos += "<br/>"

            fax = response_dict.get('Télécopieur /fax', '')

            if fax:
                infos += "<strong>Fax :</strong><br/>"
                infos += "%s<br/>" % fax
                infos += "<br/>"

        return infos

    def filter_email(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Mél', '')
        return ''

    def filter_website(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Site web(URL)', '')
        return ''

    def filter_geom(self, src, val):
        lng, lat = val
        geom = Point(float(lng), float(lat), srid=4326)  # WGS84
        geom.transform(settings.SRID)
        return geom

    def filter_category(self, src, val):
        if val == "Restauration":
            return TouristicContentCategory.objects.get(pk=5)

    def filter_attachments(self, src, val):
        result = []
        if val:
            photos = val.split('#')
            if photos:
                for photo in photos:
                    if photo:
                        url, legend, credits = photo.split('|')
                        result.append((url, legend, credits))

        return result

    def filter_practical_info(self, src, val):
        infos = ""

        if val:
            if len(val) != 3:
                raise Exception('problem with practial infos')
            langues, periode, equipements = val

            if langues:
                infos += "<strong>Langues parlées :</strong><br/>"
                infos += "<br/>".join(langues.split('#'))
                infos += "<br/><br/>"

            if periode:
                periodes = periode.split('|')
                if len(periodes) > 1:
                    if periodes[0] and periodes[1]:
                        infos += "<strong>Période d'ouverture :</strong><br/>"
                        infos += "du %s au %s" % (periodes[0], periodes[1])
                        infos += "<br/><br/>"

            if equipements:
                infos += "<strong>Équipements :</strong><br/>"
                infos += "<br/>".join(equipements.split('#'))
                infos += "<br/><br/>"

        return infos


class TourinsoftParser28(TourinsoftParser61):
    label = "TourinSoft Restauration 28"
    url = "http://wcf.tourinsoft.com/Syndication/cdt28/75578a63-e35c-4226-b910-a89a28827722/Objects"


class TourinsoftHOT28(TourinsoftParser61):
    label = "TourinSoft HOT 28"
    url = "http://wcf.tourinsoft.com/Syndication/cdt28/7780b30d-9aed-42a4-bde5-5deb6a4bc444/Objects"

    fields = {
        'eid': 'SyndicObjectID',
        'name': 'SyndicObjectName',
        'description': 'DescriptionCommerciale2',
        'description_teaser': 'DescriptionCommerciale',
        'geom': ('GmapLongitude', 'GmapLatitude'),
        'category': 'ObjectTypeName',
        'practical_info': (
            'LanguesParlees',
            'PeriodeOuverture',
            'PrestationsEquipements',
        ),
        'contact': ('MoyenDeCom', 'AdresseComplete'),
        'email': 'MoyenDeCom',
        'website': 'MoyenDeCom',
    }

    m2m_fields = {
        'type1': 'Classification',
        'type2': 'Labels',
    }

    def filter_category(self, src, val):
        return TouristicContentCategory.objects.get(pk=1)

    def filter_type1(self, src, val):
        instance, created = TouristicContentType1.objects.get_or_create(
            category_id=1,
            label=val
        )

        return [instance, ]

    def filter_type2(self, src, value):
        instances = []
        if value:
            values = value.split('#')
            if values:
                for value in values:
                    if value:
                        instance, created = TouristicContentType2.objects.get_or_create(
                            category_id=1,
                            label=value
                        )
                        instances.append(instance)
        return instances

    def filter_email(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Mail', '')
        return ''

    def filter_website(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Site web', '')


    def filter_contact(self, src, val):
        infos = ""
        com, adresse = val

        if adresse:
            address_splitted = adresse.split('|')
            if address_splitted:
                infos += "<strong>Adresse :</strong><br/>"
                infos += "%s<br/>" % address_splitted[0]
                infos += "%s - %s<br/>" % (address_splitted[4], address_splitted[5])
                infos += "<br/>"
        if com:
            response_dict = {}
            values = com.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            tel = response_dict.get('T&eacute;l&eacute;phone', '')

            if tel:
                infos += "<strong>Téléphone :</strong><br/>"
                infos += "%s<br/>" % tel
                infos += "<br/>"

            fax = response_dict.get('Fax', '')

            if fax:
                infos += "<strong>Fax :</strong><br/>"
                infos += "%s<br/>" % fax
                infos += "<br/>"

            portable = response_dict.get('Portable', '')

            if portable:
                infos += "<strong>Portable :</strong><br/>"
                infos += "%s<br/>" % portable
                infos += "<br/>"

        return infos


class TourinsoftHLO28(TourinsoftHOT28):
    label = "Tourinsoft HLO 28"
    url = "http://wcf.tourinsoft.com/Syndication/cdt28/ee0b810d-fc60-4940-83af-40b6e601d10b/Objects"


class TourinsoftHCO28(TourinsoftHOT28):
    label = "Tourinsoft HCO 28"
    url = "http://wcf.tourinsoft.com/Syndication/cdt28/d8fd02bf-c40d-4671-ada0-97998a3ff01c/Objects"

    m2m_fields = {
        'type1': 'ObjectTypeName',
        'type2': 'Labels',
    }

    def filter_contact(self, src, val):
        infos = ""
        com, adresse = val

        if adresse:
            address_splitted = adresse.split('|')
            if address_splitted:
                infos += "<strong>Adresse :</strong><br/>"
                infos += "%s<br/>" % address_splitted[0]
                infos += "%s - %s<br/>" % (address_splitted[3], address_splitted[4])
                infos += "<br/>"
        if com:
            response_dict = {}
            values = com.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            tel = response_dict.get('Téléphone filaire', '')

            if tel:
                infos += "<strong>Téléphone :</strong><br/>"
                infos += "%s<br/>" % tel
                infos += "<br/>"

            fax = response_dict.get('Télécopieur /fax', '')

            if fax:
                infos += "<strong>Fax :</strong><br/>"
                infos += "%s<br/>" % fax
                infos += "<br/>"

            portable = response_dict.get('Téléphone cellulaire', '')

            if portable:
                infos += "<strong>Portable :</strong><br/>"
                infos += "%s<br/>" % portable
                infos += "<br/>"

        return infos

    def filter_email(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Mél', '')
        return ''

    def filter_website(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Site web (URL)', '')

        return ''

    def filter_type1(self, src, val):
        instance, created = TouristicContentType1.objects.get_or_create(
            category_id=1,
            label=val
        )

        return [instance, ]

    def filter_type2(self, src, value):
        instances = []
        if value:
            values = value.split('#')
            if values:
                for value in values:
                    if value:
                        instance, created = TouristicContentType2.objects.get_or_create(
                            category_id=1,
                            label=value
                        )
                        instances.append(instance)
        return instances


class TourinsoftHPA28(TourinsoftHOT28):
    label = "Tourinsoft HPA 28"
    url = "http://wcf.tourinsoft.com/Syndication/cdt28/a286d5d5-7c9e-4d4d-ae03-d18e26681c4b/Objects"

    m2m_fields = {
        'type1': 'ObjectTypeName',
        'type2': 'Labels',
    }

    def filter_contact(self, src, val):
        infos = ""
        com, adresse = val

        if adresse:
            address_splitted = adresse.split('|')
            if address_splitted:
                infos += "<strong>Adresse :</strong><br/>"
                infos += "%s<br/>" % address_splitted[0]
                infos += "%s - %s<br/>" % (address_splitted[3], address_splitted[4])
                infos += "<br/>"
        if com:
            response_dict = {}
            values = com.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            tel = response_dict.get('Téléphone filaire', '')

            if tel:
                infos += "<strong>Téléphone :</strong><br/>"
                infos += "%s<br/>" % tel
                infos += "<br/>"

            fax = response_dict.get('Télécopieur /fax', '')

            if fax:
                infos += "<strong>Fax :</strong><br/>"
                infos += "%s<br/>" % fax
                infos += "<br/>"

            portable = response_dict.get('Téléphone cellulaire', '')

            if portable:
                infos += "<strong>Portable :</strong><br/>"
                infos += "%s<br/>" % portable
                infos += "<br/>"

        return infos

    def filter_email(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Mél', '')
        return ''

    def filter_website(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Site web (URL)', '')

        return ''

    def filter_type1(self, src, val):
        instance, created = TouristicContentType1.objects.get_or_create(
            category_id=1,
            label=val
        )

        return [instance, ]

class TourinsoftACC28(TourinsoftHOT28):
    label = "Tourinsoft ACC 28"
    url = "http://wcf.tourinsoft.com/Syndication/cdt28/fa756b5c-2914-48f3-9ca6-4a0440d79830/Objects"

    m2m_fields = {
        'type1': 'ObjectTypeName',
        'type2': 'Labels',
    }

    def filter_contact(self, src, val):
        infos = ""
        com, adresse = val

        if adresse:
            address_splitted = adresse.split('|')
            if address_splitted:
                infos += "<strong>Adresse :</strong><br/>"
                infos += "%s<br/>" % address_splitted[0]
                infos += "%s - %s<br/>" % (address_splitted[3], address_splitted[4])
                infos += "<br/>"
        if com:
            response_dict = {}
            values = com.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            tel = response_dict.get('Téléphone filaire', '')

            if tel:
                infos += "<strong>Téléphone :</strong><br/>"
                infos += "%s<br/>" % tel
                infos += "<br/>"

            fax = response_dict.get('Télécopieur /fax', '')

            if fax:
                infos += "<strong>Fax :</strong><br/>"
                infos += "%s<br/>" % fax
                infos += "<br/>"

            portable = response_dict.get('Téléphone cellulaire', '')

            if portable:
                infos += "<strong>Portable :</strong><br/>"
                infos += "%s<br/>" % portable
                infos += "<br/>"

        return infos

    def filter_email(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Mél', '')
        return ''

    def filter_website(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Site web (URL)', '')

        return ''

    def filter_type1(self, src, val):
        instance, created = TouristicContentType1.objects.get_or_create(
            category_id=1,
            label=val
        )

        return [instance, ]


class TourinsoftHPA61(TourinsoftParser61):
    label = "TourinSoft HPA 61"
    url = "http://wcf.tourinsoft.com/Syndication/cdt61/eab19ff3-8246-4391-897a-c327faef8204/Objects"
    m2m_fields = {
        'type1': 'ObjectTypeName',
    }

    def filter_contact(self, src, val):
        infos = ""
        com, adresse = val

        if adresse:
            address_splitted = adresse.split('|')
            if address_splitted:
                infos += "<strong>Adresse :</strong><br/>"
                infos += "%s<br/>" % address_splitted[0]
                infos += "%s - %s<br/>" % (address_splitted[4], address_splitted[5])
                infos += "<br/>"
        if com:
            response_dict = {}
            values = com.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            tel = response_dict.get('Téléphone filaire', '')

            if tel:
                infos += "<strong>Téléphone :</strong><br/>"
                infos += "%s<br/>" % tel
                infos += "<br/>"

            fax = response_dict.get('Télécopieur /fax', '')

            if fax:
                infos += "<strong>Fax :</strong><br/>"
                infos += "%s<br/>" % fax
                infos += "<br/>"

            portable = response_dict.get('Téléphone cellulaire', '')

            if portable:
                infos += "<strong>Portable :</strong><br/>"
                infos += "%s<br/>" % portable
                infos += "<br/>"

        return infos

    def filter_email(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Mél', '')
        return ''

    def filter_website(self, src, val):
        if val:
            response_dict = {}
            values = val.split('#')

            for value in values:
                key, data = value.split('|')
                response_dict.update({
                    key: data
                })

            return response_dict.get('Site web (URL)', '')

        return ''

    def filter_category(self, src, val):
        return TouristicContentCategory.objects.get(pk=1)

    def filter_type1(self, src, val):
        instance, created = TouristicContentType1.objects.get_or_create(
            category_id=1,
            label=val
        )

        return [instance, ]