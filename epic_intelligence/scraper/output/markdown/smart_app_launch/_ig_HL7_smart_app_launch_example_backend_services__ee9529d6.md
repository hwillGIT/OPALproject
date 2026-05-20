# Example Backend Services Flow - SMART App Launch v2.2.0

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/example-backend-services.html

---

SMART App Launch, published by HL7 International / FHIR Infrastructure. This guide is not an authorized publication; it is the continuous build for version 2.2.0 built by the FHIR (HL7® FHIR® Standard) CI Build. This version is based on the current content of [https://github.com/HL7/smart-app-launch/](https://github.com/HL7/smart-app-launch/) and changes regularly. See the [Directory of published versions](http://hl7.org/fhir/smart-app-launch/history.html)

 
## Example Backend Services Flow

 

 

 - [Retrieve .well-known/smart-configuration](#retrieve-well-knownsmart-configuration)

 - [Retrieve access token](#retrieve-access-token)

 - [Access FHIR API](#access-fhir-api)

### Retrieve .well-known/smart-configuration

```
curl -s 'https://smart.argo.run/v/r4/sim/eyJtIjoiMSIsImsiOiIxIiwiaSI6IjEiLCJqIjoiMSIsImIiOiI4N2EzMzlkMC04Y2FlLTQxOGUtODljNy04NjUxZTZhYWIzYzYifQ/fhir/.well-known/smart-configuration' \
 -H 'accept: application/json'

{
 "token_endpoint": "https://smart.argo.run/v/r4/sim/eyJtIjoiMSIsImsiOiIxIiwiaSI6IjEiLCJqIjoiMSIsImIiOiI4N2EzMzlkMC04Y2FlLTQxOGUtODljNy04NjUxZTZhYWIzYzYifQ/auth/token",
 "grant_types_supported": [
 "client_credentials"
 ],
 "token_endpoint_auth_methods_supported": [
 "private_key_jwt",
 ],
 "token_endpoint_auth_signing_alg_values_supported": [
 "RS384",
 "ES384"
 ],
 "scopes_supported": [
 "system/*.rs"
 ],
 "capabilities": [
 "client-confidential-asymmetric",
 "permission-v2",
 ]
}

```

### Retrieve access token

Generate a client authentication assertion and prepare arguments for POST to token API (newlines added for clarity):

```
grant_type=client_credentials&
scope=system%2F*.rs&
client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&
client_assertion=eyJ0eXAiOiJKV1QiLCJraWQiOiJhZmIyN2MyODRmMmQ5Mzk1OWMxOGZhMDMyMGUzMjA2MCIsImFsZyI6IkVTMzg0In0.eyJpc3MiOiJkZW1vX2FwcF93aGF0ZXZlciIsInN1YiI6ImRlbW9fYXBwX3doYXRldmVyIiwiYXVkIjoiaHR0cHM6Ly9zbWFydC5hcmdvLnJ1bi92L3I0L3NpbS9leUp0SWpvaU1TSXNJbXNpT2lJeElpd2lhU0k2SWpFaUxDSnFJam9pTVNJc0ltSWlPaUk0TjJFek16bGtNQzA0WTJGbExUUXhPR1V0T0Rsak55MDROalV4WlRaaFlXSXpZellpZlEvYXV0aC90b2tlbiIsImp0aSI6ImQ4MDJiZDcyY2ZlYTA2MzVhM2EyN2IwODE3YjgxZTQxZTBmNzQzMzE4MTg4OTM4YjAxMmMyMDM2NmJkZmU4YTEiLCJleHAiOjE2MzM1MzIxMzR9.eHUtXmppOLIMAfBM4mFpcgJ90bDNYWQpkm7--yRS2LY5HoXwr3FpqHMTrjhK60r5kgYGFg6v9IQaUFKFpn1N2Eyty62JWxvGXRlgEDbdX9wAAr8TeWnsAT_2orfpn6wz

```

Issue POST to the token endpoint:

```
curl 'https://smart.argo.run/v/r4/sim/eyJtIjoiMSIsImsiOiIxIiwiaSI6IjEiLCJqIjoiMSIsImIiOiI4N2EzMzlkMC04Y2FlLTQxOGUtODljNy04NjUxZTZhYWIzYzYifQ/auth/token' \
 -H 'accept: application/json' \
 -H 'content-type: application/x-www-form-urlencoded' \
 --data-raw 'grant_type=client_credentials&scope=system%2F*.rs&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJ0eXAiOiJKV1QiLCJraWQiOiJhZmIyN2MyODRmMmQ5Mzk1OWMxOGZhMDMyMGUzMjA2MCIsImFsZyI6IkVTMzg0In0.eyJpc3MiOiJkZW1vX2FwcF93aGF0ZXZlciIsInN1YiI6ImRlbW9fYXBwX3doYXRldmVyIiwiYXVkIjoiaHR0cHM6Ly9zbWFydC5hcmdvLnJ1bi92L3I0L3NpbS9leUp0SWpvaU1TSXNJbXNpT2lJeElpd2lhU0k2SWpFaUxDSnFJam9pTVNJc0ltSWlPaUk0TjJFek16bGtNQzA0WTJGbExUUXhPR1V0T0Rsak55MDROalV4WlRaaFlXSXpZellpZlEvYXV0aC90b2tlbiIsImp0aSI6ImQ4MDJiZDcyY2ZlYTA2MzVhM2EyN2IwODE3YjgxZTQxZTBmNzQzMzE4MTg4OTM4YjAxMmMyMDM2NmJkZmU4YTEiLCJleHAiOjE2MzM1MzIxMzR9.eHUtXmppOLIMAfBM4mFpcgJ90bDNYWQpkm7--yRS2LY5HoXwr3FpqHMTrjhK60r5kgYGFg6v9IQaUFKFpn1N2Eyty62JWxvGXRlgEDbdX9wAAr8TeWnsAT_2orfpn6wz'

{
 "token_type": "Bearer",
 "scope": "system/*.rs",
 "expires_in": 3600,
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuZWVkX3BhdGllbnRfYmFubmVyIjp0cnVlLCJzbWFydF9zdHlsZV91cmwiOiJodHRwczovL3NtYXJ0LmFyZ28ucnVuLy9zbWFydC1zdHlsZS5qc29uIiwicGF0aWVudCI6Ijg3YTMzOWQwLThjYWUtNDE4ZS04OWM3LTg2NTFlNmFhYjNjNiIsInRva2VuX3R5cGUiOiJiZWFyZXIiLCJzY29wZSI6ImxhdW5jaC9wYXRpZW50IHBhdGllbnQvT2JzZXJ2YXRpb24ucnMgcGF0aWVudC9QYXRpZW50LnJzIiwiY2xpZW50X2lkIjoiZGVtb19hcHBfd2hhdGV2ZXIiLCJleHBpcmVzX2luIjozNjAwLCJpYXQiOjE2MzM1MzIwMTQsImV4cCI6MTYzMzUzNTYxNH0.PzNw23IZGtBfgpBtbIczthV2hGwanG_eyvthVS8mrG4"
}

```

### Access FHIR API

```
curl 'https://smart.argo.run/v/r4/sim/eyJtIjoiMSIsImsiOiIxIiwiaSI6IjEiLCJqIjoiMSIsImIiOiI4N2EzMzlkMC04Y2FlLTQxOGUtODljNy04NjUxZTZhYWIzYzYifQ/fhir/Observation?code=4548-4&_sort%3Adesc=date&_count=10' \
 -H 'accept: application/json' \
 -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuZWVkX3BhdGllbnRfYmFubmVyIjp0cnVlLCJzbWFydF9zdHlsZV91cmwiOiJodHRwczovL3NtYXJ0LmFyZ28ucnVuLy9zbWFydC1zdHlsZS5qc29uIiwicGF0aWVudCI6Ijg3YTMzOWQwLThjYWUtNDE4ZS04OWM3LTg2NTFlNmFhYjNjNiIsInRva2VuX3R5cGUiOiJiZWFyZXIiLCJzY29wZSI6ImxhdW5jaC9wYXRpZW50IHBhdGllbnQvT2JzZXJ2YXRpb24ucnMgcGF0aWVudC9QYXRpZW50LnJzIiwiY2xpZW50X2lkIjoiZGVtb19hcHBfd2hhdGV2ZXIiLCJleHBpcmVzX2luIjozNjAwLCJpYXQiOjE2MzM1MzIwMTQsImV4cCI6MTYzMzUzNTYxNH0.PzNw23IZGtBfgpBtbIczthV2hGwanG_eyvthVS8mrG4'

{
 "resourceType": "Bundle",
 "id": "9e3ed23b-b62e-4a3d-9ac8-9b66a67f700d",
 "meta": {
 "lastUpdated": "2021-10-06T10:52:52.847-04:00"
 },
 "type": "searchset",
 "total": 1100,
<SNIPPED for brevity>

```