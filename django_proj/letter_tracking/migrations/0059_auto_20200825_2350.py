# Generated by Django 3.1 on 2020-08-25 23:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0058_auto_20200825_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='destinatario',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', 'N/a'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('Líder de la mayoría Cámara', 'Líder de la mayoría Cámara'), ('Líder de la minoría Cámara', 'Líder de la minoría Cámara'), ('Líder de la mayoría Senado', 'Líder de la mayoría Senado'), ('Líder de la minoría Senado', 'Líder de la minoría Senado'), ('Liderazgo Comité Apropiaciones Senado', 'Liderazgo Comité Apropiaciones Senado'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS'), ('Other', 'Other')], default='None', help_text="<em>if 'Other', please specify in the text box below</em>", max_length=100),
        ),
    ]