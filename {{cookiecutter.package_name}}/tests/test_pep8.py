#!/usr/bin/env python

import {{ cookiecutter.package_name }}
import pep8
import os.path

def test_pep8_conformance():
    """Test that we conform to PEP8."""
    pep8style = pep8.StyleGuide(prefix='E')
    result = pep8style.check_files([
        os.path.dirname({{ cookiecutter.package_name }}.__file__),
    ])
    assert result.total_errors == 0
