#!/bin/bash
cat <<EOT >> hosts
[$1]
$2
EOT

cat <<EOT >> /etc/hosts
$2  $1  flaskwpage.me
EOT