# Google Scholar Grabber

![Python3](https://img.shields.io/badge/Python3-3e74a2?logo=python&logoColor=fff&style=flat) ![GitHub license](https://img.shields.io/github/license/ThreeCatsLoveFish/GoogleScholar) 

**Google Scholar Grabber** is a Python module that implements a querier and parser for Google Scholar's output. Its classes can be used independently, but it can also be invoked as a command-line tool.

The script is originally written by christian@icir.org and link is [here](https://github.com/ckreibich/scholar.py). I made great change on it to support new features!


## Usage

1. Initialize environment:
```bash
git clone https://github.com/ThreeCatsLoveFish/GoogleScholar.git
cd GoogleScholar/
pip install bs4 requests tqdm
```
2. Add your cookies and proxies in `data/config.json`.
3. Follow the given [examples](#Examples).


## Features

* Support new version of citation.
* Support retrieving all articles written by specific author.
* Extracts publication title, most relevant web link, PDF link, number of citations, number of online versions, link to Google Scholar's article cluster for the work, Google Scholar's cluster of all works referencing the publication, and excerpt of content.
* Extracts total number of hits as reported by Scholar.
* Supports the full range of advanced query options provided by Google Scholar, such as title-only search, publication date timeframes, and inclusion/exclusion of patents and citations.
* Supports article cluster IDs, i.e., information relating to the variants of an article already identified by Google Scholar
* Supports retrieval of citation details in standard external formats as provided by Google Scholar, including BibTeX and EndNote.
* Command-line tool prints entries in CSV format, simple plain text, or in the citation export format.


## Examples

Try `scholar.py --help` for all available options. A few examples:

Retrieve 100 articles written by Einstein on quantum theory:

    $ scholar.py -c 100 --author "albert einstein" --phrase "quantum theory" --config-file data/config.json
             Title On the quantum theory of radiation
               URL http://icole.mut-es.ac.ir/downloads/Sci_Sec/W1/Einstein%201917.pdf
              Year 1917
         Citations 184
          Versions 3
        Cluster ID 17749203648027613321
          PDF link http://icole.mut-es.ac.ir/downloads/Sci_Sec/W1/Einstein%201917.pdf
    Citations list http://scholar.google.com/scholar?cites=17749203648027613321&as_sdt=2005&sciodt=0,5&hl=en
     Versions list http://scholar.google.com/scholar?cluster=17749203648027613321&hl=en&as_sdt=0,5
           Excerpt The formal similarity between the chromatic distribution curve for thermal radiation [...]
    ......


Note the cluster ID in the above. Using this ID, you can directly access the cluster of articles Google Scholar has already determined to be variants of the same paper. So, let's see the versions:

    $ scholar.py -C 17749203648027613321 --config-file data/config.json
             Title On the quantum theory of radiation
               URL http://icole.mut-es.ac.ir/downloads/Sci_Sec/W1/Einstein%201917.pdf
         Citations 184
          Versions 0
        Cluster ID 17749203648027613321
          PDF link http://icole.mut-es.ac.ir/downloads/Sci_Sec/W1/Einstein%201917.pdf
    Citations list http://scholar.google.com/scholar?cites=17749203648027613321&as_sdt=2005&sciodt=0,5&hl=en
           Excerpt The formal similarity between the chromatic distribution curve for thermal radiation [...]

             Title ON THE QUANTUM THEORY OF RADIATION
               URL http://www.informationphilosopher.com/solutions/scientists/einstein/1917_Radiation.pdf
         Citations 0
          Versions 0
          PDF link http://www.informationphilosopher.com/solutions/scientists/einstein/1917_Radiation.pdf
           Excerpt The formal similarity between the chromatic distribution curve for thermal radiation [...]
    
             Title The Quantum Theory of Radiation
               URL http://web.ihep.su/dbserv/compas/src/einstein17/eng.pdf
         Citations 0
          Versions 0
          PDF link http://web.ihep.su/dbserv/compas/src/einstein17/eng.pdf
           Excerpt 1 on the assumption that there are discrete elements of energy, from which quantum [...]


Let's retrieve a BibTeX entry for that quantum theory paper. The best BibTeX often seems to be the one linked from search results, not those in the article cluster, so let's do a search again:

    $ scholar.py -c 1 --author "albert einstein" --phrase "quantum theory" --citation bt --config-file data/config.json
    @article{einstein1917quantum,
      title={On the quantum theory of radiation},
      author={Einstein, Albert},
      journal={Phys. Z},
      volume={18},
      pages={121--128},
      year={1917}
    }

Report the total number of articles Google Scholar has for Einstein:

    $ scholar.py --txt-globals --author "albert einstein" --config-file data/config.json | grep '\[G\]' | grep Results
    [G]    Results 4190


Find all citation of articles Google Scholar has for Einstein's paper "On the quantum theory of radiation":

    $ scholar.py --citations-only -c 150 -a "albert einstein" --phrase "On the quantum theory of radiation" --citation bt --config-file data/config.json -o test.txt

License
-------

Google Scholar Grabber is using the standard [BSD license](http://opensource.org/licenses/BSD-2-Clause).