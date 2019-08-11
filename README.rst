Docker Geekbench 4 for CTP
==========================

Run Geekbench 4 and upload to CTP

::
  docker run \
      --mount type=bind,source="/Users/zulu/cb_client.json",target=/etc/cb_client.json
      -e GB4_EMAIL='you@email' -e GB4_KEY=YOUR-KEY
      cloudspectator/cb-geekbench4
