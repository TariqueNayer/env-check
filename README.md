# env-check
A python script to help you quickly check and find inconsistencies between your prod.env and local.env files, for your web projects whether its built in django or fastapi  

## download:  
```curl -O https://raw.githubusercontent.com/TariqueNayer/env-check/master/env_check.py```
## use
run the script with two arguments  
- `--env` or `-e` : for your production env file.  
- `--example` or `-x` : for your local env file to use as an example.
```bash
  python env_check.py --env .env --example .env.example
```
Honestly, it really doesn't matter which file you use for which argument. the code compare both files with each other.  
But Its better to use arguments like the one above for the sake of simplicity.  

## output
When everything is in sync:
```
Both environments are in sync...
```
When there are missing variables:
```
Inconsistency found!
.env variable: DEBUG - Is Not Found In .env.example
```
