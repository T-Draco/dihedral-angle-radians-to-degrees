import Bio.PDB
from Bio.PDB import PDBParser

#PDB file reader 

def main():
    pdb_file_path = r"C:\Users\Tania\Documents\Bioinformatics\Protein Bioinformatics\4n6n.pdb"
    parser = PDBParser
    structure = parser.get_structure('protein', pdb_file_path)

for model in Bio.PDB.PDBParser().get_structure("4N6N", r"C:\Users\Tania\Documents\Bioinformatics\Protein Bioinformatics\4n6n.pdb") :
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


        
