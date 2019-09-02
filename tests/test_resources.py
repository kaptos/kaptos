import kaptos.resources


resources = {
    "members",
    "reports",
    "sessions",
    "stations",
    "tasks",
    "teams",
    "signals",
    "users",
}


def test_resources():
    for name in resources:
        getattr(kaptos.resources, name)
