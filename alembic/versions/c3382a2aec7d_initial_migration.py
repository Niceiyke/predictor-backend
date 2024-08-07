"""initial migration

Revision ID: c3382a2aec7d
Revises: 
Create Date: 2024-07-02 17:32:21.238892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3382a2aec7d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fixtures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=220), nullable=True),
    sa.Column('week', sa.String(length=10), nullable=True),
    sa.Column('day', sa.String(length=10), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('time', sa.String(length=10), nullable=True),
    sa.Column('league', sa.String(length=100), nullable=True),
    sa.Column('home_team', sa.String(length=100), nullable=True),
    sa.Column('home_score', sa.String(length=10), nullable=True),
    sa.Column('home_xg', sa.String(length=10), nullable=True),
    sa.Column('score', sa.String(length=10), nullable=True),
    sa.Column('away_score', sa.String(length=10), nullable=True),
    sa.Column('away_xg', sa.String(length=10), nullable=True),
    sa.Column('away_team', sa.String(length=100), nullable=True),
    sa.Column('attendance', sa.Integer(), nullable=True),
    sa.Column('venue', sa.String(length=100), nullable=True),
    sa.Column('referee', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('SCHEDULED', 'IN_PROGRESS', 'COMPLETED', 'POSTPONED', name='fixturestatus'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fixtures_away_team'), 'fixtures', ['away_team'], unique=False)
    op.create_index(op.f('ix_fixtures_home_team'), 'fixtures', ['home_team'], unique=False)
    op.create_index(op.f('ix_fixtures_id'), 'fixtures', ['id'], unique=False)
    op.create_index(op.f('ix_fixtures_key'), 'fixtures', ['key'], unique=False)
    op.create_index(op.f('ix_fixtures_week'), 'fixtures', ['week'], unique=False)
    op.create_table('leagues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('premium', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_leagues_id'), 'leagues', ['id'], unique=False)
    op.create_index(op.f('ix_leagues_name'), 'leagues', ['name'], unique=False)
    op.create_table('task_statuses',
    sa.Column('task_id', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('task_id')
    )
    op.create_index(op.f('ix_task_statuses_status'), 'task_statuses', ['status'], unique=False)
    op.create_index(op.f('ix_task_statuses_task_id'), 'task_statuses', ['task_id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('point', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('predictions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('fixture_id', sa.Integer(), nullable=True),
    sa.Column('home_prediction_score', sa.String(length=10), nullable=True),
    sa.Column('away_prediction_score', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['fixture_id'], ['fixtures.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_predictions_id'), 'predictions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_predictions_id'), table_name='predictions')
    op.drop_table('predictions')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_task_statuses_task_id'), table_name='task_statuses')
    op.drop_index(op.f('ix_task_statuses_status'), table_name='task_statuses')
    op.drop_table('task_statuses')
    op.drop_index(op.f('ix_leagues_name'), table_name='leagues')
    op.drop_index(op.f('ix_leagues_id'), table_name='leagues')
    op.drop_table('leagues')
    op.drop_index(op.f('ix_fixtures_week'), table_name='fixtures')
    op.drop_index(op.f('ix_fixtures_key'), table_name='fixtures')
    op.drop_index(op.f('ix_fixtures_id'), table_name='fixtures')
    op.drop_index(op.f('ix_fixtures_home_team'), table_name='fixtures')
    op.drop_index(op.f('ix_fixtures_away_team'), table_name='fixtures')
    op.drop_table('fixtures')
    # ### end Alembic commands ###
