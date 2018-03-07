#!/bin/bash
export APP_ID="the_room"
export MASTER_KEY="oh_hi_Johnny"
export REST_API_KEY="did_not_know_it_was_you"
export CLIENT_KEY="you_are_my_favorite_customer"
export DEV_BUNDLE_ID="man_bun"
export PARSE_DASHBOARD_USER_ID="herve"
export PARSE_DASHBOARD_USER_PASSWORD="glass_door"
export PARSE_DASHBOARD_ALLOW_INSECURE_HTTP=1
export ALLOW_INSECURE_HTTP=1
export DEV_PASSPHRASE=''
export TOKEN_ID='tameretafaitdesgoffres'
export INSTALLATION_ID='sunnyvale'
export PARSE_DASHBOARD_CONFIG=$(cat <<EOF
{
  "apps": [
    {
      "appId": "the_room",
      "serverURL": "http://localhost:1337/parse",
      "masterKey": "oh_hi_Johnny",
      "appName": ""
    }
  ],
  "users": [
    {
      "user": "herve",
      "pass": "glass_door"
    }
  ]
}
EOF
)
