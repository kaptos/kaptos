import kaptos.resources


resources = {
    "members",
    "reports",
    "stations",
    "tasks",
    "teams",
    "tokens",
    "signals",
    "users",
}


def test_resources():
    for name in resources:
        getattr(kaptos.resources, name)
