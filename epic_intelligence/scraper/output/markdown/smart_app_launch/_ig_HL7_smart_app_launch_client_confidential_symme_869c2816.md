# Client Authentication: Symmetric (shared secret) - SMART App Launch v2.2.0

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/client-confidential-symmetric.html

---

SMART App Launch, published by HL7 International / FHIR Infrastructure. This guide is not an authorized publication; it is the continuous build for version 2.2.0 built by the FHIR (HL7® FHIR® Standard) CI Build. This version is based on the current content of [https://github.com/HL7/smart-app-launch/](https://github.com/HL7/smart-app-launch/) and changes regularly. See the [Directory of published versions](http://hl7.org/fhir/smart-app-launch/history.html)

 
## Client Authentication: Symmetric (shared secret)

 

 

 - [Profile Audience and Scope](#profile-audience-and-scope)

 - [Authentication using a `client_secret`](#authentication-using-a-client_secret)

### Profile Audience and Scope

This profile describes SMART’s
[`client-confidential-symmetric`](conformance.html) authentication mechanism. It is intended
for [SMART App Launch](app-launch.html) clients that can maintain a secret but cannot manage asymmetric keypairs. For clients that can manage asymmetric keypairs, [Asymmetric Authentication](client-confidential-asymmetric.html) is preferred. This profile is not intended for [SMART Backend Services](backend-services.html) clients.

### Authentication using a `client_secret`

If a client has registered for Client Password authentication (i.e.,
it possesses a `client_secret` that is also known to the EHR), the client
authenticates by supplying an `Authorization` header with HTTP Basic authentication,
where the username is the app’s `client_id` and the password is the app’s
`client_secret`.

#### Example

If the `client_id` is “my-app” and the `client_secret` is “my-app-secret-123”,
then the header uses the value B64Encode(“my-app:my-app-secret-123”), which
converts to `bXktYXBwOm15LWFwcC1zZWNyZXQtMTIz`. This gives the app the Authorization
token for “Basic Auth”.

GET header:

```
Authorization: Basic bXktYXBwOm15LWFwcC1zZWNyZXQtMTIz

```