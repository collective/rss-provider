from plone import schema
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class IRSSFeed(model.Schema):
    """Dexterity-Schema for RSS Feed"""

    title = schema.TextLine(
        title=u"Title",
        required=True,
    )

    description = RichText(
        title=u"Description",
        description="Description of the RSS Feed (max. 2000 characters)",
        max_length=2000,
        required=True,
    )

    rss_url = schema.URI(
        title=u"RSS Feed URL",
        required=True,
    )

    update_interval = schema.Int(
        title=u"Update Interval (minutes)",
        required=True,
        default=60,
    )


@implementer(IRSSFeed)
class RSSFeed(Container):
    """Content-type class for IRSSFeed"""