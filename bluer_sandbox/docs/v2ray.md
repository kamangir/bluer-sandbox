# v2ray

- [@v2ray](./aliases/v2ray.md)

```bash
@v2ray start import,vmess \
	"$BLUER_SANDBOX_V2RAY_VLMESS"
```

in another terminal.

```bash
 > @v2ray test
⚙️ curl -I https://google.com --proxy http://127.0.0.1:8080
HTTP/1.1 200 Connection established

HTTP/2 301
location: https://www.google.com/
content-type: text/html; charset=UTF-8
content-security-policy-report-only: object-src 'none';base-uri 'self';script-src 'nonce-y8P1C-SVIpNYsMYfkY6DPA' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
date: Sun, 09 Nov 2025 13:59:37 GMT
expires: Tue, 09 Dec 2025 13:59:37 GMT
cache-control: public, max-age=2592000
server: gws
content-length: 220
x-xss-protection: 0
x-frame-options: SAMEORIGIN
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
```

✅
