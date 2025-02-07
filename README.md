dihedral_angle_radians_to_degrees (converter)
=====================
Protein PDB files possess the atomic coordinates of amino acid atom locations. These atomic coordinates can be parsed into dihedral angle values, which can then be used to predict the secondary structures of proteins. To find the modules for converting dihedral angles to secondary structures, find my "dihedral_angles_to_secondary_structures" repository at: https://github.com/T-Draco/dihedral-angles-to-secondary-structures

This program utilizes Biopython, specifically the PDBParser package. This repository is intended for the conversion of PDB atomic coordinates into dihedral angle values, and then the conversion of dihedral angle values from radians to degrees. This module was made for non-profit reasons. Improvement edits to this repository are highly encouraged with proper source code citations and use of the GitHub branch function.

The PDBParser module, for PDB atomic coordinates to dihedral angle conversions, original source code was written by Dr. Peter Cock. 
Source: Cock, P. (2006), Biopython (Version 1.4) [code]. https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/ramachandran/calculate/#BioPython 

I slightly modified the code written by Dr. Peter Cock to include a file path function.

DISCLAIMER: complete accuracy is not guaranteed.

These modules require biopython and numpy.

The Biopython Project is an international association of developers of freely available Python tools for computational molecular biology.

The Biopython package is an open source software. Please see the "LICENSE.rst" file provided by: <https://github.com/biopython/biopython/blob/master/LICENSE.rst>` for further details.

Installation of biopython
========================

    pip install biopython

Biopython requires numpy, which is installed automatically when biopython is installed with the pip function.
