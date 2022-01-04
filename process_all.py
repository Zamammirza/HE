import utils, bbhe, clahe, no_processing, splinet
import no_processing

print("No Processing")
utils.apply_to_all(no_processing)
print("SpliNet")
utils.apply_to_all(splinet)
print("CLAHE")
utils.apply_to_all(clahe)
print("BBHE")
utils.apply_to_all(bbhe)