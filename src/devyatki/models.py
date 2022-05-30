from behaviors.behaviors import Timestamped
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    User class with link to telegram profile
    """
    email = models.EmailField(_('email address'), blank=True, null=True)
    password = models.CharField(_("password"), max_length=128, blank=True, null=True)

    telegram_username = models.CharField(max_length=128, unique=True)
    telegram_data = models.TextField(null=True, blank=True)
    telegram_chat_id = models.TextField(null=True, blank=True)

    rejected_count = models.SmallIntegerField(default=0)

    MODERATION_STATUS_INTRO = "intro"
    MODERATION_STATUS_ON_REVIEW = "on_review"
    MODERATION_STATUS_REJECTED = "rejected"
    MODERATION_STATUS_APPROVED = "approved"
    MODERATION_STATUS_DELETED = "deleted"
    MODERATION_STATUSES = [
        (MODERATION_STATUS_INTRO, MODERATION_STATUS_INTRO),
        (MODERATION_STATUS_ON_REVIEW, MODERATION_STATUS_ON_REVIEW),
        (MODERATION_STATUS_REJECTED, MODERATION_STATUS_REJECTED),
        (MODERATION_STATUS_APPROVED, MODERATION_STATUS_APPROVED),
        (MODERATION_STATUS_DELETED, MODERATION_STATUS_DELETED),
    ]

    moderation_status = models.CharField(
        max_length=32, choices=MODERATION_STATUSES,
        default=MODERATION_STATUS_INTRO, null=False,
        db_index=True
    )

    class Meta:
        db_table = "users"

    @property
    def is_approved(self):
        return self.moderation_status == self.MODERATION_STATUS_APPROVED


class PlateEntry(Timestamped):
    plate_number = models.CharField(_("plate"), max_length=32, null=True, blank=True)
    telegram_message = models.TextField(null=True, blank=True)
    telegram_message_id = models.IntegerField(default=0)
    telegram_photo_id = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vk_message_id = models.IntegerField(default=0)

