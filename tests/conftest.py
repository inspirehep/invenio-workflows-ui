# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.


"""Pytest configuration."""

from __future__ import absolute_import, print_function

import os

import pytest
from flask import Flask
from flask_babelex import Babel
from flask_cli import FlaskCLI
from flask_login import LoginManager
from invenio_db import InvenioDB
from invenio_workflows import InvenioWorkflows
from invenio_workflows_ui import InvenioWorkflowsUI


@pytest.fixture()
def app():
    """Flask application fixture."""
    app = Flask('testapp')
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db')
    )
    Babel(app)
    FlaskCLI(app)
    LoginManager(app)
    InvenioDB(app)
    InvenioWorkflows(app)
    InvenioWorkflowsUI(app)
    return app
