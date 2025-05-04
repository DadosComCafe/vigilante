from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="python_sample_xlsx_report",
    version="0.0.40",
    description="Um gerador de relatório de análise quantitativa e qualitativa",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DadosComCafe/vigilante",
    author="dadoscomcafe",
    author_email="dadoscomcafe.dev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=["openpyxl==3.1.5"],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'python_sample_report=python_sample_xlsx_report.src.cli:main',
        ],
    }
)