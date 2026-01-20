from bluer_objects import objects
from bluer_objects import storage

from bluer_sandbox import env
from bluer_sandbox.green.db import GreenDB


def test_green_db():
    assert storage.download(
        object_name=env.BLUER_SANDBOX_GREEN_OBJECT_NAME,
        filename="metadata.yaml",
    )

    db = GreenDB()
    assert db.raw

    assert db.review(log=True)

    db.object_name = objects.unique_object("test_green_db")
    assert db.save()

    db2 = GreenDB(db.object_name)
    assert len(db2.raw) == len(db.raw)
