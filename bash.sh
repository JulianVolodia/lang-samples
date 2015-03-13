#!/usr/bin/env bash
set -x
set -e

# Defensive bash programming: http://www.kfirlavi.com/blog/2012/11/14/defensive-bash-programming/
# Conditional expressions: http://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html

if [ conditional expression ] then
  statement1
  statement2
  .
else
  statement3
  statement4
  .
fi

for run in {1..10}
do
  command
done

# Do something based on exit code:
if [ `which ansible` ]; then
  echo 'Ansible already installed.'
  exit;
fi

# Trap exit to ensure cleanup is run.
scratch=$(mktemp -d -t tmp.XXXXXXXXXX)
function finish {
  rm -rf "$scratch"
}
trap finish EXIT
