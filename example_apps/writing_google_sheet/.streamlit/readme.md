In this folder, you would have a `secrets.toml` file.

The file needs to be populated following this tutorial:

<https://github.com/streamlit/gsheets-connection/tree/main?tab=readme-ov-file#service-account--crud-example>

Here is the example structure of the `secrets.toml` file for this app, using dummy values.

```
test_secret = "llama"

[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/gsgoignweoP1httjxBFOSmTQGKg-V7Uzpw0gphihonwCeP7YimSQE/edit?usp=sharing"
type = "service_account"
project_id = "streamlit-testing-a-792511"
private_key_id = "ae7221419b753527631f5f0886c2141254152157c1f2f4b"
private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDp39piasbcAy1N\nRAHot6tBACMoAXRN5Lz8hKU7GC6dy9gs49+Ksv+Jc9xrvdksM5Al6bCVQK1qjvL/\n5whtf7XkNWEEb3n8Ol7QCT75F0BLDhGLU9o9AlR0ed7D1cjYWw+3S+l2QqW0xpEP\ne+saa4ZiKRLDO87c4eqeuM9xToO1uL1lgnJQuK0mqRxS5KHQRbHhbiAA18sx6shw\nksDVjXfg2Y+bSggEuKrupilU6ZF7j7/uryReZBp2m4oAecJEx6fLyxGS6O3hA/fY\n3GQGJk9H+xoByTno4aueBp12512515aa3/ET0I5MmVpf1C125215125OYP7L//sd4h\noDbi12412ggEABoTXlr4wsFHDWb+/SOATvTJWiIcv2Xr6fJRq8aB9LidQ\nLYIliT1vi4KH/pXSX53JUxE2O5bLrqhw5AqpzLmOVZ/aRjAgR5RN78EOOQ25nE32\nVbqe3uv5dCywdad4G3XA12521512521569jOU71zC0Scb62O7w8uT17vB5/+Hb63oWmtYT\nXwPv+xEuYoSqTnwxUU753bwQexh5nMdc++++jww4ywPm8Zj0CGEsR8tg2PusDWi/5TlY\n/SPqjq7nj++oQNya9GcSiuKCP2x3Tgm8mM/vr85CJNm1+erZc/biPCA1AoGBAKgj\nwJ6sVRsKDmaQcMnpp2G7QPQoevatxSwmbZF2qUkuvEPy22fuIilxay0pzlbkwoE/\npwgWMIChR2nTKQZytkr3Lkj8esQ5LVnNt0WueqsrFgSonCTo6f37ppsyrrFNhR9m\nwYmaMVxBWF1ZMMKX9ecR93YW125616734379B9kZex1IkZuwtZf7MgqsRAoI12421441P9I\nVhWqHMNXme27/cBgEGLesu4e\n-----END PRIVATE KEY-----\n"
client_email = "my-hsma-testing-account@streamlit-testing-a-792511.iam.gserviceaccount.com"
client_id = "24512112521512514"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/my-hsma-testing-account%40streamlit-testing-a-792511.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```
