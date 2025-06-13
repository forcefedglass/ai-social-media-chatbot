from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="krita-scratchpad-docker",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A scratch pad docker plugin for Krita",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/krita-scratchpad-docker",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics :: Editors",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyQt5>=5.15.0",
    ],
    package_data={
        "krita_scratchpad_docker": ["*.desktop"],
    },
    entry_points={
        "krita.plugin": [
            "scratchpad_docker=krita_scratchpad_docker:register_plugin",
        ],
    },
)
