# Eve Markets

Market tool for Eve Online

## Development

### ESI Application

You must first make an application at https://developers.eveonline.com/

Setting | Value
---|---
Name | Markets
Description | Market management
Connection Type | Authentication & API access
Permissions | Copy scopes from `envs/dev.env`
Callback URL | `http://localhost:8000/sso/callback/`

### Git

```shell
cd ~/Dev
git clone https://github.com/harrelchris/eve-markets
cd eve-markets
bash scripts/init.sh
```

### Env

Add your CLIENT_ID, SECRET_KEY from your Eve Application to the `.env` file

### Aliases

```shell
nano ~/.bashrc

alias init="bash scripts/init.sh"
alias lint="bash scripts/lint.sh"
alias run="bash scripts/run.sh"
alias test="bash scripts/test.sh"

source ~/.bashrc
```
