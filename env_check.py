#!/usr/bin/env python3

# run with : python env_check.py --env (your production env file) --example (your local env file)

import argparse

def parse_env_file(filepath):
	result = {}
	try:
		with open(filepath, "r") as f:
			for line in f:
				line = line.strip()
				# Skip empty lines and comments
				if not line or line.startswith("#"):
					continue
				# Split at the first '=' only
				try:
					key, value = line.split("=", 1)
				except ValueError:
					print(f"Warning: skipping malformed line -> '{line}'")
					continue
				result[key] = value
		return result
	except FileNotFoundError:
		print(f"Error: could not find file '{filepath}'")
		exit(1)


parser = argparse.ArgumentParser(
					prog='env_check',
					description='It checks to find inconsistency with your production environment variables and example/local development environment variables',
					epilog='checkout at https://...github-link...')

parser.add_argument('-e', '--env')
parser.add_argument('-x', '--example')

args = parser.parse_args()

env_vars = parse_env_file(args.env)


example_vars = parse_env_file(args.example)



odd_on_env = []
odd_on_ex =[]

for key in env_vars:
	if not key in example_vars:
		odd_on_env.append(key)

for key in example_vars:
	if not key in env_vars:
		odd_on_ex.append(key)

if odd_on_env:
	print("Inconsistency found!")
	for i in odd_on_env:
		print(args.env, "variable: ",i, " - ", f"Is Not Found In {args.example} \n")

if odd_on_ex:
	print("Inconsistency found!")
	for i in odd_on_ex:
		print(args.example, "  variable: ",i, " - ", f"Is Not Found In {args.env} \n")

if (not odd_on_env) and (not odd_on_ex):
	print("Both environments are in sync...")
