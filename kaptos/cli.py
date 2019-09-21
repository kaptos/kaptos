import kaptos.resources
import roax.cli

cli = roax.cli.CLI()

for resource in {
    "member",
    "report",
    "station",
    "tasks",
    "team",
    "token",
    "signal",
    "user",
}:
    cli.register_resource(resource, getattr(kaptos.resources, resource))

cli.loop()
