import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lottie-nb",
    version="0.0.1",
    author="kudanai",
    author_email="kudanai@gmail.com",
    description="Simple insertion of Lottie players into Jupyter Notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LottieFiles/LottieNB",
    packages=['lottienb', ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License ::  MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)