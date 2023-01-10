# Linguistic complexity projects
Scripts and datasets used and created for measuring linguistic complexity through information theoretic methods. This is part of [my PhD project](https://www.kuleuven.be/onderzoek/portaal/#/projecten/3H220490?lang=en&hl=en). Note that this is still a work in progress with semi frequent updates!

## Experiment 1: EDGe corpus

### Overview of the experiment
more TBA

The morphological complexity ratio is calculated as follow:

$$ morphological \\ complexity \\ ratio = - {mc \\over c}$$

where mc is the compressed file size in bytes after morphological distortion, and c is the compressed file size in bytes before distortion.

The syntactic complexity ratio or the word order rigidity ratio is calculated as follows:

$$ syntactic \\ complexity \\ ratio = - {sc \\over c}$$

where sc is the compressed file size in bytes after syntactic distortion, and c is the compressed file size in bytes before distortion. 

### Datasets
The dataset used in this experiment is based on the the multilingual parallel EDGeS Diachronic Bible Corpus (Bouma, Coussé, Dijkstra & van der Sijs 2020). The analysis is limited to one book from the Old and New Testament respectively, i.e. the Book of Genesis and the Gospel of Matthew. More information about the corpus can be found at:
- Bouma, G., E. Coussé, T. Dijkstra & N. van der Sijs. 2020. The EDGeS diachronic bible corpus. In Proceedings of the 12th international conference on language resources and evaluation, 5232-5239. Paris: ELDA.
- https://spraakbanken.gu.se/en/projects/complex-verb-constructions

3 new datasets were derived from the EDGe corpus:
- EDGe_Zipped_Sizes.xlsx: contains the sizes of all the files in EDGe when they are zipped
- morph_zipped_all.xlsx: contains the sizes of all the files in EDGe when they are morphologically distorted and then zipped over 1000 iterations
- synt_zipped_all.xlsx: contains the sizes of all the files in EDGe when they are syntactically distorted and then zipped over 1000 iterations

### Workflow & code
TBA

## Further references
For more about information theory and linguistic complexity see:
- Ehret, K. 2017. An information-theoretic approach to language complexity: variation in naturalistic corpora. Freiburg: Albert-Ludwig-Universität Freiburg dissertation.
- Juola, P. 2008. Assessing linguistic complexity. In M. Miestamo, K. Sinnemäki & F. Karlsson (eds.), Language complexity: typology, contact, change, 89-108. Amsterdam: John Benjamins.
- Kolmogorov, A. Ni. 1968. Three approaches to the quantitative definition of information. International Journal of Computer Mathematics 2(1-4). 157-168. doi:10.1080/00207166808803030.
