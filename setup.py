import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cogworks_week1",
    version="1.0.0",
    author="Ryan Soklaski (@rsokl)",
    author_email="ry26099@mit.edu",
    url="https://github.com/JuliusStein/Week1_pip",
    description="Provides simple interface for recording audio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'MIT',
    zip_safe = False,
    install_requires=[
        "pyaudio",
        "ipython",
        "jupyter",
        "notebook",
        "numpy",
        "scipy",
        "matplotlib",
        "numba",
        "librosa",
        "ffmpeg",
        "mygrad"
    ],
    packages=['microphone'],
    python_requires=">=3.6",
)

# try:
#     import pyaudio
# except ImportError:
#       print("Warning: `pyaudio` must be installed in order to use `microphone`")
