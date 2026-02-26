## Epic Developer Guide & Playbooks: Clinical Data Read Access and Patient Context — Detailed Summary

Here is a comprehensive synthesis of everything found across the Epic Developer Guide (open.epic.com/DeveloperResources), the App Developer Guidelines, and the full set of Data Sharing Playbooks, specifically covering **clinical data read access** and **patient context**.

***

## 1. App Developer Guidelines — Patient Context Requirements

The [App Developer Guidelines](https://fhir.epic.com/Documentation?docId=developerguidelines) establishes the foundational rules for how apps must handle patient context and clinical data access: [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)

### Patient Identity & Context
- **Patient Identity Rule**: If an app is launched within an Epic patient workspace for patient-specific workflows, the app must maintain the correct patient in context throughout the session. It must not allow a user to accidentally act on the wrong patient's record. [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)
- **Patient Search**: When an app allows searching for a patient record, it must collect enough information to uniquely identify the correct patient. Epic strongly recommends requiring all of the following **3+1 demographic criteria**: First and Last Name, Legal Sex, Date of Birth, and at least one additional identifier (MRN, address, phone, or email). This is tied directly to 45 CFR 170.315(g)(7) (Application Access — Patient Selection). [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)
- **Accurate Display**: If the app displays patient data (medications, observations, conditions), it must do so accurately and in a manner that allows the user to confirm they're viewing the correct patient record. [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)
- **Data Separation**: The app must present data so the user can visually confirm they are accessing the correct patient record. [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)
- **Updated Data**: The app must show when data was last updated so the user knows if data may be stale. [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)

### Clinical Data Access Governance
- **Minimize PHI**: The app must not request or store more Protected Health Information than is strictly needed. Apps must be scoped for only the APIs required for the integration. [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)
- **Appropriate Methods**: The app uses only Epic-approved, industry-standard methods to read data. Software that reads data from a user interface (e.g., robotic process automation) is explicitly prohibited. [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)
- **Security for Clinical Data in Transit**: All clinical data must be secured with TLS 1.2+, and apps must use OAuth 2.0 for authentication/authorization. [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)
- **Data Integrity**: The app must not corrupt or cause inconsistencies in users' or Epic Community Members' data. [fhir.epic](https://fhir.epic.com/Documentation?docId=developerguidelines)

***

## 2. The Core Patient Context Mechanism: OAuth 2.0 / SMART on FHIR

The [OAuth 2.0 Specification](https://fhir.epic.com/Documentation?docId=oauth2) and the Developer Guide define how patient context is established and passed to apps. [fhir.epic](https://fhir.epic.com/Documentation?docId=oauth2)

### Three App Launch Modes
1. **EHR Launch (SMART on FHIR)** — The primary mechanism for patient context. Epic's Hyperspace calls the app's launch URL, passing a `launch` token and the FHIR server's ISS parameter. The app exchanges this for an authorization code, then an access token. The token response includes:
   - `patient` — the FHIR ID for the patient currently in context
   - `epic.dstu2.patient` — DSTU2 FHIR patient ID
   - `encounter` — FHIR ID for the current encounter
   - `location` — FHIR ID for the encounter department
   - `appointment` — FHIR ID for the patient's appointment
   - `loginDepartment` — FHIR ID of the user's login department
   These context tokens are only provided when a patient/encounter is in context at launch time. [fhir.epic](https://fhir.epic.com/Documentation?docId=oauth2)

2. **Standalone Launch** — The app initiates outside of an EHR session. In patient-facing workflows, the `patient` FHIR ID is returned in the token response. **In provider-facing standalone launches, the patient FHIR ID is NOT returned** — the app must determine the patient independently. [fhir.epic](https://fhir.epic.com/Documentation?docId=oauth2)

3. **Backend Services (Backend OAuth 2.0)** — No direct user interaction. The app uses a JWT signed with a private key to obtain a `client_credentials` access token. Used for system-to-system data exchange, scheduled batch pulls, or population-level access. No patient-specific context is passed at launch; the app must construct queries using known patient identifiers. [fhir.epic](https://fhir.epic.com/Documentation?docId=oauth2)

### Scopes and SMART v1/v2
SMART scopes control which FHIR resources the app can read. As of August 2024, both SMART v1 (`patient/Observation.read`) and SMART v2 (`patient/Observation.r`) scope formats are supported. The scope granted in the token response defines the exact clinical data the app is permitted to access. [fhir.epic](https://fhir.epic.com/Documentation?docId=oauth2)

### OpenID Connect (Patient/Provider Identity)
The `openid` scope returns an `id_token` JWT with a `sub` claim (the FHIR ID of the authenticated user). The `fhirUser` scope (R4+) provides an absolute FHIR resource reference:
- Provider workflow → Practitioner resource
- MyChart self-access → Patient resource
- MyChart proxy access → RelatedPerson resource [fhir.epic](https://fhir.epic.com/Documentation?docId=oauth2)

***

## 3. Patient-Facing / Consumer Health Apps Playbook

The [Patient-Facing Consumer Health Apps Playbook](https://fhir.epic.com/Documentation?docId=patient_facing_apps) defines how third-party apps access clinical data on behalf of patients. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_facing_apps)

### Core Model
- Patients use **OAuth 2.0 via MyChart credentials** to authorize apps to pull their FHIR data. Apps are redirected to the healthcare provider's MyChart page for authentication. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_facing_apps)
- Patients can revoke access at any time. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_facing_apps)
- Each app must pre-register and receive a **client ID**. The app can only pull data through FHIR APIs that are (a) registered to its client ID and (b) explicitly authorized by the patient. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_facing_apps)
- App developers must complete a **Data Use Questionnaire** as part of registration — this is what patients see during the authorization prompt. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_facing_apps)

### Clinical Data Read Access in Patient Context (FHIR API Behavior)
The [Patient-Facing Apps Using FHIR tutorial](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps) details critical nuances in how FHIR APIs respond in patient-facing contexts: [fhir.epic](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps)
- APIs **only return results relevant to the authenticated patient** (e.g., Observation/Labs won't return another patient's results) [fhir.epic](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps)
- APIs **may not return patient-entered data** that hasn't been reviewed and reconciled by a clinician [fhir.epic](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps)
- APIs return **patient-friendly medication names** (e.g., "pseudoephedrine" vs. "PSEUDOPHEDRINE HCL 30 MG PO TABS") [fhir.epic](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps)
- APIs may be configured to **exclude specific lab results** to comply with state and local regulations [fhir.epic](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps)

### USCDI Clinical Data APIs (Auto-Distribution Eligible)
Patient-facing apps using only USCDI v1 or v3 APIs qualify for automatic client ID distribution to all Epic organizations. The complete list of qualifying clinical data READ APIs includes: [fhir.epic](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps)
- **AllergyIntolerance** (Read/Search — DSTU2, STU3, R4)
- **Condition** (Problems, Health Concerns, Encounter Diagnoses, Care Plan Problems)
- **DiagnosticReport** (Lab Results)
- **DocumentReference** (Clinical Notes, Generated CCDA, Labs)
- **Encounter** (Patient Chart)
- **Immunization**
- **Medication / MedicationRequest / MedicationOrder / MedicationDispense / MedicationStatement**
- **Observation** (Labs, Vitals, Social History, Assessments, SDOH, SmartData Elements, Study Findings)
- **CarePlan / CareTeam / Goal**
- **Procedure** (Orders, Surgeries, SDOH Interventions)
- **Binary** (Clinical Notes, Generated CCDA, Labs, Studies)
- **Coverage / Device / Specimen**
- **Patient / Practitioner / PractitionerRole / Organization / Location**
- **ServiceRequest** (Order Procedure, Community Resource)
- **RelatedPerson** (Proxy, Friends and Family)
- **Provenance**

USCDI v3 additionally includes outside record variants of nearly all of the above (e.g., `Condition.Read (Outside Record Problems)`), enabling cross-organization clinical data read access. [fhir.epic](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps)

### Distribution Pathways
1. **TEFCA IAS (Individual Access Services)** — Patients use apps to retrieve records from 200+ Epic organizations via the national TEFCA framework. Benefits: record location capabilities, efficient querying. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_facing_apps)
2. **Epic on FHIR Automatic Download** — Apps meeting USCDI/CMS criteria are auto-distributed to all Epic organizations that have auto-download enabled, requiring no manual setup. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_facing_apps)
3. **Customer-Requested Distribution** — For apps using APIs outside the auto-distribution scope, or where coordination with a health system is needed. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_facing_apps)

***

## 4. Clinical Decision Support (CDS Hooks) Playbook

The [CDS Playbook](https://fhir.epic.com/Documentation?docId=cds_playbook) defines how apps access patient clinical data in real-time during provider workflows. [fhir.epic](https://fhir.epic.com/Documentation?docId=cds_playbook)

### Patient Context in CDS Hooks
- Epic's CDS Hooks implementation sends a call to the app's endpoint with **FHIR Prefetch data** when a workflow hook is triggered (e.g., when ordering a medication or opening a patient chart). This prefetch contains patient clinical data relevant to the hook context. [fhir.epic](https://fhir.epic.com/Documentation?docId=cds_playbook)
- The CDS service can then make **additional FHIR API calls** as needed to retrieve more clinical data — such as conditions, labs, medications — scoped to the current patient context. [fhir.epic](https://fhir.epic.com/Documentation?docId=cds_playbook)
- The hook defines the exact workflow point (e.g., `patient-view`, `order-select`, `medication-prescribe`) and the criteria for when the hook fires. Customer analysts configure this during implementation. [fhir.epic](https://fhir.epic.com/Documentation?docId=cds_playbook)
- Responses can include textual cards, suggested discrete actions, or a link to a SMART app — all embedded directly in the provider's workflow. [fhir.epic](https://fhir.epic.com/Documentation?docId=cds_playbook)

### Applicable Use Case Restriction
CDS Hooks is explicitly for **real-time, end user-facing decision support only**. Epic recommends against using it for notifications or background processing; those should use event-based interfaces instead. [fhir.epic](https://fhir.epic.com/Documentation?docId=cds_playbook)

***

## 5. Clinical Knowledge Set Apps Playbook

The [Clinical Knowledge Set Playbook](https://fhir.epic.com/Documentation?docId=clinical_knowledge_set_playbook) enables contextual clinical data to drive knowledge lookups: [fhir.epic](https://fhir.epic.com/Documentation?docId=clinical_knowledge_set_playbook)

- Based on the **HL7 Infobutton standard** — clinicians retrieve targeted third-party knowledge based on **patient context and clinical workflow** (e.g., diagnoses, active orders). [fhir.epic](https://fhir.epic.com/Documentation?docId=clinical_knowledge_set_playbook)
- Searches are performed automatically based on elements from the patient's chart (diagnoses, orders) rather than requiring manual clinician search entry. [fhir.epic](https://fhir.epic.com/Documentation?docId=clinical_knowledge_set_playbook)
- Data passed follows the HL7 Infobutton spec — sensitive data is encrypted and limited to patient and provider demographic information. [fhir.epic](https://fhir.epic.com/Documentation?docId=clinical_knowledge_set_playbook)
- Alternatively, if users need to manually search for content, the app can launch via **SMART on FHIR** standard. [fhir.epic](https://fhir.epic.com/Documentation?docId=clinical_knowledge_set_playbook)

***

## 6. Bayesian Medication Dosing Decision Support Playbook

The [Bayesian Medication Dosing Playbook](https://fhir.epic.com/Documentation?docId=bayesianmedicationdosing_playbook) is a clinical data read access pattern: [fhir.epic](https://fhir.epic.com/Documentation?docId=bayesianmedicationdosing_playbook)

- App launches from Hyperspace using **SMART on FHIR**, receiving patient context via the OAuth 2.0 access token. [fhir.epic](https://fhir.epic.com/Documentation?docId=bayesianmedicationdosing_playbook)
- Uses public FHIR APIs (rather than manual provider data entry) to pull **patient and medication data** — particularly the `MedicationRequest.Search` API with data/status filters to retrieve relevant active medication orders. [fhir.epic](https://fhir.epic.com/Documentation?docId=bayesianmedicationdosing_playbook)
- Provides clinicians with personalized dosing recommendations for medications with narrow therapeutic windows (e.g., vancomycin, aminoglycosides) based on the patient's current clinical data. [fhir.epic](https://fhir.epic.com/Documentation?docId=bayesianmedicationdosing_playbook)

***

## 7. Patient Rostering Playbook

The [Building a Patient Roster Playbook](https://fhir.epic.com/Documentation?docId=patient_roster_playbook) covers population-level clinical data read access: [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_roster_playbook)

### Four Methods to Establish Clinical Patient Context for Read Access

1. **Event-Based Interfaces (HL7v2 ADT)** — Real-time push of patient context events (admissions, discharges, appointment scheduling, imaging orders). Outgoing Patient Administration (ADT) interface pushes encounter-level patient context. Filterable by department. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_roster_playbook)

2. **Bulk FHIR** — Population-level read access after a roster is defined within Epic (e.g., all patients with a certain diagnosis). The `Patient.Search (R4)` API retrieves all roster patients, then RESTful FHIR calls or Bulk FHIR itself retrieves corresponding FHIR resources. Recommended for infrequent updates on smaller rosters; use `_typeFilter` for performance. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_roster_playbook)

3. **Extracts** — Epic reporting/BI tools (Clarity, Kit) can extract patient data for integration, from daily to several times per hour. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_roster_playbook)

4. **FHIR List.Search (Patient List) API** — Retrieves predefined patient lists (System Lists or My Lists). System Lists commonly include admitted/recently discharged patients per department. My Lists show the patients a provider is currently caring for. [fhir.epic](https://fhir.epic.com/Documentation?docId=patient_roster_playbook)

***

## 8. External Health Records for Patient Treatment Playbook

The [External Health Records Playbook](https://fhir.epic.com/Documentation?docId=external_health_records_for_patient_treatment) addresses cross-organizational clinical data read access: [fhir.epic](https://fhir.epic.com/Documentation?docId=external_health_records_for_patient_treatment)

- **Carequality** — All US-based Epic customers are members. Provides nationwide coordinated clinical data access across hundreds of healthcare organizations via standard trust policies and technical frameworks. [fhir.epic](https://fhir.epic.com/Documentation?docId=external_health_records_for_patient_treatment)
- **TEFCA (Epic Nexus QHIN)** — U.S. government-sponsored framework. Epic connects through Epic Nexus QHIN, enabling advanced interoperability. Supports both provider-initiated queries (treatment context) and IAS patient-directed access. [fhir.epic](https://fhir.epic.com/Documentation?docId=external_health_records_for_patient_treatment)
- **Direct Messaging** — C-CDA summaries sent provider-to-provider for referrals and transitions of care, provider-to-provider consults, HIE reporting. [fhir.epic](https://fhir.epic.com/Documentation?docId=external_health_records_for_patient_treatment)

***

## 9. CMS-0057 Access Playbook (Patient, Provider & Payer Access)

The [CMS-0057 Access Playbook](https://fhir.epic.com/Documentation?docId=cms_access_playbook) provides 70+ FHIR APIs for federally-mandated data access: [fhir.epic](https://fhir.epic.com/Documentation?docId=cms_access_playbook)

### Patient Access
- Patients access their own health and coverage data through patient-facing FHIR APIs, authenticating via MyChart. [fhir.epic](https://fhir.epic.com/Documentation?docId=cms_access_playbook)
- Tapestry (payer) customers with auto-download enabled automatically connect with patient access applications. [fhir.epic](https://fhir.epic.com/Documentation?docId=cms_access_playbook)
- App qualification requires selecting "Patients" as primary user, enabling "CMS Patient Access API" auto-download, and scoping to the filtered APIs. [fhir.epic](https://fhir.epic.com/Documentation?docId=cms_access_playbook)

### Provider Access
- System-to-system exchange. Providers or third-party systems access payer-held clinical data for coverage determination, prior authorization, and continuity of care. [fhir.epic](https://fhir.epic.com/Documentation?docId=cms_access_playbook)
- Registration uses "Backend Systems" user type + CMS Provider Access API scope. [fhir.epic](https://fhir.epic.com/Documentation?docId=cms_access_playbook)

### Payer-to-Payer Access
- Bidirectional payer data exchange, requiring both payer systems to register. Non-Epic payers provide their client ID to the Epic payer for configuration. [fhir.epic](https://fhir.epic.com/Documentation?docId=cms_access_playbook)

***

## 10. Developer Guide: Process for Clinical Data Read Access Registration

The [Developer Guide](https://open.epic.com/DeveloperResources) describes the end-to-end process: [open.epic](https://open.epic.com/DeveloperResources)

1. **Design**: Review playbooks → identify correct APIs for the clinical data needed → review developer guidelines [open.epic](https://open.epic.com/DeveloperResources)
2. **Register Client ID**: Self-service on Epic on FHIR. Select only APIs needed in production (customers assess security/privacy/licensing implications). Include patient-facing or backend systems user type as appropriate. [open.epic](https://open.epic.com/DeveloperResources)
3. **Develop & Test**: Use the Sandbox with test patients and endpoints
