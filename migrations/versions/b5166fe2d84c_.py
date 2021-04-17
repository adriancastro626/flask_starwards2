"""empty message

Revision ID: b5166fe2d84c
Revises: 
Create Date: 2021-04-17 21:17:21.264435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5166fe2d84c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('lastname', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('username')
    )
    op.create_table('personajes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('power', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('last_name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('power')
    )
    op.create_table('planeta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=False),
    sa.Column('population', sa.String(length=120), nullable=False),
    sa.Column('terrain', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name'),
    sa.UniqueConstraint('population'),
    sa.UniqueConstraint('terrain')
    )
    op.create_table('vehiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=120), nullable=False),
    sa.Column('capacity', sa.String(length=120), nullable=False),
    sa.Column('color', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('brand'),
    sa.UniqueConstraint('capacity'),
    sa.UniqueConstraint('color')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehiculos')
    op.drop_table('planeta')
    op.drop_table('personajes')
    op.drop_table('usuario')
    # ### end Alembic commands ###
