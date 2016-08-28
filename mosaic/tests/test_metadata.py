from mosaic import metadata
from mutagen import easyid3, flac, mp3
import pkg_resources
import pytest


@pytest.fixture
def mp3_file():
    """Returns a resource of the test MP3 file that can be passed as an argument
    to the unit tests. """
    file = pkg_resources.resource_filename('mosaic.tests', '01_Ghosts_I_320kb.mp3')
    return file


@pytest.fixture
def flac_file():
    """Returns a resource of the test FLAC file that can be passed as an argument
    to the unit tests."""
    file = pkg_resources.resource_filename('mosaic.tests', '02_Ghosts_I.flac')
    return file


def test_identify_mp3_filetype(mp3_file):
    """Asserts that the identify_filetype function returns an MP3 object created by mutagen."""
    assert metadata.identify_filetype(mp3_file) == mp3.MP3(mp3_file, ID3=easyid3.EasyID3)


def test_identify_flac_filetype(flac_file):
    """Asserts that the identify_filetype function returns a FLAC object created by mutagen."""
    assert metadata.identify_filetype(flac_file) == flac.FLAC(flac_file)


def test_mp3_tags(mp3_file):
    """Asserts that the extract_meta_data function returns all of the MP3 tags necessary for the
    music player to use."""
    assert isinstance(metadata.extract_meta_data(mp3_file), dict)
    assert 'Ghosts I-IV' in metadata.extract_meta_data(mp3_file).values()


def test_flac_tags(flac_file):
    """Asserts that the extract_meta_data function returns all of the FLAC tags necessary for the
    music player to use."""
    assert isinstance(metadata.extract_meta_data(flac_file), dict)
    assert 'Ghosts I-IV' in metadata.extract_meta_data(flac_file).values()


def test_mp3_metadata(mp3_file):
    """Checks that the correct metadata is extracted from an MP3 file."""
    data = metadata.metadata(mp3_file)
    assert data[0] == 'Ghosts I-IV'
    assert data[1] == 'Nine Inch Nails'
    assert data[2] == '1 Ghosts I'


def test_flac_metadata(flac_file):
    """Checks that the correct metadata is extracted from a FLAC file."""
    data = metadata.metadata(flac_file)
    assert data[0] == 'Ghosts I-IV'
    assert data[1] == 'Nine Inch Nails'
    assert data[2] == '2 Ghosts I'
