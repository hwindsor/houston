"""empty message

Revision ID: 2fd199f6ee7f
Revises: f4f2436d30f2
Create Date: 2020-09-11 13:10:16.227888

"""

# revision identifiers, used by Alembic.
revision = '2fd199f6ee7f'
down_revision = 'f4f2436d30f2'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

import app
import app.extensions


from app.modules.submissions.models import SubmissionMajorType


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asset', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_asset_ext'), ['ext'], unique=False)
        batch_op.create_index(batch_op.f('ix_asset_mime_type'), ['mime_type'], unique=False)

    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.alter_column('submission_major_type',
               existing_type=sa.VARCHAR(length=10),
               nullable=False,
               server_default=SubmissionMajorType.unknown,
        )
        batch_op.create_index(batch_op.f('ix_submission_submission_major_type'), ['submission_major_type'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_submission_submission_major_type'))
        batch_op.alter_column('submission_major_type',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)

    with op.batch_alter_table('asset', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_asset_mime_type'))
        batch_op.drop_index(batch_op.f('ix_asset_ext'))

    # ### end Alembic commands ###
