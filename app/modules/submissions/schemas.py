# -*- coding: utf-8 -*-
"""
Serialization schemas for Submissions resources RESTful API
----------------------------------------------------
"""

from flask_marshmallow import base_fields
from flask_restplus_patched import ModelSchema

from .models import Submission

from app.modules.assets.models import Asset


class BaseSubmissionSchema(ModelSchema):
    """
    Base Submission schema exposes only the most general fields.
    """

    class Meta:
        # pylint: disable=missing-docstring
        model = Submission
        fields = (
            Submission.guid.key,
            Submission.commit.key,
            Submission.major_type.key,
            Submission.description.key,
        )
        dump_only = (
            Submission.guid.key,
            Submission.commit.key,
        )


class DetailedSubmissionSchema(BaseSubmissionSchema):
    """
    Detailed Submission schema exposes all useful fields.
    """

    assets = base_fields.Nested(
        'BaseAssetSchema',
        exclude=(Asset.submission_guid.key),
        many=True,
    )

    class Meta(BaseSubmissionSchema.Meta):
        fields = BaseSubmissionSchema.Meta.fields + (
            Submission.owner_guid.key,
            Submission.created.key,
            Submission.updated.key,
            Submission.assets.key,
        )
        dump_only = BaseSubmissionSchema.Meta.dump_only + (
            Submission.owner_guid.key,
            Submission.created.key,
            Submission.updated.key,
        )
