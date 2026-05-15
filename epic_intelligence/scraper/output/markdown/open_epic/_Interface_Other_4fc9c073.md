# open.epic :: Explore By Interface Type

> Source: https://open.epic.com/Interface/Other

---

# 
 By Interface Type

 

 

 
 

 

 
 

 
 

 
 
 

## Other Integrations

 
But wait! There's more! We've also created custom integrations using the following approaches. 

### 
 Outgoing Real Time Prescription Benefit Inquiry and Response

 

 

 Supports real-time prescription benefits checking (RTPB) during the prescriber ordering process. This feature lets prescribers see expected out-of-pocket costs, lower-cost medication suggestions, and whether additional approvals from the insurance company are needed before the prescription can be filled. Providers can share this information with patients before sending the order to the pharmacy, saving time and money for patients, and help improve medication adherence. 
 Payers and vendors interested in joining the RTPB network can request more information by submitting an [Interoperability Request](https://userweb.epic.com/Forms/InteroperabilityRequest).
 

 

 [Current integrations include ](#)
 

 - Arrive Health

 - CenterX

 - COVERMYMEDS

 - DRFIRST, INC.

 - HUMANA

 - SURESCRIPTS

 

 

 

### 
 Outgoing Newborn Personal Identity Code Request and Response

 

 

 The Outgoing Newborn Personal Identity Code Request interface sends notifications of patient birth to the Population Register Centre (VRK) in Finland. The Incoming Newborn Personal Identity Code Response interface receives the response message from VRK that contains the HETU for the newborn and assigns the HETU to the patient in Epic.
 

 

 [Current integrations include ](#)
 

 - Digi- ja väestötietovirasto

 

 

 

### 
 Outgoing Death Notification and Response
 [read the spec](/Tech/TechSpec?spec=6097)

 

 

 Sends notifications of patient death to the Population Register Centre in Finland.
 

 

 [Current integrations include ](#)
 

 - Digi- ja väestötietovirasto

 

 

 

### 
 Outgoing Provider Query

 

 

 This XML interface queries the Terhikki provider database to determine whether a provider has specific rights and restrictions. The rights and restrictions associated with a provider are used to determine which features in Epic the provider has access to.
 

 

 [Current integrations include ](#)
 

 - Valvira

 

 

 

### 
 Outgoing eArchive Documents and Query

 

 

 Queries the Kanta eArchive system for document metadata and content and sends new and updated documents to Kanta eArchive. Licensing for this interface includes the Outgoing eArchive Document Query interface.
 

 

 [Current integrations include ](#)
 

 - Kela

 

 

 

### 
 Outgoing Demographics Query

 

 

 Queries the Population Register Centre (VRK) in Finland for a patient's demographics or the patient's HETU.
 

 

 [Current integrations include ](#)
 

 - Digi- ja väestötietovirasto

 

 

 

### 
 Outgoing QRDA Documents
 [read the spec](/Tech/TechSpec?spec=5218)

 

 

 Users can create QRDA Idocuments from data in their Epic EHR. Each QRDA I document is specific to one patient and contains data pertinent to quality measure reporting. Each QRDA III document includes aggregated quality measurement data for a provider or group of providers, including the quality measures they are reporting on and their performance rate. QRDA III documents are typically used by providers for quality measure submission. Many regulatory programs, including Meaningful Use, Core Measures, Inpatient Quality Reporting, ORYX Performance Measurement Reporting, and PQRS, accept QRDA documents to satisfy their quality reporting requirements.
 

 

 [Current integrations include ](#)
 

 - CMS

 - Washington - Public Health Agencies

 

 

 

### 
 Bidirectional Referrals
 [read the spec](/Tech/TechSpec?spec=5807)

 

 

 This pair of interfaces sends and receives referral and consultation requests, along with triage details and care summaries regarding those referrals. These messages are structured according to the HL7-Finland PikaXML standard.
 

 

 [Current integrations include ](#)
 

 - HUS

 - Polycon

 

 

 

### 
 Outgoing Document Notification Interface - Finland

 

 

 Sends document metadata to Navitas when Navitas queries Epic for a document ID.
 

 

 [Current integrations include ](#)
 

 - Elisa

 

 

 

### 
 Outgoing Social Care Document Query

 

 

 This XML interface queries the Kanta Social Care system for document metadata and content.
 

 

 [Current integrations include ](#)
 

 - Kela

 

 

 

### 
 Outgoing Dental Summary Interface - Singapore

 

 

 Sends a PDF report summarizing the patient's dental health. Requires Wisdom, Epic's dental product.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Referral and Provider Communication Notification Interface - Singapore

 

 

 Sends a notification to the National Electronic Health Record (NEHR) when referrals are entered in Epic or provider communications are written in the Communication Management activity in Epic.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Demographics Query Interface - Singapore

 

 

 Queries the National Electronic Health Record (NEHR) system in Singapore for a patient's demographics information.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Transaction Notification Interface - Belgium

 

 

 Sends metadata for notes, letters, results, and scans to the Belgian National Hub. This process allows the Hub to index references to the source content for external providers to request.
 

 

 [Current integrations include ](#)
 

 - Réseau Santé Wallon

 

 

 

### 
 Outgoing Transaction Query Interface - Belgium

 

 

 Interface for Belgium. A collection of web services invoked from the Chart Review activity that retrieve a list of documents for a patient from the National Hub and request the contents of specific documentation.
 

 

 [Current integrations include ](#)
 

 - Réseau Santé Wallon

 

 

 

### 
 Outgoing Birth Notification and Medical Form Interface - Belgium

 

 

 Sends birth notifications and birth-related medical forms to Belgium's eBirth registry according to the specifications in the eBirth Hospital Web Services Technical User Guide - Final version - 1.6 – 12/05/2016.
 

 

 [Current integrations include ](#)
 

 - E-Health

 

 

 

### 
 Outgoing Medication Orders Request and Response Interface - Belgium

 

 

 Interface for Belgium. Sends e-prescribing messages to, and receives acknowledgements from, Recip-e. These interfaces can be used to create new prescriptions, cancel prescriptions, and query for a list of prescriptions that a pharmacy can dispense.
 

 

 [Current integrations include ](#)
 

 - E-Health

 

 

 

### 
 Outgoing Social Care Need Query Interface - Finland

 

 

 Queries the eTotu Social Services system for patient referrals and documents.
 

 

 [Current integrations include ](#)
 

 - Kela

 

 

 

### 
 Outgoing Financial Transactions Query Interface - Belgium

 

 

 Sends charges to and receives charge verifications from an external system. Billing-related errors logged by this interface are routed to an activity in Epic where users can correct errors and resubmit affected messages in real time.
 

 

 [Current integrations include ](#)
 

 - Zorgi

 

 

 

### 
 Outgoing Imaging Document and Response Interface - Finland

 

 

 Sends reference links for R2CDA imaging documents to Navitas and receives acknowledgements in return.
 

 

 [Current integrations include ](#)
 

 - Elisa

 

 

 

### 
 Outgoing Vaccination History Query Interface - Norway
 [read the spec](/Tech/TechSpec?spec=5203)

 

 

 Queries the SYSVAK vaccination registry, per [Norwegian SYSVAK specification](https://sarepta.ehelse.no/standard/SYSVAK). Each query requests historical immunization data for a given patient. This registry does not provide immunization recommendation data. The incoming portion of the interface does not directly update immunizations in the chart; the provider sees the response from the registry and decides what should be added to the patient record.
 

 

 [Current integrations include ](#)
 

 - Norwegian Institute of Public Health

 

 

 

### 
 Outgoing Vaccination Administration Request and Response Interface - Norway
 [read the spec](/Tech/TechSpec?spec=5205)

 

 

 Sends information about vaccination administrations, per the [Norwegian SYSVAK specification](https://sarepta.ehelse.no/standard/SYSVAK).
 

 

 [Current integrations include ](#)
 

 - Norwegian Institute of Public Health

 

 

 

### 
 Outgoing Sick Leave Interface - Norway
 [read the spec](/Tech/TechSpec?spec=5209)

 

 

 Sends information regarding a patient's ability to perform work in Norway, as specified by the Norwegian Labour and Welfare administration (NAV). Relevant information includes duration of impairment, cause of impairment, and other supporting information provided by the patient's provider.
 

 

 [Current integrations include ](#)
 

 - NAV

 

 

 

### 
 Outgoing External Repricing Request Query (X12 837)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20Real-time%20837%20External%20Pricing%20Implementation%20Guide.pdf)

 

 

 Epic's managed care system supports pricing claims in real-time by sending the 837 and receiving a response of a repriced 837 with HCP Segments.
 

 

### 
 Incoming Health Care Services Authorization Interface - Netherlands

 

 

 Receives notifications from VECOZO when the status of an authorization request has changed. The incoming interface can update authorization records (RFL or AUT) in Epic, which drive referral workqueue and scheduling workflows.
 

 

### 
 Outgoing Birth Notification Interface - Norway
 [read the spec](/Tech/TechSpec?spec=5294)

 

 

 Sends notification of birth and receives back national identifier from the Norwegian citizen registry.
 

 

 [Current integrations include ](#)
 

 - Norwegian Institute of Public Health

 

 

 

### 
 Outgoing Vaccination Codeset Update Request and Response Interface - Norway

 

 

 Queries the Norwegian SYSVAK registry and returns an import file to update the immunization build for Norwegian customers.
 

 

### 
 Outgoing Financial Information Query Interface - Norway

 

 

 Retrieves income, expense, and asset information for patients and their contacts from Financial Assistance.
 

 

 [Current integrations include ](#)
 

 - NAV

 - Norwegian Tax Administration

 

 

 

### 
 Outgoing Birth Registry Interface - Norway

 

 

 Sends clinical information regarding a birth event to the MFR registry.
 

 

 [Current integrations include ](#)
 

 - Norwegian Institute of Public Health

 

 

 

### 
 Outgoing GP Patient List Subscription and Response
 [read the spec](/Tech/TechSpec?spec=5269)

 

 

 In Norway, a regional service (NAV) maintains a list of physicians (GPs) and the patients to whom they provide care. This supports integration for providers to interact with NAVs service; notably, subscribing to their list (signing up for an updated list of patients to be sent monthly), ending their subscription to the monthly list, and checking the status of their subscription.
 

 

 [Current integrations include ](#)
 

 - NHN

 

 

 

### 
 Outgoing ePrescribing Service Request and Response Interface - Norway
 [read the spec](/Tech/TechSpec?spec=8644)

 

 

 ePrescribing services with the national medication directory service (SFM)
 

 

 [Current integrations include ](#)
 

 - NHN

 

 

 

### 
 Incoming ePrescribing Service Notification Interface - Norway
 [read the spec](/Tech/TechSpec?spec=8643)

 

 

 ePrescribing services with the national medication directory service.
 

 

 [Current integrations include ](#)
 

 - NHN

 

 

 

### 
 Incoming MDS CMS Validation Report
 [read the spec](/Tech/TechSpec?spec=5356)

 

 

 Takes the CMS MDS Validation Final Report flat file, parses the result of all of the MDS assessments in the report, and files the results of the validation back to Epic The MDS Validation Final Report flat file is generated by CMS QIES and the specification for the report can be found in the CASPER Reporting User's Guide For MDS Providers. A full list of CMS error and warning codes (edits) can be found in section 5 of the MDS 3.0 Provider User's Guide.
 

 

 [Current integrations include ](#)
 

 - CMS

 

 

 

### 
 Outgoing Vaccination Administration Request and Response - Australia
 [read the spec](/Tech/TechSpec?spec=6076)

 

 

 Sends information about vaccination administrations to the Australian Immunisation Register (AIR). In an upcoming version, will also query AIR for immunization history.
 

 

 [Current integrations include ](#)
 

 - Services Australia

 

 

 

### 
 Incoming Provider Communications Interface - Finland
 [read the spec](/Tech/TechSpec?spec=5332)

 

 

 Receives incoming summary of care if patient receives care out of home municipality.
 

 

### 
 Outgoing Provider Communications - Finland
 [read the spec](/Tech/TechSpec?spec=6087)

 

 

 Sends outgoing communication and summary of care for patients receiving care outside of home municipality.
 

 

### 
 Tapestry Incoming Bank Reconciliation

 

 

 Receives status updates for check records to match the status assigned by the bank responsible for distributing the check.
 

 

 [Current integrations include ](#)
 

 - Chase Bank

 

 

 

### 
 Tapestry Incoming Benefit Accumulations

 

 

 Receives external benefit bucket information so that member cost responsibility can be calculated correctly when processing claims.
 

 

 [Current integrations include ](#)
 

 - Aetna

 - Navitus

 

 

 

### 
 Tapestry Outgoing Positive Pay Files

 

 

 Sends check information for processed claims to banks as part of the claims payment cycle.
 

 

 [Current integrations include ](#)
 

 - Chase Bank

 

 

 

### 
 Incoming Drug Supply Chain Event Notification to Willow Inventory
 [read the spec](/Tech/TechSpec?spec=5373)

 

 

 Enables supply chain partners to capture event information about supply chain events and to share that information with their trading partners securely. Uses the Electronic Product Code Information Service (EPCIS) GS1 standard and complies with the Drug Supply Change Security Act (DSCSA) regulation that requires organizations exchange package-level tracing information.
 

 

 [Current integrations include ](#)
 

 - AMERISOURCE BERGEN

 - Anda

 - Cardinal Health WaveMark

 - CENCORA

 - CuraScript

 - LSPedia

 - McKesson

 - SAP

 - SURESCRIPTS

 

 

 

### 
 Outgoing Dialysis Updates to CMS
 [read the spec](https://qnetconfluence.cms.gov/display/ELDF/Documentation+Repository)

 

 

 Sends Dialysis Data to CMS (by way of a Renal Healthcare HIE) from the Dialysis Module, per HIE specifications. Requires Nephrology license. Specifications are found - https://qnetconfluence.cms.gov/display/ELDF/Documentation+Repository 
 

 

 [Current integrations include ](#)
 

 CMS

 - ONEHEALTHPORT

 - Renal Healthcare Association

 

 

 

### 
 Outgoing eMultidose Patient Medication List Change Query

 

 

 eMultidose Patient Medication List Change Query
 

 

### 
 Outgoing eMultidose Responsibility Update

 

 

 Outgoign eMultidose Responsibilty Update
 

 

### 
 Outgoing Social Care Disclosure Notification - Finland

 

 

 Notifies the national log register storage service (Kanta) that patient social care information has been shared, per Sosiaalihuolto-r4.
 

 

### 
 Incoming Scheduling Slot Availability Query
 [read the spec](/Tech/TechSpec?spec=5320)

 

 

 Receives requests from the United Kingdom's NHS e-Referral Service (also known as Choose and Book) to request appointment slots from Cadence, Epic's scheduling system.
 

 

 [Current integrations include ](#)
 

 - National Health Service

 

 

 

### 
 Outgoing PDS Tracing Query
 [read the spec](/Tech/TechSpec?spec=5231)

 

 

 Outgoing PDS Tracing interface sends queries to the Personal Demographics Services (PDS) master index for National Health Service (NHS) patient records in the United Kingdom. PDS Trace Response messages are processed by the Incoming PDS Tracing interface. Message interactions follow HSCIC's Message Implementation Manual (MIM) version 7.2.02 and External Interface Specification 11.6. This interface uses messages expressed in XML encoding syntax.
 

 

 [Current integrations include ](#)
 

 - National Health Service

 - PDS

 

 

 

### 
 Outgoing PDS Demographics Synchronisation Query
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20PDS%20Demographics%20Synchronisation%20-%20UK%20Interface%20Technical%20Specification.pdf)

 

 

 Outgoing PDS Synchronisation interface sends queries for demographics and demographic updates to the Personal Demographics Services (PDS) master index for National Health Service (NHS) patient records in the United Kingdom. PDS Synchronisation Response messages are processed by the Incoming PDS Synchronisation interface. Message interactions follow HSCIC's Message Implementation Manual (MIM) version 7.2.02 and External Interface Specification 11.6. This interface uses messages expressed in XML encoding syntax.
 

 

 [Current integrations include ](#)
 

 - National Health Service

 - PDS

 

 

 

### 
 Outgoing PDS NHS Number Allocation Request for Acute Care
 [read the spec](/Tech/TechSpec?spec=5232)

 

 

 Sends requests to the Personal Demographics Services (PDS) to generate a new National Health Service (NHS) number for an adult patient in an acute care setting in the United Kingdom. PDS NHS Number Response messages are processed by the Incoming PDS NHS Number Allocation interface. Message interactions follow HSCIC's Message Implementation Manual (MIM) version 6.3.01 and External Interface Specification 11.6. This interface uses messages expressed in XML encoding syntax.
 

 

 [Current integrations include ](#)
 

 - National Health Service

 - PDS

 

 

 

### 
 Outgoing PDS Newborn Notification
 [read the spec](/Tech/TechSpec?spec=5233)

 

 

 Sends requests to the Personal Demographics Services (PDS) to generate a new National Health Service (NHS) number for a newborn delivery documented in Stork within the United Kingdom. PDS Create Initial Record Response messages are processed by the Incoming PDS Create Initial Record Response interface. Message interactions follow HSCIC's Message Implementation Manual (MIM) version 7.2.02 and External Interface Specification 11.6. This interface uses messages expressed in XML encoding syntax.
 

 

 [Current integrations include ](#)
 

 - National Health Service

 - PDS

 

 

 

### 
 Outgoing Medication Orders
 [read the spec](/Tech/TechSpec?spec=6433)

 

 

 Sends outgoing e-prescribed medication orders, following Dutch HL7 v3 Standards (MP6).
 

 

 [Current integrations include ](#)
 

 - Nictiz

 

 

 

### 
 Outgoing Medication Dispense History Query

 

 

 Queries the Landelijk SchakelPunt (LSP) to retrieve patient medication data. Certified with VZVZ. This interface follows the Dutch HL7 v3 standards implemented within AORTA.
 

 

 [Current integrations include ](#)
 

 - Nictiz

 

 

 

### 
 Outgoing Medication Orders
 [read the spec](/Tech/TechSpec?spec=8005)

 

 

 Sends ambulatory medication orders that are placed in Order Entry to the National Electronic Health Record (NEHR) in the format required by the NEHR putOrderedMedications service. This interface uses the XML message format.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Medication Dispenses
 [read the spec](/Tech/TechSpec?spec=8004)

 

 

 Sends outpatient medication dispenses to the National Electronic Health Record (NEHR) in the format required by the NEHR putDispensedMedications service. Messages are sent whenever an outpatient medication dispense is received from an internal pharmacy system through an Incoming Medication Orders to EpicCare Ambulatory interface. This interface uses the XML message format.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Laboratory Results

 

 

 Sends laboratory results to the National Electronic Health Record (NEHR) in the format required by the NEHR putLabResults service. This interface uses the XML message format.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Radiology Results

 

 

 Sends radiology results to the National Electronic Health Record (NEHR) in the format required by the NEHR putRadiologyResults service. This interface uses the XML message format.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Discharge Summaries

 

 

 Sends a clinical summary to the National Electronic Health Record (NEHR) in the format required by the NEHR putDischargeSummary service. The summary is generated upon discharge of a patient.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing ED Summaries

 

 

 Sends a clinical summary to the National Electronic Health Record (NEHR) in the format required by the NEHR putEDNotes service. The summary is generated when the patient is discharged or dismissed from the emergency department.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Surgical Summaries

 

 

 Sends a surgical summary to the National Electronic Health Record (NEHR) in the format required by the NEHR putOTNotes service at the time that a surgical log is posted or addended. This interface uses the XML message format.
 

 

 [Current integrations include ](#)
 

 - Singapore Ministry of Health Holdings

 

 

 

### 
 Outgoing Health Care Claim Grouper and Pricer
 [read the spec](/Tech/TechSpec?spec=staged%2FHealth%20Care%20Claim%20Grouper%20and%20Pricer%20-%20Outgoing.pdf)

 

 

 Bidirectional interface that analyzes claims to determine which codes and prices are appropriate, and can work with various external systems.
 

 

### 
 Outgoing Municipality Integrations

 

 

 Manages communication with external municipal systems according to established MedCom protocols to coordinate the delivery of home care after discharge. The outgoing interface supports: automatic admission and discharge notifications to alert municipalities when their citizens have been admitted to and discharged from the hospital, clinical reports by nursing staff to convey updated clinical information and home care needs to the home care system so they can prepare to assume responsibility for the patient, and administrative notifications to coordinate and document the extension of admissions if the municipality is not yet prepared to accept responsibility for patient care. This integration also includes an incoming interface for filing admission reports sent by municipality home care systems when they receive an admission notification from the hospital. Clinical staff can use these admission reports to review the current status of home care patients. This interface uses the Medcom XML/EDIFACT standard.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Bidirectional Correspondence
 [read the spec](/Tech/TechSpec?spec=5437)

 

 

 Sends and receives patient-centric clinical correspondence messages to external parties, including other hospitals, general practitioners, and municipal systems. These messages are used for ad hoc communication to convey additional information beyond what is included in other specifications.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Outgoing Newborn CPR Assignment Request and Response

 

 

 Registers newborns in the Danish civil registration system (CPR) and reserves a corresponding CPR identifier (national ID). This interface uses the Medcom Web Service standard.
 

 

 [Current integrations include ](#)
 

 - NSP

 

 

 

### 
 Outgoing Order Requisitions

 

 

 Sends orders placed by a clinical user to either an external LIS or Danish laboratory outside the organization. This interface supports general chemistry, blood bank, microbiology, and pathology laboratory procedures placed by users in EpicCare Inpatient and EpicCare Ambulatory, and pathology procedures placed by clinical users in OpTime. This interface uses the Medcom XML standard.
 

 

 [Current integrations include ](#)
 

 - CGI

 

 

 

### 
 Incoming Pathology Results

 

 

 Receives pathology test results from a LIS for use in Epic. Results can be received for orders placed in Epic or placed elsewhere. Additionally, this interface can update the status of the results to In Process, Preliminary, Final, or Final-Edited. This interface uses the Medcom XML standard.
 

 

 [Current integrations include ](#)
 

 - CGI

 

 

 

### 
 Incoming Lab Results Interface

 

 

 Receives general chemistry, blood bank, and microbiology test results from LIS for use in Epic. Results can be received for orders placed in Epic or placed elsewhere. Additionally, this interface can update the status of the result to In Process, Preliminary, Final, or Final- Edited. This interface uses the Medcom XML standard.
 

 

 [Current integrations include ](#)
 

 - DEDALUS

 

 

 

### 
 Outgoing Referrals and Booking Confirmation

 

 

 Manages outgoing referrals communication with external systems according to established MedCom protocols. The interface facilitates sending new referrals composed in Epic and forwarding copies of previously received referral messages. The interface can also send booking confirmations to inform a patient's referring and primary care physicians when a referral is being acted on in Epic. These notifications can be sent automatically when an appointment has been scheduled, or when a patient is preadmitted or arrived in the ED for an issue relating to the referral. This interface uses the Medcom XML/EDIFACT standard.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Incoming Referrals and Booking Confirmation

 

 

 Manages incoming referrals communications with external systems according to established MedCom protocols. This interface can both create incoming hospital referrals and file booking confirmation messages for referrals originating in Epic.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Outgoing Binary Documents

 

 

 Sends binary attachment documents associated with a MedCom message. This interface must work in conjunction with one of the following MedCom interfaces: Outgoing Summary of Care, Outgoing Referrals and Booking Confirmation, Bidirectional Correspondence, and Outgoing Order Requisitions.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Incoming Binary Documents

 

 

 Files the binary attachment documents associated with an incoming MedCom message to the Epic WebBLOB server. This interface must work in conjunction with one of the following MedCom interfaces: Incoming Summary of Care, Incoming Referrals and Booking Confirmation, Bidirectional Correspondence, Outgoing Municipality Integrations - Incoming Response, Incoming Rehabilitation Plan Summary, Incoming Lab Results, and Incoming Pathology Results.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Outgoing Procedure Log Data
 [read the spec](/Tech/TechSpec?spec=5222)

 

 

 Sends data for configured case tracking events from a Cupid procedure log case for the purpose of submitting data to external registries. Submissions to the NCDR CathPCI & NCDR ICD registries can be sent directly from Cupid, Epic's CVIS. The messages contain data on the case including panels, staff, timeouts, implants, equipment, radiation, verifications, flowsheets, events, medications, and labs.
 

 

 [Current integrations include ](#)
 

 - Fujifilm

 - General Data

 - LUMEDX

 - Philips

 - ProSolv CardioVascular

 - TSG Integrations

 

 

 

### 
 Incoming Referral Scheduling Request Query
 [read the spec](/Tech/TechSpec?spec=5325)

 

 

 Receives requests from the United Kingdom's NHS e-Referral Service (also known as Choose and Book) to book an appointment in Cadence, Epic's scheduling system.
 

 

 [Current integrations include ](#)
 

 - National Health Service

 

 

 

### 
 Incoming Summary of Care Interface

 

 

 Files a summary of care document (Epikrise) from an external hospital or specialist as a note to the patient's chart. These notes describe the care that the patient received from the external hospital or specialist and can be used as reference when providing care in Epic.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Outgoing Summary of Care Interface

 

 

 Sends a summary of care document (Epikrise) to the patient's referring provider and primary care physician to report the outcome of an ED visit, admission, or ambulatory encounter using a combination of discrete and free-text information. Summary of care messages are automatically sent for the patient whenever a designated Epikrise note has been signed and the patient's encounter is closed. This interface uses the Medcom XML/EDIFACT standard.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Outgoing PAS Data and Response Interface
 [read the spec](/Tech/TechSpec?spec=5244)

 

 

 Sends patient, referral, administrative pathway, and encounter data grouped by patient episode to the Victorian Integrated Non-Admitted Health (VINAH) database, which is run by the State of Victoria Department of Health & Human Services in Australia. Additionally, this interface receives asynchronous acknowledgments and error information from VINAH. This interface uses messages expressed in XML encoding syntax.
 

 

 [Current integrations include ](#)
 

 - Victoria Department of Health and Human Services

 

 

 

### 
 Data Exchange with 3M Core Grouping Software or Grouper Plus Content Services

 

 

 This is a proprietary specification to/from 3M's Core Grouping Software or Grouper Plus Content Services. Medicare OP claims data is sent to the 3M Module. CSG/GPCS performs APC/APG grouping, reimbursement calculations, OCE and proprietary claims scrubbing; the results are loaded back into Epic where errors can drive claim edits.
 

 

 [Current integrations include ](#)
 

 - 3M

 - Solventum

 - SYMPLR

 

 

 

### 
 Outgoing FMK Medication Card Services Request and Response
 [read the spec](/Tech/TechSpec?spec=6551)

 

 

 Manages the following interactions between Epic and the Danish medication database Falles Medicinkort (FMK): Filing medication lists for patients into Epic; pushing medication changes from Epic to the national database; and setting the reviewed status of the medication list by a clinician.
 

 

 [Current integrations include ](#)
 

 - NSP

 

 

 

### 
 Outgoing Medication Orders to Prescription Exchange Service
 [read the spec](/Tech/TechSpec?spec=5252)

 

 

 Sends medication orders and receives acknowledgements from a prescription exchange service (the currently supported service is eRx). When clinicians create, cancel, or amend medication orders, this XML interface relays the ePrescription information to eRx, which forwards the medication information to the appropriate dispensing facility. This interface uses the XML message format.
 

 

 [Current integrations include ](#)
 

 - Fred IT Group

 

 

 

### 
 Outgoing Birth Notification Interface
 [read the spec](/Tech/TechSpec?spec=5293)

 

 

 Sends a report to register newborns in the municipal child care system and begin coordination of home visits by municipal pediatric nursing after discharge.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Outgoing ECPR Assignment Request and Response

 

 

 Requests ECPR identifiers for request a new official ECPR from the Denmark national ECPR registry for non-Danish residents, anonymous, trauma, and unknown patients.
 

 

### 
 Outgoing Rehabilitation Plan Summary

 

 

 Sends a summary of the physical therapy/rehabilitation (GGOP) provided for a patient and needs for ongoing therapy/rehab. Frequently used as a way for physical therapists to document ongoing care for a patient, provide progress updates to external parties such as their primary care physician, and transition responsibility for therapy to other entities such as other hospitals or municipality rehabilitation systems. This interface uses the XML (DGOP), GGOP (MedCom XML) standard.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Incoming Rehabilitation Plan Summary

 

 

 Receives incoming summaries of physical therapy/rehabilitation (GGOP) from physical therapists. This interface can be configured to create scheduling orders, which users can use to plan future appointments for the patient's care. This interface uses the XML (DGOP) GGOP (MedCom XML) standard.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Outgoing Prescription Prior Authorization Request and Response
 [read the spec](/Tech/TechSpec?spec=8007)

 

 

 Submits prior authorization requests to the DHPO and HAAD post office. This interface uses the HAAD XML standard.
 

 

 [Current integrations include ](#)
 

 - eClaimLink

 

 

 

### 
 Outgoing Claim Submission from Willow Ambulatory
 [read the spec](/Tech/TechSpec?spec=8008)

 

 

 Submits claims to the DHPO and HAAD post office. This interface uses the HAAD XML standard.
 

 

 [Current integrations include ](#)
 

 - eClaimLink

 

 

 

### 
 Incoming Remittance Advice Download to Willow Ambulatory
 [read the spec](/Tech/TechSpec?spec=8008)

 

 

 Downloads remittance advices that are stored in HAAD post office using a batch job. This interface uses the HAAD XML standard.
 

 

### 
 Outgoing COV Verification Query

 

 

 The interface queries Vecozo and uses the VZ37/VZ38 standard to retrieve and store insurance information for a patient. This interface uses the VZ37 / VZ38 standard.
 

 

 [Current integrations include ](#)
 

 - Vecozo

 

 

 

### 
 Outgoing IHI Verification Query
 [read the spec](/Tech/TechSpec?spec=5266)

 

 

 Queries the Australian Healthcare Identifiers (HI) Service to retrieve and validate a patient's Individual Healthcare Identifier (IHI) Number. The main goal of this query is to allow modules such as Care Everywhere to interact with My Health Record, which requires valid IHI Numbers for patients when uploading documents.
 

 

 [Current integrations include ](#)
 

 - Australian Digital Health Agency

 - Services Australia

 

 

 

### 
 Outgoing Perinatal Data
 [read the spec](/Tech/TechSpec?spec=5230)

 

 

 Submits summary reports at the end of each pregnancy to Perined, a national registry in the Netherlands that records obstetric data. This interface uses the XML HL7 NL standard.
 

 

 [Current integrations include ](#)
 

 - Perined

 

 

 

### 
 Outgoing Initial Public Health Case Report (eICR)
 [read the spec](/Tech/TechSpec?spec=5263)

 

 

 Satisfies the Meaningful Use objective to send Electronic Case Reports to public health agencies using the HL7 Clinical Document - Electronic Initial Case Report (CDA-eICR) format.
 

 

 [Current integrations include ](#)
 

 - Alabama - Public Health Agencies

 - APHL

 - Arizona - Public Health Agencies

 - Arkansas - Public Health Agencies

 - Artificial Intelligence in Medicine

 - California - Public Health Agencies

 - Center for Disease Control

 - Chesapeake Regional Information System for Our Patients

 - CliniSync

 - Colorado - Public Health Agencies

 - Connecticut - Public Health Agencies

 - Delaware Health Information Network

 - EHEALTH TECHNOLOGIES

 - Florida - Public Health Agencies

 - Georgia - Public Health Agencies

 - Hawaii - Public Health Agencies

 - Houston - Public Health Agencies

 - Idaho - Public Health Agencies

 - Illinois - Public Health Agencies

 - Indiana - Public Health Agencies

 - Iowa - Public Health Agencies

 - Kentucky - Public Health Agencies

 - Kentucky Health Information Exchange

 - Louisiana - Public Health Agencies

 - Maryland - Public Health Agencies

 - Massachusetts - Public Health Agencies

 - MedAllies

 - Michigan - Public Health Agencies

 - Minnesota - Public Health Agencies

 - Missouri - Public Health Agencies

 - Nevada - Public Health Agencies

 - New Jersey - Public Health Agencies

 - New Mexico - Public Health Agencies

 - New York - Public Health Agencies

 - New York City - Public Health Agencies

 - North Carolina - Public Health Agencies

 - Ohio - Public Health Agencies

 - Oregon - Public Health Agencies

 - Pennslyvania - Public Health Agencies

 - Rhode Island - Public Health Agencies

 - Santa Clara County (CA) - Public Health Agencies

 - South Carolina - Public Health Agencies

 - SURESCRIPTS

 - Tennessee - Public Health Agencies

 - Texas - Public Health Agencies

 - Virginia - Public Health Agencies

 - Washington - Public Health Agencies

 - Wisconsin - Public Health Agencies

 

 

 

### 
 Outgoing FMK Ordered Refill Request and Response
 [read the spec](/Tech/TechSpec?spec=6435)

 

 

 Sends refill requests to the Danish medication database Fælles Medicinkort (FMK) for a patient or an entire facility.
 

 

 [Current integrations include ](#)
 

 - NSP

 

 

 

### 
 Outgoing eRx Services Request and Response

 

 

 Communicates with the prescription center of Finland any time a user makes changes to a patient's prescriptions, as well as when a user needs to reconcile a patient's existing prescriptions into Epic.
 

 

 [Current integrations include ](#)
 

 - Kela

 

 

 

### 
 Outgoing Prescription Upload Request and Response
 [read the spec](/Tech/TechSpec?spec=8006)

 

 

 Submits a prescription to the UAE Post Office hub for authorization.
 

 

 [Current integrations include ](#)
 

 - eClaimLink

 

 

 

### 
 Outgoing Prescription Download Request and Response

 

 

 Downloads a patient's prescriptions from the UAE Post Office hub.
 

 

 [Current integrations include ](#)
 

 - eClaimLink

 

 

 

### 
 HL7 InfoButton
 [read the spec](/Tech/TechSpec?spec=5312)

 

 

 The Active Guidelines (AGL) activity in the Epic EHR uses the HL7 InfoButton standard to allow clinicians to retrieve targeted information provided by third parties, specific to the context of the patient or clinical workflow. Rather than searching third party knowledge base, searches are performed automatically based off elements of the patient's chart like diagnoses or orders. 
 

 

 [Current integrations include ](#)
 

 - Clin-eguide

 - ClinicalKey

 - Dynamed

 - Facts & Comparisons

 - Isabel

 - KidsHealth

 - Lexicomp

 - MedlinePlus

 - Micromedex

 - Pub Med

 - UpToDate

 - VisualDx

 

 

 

### 
 Mobile App Integration
 [read the spec](/Tech/TechSpec?spec=5309)

 

 

 Epic's mobile applications - Haiku, Canto, and Rover - can communicate with specialized clinical review applications like document or image viewers. This framework allows our applications to launch your app with context, making for a a smooth and seamless clinical experience for the user.
 

 

 [Current integrations include ](#)
 

 - Sectra Liteview PACS

 - Voalte

 

 

 

### 
 Clinical Context Manager Integration
 [read the spec](/Tech/TechSpec?spec=5434)

 

 

 CCOW (formerly known as Clinical Context Object Workgroup) is a vendor-independent HL7 standard protocol designed to allow disparate clinical applications to synchronize data in real-time at the point of care. Epic can integrate as a participant with a third-party clinical context manager.
 

 

### 
 Patient Portal Links
 [read the spec](/Tech/TechSpec?spec=5187)

 

 

 Epic's patient portal can link to other patient-specific websites through functionality known as Dynamic Links. Dynamic Links are used to launch external websites from within the portal. The link can be configured to pass context about the patient through query string parameters, optionally encrypted using AES. 
 

 

 [Current integrations include ](#)
 

 - Apex

 - Blackhawk

 - eHealth

 - Health Media

 - HealthEquity

 - Lasernet

 - MyPreventiveCare

 - RSA Access Manager

 - RxEOB

 - The Health Heritage Family Medical History Project

 - VisionTree

 

 

 

### 
 Cash Management
 [read the spec](/Tech/TechSpec?spec=5411)

 

 

 This incoming batch interface creates a record of deposits for cash reconciliation using a configurable flat file format. The flat file is configurable and the preferred format is in the linked specification, however Epic can also support industry standard formats such as CCD+.
 

 

 [Current integrations include ](#)
 

 - Bank of America

 - Chase Bank

 - Fifth Third Bank

 - Huntington Bank

 - PNC Bank

 - SunTrust Bank

 - TD Bank

 - Texas Capital Bank

 - US Bank

 - Wells Fargo Bank

 

 

 

### 
 Incoming Claim Status Batch (Flat File)
 [read the spec](/Tech/TechSpec?spec=5428)

 

 

 This incoming batch interface loads information about claim status through a configurable flat file. This interface can update the status of claims in the system and is able to load claim error information from payer and intermediary systems.

The flat file format is configurable, but the common specification is pre-configured in the Foundation System for Epic customers and widely used with success.
 

 

 [Current integrations include ](#)
 

 - Availity

 - Change Healthcare

 - Cirius

 - eSolutions

 - Experian Health

 - Healthcare IP

 - Inovalon

 - InstaMed, a J.P. Morgan Company

 - nThrive

 - Optum

 - Quadax

 - SSI

 - TriZetto Provider Solutions, a Cognizant Company

 - WayStar

 

 

 

### 
 Incoming Self-pay Payments
 [read the spec](/Tech/TechSpec?spec=5410)

 

 

 This incoming batch interface posts self-pay and bad debt payments in a configurable flat file format.

The flat file format is configurable, but the above common specification is pre-configured in the Foundation System for Epic customers and widely used with success.
 

 

 [Current integrations include ](#)
 

 - Bank of America

 - BBVA

 - Fifth Third

 - J.P Morgan Chase

 - Patientco

 - PNC

 - Texas Capital Bank

 - US Bank

 - Wells Fargo

 

 

 

### 
 Monthly Premium Withholding Report (MPWR)
 [read the spec](/Tech/TechSpec?spec=5159)

 

 

 Transmits premium information to Medicare Advantage plans.
 

 

### 
 Outgoing 1095-B (Simple)
 [read the spec](/Tech/TechSpec?spec=5303)

 

 

 The 1095-B is a flat file for tax information.
 

 

### 
 Outgoing 1099-MISC
 [read the spec](/Tech/TechSpec?spec=5302)

 

 

 The 1099-MISC tax form is used to report miscellaneous income for Vendors from an AP Cycle processing.
 

 

### 
 Batch Eligibility Query (BEQ)
 [read the spec](/Tech/TechSpec?spec=5438)

 

 

 Outbound BEQ request and Incoming BEQ response. BEQ is a way for plans to submit batches of individuals for verification of various eligibilities.
 

 

### 
 Outbound Medicare Advantage and Prescription Drug System (MARx) files
 [read the spec](/Tech/TechSpec?spec=5306)

 

 

 File for reporting drug information between a health plan and CMS.
 

 

### 
 Tapestry Document Linker DMS Integration
 [read the spec](/Tech/TechSpec?spec=5310)

 

 

 We recommend using [the Hyperdrive Document Linker](https://open.epic.com/Prototype/Hyperdrive#TapestryDocumentLinkerDMSIntegration) instead of this technology. This VB integration enables users in an external document management system to launch the Tapestry Document Linker activity in an active Hyperspace session and pass necessary document information to link a document to records in Epic. Additionally the integration can allow for users in the DMS to create new claim and CRM records in Hyperspace with links to the desired document. 
 

 

### 
 Collections Extract and Import
 [read the spec](/Tech/TechSpec?spec=5429)

 

 

 Epic can generate a flat file extract to collections agencies containing information about charges assigned to the agency. Epic can also receive flat file imports with updates to those charges to support tracking of payments and changes to charges in Resolute.
 

 

### 
 SAML 2.0 Idp-initiated Single Sign-On (SSO)
 [read the spec](/Tech/TechSpec?spec=5187)

 

 

 Epic supports launching an external app with SAML 2.0. The SAML 2.0 Identity Provider initiated workflow initiates from Epic, playing the SAML role of Identity Provider. Implementation requires the exchange of an x509 certificate, which is used to sign the SAML claims. This process follows the OASIS SAML 2.0 specification. Epic recommends the use of [SMART on FHIR](../Interface/FHIR#AuthenticationandSingleSign-On(SSO)) over SAML if possible.
 

 

### 
 Single Sign-On (SSO) into MyChart

 

 

 
We moved the MyChart SSO specification from [open.epic.com](https://open.epic.com/) to [vendorservices.epic.com](https://vendorservices.epic.com/). This will give developers and our customers access to Epic guidance on preventing cybersecurity vulnerabilities. If you are interested in developing to the specification, please fill out an [interoperability request](https://userweb.epic.com/Forms/InteroperabilityRequest) for assistance.

 

 

### 
 Single Sign-On (SSO) into EpicCare Link
 [read the spec](/Tech/TechSpec?spec=5407)

 

 

 Other systems can provide SSO integration into Epic's web application, EpicCare Link, by passing user and optionally patient context.
 

 

### 
 Appointment Notifications
 [read the spec](/Tech/TechSpec?spec=5416)

 

 

 Interactive Voice Response systems can be used to deliver appointment reminders to patients prior to their visits, asking them to confirm. Once the appointment is confirmed, the IVR system sends this information back to the Epic EHR so clinic staff can estimate no-show probabilities. 
 

 

### 
 Recall Notifications
 [read the spec](/Tech/TechSpec?spec=5414)

 

 

 Interactive Voice Response systems can be used to remind patients to schedule appointments for upcoming recalls. Once the communication happens, the IVR system sends this information back to the Epic EHR to finish the documentation. 
 

 

### 
 Request Notifications
 [read the spec](/Tech/TechSpec?spec=5415)

 

 

 Interactive Voice Response systems can be used to remind patients to schedule appointments for upcoming appointment requests. Once the communication happens, the IVR system sends this information back to the Epic EHR to finish the documentation. 
 

 

### 
 Incoming Receipts
 [read the spec](/Tech/TechSpec?spec=5327)

 

 

 Receives receipts for messages sent to the VANS network in relation to the Medcom message sent. 
 

 

### 
 Outgoing Receipts
 [read the spec](/Tech/TechSpec?spec=5217)

 

 

 Sends positive or negative receipt messages for Medcom messages received from the VANS network using the Medcom XML/EDIFACT standard. 
 

 

### 
 eMediplan APIs

 

 

 These APIs enable queries into Epic for the full medication list for a patient and can generate a push notification when a user in Switzerland requests an eMediplan in Epic. An interface engine can use the notification to call into these APIs and standard FHIR APIs to gather the necessary information to request an eMediplan document from the HCI eMediplan system. This document can be filed into Epic with an [Incoming Scanned Document Link interface](/Interface/HL7v2#IncomingScannedDocumentLink) or shared with other healthcare organizations. The document includes a QR code that healthcare providers can use to retrieve the patient's medications from eMediplan. 
 

 

### 
 Incoming External Clinical Data
 [read the spec](/Tech/TechSpec?spec=5370)

 

 

 As organizations extend Epic to affiliated practices in their communities, there has been an increasing need to convert historical patient-level data from other vendors' systems into Epic. We recommend and very strongly prefer converting data using any of our other standards based integration options, such as from a CCDA. This is a limited import tool that allows organizations to load patient-level data from organizations that do not otherwise support standards-based data exchange.
 

 

### 
 Paid Claims Import
 [read the spec](/Tech/TechSpec?spec=9495)

 

 

 Paid claim data can be imported into Epic to support population health and care management workflows by reconciling the data with the rest of the comprehensive medical record. These formats are recommended when the data can be manipulated or the extract is flexible, to simplify the process of importing into Epic.
 

 

 [Current integrations include ](#)
 

 - Health Data Innovations

 - Milliman

 

 

 

### 
 EDManager
 [read the spec](/Tech/TechSpec?spec=5419)

 

 

 This set of APIs allow external applications that are running alongside Epic Hyperspace to programmatically take certain actions, such as logging in/out and launching activities. They also provide the ability to query Epic Hyperspace for information, as well as to be notified when key events occur. These APIs are commonly used for automating external-driven workflows, most notably logins. 
 

 

### 
 Desktop Generic Authentication
 [read the spec](/Tech/TechSpec?spec=5421)

 

 

 This interface allows external authentication software to implement authentication devices for use in Epic. The external authentication software can write installable devices that can be configured for use as devices to authenticate a user for login into Epic, to re-authenticate the user after login (for example, to sign off on medications), or to identify a patient (for example, to check into an appointment). 
 

 

### 
 Scan Acquisition
 [read the spec](/Tech/TechSpec?spec=5191)

 

 

 This COM integration enables users to seamlessly launch an external scan acquisition interface from Epic. Epic can pass the user's active context information, such as the patient, encounter, or order. 
 

 

### 
 Scan Viewing
 [read the spec](/Tech/TechSpec?spec=5190)

 

 

 This COM integration enables Epic to display an ActiveX scan viewing control in a modeless floating window. The user can interact with both the viewer and Epic, and Epic will manage closing the window if the user's patient context changes. 
 

 

### 
 EPS Document Retrieval Plugin
 [read the spec](/Tech/TechSpec?spec=5406)

 

 

 This .NET integration enables Epic print services (EPS) to query a document management system (DMS) for images or documents to insert into a print job. This is useful when you want a scan to be stored in your DMS, but want to include that scan in something you print. We recommend new implementations use the [EPS Document Retrieval Web Service](../Interface/WebServices#EPSDocumentRetrievalWebService) instead of this. 
 

 

### 
 SIEM Feed
 [read the spec](/Tech/TechSpec?spec=5188)

 

 

 Epic can feed certain security and privacy relevant events to a security information and event management (SIEM) system in near real-time. Messages coming from Epic can be formatted using Common Event Framework (CEF), Log Event Extended Format (LEEF), or RFC 5424 syslog. 
 

 

### 
 Epic Access Logging
 [read the spec](/Tech/TechSpec?spec=5417)

 

 

 The Epic Access Logging extract script extracts key Epic event logging data, including patient, user, and encounter information, from the Epic organization’s Clarity database into a pipe delimited flat file. 
 

 

### 
 Speech Recognition (Classic VB Client)
 [read the spec](/Tech/TechSpec?spec=5311)

 

 

 This set of APIs allow speech recognition systems to integrate with Epic Hyperspace (Classic VB Client). The speech recognition system can receive information about and make changes to the content of a control. 99% of customers are no longer using this client. For current specifications, see [Hyperdrive Speech Recognition](../Prototype/Hyperdrive#SpeechRecognition). 
 

 

### 
 Computable Exports

 

 

 
Epic software gives users the ability to export electronic health information in multiple formats depending on the use case. The following computable formats are available:

- [FHIR-formatted files](../Interface/FHIR#BulkDataAccess) for a subset of electronic health information in FHIR.
- [C-CDA-formatted XML documents](../Clinical/EHRtoEHR#ClinicalDocumentArchitecture(CDA)) for the subsets of electronic health information that can be expressed in C-CDA templates.
- EHI Tables for complete electronic health information, in a tab-separated value (TSV) file format native to Epic. Refer to [the EHI Tables technical specification](../EHITables) for detailed information about what’s included in this export by default. A copy of the specification might also be included in the Full EHI Export package you receive. The TSV files might also come packaged with non-computable files that are referenced in a patient record, such as media files and rich text format notes.

 

 

### 
 Welcome Accessibility for Vendors
 [read the spec](/Tech/TechSpec?spec=5153)

 

 

 Welcome is Epic’s application for patient self-service arrivals using kiosk enclosures or free-roaming tablets. This guide is intended for vendors supplying Welcome hardware and software solutions and provides an overview of some considerations associated with supporting an accessible patient workflow on those form factors
 

 

### 
 Welcome Hardware Guide For Vendors
 [read the spec](/Tech/TechSpec?spec=5757)

 

 

 Welcome is Epic’s application for patient self-service arrivals using kiosk enclosures or free-roaming tablets. This guide is intended for vendors supplying Welcome hardware solutions and provides an in-depth guide to the integration considerations soliciting organizations may have when requesting hardware.
 

 

### 
 PB Statement Form 807
 [read the spec](/Tech/TechSpec?spec=6101)

 

 

 Epic can generate a delimited plain text file of information that can be shared with a statement vendor. This file includes information about the patient and their Professional Billing balances in Epic. File format subject to change - fields and segments may be added or removed with future development. Programming should accept or ignore additional fields and segments when they occur gracefully. 
 

 

### 
 SBO Statement Form 808
 [read the spec](/Tech/TechSpec?spec=6440)

 

 

 Epic can generate a delimited plain text file of information that can be shared with a statement vendor. This file includes information about the patient and their Enterprise billing balances in Epic. File format subject to change - fields and segments may be added or removed with future development. Programming should accept or ignore additional fields and segments when they occur gracefully. 
 

 

### 
 Active Guidelines
 [read the spec](/Tech/TechSpec?spec=6476)

 

 

 The Active Guidelines (AGL) activity gives clinicians a convenient way to access web applications without leaving the Epic application. A web app can either be launched as the result of a user interacting with a response from a decision support web service or, depending upon health system configuration, by a user specifically choosing to navigate to the application from various activities or items. The web application is embedded within a sandboxed iframe in the Epic Hyperspace desktop application and can communicate with the EHR through cross-domain web messaging.
 

 

### 
 Kiosk Generic Authentication
 [read the spec](/Tech/TechSpec?spec=7517)

 

 

 Allows external authentication software to implement authentication devices for use in Epic’s self-arrival kiosk software. The external authentication software can write installable devices that can be configured to identify a patient or to enroll a patient for future identifications.
 

 

### 
 OpenID Connect
 [read the spec](/Tech/TechSpec?spec=7988)

 

 

 Epic’s Hyperspace application now supports the OpenID Connect (OIDC) authorization code flow as a means of authenticating users for logging in to Hyperspace as well as authentication within Hyperspace workflows.
 

 

### 
 Translation of Patient-Facing Content
 [read the spec](/Tech/TechSpec?spec=8706)

 

 

 Outlines the file format expectations for translation of patient-facing content which can show up in MyChart and other areas of our patient-facing software. Not all workflows that are patient-facing are currently included in this file format.
 

 

### 
 Care Gaps Import
 [read the spec](/Tech/TechSpec?spec=8737)

 

 

 Care gaps data can be imported into Epic to support population health and care management workflows. Imported quality measure outcomes can be used to drive patient outreach, enhance during-encounter decision support, and summarize measure performance for your patient populations. This format is recommended when the data can be manipulated, or the extract is flexible, to simplify the process of importing into Epic.
 

 

### 
 Bluetooth® Generic Health Sensor Device Integration with MyChart
 [read the spec](/Tech/TechSpec?spec=9421)

 

 

 The Generic Health Sensor (GHS) Profile is a Bluetooth® standard for communicating health-related observations from personal health devices. This specification describes how devices that support the GHS Profile can integrate with MyChart to file patient data.
 

 

### 
 Risk Adjustment Import
 [read the spec](/Tech/TechSpec?spec=9494)

 

 

 Risk Adjustment data can be imported into Epic to support population health and care management workflows by providing condition categories and suspected conditions. This format is recommended when the data can be manipulated or the extract is flexible, to simplify the process of importing into Epic.
 

 

### 
 Supplemental Data Import
 [read the spec](/Tech/TechSpec?spec=9493)

 

 

 Supplemental data can be imported into Epic to support population health and care management workflows by providing additional clinical data to include in HEDIS™ quality reporting. This format is recommended when the data can be manipulated or the extract is flexible, to simplify the process of importing into Epic.
 

 

### 
 Verified Safety Checks
 [read the spec](/Tech/TechSpec?spec=9773)

 

 

 Documentation to assist BLE wristband vendors in supporting Epic Verified Safety Checks for inpatient behavioral health units.
 

 

### 
 Bluetooth Wayfinding
 [read the spec](/Tech/TechSpec?spec=9921)

 

 

 Enables a web-based application embedded within MyChart Mobile to request and receive Bluetooth signals, data, and beacon information from the containing app to support indoor blue-dot wayfinding experiences.
 

 

### 
 Prospective Patient Import
 [read the spec](/Tech/TechSpec?spec=10311)

 

 

 
Prospective Patient data can be imported into or exported out of Epic to support maintaining a unified view of prospective and current patients, enabling more effective outreach, patient matching, and reporting. This is a spreadsheet-based import/export tool that allows organizations to load prospective patient data from third-party systems.