import Bio.PDB
from Bio.PDB import PDBParser

#PDB file reader 

def main():
    pdb_file_path = #Insert your PDB file path here
    parser = PDBParser
    structure = parser.get_structure('protein', pdb_file_path)

for model in Bio.PDB.PDBParser().get_structure(#add your protein PDB ID here ex. "4N6N", #Insert your PDB file path here) :
    for chain in model :
        polypeptides = Bio.PDB.PPBuilder().build_peptides(chain)
        for poly_index, poly in enumerate(polypeptides) :
            print ("Model %s Chain %s" % (str(model.id), str(chain.id))),
            print ("(part %i of %i)" % (poly_index+1, len(polypeptides))),
            print ("length %i" % (len(poly))),
            print ("from %s%i" % (poly[0].resname, poly[0].id[1])),
            print ("to %s%i" % (poly[-1].resname, poly[-1].id[1]))
            phi_psi = poly.get_phi_psi_list()
            for res_index, residue in enumerate(poly) :
                res_name = "%s%i" % (residue.resname, residue.id[1])
                print (res_name, phi_psi[res_index])


        
#Source: 
# Cock, P. (2006), Biopython (Version 1.4) [code]. https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/ramachandran/calculate/#BioPython 
# Note: this code was edited to contain a file path
