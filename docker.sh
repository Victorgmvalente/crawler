#!/bin/bash -xe

basedir="$(dirname "$0")"


cmd_stop() {
  docker rm "$USER" -f || true
}

cmd_image() {
  docker build -t crawler .
}


cmd_run() {
  docker run -it --rm --name crawler_cont -v "$PWD/.:/opt" -w "/opt" crawler
}



cmd_exec() {
  docker exec -it "$USER" "$@"
}

cmd_entrypoint() {
  _entrypoint=${1?'command'}
  shift
  cmd_exec "/opt/$USER/environment/entrypoint/$_entrypoint.sh" "$@"
}

_cmd=${1?'command'}
shift
cmd_${_cmd} "$@"
