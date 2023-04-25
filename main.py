#!/usr/bin/python3
# coding: UTF-8

"""Launches the magic.  Not much happens here."""


import configparser
import sys
import json
from pprint import pprint

from mastodon import Mastodon
from requests import Session

if __name__ == '__main__':
    _CONFIG = configparser.ConfigParser()
    _CONFIG.read('config.ini')

    # *CURRENTLY* this isn't useful, lets get the helpers sorted and come back to it
    if "oauth" not in _CONFIG['mastodon'] or _CONFIG['mastodon']['oauth'] == "":
        if "client_id" not in _CONFIG['mastodon']:
            Mastodon.create_app(
                'thegx-banner',
                scopes=['read', 'write', 'admin:read', 'admin:write' ],
                api_base_url=_CONFIG['base']['site'],
                to_file='pytooter_clientcred.secret'
            )
            print("Please add client_id to the _CONFIG.ini")
            sys.exit()
        else:
            api = Mastodon(
                _CONFIG['mastodon']['client_id'],
                _CONFIG['mastodon']['client_secret'],
                api_base_url=_CONFIG['base']['site']
                )
            print(
                    api.log_in(
                        _CONFIG['base']['bot_username'],
                        _CONFIG['base']['bot_password'],
                        scopes=['read', 'write', 'admin:read', 'admin:write' ]
                        )
                    )
            sys.exit()
    
    if 'ignore_cert' in _CONFIG['mastodon']:
        req_session = Session()
        if _CONFIG['mastodon']['ignore_cert'] == "True":
            req_session.verify = False
        else:
            req_session.verify = True
    
    else:
        req_session = None
    
    mastodon = Mastodon(
        _CONFIG['mastodon']['client_id'],
        _CONFIG['mastodon']['client_secret'],
        _CONFIG['mastodon']['oauth'],
        api_base_url=_CONFIG['base']['site'],
        mastodon_version="3.5.3",
        session=req_session
    )

    naughty_users = mastodon.admin_accounts_v2(
            origin="remote",
            status="active",
            username="thegx"
            )

    pprint( naughty_users )

    for user in naughty_users:
        print( "id: {}".format( user['id'] ) )
        result = mastodon.admin_account_moderate(
                user['id'],
                action="suspend",
                text="Spambot relating to thegx"
                )
        print( "   Result: {}".format( result ) )
