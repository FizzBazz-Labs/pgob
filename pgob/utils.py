import os
import subprocess


def convert_to_pdf(file, output):
    """Converts a file to PDF using LibreOffice."""

    command = ['libreoffice', '--headless', '--convert-to', 'pdf', file, '--outdir', os.path.dirname(output)]
    subprocess.run(command)
