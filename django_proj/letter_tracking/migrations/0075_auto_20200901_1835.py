# Generated by Django 3.1 on 2020-09-01 18:35

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0074_letter_cosigners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legislator',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='letter_tracking.state'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='caucus',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', 'N/a'), ('CHC', 'CHC'), ('Tri Caucus', 'Tri Caucus'), ('CHC', 'CHC'), ('Tri Caucus', 'Tri Caucus'), ('CHC', 'CHC'), ('Tri Caucus', 'Tri Caucus'), ('CHC', 'CHC'), ('Tri Caucus', 'Tri Caucus'), ('CHC', 'CHC'), ('Tri Caucus', 'Tri Caucus'), ('CHC', 'CHC'), ('Tri Caucus', 'Tri Caucus')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='letter',
            name='destinatario',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('N/a', 'N/a'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('Líder de la mayoría Cámara', 'Líder de la mayoría Cámara'), ('Líder de la minoría Cámara', 'Líder de la minoría Cámara'), ('Líder de la mayoría Senado', 'Líder de la mayoría Senado'), ('Líder de la minoría Senado', 'Líder de la minoría Senado'), ('Liderazgo Comité Apropiaciones Senado', 'Liderazgo Comité Apropiaciones Senado'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS'), ('Other', 'Other'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('Líder de la mayoría Cámara', 'Líder de la mayoría Cámara'), ('Líder de la minoría Cámara', 'Líder de la minoría Cámara'), ('Líder de la mayoría Senado', 'Líder de la mayoría Senado'), ('Líder de la minoría Senado', 'Líder de la minoría Senado'), ('Liderazgo Comité Apropiaciones Senado', 'Liderazgo Comité Apropiaciones Senado'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS'), ('Other', 'Other'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('Líder de la mayoría Cámara', 'Líder de la mayoría Cámara'), ('Líder de la minoría Cámara', 'Líder de la minoría Cámara'), ('Líder de la mayoría Senado', 'Líder de la mayoría Senado'), ('Líder de la minoría Senado', 'Líder de la minoría Senado'), ('Liderazgo Comité Apropiaciones Senado', 'Liderazgo Comité Apropiaciones Senado'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS'), ('Other', 'Other'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('Líder de la mayoría Cámara', 'Líder de la mayoría Cámara'), ('Líder de la minoría Cámara', 'Líder de la minoría Cámara'), ('Líder de la mayoría Senado', 'Líder de la mayoría Senado'), ('Líder de la minoría Senado', 'Líder de la minoría Senado'), ('Liderazgo Comité Apropiaciones Senado', 'Liderazgo Comité Apropiaciones Senado'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS'), ('Other', 'Other'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('Líder de la mayoría Cámara', 'Líder de la mayoría Cámara'), ('Líder de la minoría Cámara', 'Líder de la minoría Cámara'), ('Líder de la mayoría Senado', 'Líder de la mayoría Senado'), ('Líder de la minoría Senado', 'Líder de la minoría Senado'), ('Liderazgo Comité Apropiaciones Senado', 'Liderazgo Comité Apropiaciones Senado'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS'), ('Other', 'Other'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('Líder de la mayoría Cámara', 'Líder de la mayoría Cámara'), ('Líder de la minoría Cámara', 'Líder de la minoría Cámara'), ('Líder de la mayoría Senado', 'Líder de la mayoría Senado'), ('Líder de la minoría Senado', 'Líder de la minoría Senado'), ('Liderazgo Comité Apropiaciones Senado', 'Liderazgo Comité Apropiaciones Senado'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS'), ('Other', 'Other')], default='None', help_text="<em>If 'Other', please specify in the text box below</em>", max_length=100),
        ),
    ]