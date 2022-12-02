from setuptools import setup, find_packages

setup(
    name="test_action",
    version="0.1.2",
    author='Quangtri Thai',
    author_email='qthai@deepcast.ai',
    description='Test repo for actions',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license='Sabernetic Proprietary License',
    packages=find_packages(),
    install_requires=[
        "pytest>=6.2.4",
        "pandas>=1.4.2",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
