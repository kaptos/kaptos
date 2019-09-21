"""Kaptos resources module."""

import roax.resource


_resources = roax.resource.Resources(
    {
        "members": "kaptos.resources.v1.members:Members",
        "reports": "kaptos.resources.v1.reports:Reports",
        "stations": "kaptos.resources.v1.stations:Stations",
        "tasks": "kaptos.resources.v1.tasks:Tasks",
        "teams": "kaptos.resources.v1.teams:Teams",
        "tokens": "kaptos.resources.v1.tokens:Tokens",
        "signals": "kaptos.resources.v1.signals:Signals",
        "users": "kaptos.resources.v1.users:Users",
    }
)


def __getattr__(name):
    try:
        return _resources[name]
    except KeyError:
        raise AttributeError
