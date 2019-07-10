FILES = ["x", "y"]

rule all:
    input:
      expand("{something}_count.csv", something=FILES)

rule make_counts_csv:
  input: "{something}_words.txt"
  output: "{something}_count.csv"
  shell: " python script.py {input} {output} "
