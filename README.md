# Linguistic complexity projects
Scripts and datasets used and created for measuring linguistic complexity through information theoretic methods. This is part of [my PhD project](https://www.kuleuven.be/onderzoek/portaal/#/projecten/3H220490?lang=en&hl=en). Note that this is still a work in progress with semi frequent updates!

Following Juola (2008) and Ehret (2018) this project relies on Kolmogorov complexity to compare the morphological and syntactic complexity of three West-Germanic languages: Dutch, English and German. Kolmogorov complexity is an information-theoretic notion that tries to define the complexity of a string in relation to its information content. Kolmogorov essentially tried to define randomness: for any random data D of length |D|, there is an algorithm of length |D|+δ that outputs (or describes) it, where δ is that which needs to be added to D to output it. In other words, |D|+δ is the length of the shortest algorithm that describes D. If a shorter algorithm exist, then that means that the data D still contains some regularity and thus it can be compressed further using that regularity. The Kolmogorov complexity K(D) of some random data D can thus be defined as the length of the shortest algorithm that describes D.

Applied to language, Kolmogorov complexity defines the complexity of a text as the length of the shortest possible description of this text. When comparing the complexity of two different objects, one can try to describe the object, while being as concise as possible. The more words are needed to describe the object, the more complex this object is. An object is as complex as its shortest description. The object with the shortest most concise description is less complex, while the object with the longest most concise description is more complex. The complexity of two texts can be compared in the same way, as illustrated in the following example:

- abababab = 4*ab --> less complex
- agvderjip = agvderjip --> more complex

Kolmogorov complexity can be approximated by compression algorithms, such as gzip. Compression algorithms go through a text, store seen strings in a temporary lexicon and classify new strings on the basis of this lexicon. They detect structural surface regularities and achieve compression by summarizing these regularieties. The morphological and syntactic complexity of a text can then be assessed by distorting the morphological and syntactic structure of the text and compressing the text afterwards. The idea is then that a text which can be more easiliy compressed by a compression algorithm is linguistically less complex. 

## Experiment 1: EDGe corpus

### Overview of the experiment
#### General idea
The first experiment calculates the morphological and syntactic complexity of Dutch, English and German over time using information theoretic metrics.

#### Morphological complexity
Morphological distortion is achieved by randomly deleting 10% of all characters in a file. This operation leads to a higher amount of unique strings than before distortion and thus worse compressibility. A text with relatively high morphological complexity exhibits a relatively high amount of unique strings even before distortion. Its compressibility therefore is comparatively less affected by distortion than that of a text with relatively low morphological complexity and a relatively low amount of unique strings. The morphological complexity ratio is calculated as follow:

$$ morphological \\ complexity \\ ratio = - {mc \\over c}$$

where mc is the compressed file size in bytes after morphological distortion, and c is the compressed file size in bytes before distortion.

#### Syntactic complexity
Syntactic distortion is achieved by randomly deleting 10% of all tokens in a file. This operation disrupts the word order rules and leads to a higher amount of unique strings and comparatively worse compressibility than before distortion. Languages with strict word order rules will be more affected because of their high level of structural surface redundancies. In the Kolmogorov sense, these are the syntactically complex languages. Languages with free word order and a therefore low number of redundancies will be less affected. The syntactic complexity ratio or the word order rigidity ratio is calculated as follows:

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
#### Step 1: create a file with all the file sizes of the zipped files in EDGe - EDGe_Zipped_Sizes.xlsx
In order to create EDGe_Zipped_Sizes.xlsx first all the files in the dataset need to be zipped. This is done by running gzip_files.py. The second step is retrieving all the file sizes of the zipped files. This is done by running file_size.py on the newly created zipped files.

#### Step 2: morphological distortion - morph_zipped_all.xlsx
In this step all files are first morphologically distorted and subsequently zipped. Morphological distortion is achieved as described above, by randomly deleting 10% of all characters in the file. For each file this is done 1000 times and each time the size of the file is stored in morph_zipped_all.xlsx. This step requires morphological_distortion_pipeline.py.

#### Step 3: syntactic distortion - synt_zipped_all.xlsx
In this step all files are first syntactically distorted and subsequently zipped. Syntactic distortion is achieved as described above, by randomly deleting 10% of all words in the file. For each file this is done 1000 times and each time the size of the file is stored in synt_zipped_all.xlsx. This step requires syntactic_distortion_pipeline.py.

#### Step 4: statistical analysis in R
The statistical analysis of the created datasets (input = EDGe_Zipped_Sizes.xlsx, morph_zipped_all.xlsx and synt_zipped_all.xlsx) is done by running complexity_analysis.R. The script calculates the morphological and syntactic complexity as described above. The output of this script are graphs in .png format.

### Result
![Syntactic vs morphological complexity ratio](https://user-images.githubusercontent.com/107923146/212687027-2c4eaac4-89a9-45b5-b8bf-000191aa7c16.png)

## Experiment 2: pragmatic complexity EDGe corpus
Coming soon!

## References
For more about information theory and linguistic complexity see:
- Ehret, K. 2017. An information-theoretic approach to language complexity: variation in naturalistic corpora. Freiburg: Albert-Ludwig-Universität Freiburg dissertation.
- Juola, P. 2008. Assessing linguistic complexity. In M. Miestamo, K. Sinnemäki & F. Karlsson (eds.), Language complexity: typology, contact, change, 89-108. Amsterdam: John Benjamins.
- Kolmogorov, A. Ni. 1968. Three approaches to the quantitative definition of information. International Journal of Computer Mathematics 2(1-4). 157-168. doi:10.1080/00207166808803030.

