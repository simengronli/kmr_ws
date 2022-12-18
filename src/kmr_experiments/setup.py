from setuptools import setup

package_name = 'kmr_experiments'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jorgen',
    maintainer_email='myrvoldou@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drive_circle = kmr_experiments.drive_circle:main',
            'drive_square = kmr_experiments.drive_square:main',
            'drive_diagonal_square = kmr_experiments.drive_diagonal_square:main',
            'rotate = kmr_experiments.rotate:main',
        ],
    },
)
