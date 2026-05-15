# open.epic :: Explore By Interface Type

> Source: https://open.epic.com/Interface/NCPDP

---

# 
 By Interface Type

 

 

 
 

 

 
 

 
 

 
 
 

## NCPDP

 
The National Council for Prescription Drug Programs develops standards related to the real-time exchange of information about pharmacy services. You can learn more from [NCPDP](http://www.ncpdp.org). 

### 
 Outgoing Medication History for Populations Request and Response
 [read the spec](/Tech/TechSpec?spec=5256)

 

 

 Performs queries to get the medication dispense history for registries of patients to assist in tracking patients' medication adherence.
 

 

 [Current integrations include ](#)
 

 - SURESCRIPTS

 

 

 

### 
 Incoming External Paid Pharmacy Claims Interface
 [read the spec](/Tech/TechSpec?spec=5367)

 

 

 Loads external paid pharmacy claims messages into Epic Payer Platform or Tapestry, Epic's managed care application, using flag files in the NCPDP Post-Adjudication format.
 

 

 [Current integrations include ](#)
 

 - HUMANA

 - Navitus

 

 

 

### 
 Outgoing Prescription Prior Authorization Request and Reponse
 [read the spec](/Tech/TechSpec?spec=5224)

 

 

 Supports message events necessary for a prescribing provider to request an electronic prior authorization for a medication order and receive either approval or denial from a Pharmacy Benefits Manager, and supports messages to cancel requests. These interfaces for electronic prior authorization support a subset of the NCPDP standard.
 

 

 [Current integrations include ](#)
 

 - Arrive Health

 - CenterX

 - COVERMYMEDS

 - SURESCRIPTS

 

 

 

### 
 Outgoing Prescription Information from Prescriber to Pharmacies
 [read the spec](/Tech/TechSpec?spec=5254)

 

 

 Used for e-prescribing when the organization is the prescriber. Uses NCPDP SCRIPT 10.6,2017071,2023011 to send new prescriptions, renewal responses, cancel requests, and change responses with an external pharmacy. Previously known as Outgong Medication Orders to Retail Pharmacies.
 

 

 [Current integrations include ](#)
 

 - Canada Health Infoway

 - CIPHERHEALTH, INC.

 - COVERMYMEDS

 - CPS

 - DRFIRST, INC.

 - InstyMeds

 - McCreadie Group

 - McKesson

 - Rx Care Assurance

 - ScriptPro

 - SURESCRIPTS

 

 

 

### 
 Incoming Prescription Information from Pharmacies to Prescriber
 [read the spec](/Tech/TechSpec?spec=5254)

 

 

 Uses NCPDP SCRIPT 10.6 or 2017071 to receive renewal requests, cancel responses, and change requests from external pharmacies.
 

 

 [Current integrations include ](#)
 

 - Canada Health Infoway

 - CIPHERHEALTH, INC.

 - COVERMYMEDS

 - DRFIRST, INC.

 - InstyMeds

 - McCreadie Group

 - McKesson

 - Rx Care Assurance

 - ScriptPro

 - SURESCRIPTS

 

 

 

### 
 Outgoing Medication Dispense History Query
 [read the spec](/Tech/TechSpec?spec=8009)

 

 

 E-prescribing functionality when Epic is the prescriber. Uses NCPDP SCRIPT 10.6, 2017071,2023011 to receive medication history information from external sources.
 

 

 [Current integrations include ](#)
 

 - BAMBOO HEALTH

 - California Department of Justice

 - Chesapeake Regional Information System for Our Patients

 - CyncHealth

 - DRFIRST, INC.

 - Illinois Office of Health Information Technology

 - LOGICOY INC.

 - Nebraska Health Information Initiative

 - ONEHEALTHPORT

 - Rhode Island - Public Health Agencies

 - RxCheck

 - SURESCRIPTS

 - Washington - Public Health Agencies

 

 

 

### 
 Incoming Prescription Information from Prescribers to Pharmacy
 [read the spec](/Tech/TechSpec?spec=5352)

 

 

 Uses NCPDP SCRIPT to receive new prescriptions, renewal responses, and cancel requests from external providers into Epic's ambulatory pharmacy product.
 

 

 [Current integrations include ](#)
 

 - AMERISOURCE BERGEN

 - SURESCRIPTS

 

 

 

### 
 Outgoing Prescription Information from Pharmacy to Prescribers
 [read the spec](/Tech/TechSpec?spec=5352)

 

 

 E-prescribing functionality when Epic is the Pharmacy. Uses NCPDP SCRIPT 10.6,2017071,2023011 to send renewal requests and cancel responses to external providers from Willow Ambulatory.
 

 

 [Current integrations include ](#)
 

 - SURESCRIPTS

 

 

 

### 
 Outgoing Pharmacy Update from Willow Ambulatory to E-Prescribing System Interface
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20Pharmacy%20Update%20Query%20Technical%20Specification.zip)

 

 

 Sends messages to an e-prescribing system to change e-prescribing related settings of an ambulatory pharmacy, such as service levels or operating mode.
 

 

 [Current integrations include ](#)
 

 - SURESCRIPTS

 

 

 

### 
 Outgoing Provider Download to E-Prescribing System Interface
 [read the spec](/Tech/TechSpec?spec=staged%2FProvider%20Query%20Technical%20Specification.zip)

 

 

 Queries an external e-prescribing system for current and updated e-prescribing provider data.
 

 

 [Current integrations include ](#)
 

 - Cardinal Health WaveMark

 - SURESCRIPTS

 

 

 

### 
 Outgoing Organization Download to E-Prescribing System
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20Organization%20Query%20Interface%20Technical%20Specifications.zip)

 

 

 Queries an external e-prescribing system for current and updated e-prescribing pharmacy data.
 

 

 [Current integrations include ](#)
 

 - SURESCRIPTS

 

 

 

### 
 Outgoing Provider Update to E-Prescribing System Interface
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20Provider%20Update%20Query%20Interface%20Technical%20Specification.zip)

 

 

 Sends messages to an e-prescribing system when changes to e-prescribing related settings are made to provider's record, such as service levels or contact information.
 

 

 [Current integrations include ](#)
 

 - SURESCRIPTS

 

 

 

### 
 Outgoing Formulary Query to e-Prescribing System
 [read the spec](/Tech/TechSpec?spec=staged%5COutgoing%20Medication%20Formulary%20Query%20to%20E-Prescribing%20System%20Technical%20Specification.pdf)

 

 

 Downloads NCPDP Formulary & Benefit files from an external source to provide formulary information to the provider during order entry.
 

 

 [Current integrations include ](#)
 

 - SURESCRIPTS

 

 

 

### 
 Outgoing Pharmacy Benefit Claims Adjudication Query
 [read the spec](/Tech/TechSpec?spec=5229)

 

 

 This real-time interface is used to determine what portion of a prescription's cost will be paid by the patient's insurance so that the patient can be charged appropriately for the prescription fill. Claim Adjudication uses NCPDP Telecommunication version D.0.
 

 

 [Current integrations include ](#)
 

 - AMERISOURCE BERGEN

 - Cardinal Health WaveMark

 - CenterX

 - Change Healthcare

 - COVERMYMEDS

 - Fred IT Group

 - McKesson

 - Morris & Dickson

 - Optum

 - OptumRx (Catamaran)

 - Relay Health

 - Rx Linc

 - SURESCRIPTS