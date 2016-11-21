# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import v1.atomic_elements.atoms
import wagtail.wagtailimages.blocks
import v1.atomic_elements.organisms


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0023_conf_reg_form_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'image_text_25_75_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])))])), (b'image_text_50_50_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'sharing', wagtail.wagtailcore.blocks.StructBlock([(b'shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If checked, share links will be included below the items.', required=False, label=b'Include sharing links?')), (b'share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False))])), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'half_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'has_top_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_bottom_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H3 heading')), (b'sub_heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H4 heading')), (b'sub_heading_icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A list of icon names can be obtained at: https://cfpb.github.io/capital-framework/components/cf-icons/. Examples: linkedin-square, facebook-square, etc.', required=False, label=b'H4 heading icon')), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'third_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'has_top_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_bottom_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H3 heading')), (b'sub_heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H4 heading')), (b'sub_heading_icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A list of icon names can be obtained at: https://cfpb.github.io/capital-framework/components/cf-icons/. Examples: linkedin-square, facebook-square, etc.', required=False, label=b'H4 heading icon')), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'}))])), (b'expandable', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])), (b'expandable_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_accordion', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'expandables', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'job_listing_table', wagtail.wagtailcore.blocks.StructBlock([(b'first_row_is_table_header', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the first row as a header.', default=True, required=False)), (b'first_col_is_header', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the first column as a header.', default=False, required=False)), (b'is_full_width', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the table at full width.', default=False, required=False)), (b'is_striped', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the table with striped rows.', default=False, required=False)), (b'is_stacked', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Stack the table columns on mobile.', default=True, required=False)), (b'hide_closed', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Whether to hide jobs that are not currently open (jobs will automatically update)', default=True, required=False))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'question_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Was this page helpful to you?')), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit feedback'))])), (b'conference_registration_form', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Note: Additional form field options will appear in Preview and Publish modes.', required=False)), (b'code', wagtail.wagtailcore.blocks.CharBlock(label=b'GovDelivery Code')), (b'sessions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label=b'Session'), label=b'Sessions attending')), (b'capacity', v1.atomic_elements.atoms.IntegerBlock(help_text=b'Enter an integer that will be the conference attendance limit.')), (b'success_message', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Enter a message that will be shown on successful registration.')), (b'at_capacity_message', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'}))], help_text=b'Enter a message that will be shown when the event is at capacity.')), (b'failure_message', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter a message that will be shown if the GovDelivery subscription fails.'))]))], blank=True),
        ),
    ]
