from django.contrib.auth import get_user_model
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from .models import Light


class Lightadmin(ModelAdmin):
    model = Light
    menu_label = "Lights"
    menu_icon = "fa-lightbulb-o"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False


# class TrackAdmin(ModelAdmin):
#     model = Track
#     menu_label = "Track"
#     menu_icon = "fa-play"
#     menu_order = 290
#     add_to_settings_menu = False
#     exclude_from_explorer = False


# class TrackManagement(ModelAdminGroup):
#     menu_label = "Track Management"
#     menu_icon = "fa-meetup"
#     menu_order = 110
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     items = (
#         PACAdmin,
#         TrackAdmin,
#     )


modeladmin_register(Lightadmin)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
