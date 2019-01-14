"""Setup file for bruteforce package."""
from setuptools import find_packages # pylint: disable=unused-import
from numpy.distutils.core import setup, Extension
from numpy.distutils.log import set_verbosity
from setup_helpers import BuildExtCommand

set_verbosity(1)

CPU_SEARCH_EXT = Extension('isingcpu',
                           extra_compile_args=['-fPIC',
                                               '-fopenmp',
                                               '-DTHRUST_DEVICE_SYSTEM=THRUST_DEVICE_SYSTEM_OMP',
                                               '-lstdc++'],
                           sources=['./ising/ext_sources/bucketSelectCPU.cpp',
                                    './ising/ext_sources/bucketselectcpu.f90',
                                    './ising/ext_sources/cpucsort.cpp',
                                    './ising/ext_sources/cpu_thrust_sort.f90',
                                    './ising/ext_sources/cpusearch.pyf',
                                    './ising/ext_sources/cpusearch.f90'])

GPU_SEARCH_EXT = Extension('isinggpu',
                           sources=['./ising/ext_sources/gpusearch.pyf',
                                    './ising/ext_sources/gpucsort.cu',
                                    './ising/ext_sources/global.f90',
                                    './ising/ext_sources/gpu_thrust_sort.f90',
                                    './ising/ext_sources/bucketSelect.cu',
                                    './ising/ext_sources/bucketselect.f90',
                                    './ising/ext_sources/search.f90',
                                    './ising/ext_sources/gpusearch.f90'],
                           extra_link_args=['-Mcuda'],
                           extra_f90_compile_args=['-v', '-Mcuda,nordc'])

EXTENSIONS = [CPU_SEARCH_EXT, GPU_SEARCH_EXT]

setup(
    version='0.1.21',
    name='ising',
    cmdclass={'build_ext': BuildExtCommand},
    install_requires=['numpy>=0.16.0', 'psutil', 'progressbar2', 'future'],
    ext_modules=EXTENSIONS,
    packages=['ising']
)
