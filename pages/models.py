from django.db import models
from django import forms
from django.http import JsonResponse

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                StreamFieldPanel,
                                                InlinePanel,
                                                MultiFieldPanel,
                                                PageChooserPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index

from wagtail.wagtailcore.blocks import TextBlock, ChooserBlock, StructBlock, ListBlock, FieldBlock, CharBlock, RichTextBlock, PageChooserBlock, RawHTMLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from modelcluster.fields import ParentalKey


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(('left','Wrap left'),('right','Wrap right'),('mid','Mid width'),('full','Full width'),))


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(('normal','Normal'),('full','Full width'),))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    alignment = ImageFormatChoiceBlock()


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class CarouselItem(LinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField("Embed URL", blank=True)
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class Funders(LinkFields):
    name = models.CharField(max_length=255, help_text="Funder Name")
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = RichTextField()
    
    api_fields = ('name', 'logo', 'description', )
    
    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo'),
        FieldPanel('description'),
    ]


# Home Page
class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('pages.HomePage', related_name='carousel_items')


class HomePage(Page):
    about_us_heading = models.CharField(max_length=255)
    about_us = RichTextField()
    wwd_higher_ed_heading = models.CharField(max_length=255)
    wwd_higher_ed = RichTextField()
    wwd_k12_heading = models.CharField(max_length=255)
    wwd_12 = RichTextField()
    give_heading = models.CharField(max_length=255)
    give_to_openstax = RichTextField()
    adopter_heading = models.CharField(max_length=255)
    adopter = RichTextField()
    allies_heading = models.CharField(max_length=255)
    allies = RichTextField()
    ap_disclaimer = RichTextField()
    
    api_fields = (
        'about_us_heading', 
        'about_us', 
        'wwd_higher_ed_heading',
        'wwd_higher_ed',
        'wwd_k12_heading',
        'wwd_k12',
        'give_heading',
        'give_to_openstax',
        'adopter_heading',
        'adopter',
        'allies_heading',
        'allies',
        'ap_disclaimer',)

    class Meta:
        verbose_name = "Home Page"

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('about_us_heading'),
        FieldPanel('about_us'),
        FieldPanel('wwd_higher_ed_heading'),
        FieldPanel('wwd_higher_ed'),
        FieldPanel('wwd_k12_heading'),
        FieldPanel('wwd_12'),
        FieldPanel('give_heading'),
        FieldPanel('give_to_openstax'),
        FieldPanel('adopter_heading'),
        FieldPanel('adopter'),
        FieldPanel('allies_heading'),
        FieldPanel('allies'),
        FieldPanel('ap_disclaimer'),
        InlinePanel('carousel_items', label="Carousel items"),
    ]


class HigherEducationCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('pages.HigherEducation', related_name='higher_education_carousel_items')
    
    
class HigherEducation(Page):
    intro_heading = models.CharField(max_length=255)
    intro = RichTextField()
    get_started_heading = models.CharField(max_length=255)
    get_started_step_1 = RichTextField()
    get_started_step_2 = RichTextField()
    get_started_step_3 = RichTextField()
    get_started_step_4 = RichTextField()
    our_books_heading = models.CharField(max_length=255)
    our_books = RichTextField()
    our_impact_heading = models.CharField(max_length=255)
    our_impact = RichTextField()
    cnx_heading = models.CharField(max_length=255)
    cnx = RichTextField()
    allies_heading = models.CharField(max_length=255)
    allies = RichTextField()
    ally_1_heading = models.CharField(max_length=255)
    ally_1 = RichTextField()
    ally_2_heading = models.CharField(max_length=255)
    ally_2 = RichTextField()
    ally_3_heading = models.CharField(max_length=255)
    ally_3 = RichTextField()
    ally_4_heading = models.CharField(max_length=255)
    ally_4 = RichTextField()
    ally_5_heading = models.CharField(max_length=255)
    ally_5 = RichTextField()

    api_fields = (
        'intro_heading', 
        'intro', 
        'get_started_heading', 
        'get_started_step_1', 
        'get_started_step_2', 
        'get_started_step_3', 
        'get_started_step_4', 
        'our_books_heading', 
        'our_books', 
        'our_impact_heading', 
        'our_impact', 
        'cnx_heading', 
        'cnx', 
        'allies_heading', 
        'allies', 
        'ally_1_heading', 
        'ally_1', 
        'ally_2_heading', 
        'ally_2', 
        'ally_3_heading', 
        'ally_3', 
        'ally_4_heading', 
        'ally_4', 
        'ally_5_heading', 
        'ally_5', 
        'slug', 
        'seo_title', 
        'search_description', 
        'go_live_at', 
        'expire_at', 
    )
    
    content_panels = [
        FieldPanel('title', classname="full title"),
        InlinePanel('higher_education_carousel_items', label="Carousel items"),
        FieldPanel('intro_heading'),
        FieldPanel('intro'),
        FieldPanel('get_started_heading'),
        FieldPanel('get_started_step_1'),
        FieldPanel('get_started_step_2'),
        FieldPanel('get_started_step_3'),
        FieldPanel('get_started_step_4'),
        FieldPanel('our_books_heading'),
        FieldPanel('our_books'),
        FieldPanel('our_impact_heading'),
        FieldPanel('our_impact'),
        FieldPanel('cnx_heading'),
        FieldPanel('cnx'),
        FieldPanel('allies_heading'),
        FieldPanel('allies'),
        FieldPanel('ally_1_heading'),
        FieldPanel('ally_1'),
        FieldPanel('ally_2_heading'),
        FieldPanel('ally_2'),
        FieldPanel('ally_3_heading'),
        FieldPanel('ally_3'),
        FieldPanel('ally_4_heading'),
        FieldPanel('ally_4'),
        FieldPanel('ally_5_heading'),
        FieldPanel('ally_5'),
    ]
    
    def serve(self, request):
        return JsonResponse({
            'intro_heading': self.intro_heading, 
            'intro': self.intro, 
            'get_started_heading': self.get_started_heading, 
            'get_started_step_1': self.get_started_step_1, 
            'get_started_step_2': self.get_started_step_2, 
            'get_started_step_3': self.get_started_step_3, 
            'get_started_step_4': self.get_started_step_4, 
            'our_books_heading': self.our_books_heading, 
            'our_books': self.our_books, 
            'our_impact_heading': self.our_impact_heading, 
            'our_impact': self.our_impact, 
            'cnx_heading': self.cnx_heading, 
            'cnx': self.cnx, 
            'allies_heading': self.allies_heading, 
            'allies': self.allies, 
            'ally_1_heading': self.ally_1_heading, 
            'ally_1': self.ally_1, 
            'ally_2_heading': self.ally_2_heading, 
            'ally_2': self.ally_2, 
            'ally_3_heading': self.ally_3_heading, 
            'ally_3': self.ally_3, 
            'ally_4_heading': self.ally_4_heading, 
            'ally_4': self.ally_4, 
            'ally_5_heading': self.ally_5_heading, 
            'ally_5': self.ally_5, 
            'slug': self.slug, 
            'seo_title': self.seo_title, 
            'search_description': self.search_description, 
            'go_live_at': self.go_live_at, 
            'expire_at': self.expire_at, 
        })


class K12(Page):
    classroom_text = RichTextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('classroom_text'),
    ]


class Products(Page):
    intro_heading = models.CharField(max_length=255)
    intro = RichTextField()
    tutor_heading = models.CharField(max_length=255)
    tutor = RichTextField()
    concept_coach_heading = models.CharField(max_length=255)
    concept_coach = RichTextField()
    cnx_heading = models.CharField(max_length=255)
    cnx = RichTextField()
    allies_heading = models.CharField(max_length=255)
    allies = RichTextField()
    ally_1_heading = models.CharField(max_length=255)
    ally_1 = RichTextField()
    ally_2_heading = models.CharField(max_length=255)
    ally_2 = RichTextField()
    ally_3_heading = models.CharField(max_length=255)
    ally_3 = RichTextField()
    ally_4_heading = models.CharField(max_length=255)
    ally_4 = RichTextField()
    ally_5_heading = models.CharField(max_length=255)
    ally_5 = RichTextField()
    
    api_fields = (
        'intro_heading', 
        'intro', 
        'tutor_heading', 
        'tutor', 
        'concept_coach_heading', 
        'concept_coach', 
        'cnx_heading', 
        'cnx', 
        'allies_heading', 
        'allies', 
        'ally_1_heading', 
        'ally_1', 
        'ally_2_heading', 
        'ally_2', 
        'ally_3_heading', 
        'ally_3', 
        'ally_4_heading', 
        'ally_4', 
        'ally_5_heading', 
        'ally_5', 
        'slug', 
        'seo_title', 
        'search_description', 
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro_heading'),
        FieldPanel('intro'),
        FieldPanel('tutor_heading'),
        FieldPanel('tutor'),
        FieldPanel('concept_coach_heading'),
        FieldPanel('concept_coach'),
        FieldPanel('cnx_heading'),
        FieldPanel('cnx'),
        FieldPanel('allies_heading'),
        FieldPanel('allies'),
        FieldPanel('ally_1_heading'),
        FieldPanel('ally_1'),
        FieldPanel('ally_2_heading'),
        FieldPanel('ally_2'),
        FieldPanel('ally_3_heading'),
        FieldPanel('ally_3'),
        FieldPanel('ally_4_heading'),
        FieldPanel('ally_4'),
        FieldPanel('ally_5_heading'),
        FieldPanel('ally_5'),
    ]


class Research(Page):
    classroom_text = RichTextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('classroom_text'),
    ]


class ContactUs(Page):
    classroom_text = RichTextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('classroom_text'),
    ]


class AboutUsFunders(Orderable, Funders):
    page = ParentalKey('pages.AboutUs', related_name='funders')
    
    
class AboutUs(Page):
    who_we_are = RichTextField()
    funder_intro = RichTextField()

    api_fields = (
        'who_we_are', 
        'funder_intro', 
        'funders', 
        'slug', 
        'seo_title', 
        'search_description',
    )
    
    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('who_we_are'),
        FieldPanel('funder_intro'),
        InlinePanel('funders', label="Funders"),
    ]


class GeneralPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
    ])
    
    api_fields = (
        'title',
        'body',
    )
    
    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body'),
    ]

class Give(Page):
    touchnet_form = RawHTMLBlock()

    content_panels = [
        FieldPanel('title', classname="full title"),
        #FieldPanel('touchnet_form'),
    ]


class Adopters(Page):
    classroom_text = RichTextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('classroom_text'),
    ]


class EcosystemAllies(Page):
    classroom_text = RichTextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('classroom_text'),
    ]


class AdoptionForm(Page):
    classroom_text = RichTextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('classroom_text'),
    ]


#class GeneralHTMLPage(Page): #this will be used for confirmations/forms from sales force, these won't be editable
