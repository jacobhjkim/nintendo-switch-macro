import json

from macro.ssg import SSGMacro

if __name__ == "__main__":
    with open('config.json') as config:
        urls = json.loads(config.read())

    ssg_macro = SSGMacro(website_name='SSG',
                         login_url=urls['SSG']['login_url'],
                         item_url=urls['SSG']['item_url'],
                         login_id=urls['SSG']['login_id'],
                         login_pw=urls['SSG']['login_pw'])
    ssg_macro.run()
