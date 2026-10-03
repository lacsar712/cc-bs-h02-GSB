from h02_extra_trap import dirt_armed, form_visible, gate


def test_writer_can_write():
    assert gate("writer") is True


def test_reader_cannot_write():
    assert gate("reader") is False
    assert form_visible() is False
    assert dirt_armed() is False
