# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio App RDM is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Blueprint used for registering resources."""

from __future__ import absolute_import, print_function

from flask import Blueprint, current_app, render_template
from invenio_rdm_records.resources import record_resource


def create_blueprint(app):
    """Create blueprint and register resources."""

    # Register required resources
    app.register_blueprint(
        record_resource.as_blueprint(name="invenio_resource_record")
    )
