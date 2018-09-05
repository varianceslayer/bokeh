import pytest

import sys

from bokeh.command.bootstrap import main
from bokeh import __version__

is_python2 = sys.version_info[0] == 2

def test_no_subcommand(capsys):
    with pytest.raises(SystemExit):
        main(["bokeh"])
    out, err = capsys.readouterr()
    assert err == "ERROR: Must specify subcommand, one of: html, info, json, png, sampledata, secret, serve, static or svg\n"
    assert out == ""

def _assert_version_output(capsys):
    out, err = capsys.readouterr()
    if is_python2:
        err_expected = ("%s\n" % __version__)
        out_expected = ""
    else:
        err_expected = ""
        out_expected = ("%s\n" % __version__)
    assert err == err_expected
    assert out == out_expected

def test_version(capsys):
    with pytest.raises(SystemExit):
        main(["bokeh", "--version"])
    _assert_version_output(capsys)

def test_version_short(capsys):
    with pytest.raises(SystemExit):
        main(["bokeh", "-v"])
    _assert_version_output(capsys)

def test_error(capsys):
    from bokeh.command.subcommands.info import Info
    old_invoke = Info.invoke
    def err(x, y): raise RuntimeError("foo")
    Info.invoke = err
    with pytest.raises(SystemExit):
        main(["bokeh", "info"])
    out, err = capsys.readouterr()
    assert err == 'ERROR: foo\n'
    Info.invoke = old_invoke
