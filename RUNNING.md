## Database

The database the data used in this study can be found in this 
[zenodo repository](https://zenodo.org/record/4002869#.YLk5g5NKh7g). This is a mongo repository. 
Follow [INSTALL.md](INSTALL.md) to setup mongoDB. 
This repository contains collections for source code snippets, their tokens, their ASTs and IO relations as well.
Proceed directly to Search(#search)  

### Build
If a custom repository is used, first crawl the repository and generate mongo code snippets. 
Examples for this can be found in `code/src/main/python/mos/crawl/atcoder_crawl.py` or `code/src/main/python/mos/bigclonebench/crawler.py`

## Build Context Tokens
Contexts are already prebuilt in the database. That said, this can be updated using custom distance metrics or 
reexecuted by altering and running `code/src/main/python/mos/search/token_syntactic.py`.  
Ensure that elastic search is running. Check [INSTALL.md](INSTALL.md) on setting it up. 

## Build AST
AST distances are cached for a better search experience.  These distances are already precomputed in the database. 
That said, these distances can be altered and rexecuted by running `code/src/main/python/mos/search/cacher/ast_cache.py`.
 

## Build Input Output Similarity
IO in COSAL is executed using SLACC. We use SLACC as is and this can be setup using the steps from [SLACC repository](https://github.com/DynamicCodeSearch/SLACC)

## Search
COSAL uses non dominated sort to rank search results based on token, AST and IO similarity. This can be configured and run from the 
`code/src/main/python/mos/search/multi_objective.py`. Please look at the method `_test` that demonstrates this 