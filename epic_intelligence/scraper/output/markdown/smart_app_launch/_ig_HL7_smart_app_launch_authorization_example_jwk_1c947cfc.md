# Example JWS generation for Asymmetric Client Auth - SMART App Launch v2.2.0

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/authorization-example-jwks-and-signatures.html

---

SMART App Launch, published by HL7 International / FHIR Infrastructure. This guide is not an authorized publication; it is the continuous build for version 2.2.0 built by the FHIR (HL7® FHIR® Standard) CI Build. This version is based on the current content of [https://github.com/HL7/smart-app-launch/](https://github.com/HL7/smart-app-launch/) and changes regularly. See the [Directory of published versions](http://hl7.org/fhir/smart-app-launch/history.html)

 
## Example JWS generation for Asymmetric Client Auth

 

 

 - [Python](#python)

 - [Encoded JWT with RS384 Signature](#encoded-jwt-with-rs384-signature)

 - [Encoded JWT with ES384 Signature](#encoded-jwt-with-es384-signature)

### Python

```
# To create a markdown of this notebook, run: jupyter nbconvert --to markdown authorization-example-jwks-and-signatures.ipynb
# !pip3 install python-jose

import json
import jose.jwk
import jose.jwt
import jose.constants

def get_signing_key(filename):
 with open(filename) as private_key_file:
 signing_keyset = json.load(private_key_file)
 signing_key = [k for k in signing_keyset["keys"] if "sign" in k["key_ops"]][0]
 return signing_key
 
jwt_claims = {
 "iss": "https://bili-monitor.example.com",
 "sub": "https://bili-monitor.example.com",
 "aud": "https://authorize.smarthealthit.org/token",
 "exp": 1422568860,
 "jti": "random-non-reusable-jwt-id-123"
}

```

```
print("# Encoded JWT with RS384 Signature")
rsa_signing_jwk = get_signing_key("RS384.private.json")
jose.jwt.encode(
 jwt_claims,
 rsa_signing_jwk,
 algorithm='RS384',
 headers={"kid": rsa_signing_jwk["kid"]})

```

### Encoded JWT with RS384 Signature

```
eyJhbGciOiJSUzM4NCIsImtpZCI6ImVlZTlmMTdhM2I1OThmZDg2NDE3YTk4MGI1OTFmYmU2IiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2JpbGktbW9uaXRvci5leGFtcGxlLmNvbSIsInN1YiI6Imh0dHBzOi8vYmlsaS1tb25pdG9yLmV4YW1wbGUuY29tIiwiYXVkIjoiaHR0cHM6Ly9hdXRob3JpemUuc21hcnRoZWFsdGhpdC5vcmcvdG9rZW4iLCJleHAiOjE0MjI1Njg4NjAsImp0aSI6InJhbmRvbS1ub24tcmV1c2FibGUtand0LWlkLTEyMyJ9.D5kAqNJwaftCqsRdVVQDq6dMBxuGFOF5svQJuXbcYp-oEyg5qOwK9ZE5cGLTHxqwfpUPNzRKgVdIGuhawAA-8g0s1nKQae8CuKs33hhKh4J34xSEwW3MYs1gwI4GHTtR_g3kYSX6QCi14Ed3GIAvYFgqRqt-gD7sewMUXL4SB8I8cXcDbCqVizm7uPVhjw6QaeKZygJJ_AVLhM4Xs9LTy4HAhdCHpN0FrNmCerUIYJvHDpcod7A0jDmxdoeW1KIBYlhdhQNwjtsTvT1ce4qacN_3KIv_fIzCKLIgDv9eWxkjAtxOmIm8aW5gX9xX7X0nbd0QglIyiic_bZVNNEh0kg

```

```
print("# Encoded JWT with ES384 Signature")
ec_signing_jwk = get_signing_key("ES384.private.json")
jose.jwt.encode(
 jwt_claims,
 ec_signing_jwk,
 algorithm='ES384',
 headers={"kid": ec_signing_jwk["kid"]})

```

### Encoded JWT with ES384 Signature

```
eyJhbGciOiJFUzM4NCIsImtpZCI6ImNkNTIwMjExZTU2NjFkYmJhMjI1NmY2N2Y2ZDUzZjk3IiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2JpbGktbW9uaXRvci5leGFtcGxlLmNvbSIsInN1YiI6Imh0dHBzOi8vYmlsaS1tb25pdG9yLmV4YW1wbGUuY29tIiwiYXVkIjoiaHR0cHM6Ly9hdXRob3JpemUuc21hcnRoZWFsdGhpdC5vcmcvdG9rZW4iLCJleHAiOjE0MjI1Njg4NjAsImp0aSI6InJhbmRvbS1ub24tcmV1c2FibGUtand0LWlkLTEyMyJ9.ddl5N8dt5PYI_7syKg_dm1wj1LR3dYVztFlTODs6pU1vKH1Zv3d9NctbnAsZ4aZ1K7HE83_fA_hIAL0JsU1GoB7roLmrpj8zfygG9Q1ZBAmKNoR60pyONPZsGTihoR29

```