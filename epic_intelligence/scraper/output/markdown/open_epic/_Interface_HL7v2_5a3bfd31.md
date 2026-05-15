# open.epic :: Explore By Interface Type

> Source: https://open.epic.com/Interface/HL7v2

---

# 
 By Interface Type

 

 

 
 

 

 
 

 
 

 
 
 

## HL7v2

 
Health Level 7 standardizes data interchanges within and across organizations. It's one of the most widely implemented standards for health-related data. You can learn more about this standard from [HL7](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=149).

### 
 Incoming Materials Management
 [read the spec](/Tech/TechSpec?spec=5357)

 

 

 Used to automate synchronization of supply definitions from an external materials management system. The interface can add or modify properties of these items such as the supplier they are purchased from and the physical location where they are stored.
 

 

 [Current integrations include ](#)
 

 - Afas

 - Allscripts

 - Aperek

 - ARC Healthcare Technologies

 - Avanade

 - Axians

 - BD

 - Caduceus

 - Cardinal Health WaveMark

 - Censis

 - DUPLICATEIatric Systems

 - EHS

 - Elcom

 - GENESIS

 - Global Healthcare Exchange

 - Healthstream

 - IBM

 - Infor Global Solutions

 - Inventory Optimization Solutions (IOS)

 - Logibec

 - McKesson

 - MediSolution

 - Meditech

 - Microsoft

 - Multiview

 - Novell

 - O&M Solutions

 - Omnicell

 - ORACLE

 - Paragon

 - PREMIER, INC.

 - Procurement Partners

 - Prospitalia

 - Sage

 - SAP

 - Tecsys

 - TGX Medical Systems

 - Unit4

 - Workday

 - Xperthis

 - Zorgi

 

 

 

### 
 Incoming External Encounters
 [read the spec](/Tech/TechSpec?spec=5369)

 

 

 Receives data about encounters that happen at an outside entity. These encounters can then be used by care managers to follow up with the patient or by Epic population health tools for analytics. This interface is for use with Payer Platform or Healthy Planet.
 

 

 [Current integrations include ](#)
 

 - Allscripts

 - Arkansas - Public Health Agencies

 - ATHENAHEALTH, INC.

 - AUDACIOUS INQUIRY

 - Austin Radiology Association

 - BAMBOO HEALTH

 - Blue Cross/Blue Shield

 - Bronx Regional Health Information Organization

 - C3HIE

 - Care Continuity

 - Carithers

 - Chesapeake Regional Information System for Our Patients

 - CliniSync

 - Collective Medical Technologies

 - CORHIO

 - CPSI

 - Delaware Health Information Network

 - Elevance

 - EXPERIAN HEALTH, INC.

 - Hawaii Health Information Exchange

 - Health Current

 - HealtheConnections

 - HealthShare Exchange

 - Highmark

 - Horizon

 - Houston - Public Health Agencies

 - HUMANA

 - IBM

 - Indiana - Public Health Agencies

 - InterSystems

 - LANES

 - Manifest Medex

 - Michigan - Public Health Agencies

 - Mississippi - Public Health Agencies

 - NEFEDA

 - New Jersey - Public Health Agencies

 - New Jersey Innovation Institute

 - New York City - Public Health Agencies

 - Northwell Health

 - Optum

 - PCC

 - PointClickCare

 - South Dakota - Public Health Agencies

 - Tennessee - Public Health Agencies

 

 

 

### 
 Outgoing Fills to Automated Fill System from Willow Ambulatory
 [read the spec](/Tech/TechSpec?spec=5274)

 

 

 Transmits verified pharmacy fills to automated prescription fill systems.
 

 

 [Current integrations include ](#)
 

 - AccuMed

 - ARX

 - ARxIUM

 - Asembia

 - Avery Weigh-Tronix

 - BD

 - CPS

 - Dispill

 - iA

 - inHealth

 - Innovation

 - Kirby Lester

 - McKesson

 - Medifriend

 - Omnicell

 - Parata

 - RxSafe

 - Saudi Arabia Council of Health Insurance

 - ScriptPro

 - SURESCRIPTS

 - Therigy

 

 

 

### 
 Incoming Fill Status Updates and Load/Unload from Automated Fill System
 [read the spec](/Tech/TechSpec?spec=5365)

 

 

 Updates the status of the prescription fill in Willow Ambulatory Pharmacy when an automated prescription fill system fills, dispenses, or cancels a prescription.
 

 

 [Current integrations include ](#)
 

 - ARxIUM

 - Avery Weigh-Tronix

 - BD

 - CPS

 - iA

 - inHealth

 - Innovation

 - Kirby Lester

 - McKesson

 - Medifriend

 - Omnicell

 - Parata

 - RxSafe

 - ScriptPro

 - SURESCRIPTS

 

 

 

### 
 Outgoing Patient Waiting Time from Patient Administration System
 [read the spec](/Tech/TechSpec?spec=5235)

 

 

 Organizations in Ontario can collect information in diagnostic imaging and surgical workflows to report to Cancer Care Ontario's Wait Time Information System (WTIS) requirements.
 

 

 [Current integrations include ](#)
 

 - CognisantMD

 - Ontario Ministry of Health

 

 

 

### 
 Outgoing Inventory Depletion
 [read the spec](/Tech/TechSpec?spec=5262)

 

 

 Informs an external materials management system of supplies that have been using during a procedure. It indicates which supply was used, from where the user picked the supply, and the number by which the external system should decrement the balance of the supply. These messages are triggered from within Epic's surgical, radiology, and cardiology software applications.
 

 

 [Current integrations include ](#)
 

 - AccuMed

 - Afas

 - Allscripts

 - Aperek

 - ARC Healthcare Technologies

 - Axians

 - BD

 - Caduceus

 - Cardinal Health WaveMark

 - Casechek

 - Dove Tree Canyon Software

 - EHS

 - Elcom

 - GE

 - Harris

 - Infor Global Solutions

 - Inventory Optimization Solutions (IOS)

 - Kardex Remstar

 - Logibec

 - LPiT Solutions

 - LUMEDX

 - McKesson

 - Meditech

 - Modernizing Medicine

 - O&M Solutions

 - Omnicell

 - ORACLE

 - PAR Excellence

 - PREMIER, INC.

 - ReadySet Surgical

 - SAP

 - Securitas Healthcare

 - Tecsys

 - Unit4

 - Workday

 

 

 

### 
 Outgoing Blood Transfusion Status Notification
 [read the spec](/Tech/TechSpec?spec=5292)

 

 

 Sends transfusion notifications to external Blood Bank systems so that blood banks can update their records when a given blood unit is transfused. To use this interface, an organization must document the unit number and product code for blood transfusions using the Blood Product Administration Module.
 

 

 [Current integrations include ](#)
 

 - B. Braun

 - Bódegro

 - Cerner

 - Clinisys

 - EGIS

 - Haemonetics

 - IODINE SOFTWARE, LLC

 - Magentus

 - MyLab

 - Philips

 - RISKLD

 - Savant

 - SCC Soft Computer

 - Sussex Biologicals

 - SYMPLR

 - Synedra

 - VigiLanz

 - WellSky

 

 

 

### 
 Incoming External Outpatient Medication Orders Interface
 [read the spec](/Tech/TechSpec?spec=5368)

 

 

 Receives outpatient medication orders from outside sources such as other EHR systems. They are not filed directly to the chart, but instead are filed as a medication waiting to be reconciled in the Reconcile Outside Information activity. This interface is generally used for conversion purposes, and is recommended in place of the Incoming Medication Orders to EpicCare Ambulatory interface.
 

 

 [Current integrations include ](#)
 

 - Zorgdoc

 

 

 

### 
 Incoming Asynchronous Acknowledgement
 [read the spec](/Tech/TechSpec?spec=5383)

 

 

 Receives asynchronous application acknowledgements in response to any outgoing HL7v2 message sent using Bridges, Epic's core messaging infrastructure.
 

 

 [Current integrations include ](#)
 

 - Advanced

 - Alabama - Public Health Agencies

 - Allscripts

 - American Well

 - Arizona - Public Health Agencies

 - California - Public Health Agencies

 - CBORD

 - Clevermed

 - Corepoint Health

 - eMDs

 - Enclara

 - HealthLink

 - Hospital Diagnostic Imaging Repository Services

 - IBM

 - Infor Global Solutions

 - Iron Bridge

 - LifeLabs

 - Magentus

 - Minnesota - Public Health Agencies

 - National Health Service

 - New York - Public Health Agencies

 - NextGate Solutions

 - NextGen

 - NHN

 - Ohio - Public Health Agencies

 - ONEHEALTHPORT

 - Ontario Ministry of Health

 - Orion Health

 - RVC

 - SAP

 - SCC Soft Computer

 - Sectra

 - Siemens

 - Singapore Ministry of Health Holdings

 - South Carolina - Public Health Agencies

 - STChealth

 - Texas - Public Health Agencies

 - Varian Medical Systems

 - Washington - Public Health Agencies

 - Wellbeing Software

 - Zorgi

 

 

 

### 
 Outgoing Documentation
 [read the spec](/Tech/TechSpec?spec=5279)

 

 

 Notifies external systems of documentation recorded in Epic. Sends MDM messages with notes and transcriptions as they are saved and modified, and can send a document summary upon close of an encounter in EpicCare Ambulatory EHR. Documents are sent in either RTF or PDF format.
 

 

 [Current integrations include ](#)
 

 - 3M

 - 4MEDICA INC.

 - AccuMed

 - AlertMD

 - Allscripts

 - AmeriHealth Caritas

 - AMGA

 - Apollo

 - APS

 - Arizona - Public Health Agencies

 - Arkansas - Public Health Agencies

 - Arkansas Office of Health Information Technology

 - Artifact Health

 - ATHENAHEALTH, INC.

 - Atlas

 - BREG

 - Bronx Regional Health Information Organization

 - C/NET Solutions

 - California Information Exchange

 - Caradigm

 - Care Continuity

 - Carecloud

 - CAREDX INC.

 - CAREEVOLUTION

 - CareSource

 - Carolina eHealth Alliance

 - Cerner

 - Chesapeake Regional Information System for Our Patients

 - CliniSync

 - CliniWorks

 - CodeRyte

 - CognisantMD

 - Collective Medical Technologies

 - COMMURE

 - Connecticut - Public Health Agencies

 - CORHIO

 - CyncHealth

 - Deep Lens

 - Delaware Health Information Network

 - Denver County (CO) - Public Health Agencies

 - Dinmar

 - Dolbey

 - Dubai Government Services

 - E.Novation

 - eClinicalWorks

 - E-Health

 - Elekta

 - ELLKAY, LLC.

 - eMDs

 - Ensemble Health Partners

 - Envision

 - Envision Radiology

 - Equum Medical

 - ESO

 - EVIDENCECARE, LLC

 - FinThrive

 - ForCare

 - GE

 - GeniusDoc

 - GMT

 - GOHEALTH URGENT CARE

 - GovTech

 - Great Lakes Health Information Exchange

 - Harris

 - Hawaii Health Information Exchange

 - HEALTH CATALYST, INC.

 - HealthBridge

 - HealtheCNY

 - HealtheConnections

 - HEALTHeLINK

 - HealthHIE Nevada

 - HealthInfoNet

 - HealthLink

 - Healthmap Solutions

 - HealthPro Medical Billing

 - Hicuity Health

 - HUMANA

 - Hyland

 - IBM

 - iD

 - Idaho Health Data Exchange

 - Indiana - Public Health Agencies

 - Infinity Healthcare

 - Infor Global Solutions

 - InterSystems

 - IODINE SOFTWARE, LLC

 - Iowa - Public Health Agencies

 - IQMax

 - Kansas Health Information Network

 - KONZA

 - Lexmark Enterprise Software

 - LogixHealth

 - Lynx Medical Systems

 - M*Modal

 - Manifest Medex

 - MCG Diagnostics

 - McKesson

 - MDTECH

 - Med2020 Health Care Software Inc.

 - MedData

 - MediMobile

 - MediServe

 - Medisys Innovation

 - Meditech

 - MedPlus

 - Medtronic

 - Michigan - Public Health Agencies

 - Michigan Health Connect

 - Microsoft

 - MobileMD

 - Modernizing Medicine

 - Morrisey

 - Mpirik

 - MSN

 - MYHEALTH ACCESS NETWORK

 - NABIDH

 - National Institutes of Health

 - naviHealth

 - Nebraska Health Information Initiative

 - New York - Public Health Agencies

 - New York City - Public Health Agencies

 - NextGen

 - NHACNY

 - Nictiz

 - NUANCE COMMUNICATIONS INC.

 - Occupational Health Research

 - Ocuco

 - ONEHEALTHPORT

 - Ontario Ministry of Health

 - Ontario Patient Data Reporting

 - OntarioMD

 - Optum

 - Orion Health

 - Pascal Metrics

 - Pediatrix

 - PediNotes

 - Philips

 - PHREESIA, INC.

 - Picis

 - PLATOCODE

 - PREMIER, INC.

 - ProVation Medical

 - PulmOne

 - Q-Centrix

 - Quality Health Network (QHN)

 - Quovadx

 - R1 RCM

 - Radiology Partners

 - RecordsOne

 - REDOX

 - Relay Health

 - ResMed

 - Rochester Regional Health Information Organization

 - San Diego - Public Health Agencies

 - SapphireHealth

 - Sentri7

 - Siemens

 - Signify Health

 - SMARTERDX, INC

 - Softek Solutions, Inc.

 - SoftMed

 - SoftScript, Inc.

 - Solventum

 - Sound Physicians

 - South Carolina - Public Health Agencies

 - South Dakota Department of Health

 - Spheris 

 - SRS

 - Stanford School of Medicine

 - SYMPLR

 - Synedra

 - TeamHealth

 - TheraDoc

 - TIBCO

 - Truven Health

 - Utah - Public Health Agencies

 - Varian Medical Systems

 - Vermont Information Technology Leaders

 - VigiLanz

 - Virginia - Public Health Agencies

 - VITAL

 - Vituity

 - Waseel

 - WellSky

 - Wisconsin - Public Health Agencies

 - WOLTERS KLUWER

 - XSOLIS

 - Zotec Partners

 

 

 

### 
 Outgoing Provider Communications Interface
 [read the spec](/Tech/TechSpec?spec=5221)

 

 

 Notifies external systems of provider communications written in the Communication Management activity in Epic. The interface sends letter attachments as PDF documents to recipients.
 

 

 [Current integrations include ](#)
 

 - Advanced

 - Amisys Synertech Inc

 - Caresharing

 - Cerner

 - Clevermed

 - E.Novation

 - E-Health

 - eMDs

 - HealthLink

 - iD

 - Iuvo

 - Medicus

 - Mela Solutions

 - National Health Service

 - NHN

 - Norwegian Institute of Public Health

 - Ontario Ministry of Health

 - Ontario Patient Data Reporting

 - PharmOutcomes

 - Synedra

 

 

 

### 
 Outgoing Medication Verification Queue Update Notification from Willow Inpatient Interface
 [read the spec](/Tech/TechSpec?spec=5250)

 

 

 Informs external systems when an inpatient medication order is added or removed from the pharmacist verification queue.
 

 

 [Current integrations include ](#)
 

 - CarepathRx

 - CPS

 - SURESCRIPTS

 - Therigy

 

 

 

### 
 Outgoing External Encounters
 [read the spec](/Tech/TechSpec?spec=5276)

 

 

 Sends HL7v2 ADT messages using data filed as external encounters in Received Documents records and using message data filed on the Incoming External Encounters interface. This is intended for use with Payer Platform.
 

 

 [Current integrations include ](#)
 

 - CVS Pharmacy

 - InterSystems

 

 

 

### 
 Incoming Provider Communications Interface
 [read the spec](/Tech/TechSpec?spec=5331)

 

 

 Notifies Epic users of provider communications written in other systems. Communications can have attached letters or documents and are routed to the recipient (Provider, Department, etc) based on preferences (In Basket, Fax, Mail, etc) the same as if the communication was written in Epic and routed with the Communication Management activity. 
 

 

 [Current integrations include ](#)
 

 - DDX Dental

 - Eon

 - NAV

 - NHN

 - NUANCE COMMUNICATIONS INC.

 - SAP

 

 

 

### 
 Outgoing Asynchronous Acknowledgement Interface
 [read the spec](/Tech/TechSpec?spec=5295)

 

 

 Sends asynchronous application acknowledgements in response to any incoming HL7v2 message received in Bridges, Epic's core messaging infrastructure.
 

 

 [Current integrations include ](#)
 

 - eConsult

 - MULESOFT, INC.

 - NHN

 - SALESFORCE

 - Singapore Ministry of Health Holdings

 - SUKI AI, INC.

 

 

 

### 
 Incoming External Appointments Interface
 [read the spec](/Tech/TechSpec?spec=5371)

 

 

 Receives HL7v2 scheduling messages about appointments that happen at an outside entity. These encounters can then be used by care managers to follow up with the patient or by Epic population health tools for analytics. This interface is different from the Incoming Appointment Scheduling interface in that it does not make appointments that can be acted upon (checked in, canceled, etc) or accessed from the clinical schedule to be charted in.
 

 

 [Current integrations include ](#)
 

 - ATHENAHEALTH, INC.

 - eClinicalWorks

 

 

 

### 
 Outgoing External Appointments Interface
 [read the spec](/Tech/TechSpec?spec=6436)

 

 

 Sends HL7v2 scheduling messages using data filed as external appointments and using message data filed on the Incoming External Appointments interface. This is intended for use with Payer Platform.
 

 

### 
 Incoming Provider Information
 [read the spec](/Tech/TechSpec?spec=5330)

 

 

 Receives messages that can create, update, inactivate, or delete records in the provider master file, typically from an external credentialing system. While this interface can build the shell of a provider record, for example, address and contact information, this interface can't completely automate the addition of new providers to an organization because Epic has many settings and features that are built by association to provider records. These settings cannot by nature be controlled by an external system. There are also use cases requiring provider records to be built that will not be tracked in a credentialing system.
 

 

 [Current integrations include ](#)
 

 - American Well

 - Cerner

 - Enclara

 - Health Technology Solutions Victoria

 - Healthstream

 - HealthStream

 - IBM

 - Infor Global Solutions

 - Initiate

 - McKesson

 - MD-Staff

 - Medtronic

 - Morrisey

 - Navina

 - NetIQ

 - NextGen

 - Novell

 - Ontario Ministry of Health

 - ORACLE

 - Orion Health

 - SailPoint

 - SAP

 - Spheris 

 - SURESCRIPTS

 - SYMPLR

 - Tenet Healthcare Corporation

 - TriZetto Provider Solutions, a Cognizant Company

 - Veeva Systems

 - Vistar Technologies

 - Workday

 

 

 

### 
 Incoming Medication Stock Reservation to Willow Inventory
 [read the spec](/Tech/TechSpec?spec=5778)

 

 

 Reserves medication stock for use at a specific inventory location.
 

 

 [Current integrations include ](#)
 

 - CompuGroup Medical

 

 

 

### 
 Outgoing Provider Information
 [read the spec](/Tech/TechSpec?spec=5220)

 

 

 Sends provider information to an external system whenever a provider record is created, updated, inactivated, or deleted.
 

 

 [Current integrations include ](#)
 

 - 3M

 - AccuMed

 - Ace

 - Agfa

 - Allscripts

 - Ambra Health

 - ANDOR HEALTH

 - AQuity Solutions

 - AS Software

 - Axel Health

 - BD

 - Bódegro

 - Cardea Technology

 - Care Continuity

 - CAREDX INC.

 - Carestream Health

 - CentralLogic

 - Cerner

 - Clinisys

 - CompuGroup Medical

 - Conifer Health Solutions

 - CoPath

 - Corepoint Health

 - CPSI

 - DELIVERHEALTH

 - Deutsche Telekom

 - Dolbey

 - EDCO

 - Efertility

 - Elekta

 - EMC2

 - EXPERIAN HEALTH, INC.

 - Extract Systems

 - Fibroblast

 - GE

 - Haemonetics

 - HEALTHeLINK

 - Horizon

 - Hyland

 - IBM

 - INFINITT NORTH AMERICA

 - Initiate

 - InterSystems

 - Lifelines

 - LifePoint Health

 - LUMEDX

 - LVM Systems

 - M*Modal

 - MagView

 - Mammography Reporting System

 - McKesson

 - MD-Staff

 - Mediconsult

 - Meditech

 - MedPlus

 - Microsoft

 - MobileMD

 - Modernizing Medicine

 - Morrisey

 - NewCura

 - NextGate Solutions

 - NextGen

 - Northwell Health

 - NUANCE COMMUNICATIONS INC.

 - Omnicell

 - Optum

 - Parallon Business Solutions

 - PenRad

 - Pentax

 - Philips

 - Primordial Designs

 - ProVation Medical

 - Roosterplatform

 - RVC

 - SALESFORCE

 - SCC Soft Computer

 - Sectra

 - Siemens

 - SolCom

 - Solventum

 - Spacelabs

 - SYMPLR

 - Sysmex Corporation

 - Taylor Healthcare

 - Transcend

 - T-System

 - Varian Medical Systems

 - VIR

 - Vistar Technologies

 - Vynca

 - Vyne Medical

 - WellSky

 - Yenlo

 

 

 

### 
 Outgoing Device Association Interface
 [read the spec](/Tech/TechSpec?spec=10257)

 

 

 IHE PCD Profile standard to associate device record to patient.
 

 

### 
 Incoming Drug Supply Receipt to Willow Inventory
 [read the spec](/Tech/TechSpec?spec=6420)

 

 

 Files drug supply items on stock that are received and invoiced on a purchase order in central pharamcy management.
 

 

### 
 Outgoing Birth Registry Reporting - Canada

 

 

 Sends messages to the BORN Birth Registry Ontario.
 

 

 [Current integrations include ](#)
 

 - BORN

 - Ontario Ministry of Health

 

 

 

### 
 Incoming Financial Transactions
 [read the spec](/Tech/TechSpec?spec=5364)

 

 

 Receives financial transactions. It can receive charge and credit transactions for hospital accounts for Epic's Hospital Billing application, and post or void charges on guarantor accounts for Epic's Professional Billing application. These charges are subject to charge entry checks.
 

 

 [Current integrations include ](#)
 

 - 3M

 - Abbott Diagnostics

 - Accuhealth

 - ADP AdvancedMD

 - Agfa

 - AGILITI

 - AlertMD

 - Allscripts

 - Ameripath

 - AMERISOURCE BERGEN

 - AneScan

 - Aperek

 - Apollo

 - Apotti

 - APS

 - Arintra

 - ARUP Laboratories

 - AS Software

 - Ascend Clinical

 - Askesis

 - Astraia

 - Avatar Solutions

 - Avinty

 - BD

 - Bódegro

 - BREG

 - BRIGHT.MD

 - Brightree

 - BUDDI.AI

 - Byram Healthcare

 - Cadence

 - Caduceus

 - Cadwell

 - Cardiac Science

 - Cardinal Health WaveMark

 - CareLogistics

 - CARESIMPLE INC.

 - Carestream Health

 - Cedaron

 - CellNetix

 - Cerner

 - Change Healthcare

 - Chartspan

 - Clinical Labs of Hawaii (CLH)

 - Clinical Science System

 - Clinisys

 - ClinLab

 - CODAMETRIX

 - CodeRyte

 - COMMURE

 - CompuGroup Medical

 - Computer Trust Corporation

 - Computers Unlimited

 - Conexsys

 - Consensus Medical Systems

 - CoPath

 - Cortex Medical Management Systems

 - Craneware

 - Cybernius Medical Ltd.

 - Delta

 - Dentrix

 - Deutsche Telekom

 - Diagnostic Lab Services, Inc.

 - Diasoft

 - Digisonics

 - eClinicalWorks

 - Eclipsys

 - Edelberg

 - Efertility

 - Electronic

 - Elekta

 - ENDOSOFT LLC

 - Ensemble Health Partners

 - Exan Academic

 - EXYM

 - FATHOM, INC.

 - Finalist Noord Nederland C.V.

 - FinThrive

 - Flatiron

 - Flexsys

 - Foundation Systems Inc.

 - Fresenius Medical Care

 - Fujifilm

 - Fysicon

 - GE

 - GENEVA HEALTH SOLUTIONS

 - Genial Genetics

 - GeniusDoc

 - Gottlieb

 - Greenway Health

 - Haemonetics

 - HEALOGICS, INC.

 - HealthSnap

 - Healthstream

 - Helix

 - Hillrom

 - HLA Data Systems LLC

 - Horizon

 - Hyland

 - IBM

 - iMDsoft

 - Infian

 - Infor Global Solutions

 - Infotrom

 - INGENIOUS MED

 - INNOVACCER INC.

 - InteGreat

 - INTELLICURE, INC.

 - IntelliDose

 - IntrinsiQ Specialty Solutions

 - ION Solutions

 - iRCODER.COM

 - iRhythm

 - IRIS (Intelligent Retinal Imaging Systems)

 - Itemedical

 - ITxM

 - Kodak

 - LifePoint Health

 - Lighthouse Lab Services

 - LigoLab

 - Locus Solutions

 - LogixHealth

 - LPiT Solutions

 - LUMEDX

 - Lynx Medical Systems

 - Macro Helix

 - McKesson

 - MD REVOLUTION, INC.

 - MedAptus

 - MedData

 - MedInformatix

 - MediServe

 - Meditech

 - MedKoder

 - Medline

 - Medstreaming

 - Medtronic

 - Merge Healthcare

 - Metropolitan Medical Laboratories

 - Modernizing Medicine

 - Morgan Scientific

 - Mortara

 - Multidata

 - MURJ, INC.

 - NDCHealth

 - NET HEALTH SYSTEMS, INC.

 - Netalytics

 - Netsmart

 - Netsoft, Inc.

 - NextGen

 - Nexus

 - NINETY ONE

 - NovaRad

 - NovoPath

 - NUANCE COMMUNICATIONS INC.

 - Nym

 - O&M Solutions

 - Occupational Health Research

 - Ocuco

 - Omda

 - Omnicell

 - OncoChart

 - Optum

 - Orb Health

 - Orchard Software

 - Össur

 - PACEMATE, LLC

 - PAR Excellence

 - PathGroup

 - PathView Systems

 - PenRad

 - Philips

 - Picis

 - pMDsoft, Inc.

 - Point and Click Solutions

 - PointClickCare

 - Portavita

 - PREMIER, INC.

 - Press Ganey

 - ProSolv CardioVascular

 - ProVation Medical

 - Psyche

 - Puritan Bennett

 - QS/1

 - QSI

 - QuadraMed

 - QUEST DIAGNOSTICS

 - RADNET

 - RamSoft

 - Recora

 - REDOX

 - Regional Medical Laboratory

 - Rehab Documentation Company, Inc.

 - RestorixHealth

 - RHYTHMSCIENCE INC

 - Rosch Visionary Systems

 - RVC

 - SALESFORCE

 - SCC Soft Computer

 - Schuyler House

 - ScImage

 - ScottCare

 - Sectra

 - Securitas Healthcare

 - Select Medical

 - Siemens

 - SIS

 - SoftLink International

 - SoftWriters

 - Solventum

 - Somnoware

 - Spectrum Medical

 - SUNQUEST

 - Sysmex Corporation

 - SystemLink

 - TeamHealth

 - Technidata

 - TELCOR

 - Telemetrix

 - Telexy HealthCare

 - Tieto

 - TIMEDOC, INC

 - T-System

 - Ultromics

 - Uniform Data Systems

 - United Clinical Laboratories

 - Varian Medical Systems

 - Vision Chips

 - VitalAxis

 - WebPT

 - WeInfuse

 - WELL BEAM INC

 - Welligent

 - WellSky

 - Wellsoft

 - Workday

 - Xtract Solutions

 - Yenlo

 - Zipnosis

 

 

 

### 
 Incoming Procedural Supply Usage
 [read the spec](/Tech/TechSpec?spec=5334)

 

 

 Updates supply or implant usage information in OpTime (Epic's OR module) or Cupid (Epic's CVIS) procedural logs.
 

 

 [Current integrations include ](#)
 

 - ARC Healthcare Technologies

 - AssistIQ

 - BD

 - Cardinal Health WaveMark

 - Copernicus

 - EHS

 - GENESIS

 - Infor Global Solutions

 - INSYSIV

 - iRCODER.COM

 - LUMEDX

 - McKesson

 - Merge Healthcare

 - Mobile Aspects

 - O&M Solutions

 - Omnicell

 - ORACLE

 - PAR Excellence

 - Prospitalia

 - Siemens

 - Tecsys

 - VueMed

 

 

 

### 
 Outgoing Results and Orders
 [read the spec](/Tech/TechSpec?spec=5211)

 

 

 You can configure each copy of this interface one of the following ways:
- This interface can send result messages in the LRI format. LRI format results follow the HL7 version 2.5.1 Implementation Guide: S&I Framework Lab Results Interface, Release 1. It can send both order status and result messages from Beaker to external systems, when Beaker is the reference lab for another LIS or clinical system.
- This interface can send result messages in the ELR format. ELR format results follow the HL7 version 2.5.1 Implementation Guide: Electronic Laboratory Reporting to Public Health, Release 1. This format is often used to notify public health agencies of tests which must be reported for disease tracking, and meet Meaningful Use (MU) or Promoting Interoperability (PI) measures in the U.S.
- This interface can send messages for pathology reports that contain electronic cancer checklists. These messages conform to the North American Association of Central Cancer Registries (NAACCR) Standards for Cancer Registries Volume V rules for constructing HL7 messages for CAP electronic cancer checklist synoptic reporting.

Use the LRI format unless you have a specific need to use the ELR or NAACCR formatted results.
 

 

 [Current integrations include ](#)
 

 - 3M

 - 4MEDICA INC.

 - 4S Informational Systems

 - Abbott Diagnostics

 - ACCESS TELECARE, LLC (FKA SOC TELEMED)

 - AccuMed

 - Accumen

 - ADAPTIVE BIOTECH

 - AdvantEdge Healthcare Solutions

 - Advarra

 - Agfa

 - AGILEMD, INC.

 - Agilent

 - AIDOC

 - Alabama - Public Health Agencies

 - Alaska - Public Health Agencies

 - Alberta Health Services Public Health Surveillance

 - AlertMD

 - Allscripts

 - Amazing Charts

 - Ameripath

 - Apache

 - APHL

 - Apollo

 - APS

 - Arizona - Public Health Agencies

 - Arkansas - Public Health Agencies

 - Arkansas Office of Health Information Technology

 - Artificial Intelligence in Medicine

 - ARUP Laboratories

 - Atalan

 - ATHENAHEALTH, INC.

 - Atlas

 - Australian Digital Health Agency

 - AVAILITY

 - Azalea

 - BabySentry

 - BAYESIAN HEALTH INC.

 - BD

 - bioMerieux, Inc.

 - Bio-Reference Laboratories, Inc

 - Blue Cross/Blue Shield

 - Bódegro

 - Bronx Regional Health Information Organization

 - C/NET Solutions

 - California - Public Health Agencies

 - CANFIELD SCIENTIFIC, INC.

 - Caradigm

 - Care Continuity

 - CAREDX INC.

 - CAREEVOLUTION

 - CarepathRx

 - Center for Disease Control

 - CentriHealth

 - Cerner

 - Change Healthcare

 - Chesapeake Regional Information System for Our Patients

 - CIS Oncology

 - CIVICA

 - Clinical Computer Systems, Inc.

 - CliniSync

 - Clinisys

 - CliniWorks

 - CODAMETRIX

 - Colorado - Public Health Agencies

 - CompuGroup Medical

 - Conceptual Mindworks, Inc.

 - Connecticut - Public Health Agencies

 - Consensus Medical Systems

 - CoPath

 - Corepoint Health

 - CORHIO

 - CORITY

 - CorrecTek, Inc.

 - Cortex Medical Management Systems

 - CVS Pharmacy

 - Cybernius Medical Ltd.

 - CyncHealth

 - Dako

 - DATA INNOVATIONS

 - Decisio Health

 - Deep Lens

 - Delaware - Public Health Agencies

 - Delaware Health Information Network

 - Denver County (CO) - Public Health Agencies

 - Diaverum

 - District of Columbia - Public Health Agencies

 - Dolbey

 - Dynacare

 - E.Novation

 - eClinicalWorks

 - Eclipsys

 - EDCO

 - E-Health

 - eIVF

 - Elekta

 - ELLKAY, LLC.

 - ELSEVIER INC.

 - eMDs

 - ENDOSOFT LLC

 - Ensemble Health Partners

 - Enterprise Health

 - Eon

 - ePath Logic, Inc.

 - Equum Medical

 - ESO

 - ETIOMETRY, INC.

 - Evolent Health

 - Falcon

 - Flatiron

 - Florida - Public Health Agencies

 - Foundation Medicine

 - Fresenius Medical Care

 - Gaia

 - GE

 - Georgia - Public Health Agencies

 - Glytec

 - GOOGLE LLC

 - Graphnet

 - Greenway Health

 - Haemonetics

 - HalfPenny

 - Harris

 - Hawaii - Public Health Agencies

 - Hawaii Health Information Exchange

 - hc1

 - HEALOGICS, INC.

 - HEALTH CATALYST, INC.

 - Health Current

 - Health Monitoring Systems

 - Health Resources and Services Administration

 - Health Sciences South Carolina

 - HealthBridge

 - HealtheCNY

 - HealtheConnections

 - HEALTHeLINK

 - HealthHIE Nevada

 - HealthLink

 - Healthmap Solutions

 - HealthNet

 - HealthShare Exchange

 - Helix

 - Hicuity Health

 - Hillrom

 - HODS Systems

 - Houston - Public Health Agencies

 - Hyland

 - IBM

 - ICNet

 - iD

 - Idaho - Public Health Agencies

 - Idaho Health Data Exchange

 - Illinois - Public Health Agencies

 - Illinois Office of Health Information Technology

 - ILLUMICARE, INC.

 - In-Common Laboratories

 - Indiana - Public Health Agencies

 - Indigo 4 Systems

 - Infian

 - Infor Global Solutions

 - Inform Health

 - Informatics Corporation of America

 - Infotrom

 - Inland Empire Health Plan

 - Inspirata, Inc

 - Instrumentation Laboratory (Werfen)

 - IntelliDose

 - InterSystems

 - IODINE SOFTWARE, LLC

 - Iowa - Public Health Agencies

 - Iron Bridge

 - Isoprime

 - It Starts With Me Health

 - Joint Venture Hospital Laboratories

 - Kansas - Public Health Agencies

 - Kansas Health Information Network

 - KaZee

 - Kentucky - Public Health Agencies

 - Kentucky Health Information Exchange

 - Keystone Therapeutics, Inc.

 - KONZA

 - LabCorp

 - LEANTAAS, INC.

 - Leica

 - LifeLabs

 - LifePoint Health

 - Louisiana - Public Health Agencies

 - M*Modal

 - Magentus

 - MagView

 - Maine - Public Health Agencies

 - MAK-SYSTEM

 - Manifest Medex

 - Maryland - Public Health Agencies

 - Massachusetts - Public Health Agencies

 - Massachusetts Health Information Highway

 - MCG Diagnostics

 - McKesson

 - MEDENT

 - MEDHOST

 - MEDICAL DATA SYSTEMS

 - MEDICAL INFORMATICS CORP.

 - Meditech

 - Medtronic

 - Medusind

 - Mellowood Medical

 - Merge Healthcare

 - Michigan - Public Health Agencies

 - Michigan Health Connect

 - Microsoft

 - Milagro AI

 - Minnesota - Public Health Agencies

 - Mississippi - Public Health Agencies

 - Missouri - Public Health Agencies

 - MOBILE HEARTBEAT, LLC

 - MobileMD

 - Modernizing Medicine

 - Modica Group

 - Molina Healthcare

 - MONARCH MEDICAL TECHNOLOGIES

 - Montana - Public Health Agencies

 - Mountain Star Clinical Laboratories

 - MYHEALTH ACCESS NETWORK

 - myOnsite Healthcare

 - NABIDH

 - NaphCare

 - Natera

 - National Health Service

 - National Institutes of Health

 - Nebraska - Public Health Agencies

 - Nebraska Health Information Initiative

 - NET HEALTH SYSTEMS, INC.

 - Netsmart

 - Netsoft, Inc.

 - Nevada - Public Health Agencies

 - New Hampshire - Public Health Agencies

 - New Jersey - Public Health Agencies

 - New Mexico - Public Health Agencies

 - New York - Public Health Agencies

 - New York Cancer & Blood Specialists

 - New York City - Public Health Agencies

 - NewCura

 - NextGen

 - Nexus

 - NHN

 - North Carolina - Public Health Agencies

 - North Carolina Health Information Exchange Authority

 - North Dakota - Public Health Agencies

 - Northwell Health

 - Norwegian Institute of Public Health

 - NUANCE COMMUNICATIONS INC.

 - Occupational Health Research

 - Office Practicum

 - Ohio - Public Health Agencies

 - Oklahoma - Public Health Agencies

 - Omda

 - ONCO Inc.

 - ONEHEALTHPORT

 - Ontario Ministry of Health

 - Ontario Patient Data Reporting

 - OntarioMD

 - OpenText

 - Optum

 - Orchard Software

 - Oregon - Public Health Agencies

 - Orion Health

 - Oztech

 - PALANTIR

 - Pascal Metrics

 - PathGroup

 - Pathology Associates Medical Laboratories

 - PATIENT ENGAGEMENT ADVISORS, LLC

 - Patient Knows Best

 - Pediatrix

 - PediNotes

 - Penn Medicine

 - Pennslyvania - Public Health Agencies

 - Pentax

 - Perahealth

 - Peridos

 - Philadelphia - Public Health Agencies

 - Philips

 - PHLEBIO

 - Picis

 - PierianDx

 - PLATOCODE

 - Point and Click Solutions

 - Practice

 - PREMIER, INC.

 - PRIMARY.HEALTH

 - PrognoCIS

 - Propelus

 - ProStar Technologies

 - ProVation Medical

 - Q-Centrix

 - QuadraMed

 - Quality Health Network (QHN)

 - Quantitative Diagnostic Software Group

 - QUEST DIAGNOSTICS

 - Quovadx

 - QVENTUS, INC.

 - Radiology Associates of Hawaii

 - ReadySet Surgical

 - Real-Time Outbreak Disease Surveillance Lab (RODS at University of Pittsburgh)

 - REDOX

 - Relay Health

 - Revvity

 - Rhode Island - Public Health Agencies

 - RIVM

 - RLDATIX

 - Roche Diagnostics

 - Rochester Regional Health Information Organization

 - Royal Devon and Exeter

 - SALESFORCE

 - San Diego - Public Health Agencies

 - San Diego Health Connect

 - SAP

 - Saudi Arabia Council of Health Insurance

 - Saudi Arabia Ministry of Health

 - SCC Soft Computer

 - Sectra

 - Select Medical

 - Sentri7

 - Singapore Ministry of Health Holdings

 - SISCO

 - SMARTERDX, INC

 - Softek Solutions, Inc.

 - Softmedex

 - Solventum

 - Sound Physicians

 - South Carolina - Public Health Agencies

 - South Dakota - Public Health Agencies

 - South Dakota Department of Health

 - Spectrum Medical

 - Spheris 

 - Stanford School of Medicine

 - STEMSOFT

 - Stichting HIV Monitoring (SHM)

 - Sunrise Medical Laboratories

 - SYMPLR

 - Talis Clinical

 - TeamHealth

 - TELCOR

 - Telemis

 - TELETRACKING

 - Telexy HealthCare

 - Telstra Health

 - Tennessee - Public Health Agencies

 - Texas - Public Health Agencies

 - TheraDoc

 - Thynk Health

 - Title21 Health Solutions

 - TransChart

 - Truven Health

 - UC Davis Health

 - United Healthcare

 - University of Arkansas for Medical Sciences

 - University of California

 - Utah - Public Health Agencies

 - Valab

 - Varian Medical Systems

 - vChart

 - Vermont - Public Health Agencies

 - Vermont Information Technology Leaders

 - Vibra Healthcare

 - VigiLanz

 - Virginia - Public Health Agencies

 - virtuwell

 - VISION SOFTWARE TECHNOLOGIES, INC.

 - Visonex

 - VITAL

 - Vituity

 - Vyaire Medical

 - Waseel

 - Washington - Public Health Agencies

 - WebReach, Inc

 - WellMed Medical Management

 - WellSky

 - West Virginia - Public Health Agencies

 - Wisconsin - Public Health Agencies

 - WOLTERS KLUWER

 - Wyoming - Public Health Agencies

 - XSOLIS

 - Yellowstone Pathology Institute (YPI)

 

 

 

### 
 Incoming Surgical Cart Tracking
 [read the spec](/Tech/TechSpec?spec=5319)

 

 

 After a surgical case is created, this interface files the identifier, current location, and transport status of the surgical carts that have been prepared for or assigned to the surgical case.
 

 

### 
 Outgoing Infusion Orders
 [read the spec](/Tech/TechSpec?spec=5264)

 

 

 Sends infusion order details to infusion pump gateways for the purposes of prepopulating infusion parameters on associated infusion pumps. When an infusion order message is sent on the Outgoing Infusion Orders interface, an immediate response is expected back from the infusion pump gateway via the Incoming Verification interface. These are advanced interfaces with a particular set of pre-requisites for successful implementation.
 

 

 [Current integrations include ](#)
 

 - B. Braun

 - Baxter

 - BD

 - Fresenius Medical Care

 - ICU Medical

 - Smiths Medical

 

 

 

### 
 Incoming External Push Notifications
 [read the spec](/Tech/TechSpec?spec=9907)

 

 

 Used for receiving alerts that are appropriate for one-way informational notifications that do not need to be acknowledged by the receiving user. See also Incoming Alerts from Alert Manager or Incoming Alerts from Patient Care Devices for other workflows.
 

 

### 
 Incoming Patient Education Interface
 [read the spec](/Tech/TechSpec?spec=5340)

 

 

 Integrates Epic's Patient Education activity with a third-party education content management or content delivery system. The interface is used to record whether the patient has completed an educational assignment, and it can also be used to record ad hoc educational activities that were not assigned by the clinician.
 

 

 [Current integrations include ](#)
 

 - Aceso

 - APPLE INC.

 - Avidex

 - GETWELLNETWORK, INC.

 - MDM Healthcare

 - MYTONOMY INC.

 - OneView

 - Optimal Solutions

 - PCARE BY UNIGUEST

 - REDOX

 - Skylight

 - SONIFI Solutions

 - WOLTERS KLUWER

 

 

 

### 
 Outgoing Patient Education Interface
 [read the spec](/Tech/TechSpec?spec=5236)

 

 

 Integrates the Patient Education Activity with a third-party education content management or delivery system. This interface is used to send clinician-initiated education assignments to a third-party system so that the content can be viewed and acted upon there.
 

 

 [Current integrations include ](#)
 

 - Aceso

 - API Healthcare

 - APPLE INC.

 - Avidex

 - GETWELLNETWORK, INC.

 - hellocare

 - LANA HEALTH INC.

 - MDM Healthcare

 - MYTONOMY INC.

 - OneView

 - Optimal Solutions

 - PCARE BY UNIGUEST

 - QuadraMed

 - Skylight

 - SONIFI Solutions

 - WOLTERS KLUWER

 

 

 

### 
 Incoming Deficiency Tracking
 [read the spec](/Tech/TechSpec?spec=5375)

 

 

 An HIM deficiency represents incomplete work by a provider. Receives and processes messages that can create or delete deficiencies, and update deficiency status and assigned providers. The interface adds external deficiency information in HIM when a deficiency is not automatically created by standard application functionality. This interface is useful if transcriptions are stored in an external system (obviating the need for an Incoming Transcription interface, which can also update deficiency statuses). The deficiency created by the interface can be configured to follow the rules defined in HIM for aging and delinquency or they can be controlled by an external system in a direct fashion. This interface also plays a key role if integrating with an external web-based deficiency system, receiving messages that allow a URL to be launched from the Chart Completion module.
 

 

 [Current integrations include ](#)
 

 - McKesson

 - NUANCE COMMUNICATIONS INC.

 

 

 

### 
 Incoming Patient Administration
 [read the spec](/Tech/TechSpec?spec=5342)

 

 

 Receives messages for new or changed demographic information, visits (ADT), registration (guarantors and insurance coverage), allergies, and bed status updates.
 

 

 [Current integrations include ](#)
 

 - 3M

 - 4MEDICA INC.

 - ADAPTIVE BIOTECH

 - ADL

 - ADP AdvancedMD

 - Akamai Practice Management

 - AlertMD

 - Allscripts

 - Amazon

 - Ambulancezorg Nederland

 - American Healthware

 - American Well

 - ANDOR HEALTH

 - Apotti

 - ARAMARK

 - Atalan

 - ATHENAHEALTH, INC.

 - Atlas

 - ATT Group

 - Avinty

 - Banner University Health Plan

 - BedWatch

 - Blackbaud

 - Bluebell Discovery

 - Bronx Regional Health Information Organization

 - Care

 - CareLogistics

 - Cedar

 - Cegedim

 - Cerner

 - CGI

 - Change Healthcare

 - Chesapeake Regional Information System for Our Patients

 - Citra Health Solutions

 - CLEARWAVE, INC.

 - Cleric

 - CliniSync

 - Clinisys

 - CognisantMD

 - Collective Medical Technologies

 - COMMURE

 - Concentra

 - CONCERT HEALTH

 - Consight

 - CoPath

 - Corepoint Health

 - CORITY

 - CPSI

 - Creative EMS

 - CRITEX

 - CureMD

 - CVS Pharmacy

 - DEDALUS

 - Digi- ja väestötietovirasto

 - Dubai Government Services

 - eClinicalWorks

 - Eclipsys

 - eConsult

 - Elekta

 - Elevance

 - ELLKAY, LLC.

 - EMS Software

 - Enterprise Health

 - ESO

 - Evolent Health

 - Federal Authority for Identity & Citizenship

 - Flatiron

 - Fujifilm

 - Fusion

 - GE

 - Global Health

 - GOHEALTH URGENT CARE

 - Greenway Health

 - Grouptech

 - Guardant Health

 - HalfPenny

 - HARMONY HEALTHCARE IT

 - Harris

 - HEALTH CATALYST, INC.

 - HEALTHeLINK

 - HealthSnap

 - Healthstream

 - HealthWare Systems

 - Helix

 - HelseNorge

 - Highmark

 - HMS

 - Homecare Homebase

 - Humata Health

 - HUS

 - Hyland

 - IBM

 - IHOMER

 - ImageTrend

 - IMPRIVATA, INC.

 - Indigo 4 Systems

 - Infor Global Solutions

 - INGENIOUS MED

 - Initiate

 - Intelerad

 - InterSystems

 - IntraNexus

 - Keane

 - KEEBLER HEALTH

 - LEANTAAS, INC.

 - LifePoint Health

 - Logis Solutions

 - M*Modal

 - Maxor

 - McKesson

 - MedAptus

 - MedData

 - MEDENT

 - MEDHOST

 - MedInformatix

 - Meditech

 - Mellowood Medical

 - Michigan - Public Health Agencies

 - Michigan Health Connect

 - Microsoft

 - Microsys

 - Minnesota - Public Health Agencies

 - Modernizing Medicine

 - Motorola

 - MULESOFT, INC.

 - MURJ, INC.

 - MyHealth First Network

 - National Health Service

 - Navina

 - NCS

 - NetIQ

 - Netsmart

 - New Jersey - Public Health Agencies

 - New Jersey Innovation Institute

 - New York City - Public Health Agencies

 - Nexa

 - NextGate Solutions

 - NextGen

 - NHN

 - Northwell Health

 - Notable

 - NSP

 - Ontario Ministry of Health

 - OpenText

 - Optima

 - Optum

 - ORACLE

 - Orchard Software

 - Orion Health

 - Ortivus

 - PathPresenter

 - Perkin Elmer

 - Philips

 - PHREESIA, INC.

 - Picis

 - Point and Click Solutions

 - PointClickCare

 - Practice Fusion, Inc.

 - Praxis

 - PREMIER, INC.

 - Qmatic

 - QuadraMed

 - QUEST DIAGNOSTICS

 - QVENTUS, INC.

 - QVERA LLC

 - Recondo

 - Relay Health

 - ResMed

 - RightPatient

 - RLDATIX

 - Rocket Systems Laboratory Inc

 - Royal Devon and Exeter

 - SALESFORCE

 - SAP

 - SapphireHealth

 - Saudi Arabia Council of Health Insurance

 - SCC Soft Computer

 - SCI

 - ScImage

 - Select Medical

 - Shields Health Care Group

 - Siemens

 - Singapore Ministry of Health Holdings

 - Softmedex

 - Solis Mammography

 - Soobr

 - Sound Diagnostics

 - Spacelabs

 - Spectrum Medical

 - Summit Healthcare Services

 - Sundhedsdatastyrelsen

 - TELADOC, INC.

 - TELETRACKING

 - TheraDoc

 - Tonic Solutions Inc.

 - TrakGene

 - TriZetto Provider Solutions, a Cognizant Company

 - T-System

 - UiPath

 - Utah - Public Health Agencies

 - virtuwell

 - Visma

 - Visonex

 - WellSky

 - Workday

 - Zipnosis

 - ZORGDOMEIN

 - Zorgi

 

 

 

### 
 Incoming Problem List
 [read the spec](/Tech/TechSpec?spec=5335)

 

 

 Used to add, modify, or remove problems from the patient-level problem list. This interface works specifically with the longitudinal problem list, not problems specific to a particular hospitalization. This integration has been implemented only for conversions.
 

 

 [Current integrations include ](#)
 

 - OncoChart

 

 

 

### 
 Outgoing Problem List
 [read the spec](/Tech/TechSpec?spec=5223)

 

 

 Sends notification of added, modified, or deleted problems from the patient-level problem list in the EHR to an external system. This interface works specifically with the longitudinal problem list, not problems specific to a particular hospitalization.
 

 

 [Current integrations include ](#)
 

 - Allscripts

 - Deep6 AI

 - GE

 - Harris

 - HealthInfoNet

 - Jvion

 - MCG Diagnostics

 - MYHEALTH ACCESS NETWORK

 - New York City - Public Health Agencies

 - Pascal Metrics

 - QuadraMed

 - SONIFI Solutions

 - VigiLanz

 - XSOLIS

 

 

 

### 
 Incoming Clinical Observations
 [read the spec](/Tech/TechSpec?spec=5378)

 

 

 Receives and processes clinical observations (past medical history, smoking history, and so on), that do not fit into other tools. This interface is typically used for filing clinical data for the purposes of a conversion. The Incoming Clinical Documentation Flowsheet interface is recommended if the data will be filed only to a documentation flowsheet.
 

 

 [Current integrations include ](#)
 

 - Ambulancezorg Nederland

 - Astraia

 - Axians

 - Cegedim

 - CLEARWAVE, INC.

 - DRDOCTOR

 - GE

 - Lameris Ootech

 - MEDTRAK, INC.

 - PDHI

 

 

 

### 
 Outgoing Ancillary Orders
 [read the spec](/Tech/TechSpec?spec=5298)

 

 

 Sends orders placed by a clinical user in EpicCare to external ancillary systems - including messages for new orders, order cancellations, and number assignment responses to externally-initiated orders. Use cases include: Send physician placed orders to external laboratory, radiology or cardiology systems, when not using Epic equivalent product. Send orders from Beaker, Epic's LIS, to an external LIS if test needs to be performed at another lab. Send orders to blood bank system from Beaker. To send orders to both an external lab system (not to Beaker) and an external radiology system (not Radiant, Epic's RIS), two copies of the interface are needed, one for each purpose.
 

 

 [Current integrations include ](#)
 

 - 3M

 - 4MEDICA INC.

 - Abaxis

 - Abbott Diagnostics

 - ABOUT HEALTHCARE, INC.

 - Accuhealth

 - AccuMed

 - ACL Laboratories

 - ACTX, INC.

 - ADAPTIVE BIOTECH

 - Agfa

 - AGILEMD, INC.

 - AGILITI

 - Alameda County (CA) - Public Health Agencies

 - AlertMD

 - all.health

 - Alliance Medical

 - Allscripts

 - Alverno

 - Ambra Health

 - Ambry Genetics

 - AMEDTEC

 - American RFID Solutions

 - Ameripath

 - Ameritox

 - AMGA

 - Anatechnic

 - ANDOR HEALTH

 - ANGELEYE HEALTH, INC.

 - Apollo

 - Apollo Laboratories

 - Apria

 - APS

 - ARAMARK

 - Arbor

 - Arkansas - Public Health Agencies

 - Arthrex

 - ARUP Laboratories

 - AS Software

 - Ascend Clinical

 - Astraia

 - Atalan

 - ATHENAHEALTH, INC.

 - Atlas

 - Aurora Diagnostics

 - autonik ab

 - AVASURE

 - Avidex

 - Axis Clinical

 - Babyscripts

 - BardyDx

 - Basys Data

 - Baxter

 - BD

 - BedWatch

 - Benetech

 - BILLIONTOONE

 - Biocoustics Instruments

 - Biofourmis

 - Bio-Reference Laboratories, Inc

 - Bioscientia

 - Bloodworks Northwest

 - Bódegro

 - Boston Scientific

 - BRAID.HEALTH INC.

 - BRAINCHECK, INC

 - BREG

 - Brightree

 - Brown & Associates Medical Laboratories

 - Buhlmann Labs

 - Cadence

 - Cadwell

 - California - Public Health Agencies

 - CANFIELD SCIENTIFIC, INC.

 - Capital Solution Design

 - Cardiac Science

 - Cardinal Health WaveMark

 - CareDx

 - CAREDX INC.

 - CareLogistics

 - CAREMESSAGE

 - CarepathRx

 - CareSignal

 - CBORD

 - CellCura

 - CellNetix

 - Center for Disease Detection

 - Central Clinical Labs

 - Cerner

 - CGI

 - Change Healthcare

 - CIVICA

 - Cleveland HeartLab, Inc.

 - Clinical Labs of Hawaii (CLH)

 - Clinisys

 - CODAMETRIX

 - Columbus Diagnostic Center

 - Compass Group

 - CompuGroup Medical

 - Compumedics

 - Computer Trust Corporation

 - COMPUTRITION, INC.

 - Comtron

 - Concert Genetics

 - CONCERT HEALTH

 - Consensus Medical Systems

 - Continuum Health Partners

 - Coordinated Care Washington

 - CoPath

 - Cordata Health

 - Core Sound Imaging

 - Cortex Medical Management Systems

 - Counsyl

 - Cox Communications

 - CPL

 - CPSI

 - Current Health

 - DATA INNOVATIONS

 - DataStar Systems

 - DEDALUS

 - Delaware - Public Health Agencies

 - Delta

 - Dentognostics

 - DeRoyal

 - Deutsche Telekom

 - Diagnostic Lab Services, Inc.

 - Diasoft

 - Digisonics

 - Digital Diagnostics

 - DigiVis

 - DISPATCHHEALTH

 - DJO GLOBAL, INC.

 - DMDC

 - Dolbey

 - Dominion Diagnostics

 - Dorner

 - DR Systems

 - DRUGSCAN INC.

 - Dynacare

 - E.Novation

 - Echosens

 - EDCO

 - EDITLife

 - Efertility

 - EGIS

 - E-Health

 - EHS

 - Elekta

 - ELLKAY, LLC.

 - Emageon

 - Embla

 - ENDOSOFT LLC

 - Envision Radiology

 - Esoterix

 - Esprit Health

 - EVIDENCECARE, LLC

 - EvoHealth

 - Exact Sciences

 - Exan Academic

 - Exceltox

 - Extract Systems

 - EyeNuk

 - Finalist Noord Nederland C.V.

 - Fleischhacker

 - Fotoware

 - Foundation Medicine

 - Freeland

 - Fuel Medical

 - Fujifilm

 - Fulgent Genetics

 - GE

 - GeneDx

 - General Medical Laboratories

 - GENEVA HEALTH SOLUTIONS

 - Genial Genetics

 - GenomOncology

 - Genzyme Corporation

 - GETWELLNETWORK, INC.

 - GLOOKO, INC.

 - Glytec

 - Grail

 - Greenwood Genetics

 - Guardant Health

 - Haemonetics

 - HalfPenny

 - Hasana

 - Hawaii Health Information Exchange

 - HCI Solutions

 - Health Recovery Solutions

 - HealthLab

 - HEALTHPARTNERS

 - HealthSnap

 - Heartflow

 - Helix

 - hellocare

 - Hicuity Health

 - Hillrom

 - HLA Data Systems LLC

 - HNL Lab Medicine

 - Horiba Medical

 - Hyland

 - IBM

 - iCRco

 - IDx

 - Illinois - Public Health Agencies

 - Illinois Bone and Joint Institute

 - Illinois Office of Health Information Technology

 - Illumina

 - ImageMoverMD

 - In-Common Laboratories

 - INFINITT NORTH AMERICA

 - Infor Global Solutions

 - Inland Empire Health Plan

 - Instrumentation Laboratory (Werfen)

 - Integrated Ophthalmic Systems

 - Intelerad

 - Intelligent Business Solutions

 - InvisALERT

 - IODINE SOFTWARE, LLC

 - iRhythm

 - IRIS (Intelligent Retinal Imaging Systems)

 - Itamar Medical

 - iTero

 - ITxM

 - J&S Medical Associates

 - Kainos

 - Karl Storz

 - Keriton Kare

 - Kestral

 - KIBI

 - Kodak

 - Konica Minolta

 - LabCorp

 - Laboratory Services Cooperative

 - Laborie Medical Technologies

 - LabSoft

 - Labtech

 - LabVantage

 - Lexmark Enterprise Software

 - L-Force

 - LIFE IMAGE

 - Life Systems International

 - LifeLabs

 - LifePoint Health

 - Lighthouse Lab Services

 - LigoLab

 - Locus Health

 - Los Angeles County Public Health Laboratory

 - Louisiana - Public Health Agencies

 - LUMEDX

 - M*Modal

 - Machaon Diagnostics

 - Magentus

 - MagView

 - Mako Medical

 - Mammography Reporting System

 - Maryland - Public Health Agencies

 - Masimo

 - MCG Diagnostics

 - McKesson

 - MCR TECHNOLOGIES, INC.

 - MD Interconnect

 - MD REVOLUTION, INC.

 - MEDHOST

 - Medical Diagnostic Laboraties

 - Medical Genetics Information System

 - Medically Home

 - Mediconsult

 - Medicor Imaging

 - Medicus

 - Medify

 - MediLIMS

 - MedInformatix

 - Medisanté

 - MediServe

 - Medisys Innovation

 - Meditech

 - MedPlus

 - MedStar Health

 - Medstrat

 - Medstreaming

 - Medtox

 - Medtronic

 - MedVirginia

 - Merge Healthcare

 - MGC Diagnostics

 - MIET Healthcare

 - Millenium Health

 - Minnesota - Public Health Agencies

 - MONARCH MEDICAL TECHNOLOGIES

 - Morgan Scientific

 - Mortara

 - MSF&W

 - MULESOFT, INC.

 - Multidata

 - MURJ, INC.

 - MyLab

 - MYTONOMY INC.

 - NantHealth

 - Natera

 - National Health Service

 - National Technology

 - Natus

 - NCSCT

 - NDD Medical Technologies

 - NEC

 - NeoGenomics

 - Netsoft, Inc.

 - New York - Public Health Agencies

 - New York Cancer & Blood Specialists

 - NewCura

 - Nexus

 - NHN

 - Nihon Kohden

 - North Dakota - Public Health Agencies

 - Northwell Health

 - Notable

 - NovaRad

 - NovoPath

 - Nox

 - nSpire

 - NUANCE COMMUNICATIONS INC.

 - Octagos

 - Olympus Endoworks

 - Olympus Medical Systems

 - Omda

 - Omron

 - OneOme

 - OnePACS

 - Ontario Ministry of Health

 - OpenText

 - Optopol Technology

 - Optum

 - Opus Pathology

 - ORACLE

 - OralDNA

 - Orchard Software

 - Oregon - Public Health Agencies

 - Orion Health

 - Össur

 - OZ Systems

 - Oztech

 - PACSGear

 - PALANTIR

 - Palo Alto Pathology

 - Pangaea Information Technologies

 - PARKLAND CENTER FOR CLINICAL INNOVATION

 - PathAdvantage

 - PathGroup

 - Pathline

 - Pathology Associates Medical Laboratories

 - PathView Systems

 - PATIENT ENGAGEMENT ADVISORS, LLC

 - PCARE BY UNIGUEST

 - PenRad

 - Pentax

 - Peridos

 - Perkin Elmer

 - Philips

 - PierianDx

 - Polaris Health

 - PowerWellness

 - Precision Genetics

 - PREMIER, INC.

 - Preventice

 - Proficient Health

 - Progenity, Inc.

 - ProPath

 - ProSolv CardioVascular

 - ProVation Medical

 - PROVIDERFLOW

 - Psyche

 - PulmOne

 - Puritan Bennett

 - Q-Centrix

 - QuadraMed

 - Quality Health Network (QHN)

 - QUEST DIAGNOSTICS

 - Radiometer America

 - RADNET

 - Radsource

 - RAYUS

 - Recora

 - REDOX

 - Region Midtjylland Microbiology Department

 - Regional Medical Laboratory

 - Relay Health

 - Relaymed

 - Renesan Software

 - ResMed

 - Revvity

 - Rhode Island - Public Health Agencies

 - Rhythm

 - RMI Physician Services Corporation

 - Royal Solutions Group

 - RVC

 - SALESFORCE

 - SanaNet

 - SAP

 - Savant

 - SCC Soft Computer

 - Schuyler House

 - Scientific Software Solutions

 - ScImage

 - ScottCare

 - Sectra

 - Semler Scientific

 - Sentri7

 - Sharp Health Plan

 - SHL Telemedicine

 - Siemens

 - SimonMed

 - Skylight

 - SleepEx

 - Smiths Medical

 - Smokefree

 - Softek Solutions, Inc.

 - SoftLink International

 - SoftScript, Inc.

 - Soliton IT

 - Somnomedics

 - Somnoware

 - Sonic Reference Laboratory

 - SONIFI Solutions

 - South Carolina - Public Health Agencies

 - Spacelabs

 - St. Charles Health System

 - Stanford School of Medicine

 - Steeper Group

 - Stryker

 - SUNQUEST

 - Sunrise Medical Laboratories

 - SYMPLR

 - Sysmex Corporation

 - SystemLink

 - Tacoma Radiology Associates

 - Technidata

 - TekLabs

 - TELADOC, INC.

 - TELCOR

 - Telemetrix

 - TELETRACKING

 - Telexy HealthCare

 - TelmedIQ

 - TEMPUS, INC.

 - Tenet Healthcare Corporation

 - Teramedica

 - Texas - Public Health Agencies

 - The Advisory Board

 - TheraDoc

 - Thermo Fisher Scientific

 - TIDEPOOL

 - Tieto

 - Timeless Medical Systems

 - Title21 Health Solutions

 - Topcon Medical Systems

 - Total Orbit

 - Transolutions

 - TridentUSA

 - Trubridge

 - UC San Diego

 - United Medical Imaging Healthcare

 - United States Drug Testing Laboratories, Inc

 - University of Arkansas for Medical Sciences

 - University of California

 - Valley Radiology Consultants

 - Varian Medical Systems

 - Variantyx

 - VAXCARE

 - vChart

 - Velos

 - Velox Imaging

 - Velsera

 - Vibra Healthcare

 - VigiLanz

 - Vignette

 - Viracor-IBT Laboratories

 - Virtual Radiologic

 - VISAGE IMAGING, INC.

 - Vision Chips

 - VISION SOFTWARE TECHNOLOGIES, INC.

 - VISUS

 - VitalAxis

 - VitalConnect

 - VitalTech

 - Vivify Health

 - VOLPARA HEALTH, INC.

 - Vyaire Medical

 - Vyne Medical

 - Waba

 - Waseel

 - Washington - Public Health Agencies

 - WELBY HEALTH, INC.

 - Wellbeing Software

 - WellSky

 - WestCall

 - WiserCare

 - Withings Health Solutions

 - WOLTERS KLUWER

 - Workday

 - XEALTH

 - XIFIN

 - X-Lab

 - XSOLIS

 - Yellowstone Pathology Institute (YPI)

 - Yenlo

 - Zeiss

 - Zoll

 - ZORGDOMEIN

 - Zotec Partners

 

 

 

### 
 Outgoing Medication Administration Notification
 [read the spec](/Tech/TechSpec?spec=5259)

 

 

 Sends medication administration notification when a clinician marks a medication as administered on the MAR. This interface also sends updates regarding prior administrations, and change of status notifications for medications previously marked as administered. It does not send due times for medications that need to be administered in the future. The interface does not send messages when clinicians document the administration of blood products on the MAR or patient-controlled analgesia (PCA) medications on a documentation flowsheet.
 

 

 [Current integrations include ](#)
 

 - 3M

 - Allscripts

 - AMERISOURCE BERGEN

 - BD

 - Bronx Regional Health Information Organization

 - California Department of Justice

 - CENCORA

 - CenterX

 - Clinical Computer Systems, Inc.

 - CPS

 - CyncHealth

 - Decisio Health

 - Deep Lens

 - Dolbey

 - EDITLife

 - GE

 - GETWELLNETWORK, INC.

 - Glytec

 - Health Sciences South Carolina

 - HealthShare Exchange

 - HMS

 - ILLUMICARE, INC.

 - Infor Global Solutions

 - IntelliGuard

 - IODINE SOFTWARE, LLC

 - Iowa - Public Health Agencies

 - K2 Medical Systems

 - LEANTAAS, INC.

 - McKesson

 - MEDICAL INFORMATICS CORP.

 - Medically Home

 - Milagro AI

 - NUANCE COMMUNICATIONS INC.

 - Omnicell

 - PACEMATE, LLC

 - PARKLAND CENTER FOR CLINICAL INNOVATION

 - Pascal Metrics

 - PCARE BY UNIGUEST

 - PediNotes

 - PERIGEN

 - Philips

 - PREMIER, INC.

 - QuadraMed

 - QVENTUS, INC.

 - RISKLD

 - Sentri7

 - SMARTERDX, INC

 - Softmedex

 - Solventum

 - SURESCRIPTS

 - SYMPLR

 - TheraDoc

 - VigiLanz

 - WOLTERS KLUWER

 - XSOLIS

 

 

 

### 
 Outgoing Diet Orders
 [read the spec](/Tech/TechSpec?spec=5280)

 

 

 Sends information about new or canceled diet orders to an external nutrition system. Messages are triggered when diet orders are created or canceled in EpicCare Inpatient EHR.
 

 

 [Current integrations include ](#)
 

 - ANGELEYE HEALTH, INC.

 - CareLogistics

 - CBORD

 - CGI

 - Common Cents Solutions

 - Compass Group

 - COMPUTRITION, INC.

 - Delegate Technology Group

 - DFM Technologies

 - GE

 - GETWELLNETWORK, INC.

 - HHS

 - Horizon

 - IODINE SOFTWARE, LLC

 - MCR TECHNOLOGIES, INC.

 - MealIQ

 - Mealsuite

 - Medically Home

 - PinkRoccade Healthcare

 - Serial Multivision

 - Sodexo

 - Softlogic Australia Pty Ltd

 - SONIFI Solutions

 - TCM

 - Timeless Medical Systems

 - VigiLanz

 - VISION SOFTWARE TECHNOLOGIES, INC.

 - XSOLIS

 

 

 

### 
 Outgoing Imaging Results and Orders
 [read the spec](/Tech/TechSpec?spec=5265)

 

 

 Sends orders and results from Radiant (Epic's RIS) or Cupid (Epic's CVIS) to PACS, radiology transcription systems, or other external systems. This is the only interface that sends orders or results from Radiant or Cupid. Messages are triggered for new orders when an order reaches a status of scheduled or arrived, changes to the status of an order, for results, and when the appointment associated with an order is canceled.
 

 

 [Current integrations include ](#)
 

 - 3M

 - 4MEDICA INC.

 - 4ways Diagnostics

 - AbbaDox

 - Abbott Diagnostics

 - AccuMed

 - Acousoft

 - Acuo Technologies

 - AdvantEdge Healthcare Solutions

 - Agfa

 - AGILEMD, INC.

 - AGILON HEALTH

 - AIDOC

 - AlertMD

 - Allscripts

 - Ambra Health

 - AMEDTEC

 - American Well

 - Apache

 - APHL

 - Apollo

 - APS

 - Arkansas - Public Health Agencies

 - Arkansas Office of Health Information Technology

 - Arthrex

 - AS Software

 - Ascencia

 - Astraia

 - ATHENAHEALTH, INC.

 - Atlas

 - Australian Digital Health Agency

 - AVAILITY

 - Axis Clinical

 - BardyDx

 - Baxter

 - Bayer Healthcare

 - BD

 - Benetech

 - Biotronik

 - Boston Scientific

 - Brainlab

 - BRIT

 - Bronx Regional Health Information Organization

 - BUDDI.AI

 - BUTTERFLY NETWORK, INC

 - Cadwell

 - California Information Exchange

 - Cardea Technology

 - Cardiac Science

 - Cardinal Health WaveMark

 - CardioReportware

 - Care Continuity

 - CAREDX INC.

 - CAREEVOLUTION

 - CareLogistics

 - Carestream Health

 - Cerner

 - CGI

 - Change Healthcare

 - Chesapeake Regional Information System for Our Patients

 - ChipSoft

 - CIMAR

 - Circle Cardiovascular Imaging

 - Clario

 - ClickView

 - Clinical Network Systems

 - Clinical Science System

 - CliniSync

 - Clinisys

 - CoActiv Medical

 - CODAMETRIX

 - CodeRyte

 - CognisantMD

 - Cohesic

 - Comercer

 - Comercer

 - Compressus

 - Compumedics

 - Conexsys

 - Connecticut - Public Health Agencies

 - Consensus Medical Systems

 - Consulting Radiologists Ltd.

 - Core Sound Imaging

 - CORHIO

 - CORITY

 - Cosmed

 - CyncHealth

 - Decisio Health

 - Delaware Health Information Network

 - DELIVERHEALTH

 - Digisonics

 - Dinmar

 - Direct Radiology

 - DocPanel Technologies

 - Dolbey

 - DoseMonitor

 - DR Systems

 - DUPLICATEIatric Systems

 - Dynamic

 - E.Novation

 - ec2

 - Echosens

 - eClinicalWorks

 - Eclipsys

 - EDCO

 - E-Health

 - ELCAT

 - Elekta

 - ELLKAY, LLC.

 - Emageon

 - eMDs

 - EMS Software

 - ENDOSOFT LLC

 - Envision

 - Envision Radiology

 - Eon

 - ePath Logic, Inc.

 - ESO

 - EVERLIGHT RADIOLOGY

 - Exo Works Enterprise

 - Experity

 - Family HealthCare Network

 - FinThrive

 - First-Call Medical

 - Fleischhacker

 - ForCare

 - Foundation Medicine

 - Foundation Systems Inc.

 - Fujifilm

 - Fysicon

 - GE

 - GENEVA HEALTH SOLUTIONS

 - GERRIT

 - Getinge

 - GETWELLNETWORK, INC.

 - GOOGLE LLC

 - Graphnet

 - Greenway Health

 - Hawaii Health Information Exchange

 - HEALOGICS, INC.

 - HEALTH CATALYST, INC.

 - Health Current

 - Health Images

 - HealthBridge

 - Healthcare Administrative Partners

 - HealtheCNY

 - HealtheConnections

 - HEALTHeLINK

 - HealthHIE Nevada

 - HealthInfoNet

 - HealthLink

 - Healthmap Solutions

 - HealthPro Medical Billing

 - Healthstream

 - Heart Imaging Technologies

 - Heartflow

 - Heidelberg Engineering

 - Hermes Medical Solutions

 - Hillrom

 - Hologic

 - Hospital Diagnostic Imaging Repository Services

 - HUS

 - Hyland

 - IBM

 - iCRco

 - iD

 - ILLUMICARE, INC.

 - ImagineSoftware

 - Imorgon

 - Indiana - Public Health Agencies

 - Indigo 4 Systems

 - INFINITT NORTH AMERICA

 - Infor Global Solutions

 - Informatics Corporation of America

 - Insight HealthCare Information Systems

 - Integrated Medical Partners

 - Integrated Ophthalmic Systems

 - Intelerad

 - Intelligent Business Solutions

 - INTUITIVE SURGICAL

 - IODINE SOFTWARE, LLC

 - Iowa - Public Health Agencies

 - IQMax

 - iRCODER.COM

 - iRhythm

 - Iris

 - Iuvo

 - iViews Imaging

 - Karl Storz

 - Karos Health

 - KaZee

 - KDH Systems

 - Keane

 - Kodak

 - Konica Minolta

 - Laborie Medical Technologies

 - Lameris Ootech

 - Lanier

 - Laurel Bridge

 - Lexmark Enterprise Software

 - LIFE IMAGE

 - Lifetrack Medical Systems

 - LucidHealth

 - LUMEDX

 - M*Modal

 - Mach7 Technologies

 - MagView

 - Mammography Reporting System

 - Mammologix

 - Manifest Medex

 - MCG Diagnostics

 - McKesson

 - MCR TECHNOLOGIES, INC.

 - MEDENT

 - Medical Management Resources, Inc.

 - Medical Measurement Systems

 - Medically Home

 - Medicomp

 - Medicor Imaging

 - Medigistics

 - MedInformatix

 - Medisys Innovation

 - Meditech

 - MEDNAX

 - MedPlus

 - Medstrat

 - Medstreaming

 - Medtronic

 - MedVirginia

 - Mennen

 - Merge Healthcare

 - MGC Diagnostics

 - Michigan Health Connect

 - Microsoft

 - MIET Healthcare

 - MILLIMAN, INC.

 - Mirion

 - MobileMD

 - Modernizing Medicine

 - Morgan Scientific

 - Morrisey

 - Mortara

 - Mpirik

 - MSN

 - MURJ, INC.

 - MYHEALTH ACCESS NETWORK

 - MyLab

 - NABIDH

 - National Decision Support Company

 - National Health Service

 - National Institutes of Health

 - Natus

 - NDD Medical Technologies

 - NET HEALTH SYSTEMS, INC.

 - Neurotargeting

 - New York City - Public Health Agencies

 - NewCura

 - NextGen

 - NexxRad

 - NHN

 - Nihon Kohden

 - NovaRad

 - Novo Innovations

 - nSpire

 - NUANCE COMMUNICATIONS INC.

 - Nuclear Medicine Information Systems LLC

 - NucleusHealth

 - Nym

 - Occupational Health Research

 - Octagos

 - Olympus America

 - Olympus Endoworks

 - Olympus Medical Systems

 - Omnicell

 - OneView

 - ONRAD

 - Ontario Ministry of Health

 - Ontario Patient Data Reporting

 - OntarioMD

 - OpenText

 - Optopol Technology

 - Optum

 - Orpheus

 - OSG

 - OTiS Medical Analytics

 - PACEMATE, LLC

 - PACSGear

 - PALANTIR

 - Pangaea Information Technologies

 - PATIENT ENGAGEMENT ADVISORS, LLC

 - PaxeraHealth

 - PediNotes

 - Penn Medicine

 - Pennslyvania - Public Health Agencies

 - PenRad

 - Pentax

 - Philips

 - Picis

 - Point and Click Solutions

 - Practice Fusion, Inc.

 - Praxis

 - PREMIER, INC.

 - Preventice

 - Primordial Designs

 - ProSolv CardioVascular

 - ProVation Medical

 - PulmOne

 - Q-Centrix

 - QuadraMed

 - Quality Health Network (QHN)

 - Quantitative Diagnostic Software Group

 - QUEST DIAGNOSTICS

 - Quovadx

 - QVENTUS, INC.

 - RAD AI, INC.

 - RADIA INC.

 - Radiologic Associates, P.C.

 - Radiological Society of North America

 - Radiology Associates Imaging Centers (FL)

 - Radiology Associates of Hawaii

 - Radiology Partners

 - RADNET

 - Radsource

 - RamSoft

 - RAYS

 - RAYUS

 - ReadySet Surgical

 - REAL RADIOLOGY

 - REDOX

 - Relay Health

 - Rhythm

 - Rivendale Systems

 - Roche Diagnostics

 - Royal Solutions Group

 - RVC

 - San Diego - Public Health Agencies

 - Sandlot Solutions

 - Saudi Arabia Council of Health Insurance

 - Saudi Arabia Ministry of Health

 - SCC Soft Computer

 - Schiller AG

 - Scientific Software Solutions

 - ScImage

 - ScottCare

 - ScriptSender

 - Sectra

 - Select Medical

 - Sentri7

 - Shields Health Care Group

 - Siemens

 - Singapore Ministry of Health Holdings

 - Softek Solutions, Inc.

 - SoftLink International

 - SoftMed

 - Solis Mammography

 - Soliton IT

 - Solventum

 - Somnoware

 - SONIFI Solutions

 - Sound Physicians

 - South Carolina - Public Health Agencies

 - Spacelabs

 - Spectrum Medical

 - St. Jude's

 - Stanford School of Medicine

 - Streamline Health

 - Stryker

 - SYMPLR

 - Synedra

 - TeamHealth

 - Technidata

 - Tecsys

 - Telexy HealthCare

 - Teramedica

 - TheraDoc

 - ThinAir Data Corp.

 - Thynk Health

 - Topcon Medical Systems

 - Tradsol Teleradiology

 - Transcend

 - Transolutions

 - Transparent Imaging

 - TridentCare

 - TridentUSA

 - TSG Integrations

 - UltraRAD

 - Utah - Public Health Agencies

 - VantageMed

 - Varian Medical Systems

 - Velos

 - Vermont Information Technology Leaders

 - Vidistar

 - VigiLanz

 - Virtual Radiologic

 - VISAGE IMAGING, INC.

 - Vision Chips

 - Vista Radiology

 - VISUS

 - Vital Images

 - Vituity

 - VOLPARA HEALTH, INC.

 - VueMed

 - Vyaire Medical

 - Vyne Medical

 - Waseel

 - WebReach, Inc

 - Wellbeing Software

 - WellSky

 - Wisconsin - Public Health Agencies

 - WOLTERS KLUWER

 - Xperthis

 - XSOLIS

 - Zeiss

 - Zotec Partners

 

 

 

### 
 Incoming Blood Product Matching to BPAM
 [read the spec](/Tech/TechSpec?spec=5382)

 

 

 This interface is included with the Blood Product Administration Module and facilitates matching (positive patient identification with blood) of blood products received from an external blood bank system.
 

 

 [Current integrations include ](#)
 

 - Allscripts

 - Bloodworks Northwest

 - Bódegro

 - Cerner

 - Clinical Labs of Hawaii (CLH)

 - Clinisys

 - CompuGroup Medical

 - CoPath

 - Diagnostic Lab Services, Inc.

 - Dorner

 - EGIS

 - Haemonetics

 - ITxM

 - Kestral

 - Magentus

 - McKesson

 - Meditech

 - MyLab

 - Orchard Software

 - Philips

 - Savant

 - SCC Soft Computer

 - SUNQUEST

 - Sussex Biologicals

 - WellSky

 

 

 

### 
 Incoming Medication Orders to EpicCare Ambulatory
 [read the spec](/Tech/TechSpec?spec=5349)

 

 

 Receives medication order information from an external ambulatory pharmacy system other than Willow Ambulatory. In the past, this interface was used only by an organization that maintained its own ambulatory pharmacy system and interfaced it with EpicCare Ambulatory EHR. In its original implementation mode, this interface encodes and cancels orders, tracks and cancels dispenses, and requests the originator of a refill order. However, since external pharmacy systems have now moved to NCPDP/e-prescribing workflows, this interface is no longer implemented in real time, and is sparingly used for certain types of electronic conversions (see Patient Abstractor for preferred method of converting at home medications). Note that this interface cannot be used to receive medications from an external Hospital Information System and file them for use with Willow Inpatient, nor can it file medication administration information discretely to the electronic MAR.
 

 

 [Current integrations include ](#)
 

 - Abbott Diagnostics

 - McKesson

 - NCS

 - SapphireHealth

 - ScriptPro

 - TruMed Systems

 

 

 

### 
 Outgoing Medication Orders from EpicCare Ambulatory
 [read the spec](/Tech/TechSpec?spec=5253)

 

 

 Sends ambulatory medication orders that are placed in Order Entry to an external pharmacy system internal to the organization other than Willow Ambulatory Pharmacy. Messages are triggered as a user orders, discontinues, or reorders a medication.
 

 

 [Current integrations include ](#)
 

 - Allscripts

 - AMERISOURCE BERGEN

 - CAREXM

 - CBORD

 - ConnectiveRx

 - Deep Lens

 - Enclara

 - Glytec

 - iLabel

 - inHealth

 - IntelliDose

 - Kansas Health Information Network

 - Manifest Medex

 - McCreadie Group

 - Medically Home

 - Medicom Health

 - Medicomp

 - MedImpact

 - Medline

 - MULESOFT, INC.

 - NABIDH

 - NCS

 - Onepoint Health Services

 - Optum

 - OptumRx (Catamaran)

 - Pascal Metrics

 - Philips

 - PREMIER, INC.

 - ProCare Rx

 - Rx Savings Solutions

 - SapphireHealth

 - Script Care

 - ScriptPro

 - Therigy

 - TruMed Systems

 - VAXCARE

 - Velos

 - Waseel

 - WeInfuse

 - XSOLIS

 

 

 

### 
 Outgoing Scanned Document Link Maintenance
 [read the spec](/Tech/TechSpec?spec=5210)

 

 

 Sends updated document link keywords to an external document management system (DMS) when key information about where the content is located changes, for example, if a scan that originated in the DMS is moved from one encounter to another by HIM Chart Correction processes.
 

 

 [Current integrations include ](#)
 

 - 3M

 - Agfa

 - CIVICA

 - ELLKAY, LLC.

 - FOTO Inc.

 - Fujifilm

 - Hyland

 - IBM

 - Lexmark Enterprise Software

 - MedPlus

 - OpenText

 - Paragon

 - QUEST DIAGNOSTICS

 - RVC

 - Synedra

 

 

 

### 
 Incoming Results from Lab Instruments
 [read the spec](/Tech/TechSpec?spec=8000)

 

 

 Receives test results from instruments into Beaker, Epic's LIS. This is also the interface to use to receive point of care testing results, such as from docked glucometer systems, into Beaker.
 

 

 [Current integrations include ](#)
 

 - 4S Informational Systems

 - Abaxis

 - Abbott Diagnostics

 - Accelerate Diagnostics

 - Acuo Technologies

 - Advanced Instruments, Inc.

 - Aegis Sciences Corporation

 - Agilent

 - Alfa Wassermann

 - Allscripts

 - Ameripath

 - Analys Instrument - Streck Laboratories

 - Arkray Clinical Diagnostics

 - BD

 - Beckman Coulter, Inc

 - Bio-chrome

 - bioMerieux, Inc.

 - Bio-Rad Laboratories

 - Bruker

 - CellaVision

 - Cepheid

 - Cerner

 - Click Commerce

 - Clinical Diagnostic Solutions

 - ClinLab

 - CONWORX

 - Copan Diagnostics

 - Cytognos

 - Dako

 - DATA INNOVATIONS

 - Dawning

 - Diagnostica Stago

 - DiaSorin Biomedia

 - DreamPath

 - Dynex Technologies

 - ELITechGroup

 - Fujifilm

 - Gateway Electronic Medical Management Systems

 - GE

 - Giles Scientific, Inc.

 - Haemonetics

 - Helena Laboratories

 - HemaTechnologies

 - HemoCue

 - Hitachi

 - Hologic

 - Hologic Gen-Probe, Inc.

 - Horiba Medical

 - Immucor

 - Indica Lab

 - Infinity Healthcare

 - Inova Diagnostics (Werfen)

 - Inspirata, Inc

 - Instrumentation Laboratory (Werfen)

 - Iris

 - ITC

 - Kuali

 - LabConco

 - LabCorp

 - Leica

 - Luminex

 - Macro Helix

 - Magellan Diagnostics

 - McKesson

 - Medica Corporation

 - MedicaLogic

 - Medtox

 - Medtronic

 - Meridian Bioscience

 - myOnsite Healthcare

 - NantHealth

 - Natera

 - New York Cancer & Blood Specialists

 - Nova Biomedical

 - Nova Biomedical

 - Nova Diagnostic

 - NUANCE COMMUNICATIONS INC.

 - Olympus America

 - Ortho-Clinical Diagnostics, a Johnson & Johnson Company

 - Paige AI

 - PathPresenter

 - Perkin Elmer

 - Phadia

 - Philips

 - PolyMedCo Inc.

 - PREMIER, INC.

 - Qiagen

 - QUAKE GLOBAL

 - Radiometer America

 - Roche Diagnostics

 - Rosch Visionary Systems

 - Rotem

 - RR Mechatronics

 - Sakura

 - SCC Soft Computer

 - Sebia

 - Sectra

 - Siemens

 - SNAPS Solution

 - Sybase

 - Sysmex Corporation

 - TELCOR

 - Thermo Fisher Scientific

 - Tosoh Medics

 - Trinity Biotech

 - Valab

 - Ventana Medical Systems

 - Vital Diagnostics

 - Waters Corporation

 - WellSky

 - Zeus Scientific

 

 

 

### 
 Outgoing Orders to Lab Instruments
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20Orders%20to%20Lab%20Instruments%20Interface%20Technical%20Specification.pdf)

 

 

 Sends information about new or canceled laboratory orders from Beaker, Epic's LIS, to an instrument. This is also the interface to use for Point of Care testing with Beaker, for example, docked glucometer systems. It can trigger messages when a new specimen is received, a test is reordered, an add-on test is ordered for a specimen that has already been received, or a test is canceled.
 

 

 [Current integrations include ](#)
 

 - Abbott Diagnostics

 - Ameripath

 - Apache

 - BD

 - Beckman Coulter, Inc

 - bioMerieux, Inc.

 - Bio-Rad Laboratories

 - Bruker

 - CellaVision

 - Click Commerce

 - Dako

 - DATA INNOVATIONS

 - Dawning

 - Diagnostica Stago

 - Fujifilm

 - Haemonetics

 - Indica Lab

 - Inspirata, Inc

 - Instrumentation Laboratory (Werfen)

 - Iris

 - Leica

 - Ortho-Clinical Diagnostics, a Johnson & Johnson Company

 - Paige AI

 - PathGroup

 - PathPresenter

 - Phadia

 - Philips

 - Q-Centrix

 - QUAKE GLOBAL

 - Radiometer America

 - Roche Diagnostics

 - Rosch Visionary Systems

 - Sectra

 - Siemens

 - SOPHiA GENETICS

 - Sysmex Corporation

 - TELCOR

 - Thermo Fisher Scientific

 - Varian Medical Systems

 - Ventana Medical Systems

 - Waters Corporation

 

 

 

### 
 Incoming Orders from CPOE Systems
 [read the spec](/Tech/TechSpec?spec=staged%2FIncoming%20Orders%20from%20CPOE%20Systems%20Interface%20Technical%20Specification.pdf)

 

 

 Receives orders from external ordering systems. The interface can create, update, or cancel orders. Common use cases are routing lab orders to Beaker (Epic's LIS), radiology orders to Radiant (Epic's RIS), or cardiology orders to Cupid (Epic's CVIS). Some integrations may additionally require either an Incoming Patient Administration interface to create or update patient records or an incoming query to look up patient information before sending the order message.
 

 

 [Current integrations include ](#)
 

 - 3M

 - 4MEDICA INC.

 - Accumen

 - ADAPTIVE BIOTECH

 - Agfa

 - Allscripts

 - Ambra Health

 - American Well

 - ARUP Laboratories

 - Atalan

 - ATHENAHEALTH, INC.

 - Atlas

 - Avinty

 - Baxter

 - BD

 - Bódegro

 - BUTTERFLY NETWORK, INC

 - Cadence

 - Cardiac Science

 - Cegedim

 - Cerner

 - Change Healthcare

 - ChipSoft

 - Clinisys

 - Code24

 - CognisantMD

 - Corepoint Health

 - CORITY

 - CorrecTek, Inc.

 - Crystal Clinic

 - CureMD

 - DATA INNOVATIONS

 - DEDALUS

 - Digital Workforce

 - DUPLICATEIatric Systems

 - Dynacare

 - eClinicalWorks

 - eIVF

 - Elekta

 - ELLKAY, LLC.

 - ELSEVIER INC.

 - Enterprise Health

 - Exo Works Enterprise

 - FLARE HEALTH, INC.

 - Foundation Medicine

 - Fresenius Medical Care

 - Fujifilm

 - Fujifilm Sonosite

 - Fysicon

 - GE

 - GeniusDoc

 - GERRIT

 - GGD Zuid-Limburg

 - Greenway Health

 - HalfPenny

 - HEALTH CATALYST, INC.

 - Healthstream

 - Hillrom

 - HUS

 - Hyland

 - I.R.I.S.

 - ImageMoverMD

 - In-Common Laboratories

 - Indigo 4 Systems

 - Infian

 - Inform Health

 - Infotrom

 - Intelerad

 - It Starts With Me Health

 - Itemedical

 - Janus

 - Kaiser Permanente

 - KaZee

 - Kitman Labs

 - LabCorp

 - Laurel Bridge

 - Lexmark Enterprise Software

 - LIFE IMAGE

 - LifeLabs

 - LifePoint Health

 - Luma

 - MagView

 - MAK-SYSTEM

 - MCG Diagnostics

 - MEDENT

 - MEDHOST

 - Meditech

 - Midmark

 - Modernizing Medicine

 - Mountain Star Clinical Laboratories

 - MURJ, INC.

 - MyLab

 - NaphCare

 - National Health Service

 - NEC

 - NET HEALTH SYSTEMS, INC.

 - Netsmart

 - NextGen

 - NHN

 - Notable

 - Novari Health

 - NUANCE COMMUNICATIONS INC.

 - Occupational Health Research

 - Octagos

 - Ohio - Public Health Agencies

 - Omda

 - OpenText

 - Orchard Software

 - Oxford Diagnostic Laboratories

 - Oztech

 - PACEMATE, LLC

 - PathGroup

 - Pathology Associates Medical Laboratories

 - PathPresenter

 - PCC

 - PediNotes

 - Philips

 - Point and Click Solutions

 - PointClickCare

 - Practice Fusion, Inc.

 - PRIMARY.HEALTH

 - Primetime Medical Software

 - QuadraMed

 - QUEST DIAGNOSTICS

 - RADNET

 - ReadySet Surgical

 - Relay Health

 - ResMed

 - Rhythm

 - RHYTHMSCIENCE INC

 - Rimidi

 - Royal Devon and Exeter

 - Royal Solutions Group

 - SAP

 - SCC Soft Computer

 - Schiller AG

 - SCI

 - ScottCare

 - Sectra

 - Select Medical

 - Shields Health Care Group

 - Siemens

 - Snowflake

 - Softmedex

 - Solis Mammography

 - Spacelabs

 - Summit Healthcare Services

 - Sunrise Medical Laboratories

 - TeamHealth

 - Telexy HealthCare

 - ThinAir Data Corp.

 - Title21 Health Solutions

 - UiPath

 - University of Arkansas for Medical Sciences

 - VANDERBILT UNIVERSITY MEDICAL CENTER

 - Varian Medical Systems

 - vChart

 - Vibra Healthcare

 - virtuwell

 - Vyne Medical

 - WebReach, Inc

 - WellSky

 - Wisconsin - Public Health Agencies

 - Zeiss

 - ZORGDOMEIN

 

 

 

### 
 Incoming Medication Dispenses and Load/Unload from ADS to Willow Inpatient
 [read the spec](/Tech/TechSpec?spec=5354)

 

 

 Processes dispense, return, and waste information from medication cabinet systems (automated dispense systems), dispensing workflow engines, and robots. Also processes "load/unload" messages received when a drawer, pocket, or bin is emptied or stocked.
 

 

 [Current integrations include ](#)
 

 - Aesynt

 - Allscripts

 - AMERISOURCE BERGEN

 - ARX

 - ARxIUM

 - AutoMed

 - Baxa

 - Baxter

 - BD

 - Betrace

 - California Department of Justice

 - Cato Software Solutions GmbH

 - CGI

 - DEDALUS

 - IntelliGuard

 - Kiro Grifols

 - Loccioni

 - McKesson

 - MEDHOST

 - MedKeeper

 - Morris & Dickson

 - National Committee for Quality Assurance

 - Omnicell

 - Parmed 

 - PhACTs

 - Swisslog

 - TouchPoint Medical

 - TruMed Systems

 - WellSky

 - Zorgi

 

 

 

### 
 Outgoing Verified Medication Orders from Willow Inpatient
 [read the spec](/Tech/TechSpec?spec=5200)

 

 

 Sends verified pharmacy orders. This interface is typically used with cabinet, robotic, TPN, or carousel dispensing systems. It is sometimes used to transmit medication orders to an external medical record or surgery system. Messages are triggered from Willow Inpatinet Pharmacy when a user verifies, re-verifies, discontinues, or modifies an order, reverses a discharge, changes a patient's location such that the dispense location changes, or loads a medication into a station that did not previously contain that medication. We recommend one interface for cabinets and a separate interface for robotic dispensing systems, since the requirements for message content varies between systems, as the robot is dispensing multiple doses of a given medication for a cart, whereas the cabinet order will be dispensed by a user.
 

 

 [Current integrations include ](#)
 

 - Aceso

 - Aesynt

 - Aethon Inc.

 - Allscripts

 - AMERISOURCE BERGEN

 - ANGELEYE HEALTH, INC.

 - ARX

 - ARxIUM

 - AutoMed

 - Baxa

 - Baxter

 - BD

 - Betrace

 - CAPS Pharmacy

 - Capsule Technologies

 - Cardinal Health WaveMark

 - CarepathRx

 - Cato Software Solutions GmbH

 - CBORD

 - CENCORA

 - CenterX

 - Cerner

 - CGI

 - Compass Group

 - COMPUTRITION, INC.

 - Decisio Health

 - E-Health

 - Enclara

 - Equum Medical

 - EVIDENCECARE, LLC

 - GE

 - GETWELLNETWORK, INC.

 - Glytec

 - Health Robotics

 - Hicuity Health

 - ICNet

 - iLabel

 - ILLUMICARE, INC.

 - InfuSystem

 - Inland Empire Health Plan

 - Intellidot

 - IODINE SOFTWARE, LLC

 - ION Solutions

 - Kiro Grifols

 - KONZA

 - Loccioni

 - Manifest Medex

 - Maxor

 - McCreadie Group

 - McKesson

 - MCR TECHNOLOGIES, INC.

 - MEDECS

 - MEDHOST

 - MEDICAL INFORMATICS CORP.

 - Medically Home

 - Meditech

 - MedKeeper

 - MONARCH MEDICAL TECHNOLOGIES

 - National Committee for Quality Assurance

 - NCS

 - Nuclear Medicine Information Systems LLC

 - Omnicell

 - Optum

 - Parata

 - Parlando

 - PhACTs

 - Pharmacy OneSource

 - Philips

 - PREMIER, INC.

 - Q-Centrix

 - QuadraMed

 - Rochester Regional Health Information Organization

 - Saudi Arabia Council of Health Insurance

 - Sentri7

 - Sinteco Robotics

 - SMARTERDX, INC

 - Softmedex

 - Sound Physicians

 - Stanford School of Medicine

 - SURESCRIPTS

 - Swisslog

 - SYMPLR

 - Tecsys

 - TheraDoc

 - Timeless Medical Systems

 - TouchPoint Medical

 - TruMed Systems

 - VigiLanz

 - Vituity

 - Waseel

 - WellSky

 - WOLTERS KLUWER

 - XSOLIS

 

 

 

### 
 Outgoing Patient Administration
 [read the spec](/Tech/TechSpec?spec=5238)

 

 

 Informs external systems of new patient creation, changes to patient demographic information, visits (ADT), registration (guarantors and insurance coverage), allergies, and bed status updates. These messages are triggered from many of Epic's applications. The ability to send allergy updates is only available from the Allergy activity. This interface does not send final coded diagnoses, procedures, or DRGs after a hospital account is coded.
 

 

 [Current integrations include ](#)
 

 - 3M

 - 4MEDICA INC.

 - 4S Informational Systems

 - Abbott Diagnostics

 - abeo

 - ABOUT HEALTHCARE, INC.

 - Access eForms

 - ACCESS TELECARE, LLC (FKA SOC TELEMED)

 - AccuMed

 - AccuReg

 - Achieve

 - ACL Laboratories

 - Acuo Technologies

 - Acusis

 - ADL

 - Advanced Patient Advocacy

 - AdvantEdge Healthcare Solutions

 - Advarra

 - Aesynt

 - Aethon Inc.

 - Aetna

 - Agfa

 - AGILITI

 - AGILON HEALTH

 - AIDOC

 - AirStrip

 - Akamai Practice Management

 - Akousoft

 - Alberta Health Services Public Health Surveillance

 - AlertMD

 - Allscripts

 - Alphatron

 - AMBIENT CLINICAL ANALYTICS

 - Ambient Consulting

 - Ambra Health

 - Ambulancezorg Nederland

 - AMEDTEC

 - American Association of Orthopaedic Executives

 - American Healthware

 - American Well

 - AMERISOURCE BERGEN

 - AMGA

 - Amphion Medical

 - AMTELCO

 - Amyyon

 - Anatechnic

 - ANDOR HEALTH

 - AnewHealth

 - ANGELEYE HEALTH, INC.

 - Anthem

 - Apache

 - ApexHealth

 - API Healthcare

 - Apollo

 - Applied Statistics & Management, Inc

 - APS

 - AQuity Solutions

 - ARAMARK

 - ARC Healthcare Technologies

 - Arintra

 - Arkansas - Public Health Agencies

 - Arkansas Office of Health Information Technology

 - ARMUS

 - Artera

 - Artera

 - Arthrex

 - Artifact Health

 - ARUP Laboratories

 - ARxIUM

 - AS Software

 - Ascencia

 - Ascom

 - Ascribe

 - Aspyra

 - Astraia

 - ATHENAHEALTH, INC.

 - Atlas

 - Atlassian

 - ATT Group

 - AUDACIOUS INQUIRY

 - AuditData

 - Aurora Diagnostics

 - Australian Digital Health Agency

 - AutoMed

 - Autoscribe Informatics

 - AVAILITY

 - Avidex

 - Avinty

 - Axel Health

 - Axians

 - Axis Clinical

 - B. Braun

 - BabySentry

 - BAMBOO HEALTH

 - Baxa

 - Baxter

 - Bayer Healthcare

 - BCB Medical

 - BD

 - Benetech

 - Betrace

 - BinaryFountain

 - Biocoustics Instruments

 - Biogen

 - Blue Cross Blue Shield of Minnesota

 - Blue Cross/Blue Shield

 - Bódegro

 - BookWise Solutions

 - BORN

 - Bossers & Cnossen

 - Boston Scientific

 - Bottomline

 - Bracco

 - BRAID.HEALTH INC.

 - Brainlab

 - BREG

 - BRIGHT.MD

 - Brightree

 - BRIT

 - Bronx Regional Health Information Organization

 - BUDDI.AI

 - BUTTERFLY NETWORK, INC

 - C/NET Solutions

 - Caduceus

 - Cadwell

 - California - Public Health Agencies

 - California Department of Justice

 - California Information Exchange

 - CANFIELD SCIENTIFIC, INC.

 - Capsule Technologies

 - Cardiac Science

 - Cardinal Health WaveMark

 - Cardiocom

 - Cardone Record Services

 - Care Continuity

 - Care Directives

 - Carecloud

 - CAREDX INC.

 - CAREEVOLUTION

 - CareLogistics

 - CAREMESSAGE

 - CarepathRx

 - Carestream Dental

 - Carestream Health

 - CareView

 - Carevive

 - CAREXM

 - CASMED

 - Cato Software Solutions GmbH

 - CBAY Transcription Services, Inc.

 - CBORD

 - Cedar

 - Cedaron

 - CellNetix

 - Centaur Software

 - Centene Corporation

 - Center for Disease Control

 - CENTRAK, INC.

 - CentralLogic

 - Cerner

 - CGI

 - Change Healthcare

 - Chesapeake Regional Information System for Our Patients

 - Cigna

 - CIPHERHEALTH, INC.

 - CIS Oncology

 - Cisco

 - Citra Health Solutions

 - CIVICA

 - Clairvia

 - Clario

 - Clevermed

 - Click Commerce

 - Clinical Computer Systems, Inc.

 - Clinical Science System

 - CliniSync

 - Clinisys

 - ClinLab

 - CloudMed Solutions

 - CMS

 - CoActiv Medical

 - CODAMETRIX

 - CodeRyte

 - Collective Medical Technologies

 - Comercer

 - Common Cents Solutions

 - COMMURE

 - Compass Group

 - CompuGroup Medical

 - Compulink

 - Compumedics

 - Computer Trust Corporation

 - COMPUTRITION, INC.

 - Conifer Health Solutions

 - Connecticut - Public Health Agencies

 - ConnectiveRx

 - Consensus Medical Systems

 - Consight

 - Constellation Kidney Group

 - Contessa Health

 - Continuum Health Partners

 - CONWORX

 - CoPath

 - CORHIO

 - CORI

 - CORITY

 - Cortex Medical Management Systems

 - Covisint Corporation

 - CPR Technologies

 - CPSI

 - Craneware

 - Crescendo Systems Corporation

 - CribNotes

 - CRITEX

 - CS STARS

 - Cureatr

 - Current Health

 - CVS Pharmacy

 - Cybernius Medical Ltd.

 - CyncHealth

 - DATA INNOVATIONS

 - Data Management Systems

 - DataStar Systems

 - DATAVANT

 - DDOTS

 - DEDALUS

 - Delaware Health Information Network

 - Delegate Technology Group

 - DELIVERHEALTH

 - Delta

 - Dentrix

 - DeRoyal

 - Deutsche Telekom

 - DFM Technologies

 - Diagnostic Lab Services, Inc.

 - Diasoft

 - Dictate IT

 - Digisonics

 - Digital Healthcare

 - Digital Innovations, Inc.

 - DJO GLOBAL, INC.

 - DOCASAP, INC.

 - Dolbey

 - DoseMonitor

 - DR Systems

 - Dräger

 - DRDOCTOR

 - D-Scope Systems

 - DUPLICATEIatric Systems

 - E.Novation

 - Easy Software

 - ec2

 - eClinicalWorks

 - Eclipsys

 - EDCi

 - EDCO

 - Edelberg

 - EDGE

 - EF Software

 - Efertility

 - EHEALTH TECHNOLOGIES

 - EHS

 - eIVF

 - Electronic

 - Elekta

 - Elevance

 - ELLKAY, LLC.

 - ELSEVIER INC.

 - Emageon

 - Embla

 - EMC2

 - EmCare

 - EMDAT

 - eMDs

 - EMIS

 - EMS Software

 - emsCharts

 - Enclara

 - ENDOSOFT LLC

 - Ensemble Health Partners

 - Enterprise Health

 - Envision

 - Envision Radiology

 - ePath Logic, Inc.

 - Equum Medical

 - ESO

 - ETIOMETRY, INC.

 - eTransPlus

 - EVERLIGHT RADIOLOGY

 - EVIDENCECARE, LLC

 - EvoHealth

 - Evolent Health

 - Exact (Business Software)

 - Exan Academic

 - Excel Medical

 - Exo Works Enterprise

 - EXPERIAN HEALTH, INC.

 - Extract Systems

 - EyeCare Leaders

 - Family HealthCare Network

 - FinThrive

 - Flatiron

 - Fleischhacker

 - Flexsys

 - FLIGHT VECTOR, LLC

 - Florida - Public Health Agencies

 - ForCare

 - FORCE THERAPEUTICS

 - FormFast

 - Forsante

 - Foundation Systems Inc.

 - Fresenius Medical Care

 - Fuel Medical

 - Fujifilm

 - Fusion

 - FutureNet

 - Fysicon

 - Gambro

 - Gastro Health

 - GE

 - GENE42

 - GENEVA HEALTH SOLUTIONS

 - Genial Genetics

 - GeniusDoc

 - Georgia - Public Health Agencies

 - Georgia Regional Academic Community Health Information Exchange

 - Getinge

 - GETWELLNETWORK, INC.

 - Global Health

 - Global Mobility Laboratory

 - GlobeStar

 - GLOOKO, INC.

 - Glytec

 - gMed

 - Gottlieb

 - Graphnet

 - Grasp

 - Great Lakes Health Information Exchange

 - Greenway Health

 - HAAD

 - Haemonetics

 - HalfPenny

 - Hasana

 - Hawaii Health Information Exchange

 - HCI Solutions

 - HCS

 - HD Clinical

 - HDX

 - HEALOGICS, INC.

 - HEALTH CATALYST, INC.

 - Health Outcomes Sciences

 - Health Recovery Solutions

 - HealthBridge

 - Healthcare Control Systems

 - Healthcare Systems & Technologies

 - HealtheCNY

 - HealtheConnections

 - HEALTHeLINK

 - HealthFirst

 - Healthgrades

 - HealthHIE Nevada

 - HealthInfoNet

 - Healthmap Solutions

 - HealthNautica

 - HealthNet

 - HealthPro Medical Billing

 - HealthShare Exchange

 - HealthSnap

 - Healthstream

 - HealthStream

 - HealthWare Systems

 - Healthways

 - Heart Imaging Technologies

 - Heartbase

 - Heartland Information Services

 - Heidelberg Engineering

 - Helix

 - Hermes Medical Solutions

 - Hero Health

 - Hicuity Health

 - HID GLOBAL CORPORATION

 - Highmark

 - Hillrom

 - Hitachi

 - HLA Data Systems LLC

 - HMI

 - HMS

 - Hologic

 - Homecare Homebase

 - Horizon

 - Hospital Diagnostic Imaging Repository Services

 - HOTflo

 - Houston - Public Health Agencies

 - HUMANA

 - Humata Health

 - Huntleigh Diagnostics

 - HUS

 - Hyland

 - I.R.I.S.

 - IBM

 - ICT HCTS

 - Idaho Health Data Exchange

 - Ideagen

 - Idox Health

 - iGuana

 - Ikonopedia

 - Illinois - Public Health Agencies

 - Illinois Office of Health Information Technology

 - ILLUMICARE, INC.

 - ImageMoverMD

 - ImageTrend

 - ImageVision.net

 - ImagineSoftware

 - iMDsoft

 - iMedX

 - Imorgon

 - IMPRIVATA, INC.

 - Indian Health Service

 - Indiana - Public Health Agencies

 - Infian

 - INFINITT NORTH AMERICA

 - Infinity Healthcare

 - InfoMedix

 - Infor Global Solutions

 - Infotrom

 - InfraWare

 - InfuSystem

 - INGENIOUS MED

 - Initiate

 - Innivo

 - Innoforce

 - INNOVACCER INC.

 - Insight HealthCare Information Systems

 - Insignia Medical Systems

 - Instrumentation Laboratory (Werfen)

 - InstyMeds

 - Integrated Informatics Inc.

 - Integrated Ophthalmic Systems

 - InteGreat

 - Intelerad

 - INTELLICURE, INC.

 - IntelliDose

 - Intelligent Business Solutions

 - IntelliGuard

 - INTERFACEWARE

 - Intermedix

 - InterSystems

 - InvisALERT

 - IODINE SOFTWARE, LLC

 - ION Solutions

 - IQMax

 - iRCODER.COM

 - iRhythm

 - IRIS (Intelligent Retinal Imaging Systems)

 - Irisoft

 - Isoprime

 - Itemedical

 - ITxM

 - JLG Medical Transcription Services

 - Jvion

 - K2 Medical Systems

 - Kainos

 - Kansas Health Information Network

 - Karl Storz

 - Keane

 - Kentucky - Public Health Agencies

 - Kentucky Health Information Exchange

 - Keriton Kare

 - KFL&A Public Health

 - Konica Minolta

 - KONZA

 - Kramer Technologies

 - Krames

 - Krishagni Solutions

 - LabCorp

 - Laborie Medical Technologies

 - LabVantage

 - Lameris Ootech

 - Landacorp

 - Lanier

 - Lattice Solutions

 - LEANTAAS, INC.

 - Lexmark Enterprise Software

 - L-Force

 - Liberty Software

 - LIFE IMAGE

 - Life Systems International

 - LifePoint Health

 - Limber Health

 - LivaNova

 - Locus Health

 - Locus Solutions

 - Logis Solutions

 - LogixHealth

 - LPiT Solutions

 - LUMEDX

 - Lumin Medical LLC

 - LVM Systems

 - Lynx Medical Systems

 - M*Modal

 - Mach7 Technologies

 - Macro Helix

 - Magentus

 - MagView

 - Mammography Reporting System

 - Manifest Medex

 - Masimo

 - Maxor

 - MCG Diagnostics

 - McKesson

 - MCR TECHNOLOGIES, INC.

 - MD REVOLUTION, INC.

 - MDA Technologies

 - MDI SOLUTIONS

 - MDLIVE, INC.

 - MDM Healthcare

 - MDnetwork

 - MD-Staff

 - MDTECH

 - MealIQ

 - Med Receivables

 - Med2020 Health Care Software Inc.

 - MedAptus

 - MedAssets

 - MedData

 - MEDEANALYTICS

 - MEDECS

 - MEDENT

 - MEDHOST

 - MEDICAL DATA SYSTEMS

 - Medical Decision Network

 - Medical Genetics Information System

 - MEDICAL INFORMATICS CORP.

 - Medical Management Resources, Inc.

 - Medical Measurement Systems

 - Medically Home

 - Medicare Shared Saving Program

 - Medicom Health

 - Medicor Imaging

 - MediLIMS

 - Medilogik

 - MedInformatix

 - Mediquant

 - MediServe

 - Medisoft

 - Meditech

 - MedKeeper

 - Medline

 - MEDNAX

 - MEDNITION INC.

 - MedPlus

 - Med-Scribe

 - MedServe

 - Medstreaming

 - Medtronic

 - Medvantx

 - MedVision AG

 - Mellowood Medical

 - Mennen

 - MercuryMD

 - Merge Healthcare

 - MetroPlus

 - MGC Diagnostics

 - Michigan - Public Health Agencies

 - Michigan Health Connect

 - Michigan Health Information Network Shared Services

 - MicroMan2000

 - Microsoft

 - Midmark

 - MIET Healthcare

 - Milagro AI

 - MILLIMAN, INC.

 - Mindray

 - Minnesota - Public Health Agencies

 - Missouri - Public Health Agencies

 - Mobile Aspects

 - MOBILE HEARTBEAT, LLC

 - MobileMD

 - Modernizing Medicine

 - MONARCH MEDICAL TECHNOLOGIES

 - Morgan Scientific

 - Morris & Dickson

 - Morrisey

 - Mortara

 - MRO Corp

 - MSN

 - MULESOFT, INC.

 - Multidata

 - MURJ, INC.

 - My Vision Express

 - MYHEALTH ACCESS NETWORK

 - MyHealth First Network

 - MyLab

 - MYTONOMY INC.

 - NABIDH

 - NantHealth

 - National Cancer Institute

 - National Health Service

 - Natus

 - Navicure

 - naviHealth

 - Navina

 - NCS

 - NDCHealth

 - NEBO

 - Nebraska Health Information Initiative

 - NEC

 - NEC Unified Solutions

 - NEDOCS

 - NET HEALTH SYSTEMS, INC.

 - Netalytics

 - Netsmart

 - Netsoft, Inc.

 - New England Donor Services

 - New Jersey - Public Health Agencies

 - New Jersey Innovation Institute

 - New York - Public Health Agencies

 - New York City - Public Health Agencies

 - NewCura

 - NextGate Solutions

 - NextGen

 - Nexus

 - NHN

 - Nihon Kohden

 - nobl Health

 - North American Partners in Anesthesia

 - North Carolina - Public Health Agencies

 - North Carolina Health Information Exchange Authority

 - Northwell Health

 - Notable

 - Nova Biomedical

 - NovaRad

 - Novo RCM Solutions

 - NovoPath

 - NowPow

 - NRC

 - nSpire

 - NUANCE COMMUNICATIONS INC.

 - Nuclear Medicine Information Systems LLC

 - Nutshell

 - Nuvem

 - O&M Solutions

 - Occupational Health Research

 - Ocuco

 - Odeza

 - OFFICE ALLY

 - Olympus Endoworks

 - Olympus Medical Systems

 - Omnicell

 - ONCO Inc.

 - OncoChart

 - ONEHEALTHPORT

 - Onepoint Health Services

 - OneView

 - ONRAD

 - Ontario Ministry of Health

 - Ontario Patient Data Reporting

 - OntarioMD

 - OpenTempo

 - OpenText

 - Ophthalmic Imaging Systems

 - Optimal Solutions

 - Optum

 - OptumRx (Catamaran)

 - ORACLE

 - Orange County Health

 - Orchard Software

 - Oregon - Public Health Agencies

 - Orion Health

 - Ortech

 - Oscar Insurance

 - OSG

 - Össur

 - OTiS Medical Analytics

 - Owl

 - OZ Systems

 - PALANTIR

 - Pangaea Information Technologies

 - PAR Excellence

 - Parallon Business Solutions

 - Parata

 - PARKLAND CENTER FOR CLINICAL INNOVATION

 - Pascal Metrics

 - PathGroup

 - PathView Systems

 - PATIENT RESOURCE LLC

 - PATIENTIQ

 - PatientPrompt

 - PCARE BY UNIGUEST

 - PDHI

 - PDX

 - Pediatrix

 - PediNotes

 - Pelitas

 - Penn Medicine

 - Pennslyvania - Public Health Agencies

 - PenRad

 - Pentax

 - Perahealth

 - PERFECTSERVE, INC.

 - PERIGEN

 - Pharmacy OneSource

 - Pharmhos

 - Philips

 - PHREESIA, INC.

 - Picis

 - PinkRoccade Healthcare

 - pMDsoft, Inc.

 - Point and Click Solutions

 - PointClickCare

 - Polycon

 - Portavita

 - Post Acute Analytics

 - PowerHealth

 - Praxis

 - PRC Excellence

 - PREMIER, INC.

 - Press Ganey

 - Primordial Designs

 - ProCare Rx

 - Proficient Health

 - ProSolv CardioVascular

 - ProVation Medical

 - PROVIDERFLOW

 - Provox

 - Psyche

 - Pt Pal

 - Puritan Bennett

 - Q-Centrix

 - QS/1

 - QSI

 - Quadax

 - QuadraMed

 - Quality Health Network (QHN)

 - Quantros

 - Quantum Secure

 - QUEST DIAGNOSTICS

 - QVENTUS, INC.

 - R1 RCM

 - RADIA INC.

 - Radiologic Associates, P.C.

 - Radiology Associates Imaging Centers (FL)

 - Radiology Associates of Hawaii

 - Radiology Partners

 - Radiometer America

 - RADNET

 - Rauland

 - Readiness Rounds

 - Real-Time Outbreak Disease Surveillance Lab (RODS at University of Pittsburgh)

 - Recondo

 - RecordsOne

 - REDOX

 - Rehab Documentation Company, Inc.

 - Relay Health

 - Remedi SeniorCare

 - Resideo

 - RESPOND CLINICAL INC.

 - RestorixHealth

 - RevSpring

 - Revvity

 - Rhapsody

 - RISKONNECT, INC.

 - RLDATIX

 - Roche Diagnostics

 - Rosch Visionary Systems

 - Rotem

 - Roundtrip

 - RTZ Systems

 - RVC

 - Rx Care Assurance

 - Safecare Technology

 - Safety Net Connect

 - Salar

 - SALESFORCE

 - SAP

 - ScanMed

 - SCC Soft Computer

 - Schiller AG

 - SCI

 - ScImage

 - ScottCare

 - Script Care

 - ScriptPro

 - Sectra

 - Securitas Healthcare

 - Select Medical

 - Sentri7

 - Sentry Data Systems

 - Serial Multivision

 - ServiceHub

 - Sharp Health Plan

 - Shields Health Care Group

 - Siemens

 - Signify Health

 - Simplee

 - SimplexGrinnell

 - Singapore Ministry of Health Holdings

 - SIS

 - SISCO

 - Skylight

 - SMARTERDX, INC

 - Smith + Nephew

 - Sodexo

 - Softek Solutions, Inc.

 - SoftLink International

 - SoftMed

 - Softmedex

 - SoftScript, Inc.

 - SoftWriters

 - SolCom

 - Solis Mammography

 - Soliton IT

 - Solventum

 - Somerset

 - Somnomedics

 - Somnoware

 - SONIFI Solutions

 - Sonomed Escalon

 - Soobr

 - Sotera Wireless

 - Sound Physicians

 - SourceCorp

 - South Carolina - Public Health Agencies

 - South Dakota Department of Health

 - Spacelabs

 - Spectrum Medical

 - Spheris 

 - Spok

 - SSi Healthcare

 - SSIMED

 - St. George's Genomics Service

 - St. Jude's

 - Standing Stone

 - StarTel

 - STEMSOFT

 - Stericycle Communication Solutions

 - STERIS Corporation

 - STOPware

 - Streamline Health

 - Streets Heaver

 - Strivant Health

 - Stryker

 - StuderGroup

 - Sun

 - Sun Ridge Systems, Inc.

 - SUNQUEST

 - Sunrise Medical Laboratories

 - SunRx

 - Sussex Biologicals

 - Swisslog

 - SXC

 - Sybase

 - SYFT

 - SYMPLR

 - Synedra

 - Sysmex Corporation

 - SystemLink

 - Tacoma Radiology Associates

 - Tarawerkz

 - Taylor Healthcare

 - TCM

 - TDSS

 - Team Health

 - TeamHealth

 - Tecsys

 - TELCOR

 - TeleResults

 - TELETRACKING

 - Televox

 - Telexy HealthCare

 - TelmedIQ

 - Tennessee Hospital Association

 - Teramedica

 - Texas - Public Health Agencies

 - The Advisory Board

 - The Claro Group

 - The IPC Group

 - TheraDoc

 - Therigy

 - Thermo Fisher Scientific

 - Theronyx

 - Thornberry

 - Timeless Medical Systems

 - T-Metrics

 - Topcon Medical Systems

 - TouchPoint Medical

 - TrakGene

 - Transaction Data Systems

 - Transcend

 - TransUnion

 - Trend Care Systems

 - Truven Health

 - TSG Integrations

 - T-System

 - Twistle

 - UHLIG LLC

 - UKG

 - Uniform Data Systems

 - UnisonMD

 - United Healthcare

 - United Telemanagement Corporation

 - Universal Research Solutions, LLC

 - University of Arkansas for Medical Sciences

 - University of California

 - USA

 - Utah - Public Health Agencies

 - UTECH

 - Varian Medical Systems

 - VAXCARE

 - vChart

 - Velos

 - Verato

 - Vergesolutions

 - Vermont Information Technology Leaders

 - Versio

 - Versus

 - Via Oncology

 - Vidistar

 - VigiLanz

 - Vignette

 - Virginia - Public Health Agencies

 - Virtual Radiologic

 - VISAGE IMAGING, INC.

 - Vision Chips

 - VISION SOFTWARE TECHNOLOGIES, INC.

 - VisionTree

 - Visonex

 - VISUS

 - VITAL

 - Vital Images

 - VitalAxis

 - Vitalhub

 - Vituity

 - Vizabli

 - VIZIENT INC.

 - VOLPARA HEALTH, INC.

 - Vyaire Medical

 - Vyne Medical

 - Waba

 - Waystar

 - WebMedX

 - WebPT

 - WebReach, Inc

 - WeInfuse

 - Wellbeing Software

 - Wellpartner

 - WellSky

 - Wellsoft

 - West Virginia - Public Health Agencies

 - WestCall

 - Whytespace

 - Wisconsin - Public Health Agencies

 - Wisconsin PDMP Routing Hub

 - WOLTERS KLUWER

 - XIFIN

 - XSOLIS

 - Xtend

 - Xtract Solutions

 - Yellowstone Pathology Institute (YPI)

 - Yenlo

 - ZAN

 - Zeiss

 - Zoll

 - Zorgi

 - Zotec Partners

 - ZULAFLY, INC.

 

 

 

### 
 Outgoing Formulary Information to ADS from Willow Inpatient Interface
 [read the spec](/Tech/TechSpec?spec=5270)

 

 

 Also known as ADS Console Management. The interface can be used to populate the master medication list of an automated dispense system when a medication is added or removed from the Willow Inpatient Pharmacy formulary.
 

 

 [Current integrations include ](#)
 

 - ARxIUM

 - AutoMed

 - BD

 - GETWELLNETWORK, INC.

 - Health Robotics

 - Omnicell

 - RLDATIX

 - SURESCRIPTS

 - Swisslog

 - VigiLanz

 

 

 

### 
 Incoming EOB Scanning
 [read the spec](/Tech/TechSpec?spec=5372)

 

 

 Receives messages that notify the billing applications (Resolute Hospital, Professional, Home Health (Dorothy), or Enterprise Billing) that a scanned explanation of benefits document exists. Receiving a message opens a new payment batch in the appropriate billing application based on scan type.
 

 

 [Current integrations include ](#)
 

 - EMC2

 - Hyland

 - Lexmark Enterprise Software

 - McKesson

 - MedPlus

 - OpenText

 - QUEST DIAGNOSTICS

 - SolCom

 - Streamline Health

 

 

 

### 
 Incoming Device Data
 [read the spec](/Tech/TechSpec?spec=5374)

 

 

 Receives discrete measurements from patient monitoring and documentation devices. The messages file to the application, where the data can be validated by the user and added to the chart, or in the case of surgical procedures, can be set to automatically validate and file to the chart. This type of integration is usually done with device aggregators to file samples from continuous physiological monitoring. It is not used for consumer-initiated monitoring or home monitoring.
 

 

 [Current integrations include ](#)
 

 - Acutronic Medical

 - A-S Medication Solutions LLC

 - B. Braun

 - Baxter

 - Bayer Healthcare

 - BD

 - Bernoulli

 - BMA

 - Capsule Technologies

 - Cardiac Science

 - CASMED

 - Cerner

 - Cheetah Medical

 - Clinical Computer Systems, Inc.

 - Constellation Kidney Group

 - CooperSurgical

 - CorVascular

 - Criticare Technologies

 - Deltex Medical

 - Diasoft

 - Dräger

 - Edwards LifeSciences

 - Excel Medical

 - Fresenius Medical Care

 - Fukuda Denshi

 - Gambro

 - Gateway Electronic Medical Management Systems

 - GE

 - GLOOKO, INC.

 - Hamilton Medical

 - Hillrom

 - Homecare Homebase

 - Hutchinson Technology

 - ICU Medical

 - INOmax

 - IRadimed

 - Iris

 - K2 Medical Systems

 - Kinseed

 - LiDCO

 - LivaNova

 - Maquet

 - Masimo

 - McKesson

 - MDI SOLUTIONS

 - MEDICAL INFORMATICS CORP.

 - Medically Home

 - Medtronic

 - Midmark

 - Mindray

 - Mobile Aspects

 - NantHealth

 - NEUROPTICS, INC.

 - Neximatic

 - Nihon Kohden

 - Nonin Medical

 - NxStage

 - OUTSET MEDICAL, INC.

 - Patient-Centered Outcomes Research Institute

 - Penlon

 - PERIGEN

 - Philips

 - PULSION Medical Systems

 - Puritan Bennett

 - Radiometer America

 - Rauland

 - Roche Diagnostics

 - SenTec

 - Siemens

 - Smith + Nephew

 - Smiths Medical

 - Sotera Wireless

 - Spacelabs

 - Spectrum Medical

 - Stryker

 - SURESCRIPTS

 - Talis Clinical

 - Teleflex

 - Terumo

 - Transcend

 - Vyaire Medical

 - WestCall

 - ZAN

 - Zoll

 

 

 

### 
 Incoming MPI and Demographics Query
 [read the spec](/Tech/TechSpec?spec=staged%2FIncoming%20MPI%20and%20Demographics%20Query%20Interface%20Technical%20Specification.pdf)

 

 

 Receives and responds to queries for demographic data from an external system when Epic is the EMPI. Does not modify patient data.
 

 

 [Current integrations include ](#)
 

 - Acousoft

 - Afas

 - Agfa

 - Akamai Practice Management

 - Akousoft

 - Ambulancezorg Nederland

 - AMEDTEC

 - Astraia

 - ATHENAHEALTH, INC.

 - ATT Group

 - Audiologicx

 - AuditData

 - Axians

 - BCB Medical

 - BD

 - BMA

 - Cardiac Science

 - Caresharing

 - Cato Software Solutions GmbH

 - Change Healthcare

 - CIS Oncology

 - Click Commerce

 - Clinisys

 - CompuGroup Medical

 - Corepoint Health

 - CRITEX

 - Curit

 - DECOS

 - DEDALUS

 - Deutsche Telekom

 - Diasoft

 - E.Novation

 - Easy Software

 - Efertility

 - Elekta

 - ELLKAY, LLC.

 - Evry

 - Expansion

 - Fleischhacker

 - ForCare

 - Fresenius Medical Care

 - GE

 - Gecko-ict

 - Genial Genetics

 - GERRIT

 - Helix

 - Hillrom

 - HOTflo

 - I.R.I.S.

 - Ideagen

 - IHOMER

 - iMDsoft

 - Infoland

 - Infotrom

 - Innoforce

 - Instrumentation Laboratory (Werfen)

 - Itemedical

 - Laborie Medical Technologies

 - Lameris Ootech

 - Lexmark Enterprise Software

 - Lifelines

 - LifePoint Health

 - Medical Measurement Systems

 - Medical Workshop

 - Meditech

 - Medtronic

 - Mela Solutions

 - Mellowood Medical

 - Meridian Bioscience

 - MicroMan2000

 - Microsoft

 - Mindray

 - Natus

 - Netpoint Group

 - Neuro Medical

 - NHN

 - Nihon Kohden

 - NUANCE COMMUNICATIONS INC.

 - Olympus Endoworks

 - OSG

 - Philips

 - PinkRoccade Healthcare

 - Portavita

 - Posicom

 - Radiometer America

 - REDOX

 - RLDATIX

 - Roche Diagnostics

 - RVC

 - SanaNet

 - Sectra

 - Softmedex

 - Solution-Team

 - Spacelabs

 - Sysmex Corporation

 - SystemLink

 - Technidata

 - TrakGene

 - University Hospitals Birmingham

 - Varian Medical Systems

 - VISUS

 - VogelCode

 - Waba

 - WellSky

 - ZAN

 

 

 

### 
 Incoming Personnel Management
 [read the spec](/Tech/TechSpec?spec=staged%2FIncoming%20Personnel%20Management%20Interface%20Technical%20Specification.pdf)

 

 

 Receives messages from an external user management system to create, update, or delete user records in Epic. While this interface can build the shell of a user record and associate role based information, this interface can't completely automate the addition of new users to an organization, because Epic has settings and features built by association to a user record. These settings cannot be controlled by an external system. We recommend you use the [Personnel Management web services](https://open.epic.com/Interface/WebServices#PersonnelManagement) rather than this HL7v2 interface as it offers significantly greater capabilities.
 

 

 [Current integrations include ](#)
 

 - ORACLE

 - Orion Health

 

 

 

### 
 Incoming Location and Department Information
 [read the spec](/Tech/TechSpec?spec=staged%2FIncoming%20Location%20and%20Department%20Information%20Interface%20Technical%20Specification.pdf)

 

 

 Used to automate synchronization of the facility structure (locations and departments). To this point, this integration has been completed only with custom in-house systems previously developed by our organizations.
 

 

### 
 Outgoing MPI and Demographics Query
 [read the spec](/Tech/TechSpec?spec=5249)

 

 

 Queries an external EMPI during a patient search after a local search is performed. The correct patient is then selected by a user from a list of candidates returned in the response message.
 

 

 [Current integrations include ](#)
 

 - Allscripts

 - Initiate

 - NHN

 - NSP

 

 

 

### 
 Outgoing Claim Scrubber Query
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20Claim%20Scrubber%20Query%20Interface%20Technical%20Specification.pdf)

 

 

 Claim Scrubbing functionality integrated into various workflows in Resolute, Epic's billing system.
 

 

 [Current integrations include ](#)
 

 - EXPERIAN HEALTH, INC.

 - Netwerkes (Ingenix)

 - Optum

 - RCxRules

 - White Plume Technologies, LLC

 

 

 

### 
 Outgoing Address Verification Query
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20Address%20Verification%20Query%20Interface%20Technical%20Specification.pdf)

 

 

 Queries a third-party system to verify and validate patient-level and guarantor-level demographic data the time of registration. This interface works with Prelude, Epic's registration system.
 

 

 [Current integrations include ](#)
 

 - AVAILITY

 - Change Healthcare

 - EXPERIAN HEALTH, INC.

 - FinThrive

 - GE

 - HealthNautica

 - Loxogon

 - McKesson

 - MedAssets

 - Mindray

 - NUANCE COMMUNICATIONS INC.

 - Optum

 - Pelitas

 - Relay Health

 - Search America

 - SSIMED

 - The Advisory Board

 - TransUnion

 - Waystar

 

 

 

### 
 Outgoing Clinical Documentation Flowsheet Data
 [read the spec](/Tech/TechSpec?spec=5286)

 

 

 Sends discrete documentation flowsheet data to another system.
 

 

 [Current integrations include ](#)
 

 - 3M

 - ABOUT HEALTHCARE, INC.

 - Accuhealth

 - Aceso

 - AGILEMD, INC.

 - Allscripts

 - Ambulancezorg Nederland

 - Anatechnic

 - Apache

 - API Healthcare

 - A-S Medication Solutions LLC

 - ATHENAHEALTH, INC.

 - Atlas

 - Avidex

 - Baxter

 - BD

 - Bernoulli

 - BHAI Systems

 - BioIntellisense

 - BMA

 - Bronx Regional Health Information Organization

 - Capsule Technologies

 - Caradigm

 - CAREDX INC.

 - CAREEVOLUTION

 - CareLogistics

 - CBORD

 - Cerner

 - CIPHERHEALTH, INC.

 - Clairvia

 - Clevermed

 - Clinical Computer Systems, Inc.

 - CliniSync

 - Comercer

 - Compass Group

 - CORHIO

 - Decisio Health

 - Delaware Health Information Network

 - Denver County (CO) - Public Health Agencies

 - Dolbey

 - eBasis

 - Efertility

 - Elekta

 - ELSEVIER INC.

 - Equum Medical

 - ESO

 - findhelp

 - GE

 - GETWELLNETWORK, INC.

 - GlobeStar

 - GOOGLE LLC

 - Harbor Performance Initiative

 - Harris

 - Hasana

 - HCI Solutions

 - Health Outcomes Sciences

 - HealthSnap

 - HealthStream

 - hellocare

 - Hero Health

 - Hicuity Health

 - Hillrom

 - ICNet

 - iD

 - IHOMER

 - Infor Global Solutions

 - Inland Empire Health Plan

 - IntelliDose

 - IODINE SOFTWARE, LLC

 - IQMax

 - Jvion

 - K2 Medical Systems

 - Kansas Health Information Network

 - LEANTAAS, INC.

 - Louisiana - Public Health Agencies

 - LUMEDX

 - M*Modal

 - Maine - Public Health Agencies

 - MCG Diagnostics

 - McKesson

 - MCR TECHNOLOGIES, INC.

 - MDI SOLUTIONS

 - MEDICAL INFORMATICS CORP.

 - MediServe

 - Michigan Health Connect

 - Microsoft

 - MONARCH MEDICAL TECHNOLOGIES

 - Morrisey

 - Natus

 - naviHealth

 - NEC

 - New England Donor Services

 - New York - Public Health Agencies

 - nobl Health

 - NowPow

 - NUANCE COMMUNICATIONS INC.

 - Nuclear Medicine Information Systems LLC

 - Ontario Ministry of Health

 - Ontario Patient Data Reporting

 - Optimal Solutions

 - Optum

 - Oregon - Public Health Agencies

 - Orion Health

 - PALANTIR

 - Pangaea Information Technologies

 - Pascal Metrics

 - PATIENT ENGAGEMENT ADVISORS, LLC

 - PCARE BY UNIGUEST

 - Pediatrix

 - PediNotes

 - Penn Medicine

 - Perahealth

 - PERIGEN

 - Philips

 - PinkRoccade Healthcare

 - PLATOCODE

 - PREMIER, INC.

 - Q-Centrix

 - QuadraMed

 - QVENTUS, INC.

 - Rauland

 - Rhode Island - Public Health Agencies

 - RLDATIX

 - SAP

 - ScanMed

 - Sentri7

 - Serial Multivision

 - SISCO

 - SMARTERDX, INC

 - Sodexo

 - SONIFI Solutions

 - Spectrum Medical

 - Spok

 - Stericycle Communication Solutions

 - Streamline Health

 - Stryker

 - SYMPLR

 - TCM

 - TELETRACKING

 - TheraDoc

 - Theronyx

 - TIBCO

 - UKG

 - Uniform Data Systems

 - UNITE US, INC.

 - University of Florida Health

 - Unspecified vendor(s) through open.epic

 - VigiLanz

 - VITAL

 - Vizabli

 - WestCall

 - Whytespace

 - WOLTERS KLUWER

 - XSOLIS

 

 

 

### 
 Incoming Appointment Scheduling
 [read the spec](/Tech/TechSpec?spec=5384)

 

 

 Receives scheduling information from external systems to show that information in Epic or provide clinical access to the patient's appointments. It can receive messages for new, rescheduled, updated, or canceled appointments, as well as notifications that a patient did not show for an appointment.
 

 

 [Current integrations include ](#)
 

 - AccuReg

 - ADP AdvancedMD

 - Agfa

 - Akamai Practice Management

 - Allscripts

 - Amelia 

 - American Well

 - ANDOR HEALTH

 - Artera

 - Artera

 - ATHENAHEALTH, INC.

 - AuditData

 - CAREMESSAGE

 - Carestream Health

 - Cerner

 - CIPHERHEALTH, INC.

 - CLEARWAVE, INC.

 - Clinisys

 - Dentrix

 - eClinicalWorks

 - eIVF

 - Elekta

 - Enterprise Health

 - Envera Health

 - Exan Academic

 - EXPERIAN HEALTH, INC.

 - Experity

 - Galvanon

 - GE

 - GENEVA HEALTH SOLUTIONS

 - GOHEALTH URGENT CARE

 - Healthcare Systems & Technologies

 - K HEALTH

 - Kestral

 - Locus Solutions

 - McKesson

 - Mediconsult

 - MediServe

 - MURJ, INC.

 - myOnsite Healthcare

 - Netpoint Group

 - Nexa

 - NextGen

 - Octagos

 - Odeza

 - Orion Health

 - PATIENT ENGAGEMENT ADVISORS, LLC

 - Praxis

 - QuadraMed

 - REDOX

 - Royal Solutions Group

 - SALESFORCE

 - SAP

 - SCI

 - Sectra

 - Shields Health Care Group

 - Solis Mammography

 - Soliton IT

 - Stericycle Communication Solutions

 - TELADOC, INC.

 - Varian Medical Systems

 - Velox Imaging

 - WeInfuse

 - Wellbeing Software

 - WellSky

 - Zipnosis

 - Zorgi

 

 

 

### 
 Incoming Schedule Query
 [read the spec](/Tech/TechSpec?spec=5322)

 

 

 Receives patient information queries and returns information regarding scheduled appointments.
 

 

 [Current integrations include ](#)
 

 - CGI

 - Softmedex

 

 

 

### 
 Incoming Clinical Documentation Flowsheet Data
 [read the spec](/Tech/TechSpec?spec=5379)

 

 

 Receives discrete patient data from an external system (where a user has previously validated the data), and files directly to the documentation flowsheet. This interface can also be used with clinically regulated home monitoring device vendors for post discharge monitoring programs, home care, home hospice, or other types of patient monitoring episodes.
 

 

 [Current integrations include ](#)
 

 - 3M

 - Abbott Diagnostics

 - ABOUT HEALTHCARE, INC.

 - Accuhealth

 - Aceso

 - Aetna

 - Aetonix

 - AGILEMD, INC.

 - AGILON HEALTH

 - AirStrip

 - AIT

 - all.health

 - Alphatron

 - Ambra Health

 - Ambry Genetics

 - Ambulancezorg Nederland

 - AMC Health

 - American Well

 - AmeriHealth Caritas

 - ANDOR HEALTH

 - ANGELEYE HEALTH, INC.

 - Anthem

 - Arcadia.io

 - ARTISIGHT, INC.

 - A-S Medication Solutions LLC

 - Astraia

 - Atlas

 - B. Braun

 - Babyscripts

 - BAMBOO HEALTH

 - Baxter

 - BD

 - Bender

 - BHAI Systems

 - Biocoustics Instruments

 - Biofourmis

 - BioIntellisense

 - Blue Cross/Blue Shield

 - BRAINCHECK, INC

 - Cadence

 - Capsule Technologies

 - Cardinal Health WaveMark

 - Cardiocom

 - CareLogistics

 - CareSignal

 - CareSource

 - Cedargate

 - Center for Disease Control

 - Cerner

 - CGI

 - Children's Mercy

 - CIPHERHEALTH, INC.

 - CLEARWAVE, INC.

 - Cleric

 - Clinical Computer Systems, Inc.

 - Cognitive

 - CONCERT HEALTH

 - Creative EMS

 - Current Health

 - DEDALUS

 - Delaware - Public Health Agencies

 - Delegate Technology Group

 - Diasoft

 - Diaverum

 - Digisonics

 - Doctor Alliance

 - Echosens

 - eConsult

 - ELSEVIER INC.

 - ESO

 - Excel Medical

 - Extract Systems

 - Florida - Public Health Agencies

 - FORCE THERAPEUTICS

 - Forsante

 - FOTO Inc.

 - Fresenius Medical Care

 - GE

 - Gecko-ict

 - GETWELLNETWORK, INC.

 - GLOOKO, INC.

 - Glytec

 - Graphnet

 - Growth Analyser

 - Haemonetics

 - Harbor Performance Initiative

 - HCI Solutions

 - Health Recovery Solutions

 - Healthloop

 - HealthSnap

 - Highmark

 - Hillrom

 - Hippocratic AI

 - Homecare Homebase

 - Honeywell (Intermec)

 - Horizon Blue Cross Blue Shield of New Jersey

 - HUMANA

 - Hyland

 - IHOMER

 - ImageTrend

 - impedimed

 - Inland Empire Health Plan

 - InteGreat

 - InvisALERT

 - IODINE SOFTWARE, LLC

 - Jvion

 - Keriton Kare

 - KINESICS LLC

 - Kryptiq

 - Life Systems International

 - LivaNova

 - LM Software

 - Locus Health

 - Locus Solutions

 - Logis Solutions

 - LUMEDX

 - Macmillan Cancer Support

 - Masimo

 - Materials Management Microsystems

 - MCG Diagnostics

 - McKesson

 - MD REVOLUTION, INC.

 - MDI SOLUTIONS

 - MDLogix

 - MEDHOST

 - MEDICAL INFORMATICS CORP.

 - Medisanté

 - Meditech

 - MEDTRAK, INC.

 - Medtronic

 - MedVision AG

 - MGC Diagnostics

 - Microsoft

 - Mindray

 - Minze

 - Mississippi - Public Health Agencies

 - MONARCH MEDICAL TECHNOLOGIES

 - Mortara

 - Mozzaz

 - MyHealth First Network

 - MyVitalz

 - National Health Service

 - Natus

 - naviHealth

 - Navina

 - NDD Medical Technologies

 - NEUROFLOW

 - Neurotargeting

 - New England Donor Services

 - New York City - Public Health Agencies

 - Nihon Kohden

 - nobl Health

 - Nonin Medical

 - Notable

 - nSpire

 - Omron

 - Ontario Ministry of Health

 - Ontario Patient Data Reporting

 - Optum

 - ORACLE

 - OZ Systems

 - PAAMOST

 - Paragon

 - PARKLAND CENTER FOR CLINICAL INNOVATION

 - PATIENT ENGAGEMENT ADVISORS, LLC

 - PATIENTIQ

 - PCARE BY UNIGUEST

 - Penn Medicine

 - Perahealth

 - PERIGEN

 - Perkin Elmer

 - Philips

 - PHREESIA, INC.

 - PinkRoccade Healthcare

 - Procare

 - Promis Health Organization

 - QualComm

 - QUEST DIAGNOSTICS

 - QVENTUS, INC.

 - QVERA LLC

 - Raisoft

 - Rauland

 - REDOX

 - Rehab Documentation Company, Inc.

 - Resideo

 - ResMed

 - RESPOND CLINICAL INC.

 - Rimidi

 - RoQua

 - RPM Healthcare

 - SALESFORCE

 - SanaNet

 - Saudi Arabia Ministry of Health

 - SCC Soft Computer

 - SCHEDULEINTERPRETER

 - ScottCare

 - seca

 - Sentry Data Systems

 - Serial Multivision

 - SilverCloud Health

 - Singapore Ministry of Health Holdings

 - Smart Meter

 - SNAPS Solution

 - Sodexo

 - Softmedex

 - Somnomedics

 - Somnoware

 - Spacelabs

 - Spectrum Medical

 - St. Jude's

 - Stryker

 - SYAPSE

 - Talis Clinical

 - TCM

 - TelASK

 - TELCOR

 - Telemetrix

 - The Surgical Company

 - TIBCO

 - TIDEPOOL

 - Timeless Medical Systems

 - Tonic Solutions Inc.

 - Tridiuum

 - Twistle

 - UC Davis Health

 - UC San Diego

 - United Healthcare

 - Universal Research Solutions, LLC

 - Upfront Healthcare

 - VALIDIC, INC.

 - Varian Medical Systems

 - VisionTree

 - VitalTech

 - Vivify Health

 - Vyaire Medical

 - WELBY HEALTH, INC.

 - WellMed Medical Management

 - WellSky

 - Wellworks For You

 - XEALTH

 - XSOLIS

 - Zorgi

 - Zyter

 

 

 

### 
 Incoming Procedure Log Data
 [read the spec](/Tech/TechSpec?spec=5333)

 

 

 Receives information about cardiac catheterization, electrophysiology and interventional radiology procedures when using the Cupid (CVIS) procedure log for intra-procedure documentation. This information is sent from a hemodynamic product that collects vitals and pressures during the procedure. This interface can file information to flowsheets and free text events such that it appears on the Cupid procedure log. This interface is typically not used if Cupid's procedure log is not in use and the procedure log is being completed in the hemodynamic system.
 

 

 [Current integrations include ](#)
 

 - Abbott Diagnostics

 - Change Healthcare

 - GE

 - IBM

 - McKesson

 - Medtronic

 - Merge Healthcare

 - NUANCE COMMUNICATIONS INC.

 - Philips

 - Schwarzer Cardiotek

 - Siemens

 - St. Jude's

 - Vyaire Medical

 - Xperthis

 

 

 

### 
 Outgoing Financial Transactions
 [read the spec](/Tech/TechSpec?spec=5273)

 

 

 Sends financial transactions. Typically, the relevant situation for the use of this interface is when clinical services are provided at an organization that is not responsible for the associated revenue.
 

 

 [Current integrations include ](#)
 

 - 3M

 - AccuMed

 - ADP AdvancedMD

 - Allscripts

 - American Healthware

 - APS

 - Arintra

 - ARUP Laboratories

 - ATHENAHEALTH, INC.

 - Avinty

 - BCB Medical

 - Betrace

 - BUDDI.AI

 - Carecloud

 - Cerner

 - Clinisys

 - CODAMETRIX

 - Delta

 - eClinicalWorks

 - Enter Health

 - FATHOM, INC.

 - Gastro Health

 - GE

 - IBM

 - iD

 - InfuSystem

 - Inova Diagnostics (Werfen)

 - Integrated Medical Partners

 - LifePoint Health

 - MaximEyes

 - McKesson

 - MedAptus

 - MEDENT

 - MEDHOST

 - Meditech

 - MSN

 - NCS

 - Netsoft, Inc.

 - NextGen

 - Nym

 - Optum

 - Pharmhos

 - PLATOCODE

 - PowerHealth

 - Prairie States

 - Quadax

 - Radiation Business Solutions

 - SAP

 - Select Medical

 - Siemens

 - Solventum

 - Stanford Health Care Alliance

 - Sunrise Medical Laboratories

 - Sutherland

 - TELCOR

 - Waseel

 - Wellsoft

 - XIFIN

 - Yellowstone Pathology Institute (YPI)

 - Zorgi

 

 

 

### 
 Outgoing Syndromic Data
 [read the spec](/Tech/TechSpec?spec=5207)

 

 

 Follows the PHIN Messaging Guide for Syndromic Surveillance: Emergency Department and Urgent Care Data. Used to meet Meaningful Use Objectives to send Syndromic Surveillance data to Public Health agencies.
 

 

 [Current integrations include ](#)
 

 - Alabama - Public Health Agencies

 - Arizona - Public Health Agencies

 - Arkansas - Public Health Agencies

 - Arkansas Office of Health Information Technology

 - AUDACIOUS INQUIRY

 - BAMBOO HEALTH

 - Biosense Webster

 - California - Public Health Agencies

 - Center for Disease Control

 - Chesapeake Regional Information System for Our Patients

 - CliniSync

 - Colorado - Public Health Agencies

 - Connecticut - Public Health Agencies

 - CORHIO

 - CyncHealth

 - Delaware - Public Health Agencies

 - Delaware Health Information Network

 - Denver County (CO) - Public Health Agencies

 - District of Columbia - Public Health Agencies

 - Florida - Public Health Agencies

 - Georgia - Public Health Agencies

 - Hawaii - Public Health Agencies

 - Hawaii Health Information Exchange

 - Hawaii State Department of Health

 - HEALTH CATALYST, INC.

 - Health Monitoring Systems

 - HealthBridge

 - HealthHIE Nevada

 - HealthInfoNet

 - HMS

 - Houston - Public Health Agencies

 - Idaho - Public Health Agencies

 - Idaho Health Data Exchange

 - Illinois - Public Health Agencies

 - Illinois Office of Health Information Technology

 - Indiana - Public Health Agencies

 - IODINE SOFTWARE, LLC

 - Iowa - Public Health Agencies

 - Iron Bridge

 - Kansas - Public Health Agencies

 - Kansas Health Information Network

 - Kentucky - Public Health Agencies

 - Kentucky Health Information Exchange

 - Louisiana - Public Health Agencies

 - Maine - Public Health Agencies

 - Maryland - Public Health Agencies

 - Massachusetts - Public Health Agencies

 - Massachusetts Health Information Highway

 - Michigan - Public Health Agencies

 - Michigan Health Connect

 - Minnesota - Public Health Agencies

 - Mississippi - Public Health Agencies

 - Missouri - Public Health Agencies

 - Montana - Public Health Agencies

 - Monterey County (CA) - Public Health Agencies

 - Nebraska Health Information Initiative

 - Nevada - Public Health Agencies

 - New Hampshire - Public Health Agencies

 - New Jersey - Public Health Agencies

 - New Mexico - Public Health Agencies

 - New Mexico Health Information Collaborative

 - New York - Public Health Agencies

 - New York City - Public Health Agencies

 - North Carolina - Public Health Agencies

 - North Dakota - Public Health Agencies

 - Ohio - Public Health Agencies

 - Oklahoma - Public Health Agencies

 - ONEHEALTHPORT

 - Orange County Health

 - Oregon - Public Health Agencies

 - Pennslyvania - Public Health Agencies

 - Real-Time Outbreak Disease Surveillance Lab (RODS at University of Pittsburgh)

 - Revvity

 - Rhode Island - Public Health Agencies

 - Riverside County (CA) - Public Health Agencies

 - San Diego - Public Health Agencies

 - San Mateo County (CA) - Public Health Agencies

 - Santa Clara County (CA) - Public Health Agencies

 - South Carolina - Public Health Agencies

 - South Dakota - Public Health Agencies

 - South Dakota Department of Health

 - Stryker

 - Tennessee - Public Health Agencies

 - Texas - Public Health Agencies

 - Truven

 - Utah - Public Health Agencies

 - Virginia - Public Health Agencies

 - Vyaire Medical

 - Washington - Public Health Agencies

 - WellSky

 - West Virginia - Public Health Agencies

 - Wisconsin - Public Health Agencies

 - Wyoming - Public Health Agencies

 - Zotec Partners

 

 

 

### 
 Outgoing Results Query to Ontario Lab Information System

 

 

 Sends a patient-level query to the Ontario Laboratories Information System (OLIS) when a patient checks in for an appointment, and receives results OLIS returns in response to the query. The query can also be initiated on demand by a user at any time. Follows eHealthOntario OLIS Interface Specification R01.20. www.ehealthontario.on.ca.
 

 

 [Current integrations include ](#)
 

 - Ontario Ministry of Health

 

 

 

### 
 Outgoing Registration to Home Device Data Concentrator
 [read the spec](/Tech/TechSpec?spec=5215)

 

 

 Sends registration information to a device data concentrator system to register patients and devices. This interface would be used instead of the standard Patient Administration interface when collecting data from patient home monitoring devices using an external system.
 

 

 [Current integrations include ](#)
 

 - Cardiocom

 - Health Recovery Solutions

 - Honeywell (Intermec)

 - MD REVOLUTION, INC.

 - Medtronic

 - Resideo

 - Vivify Health

 

 

 

### 
 Outgoing Appointment Scheduling
 [read the spec](/Tech/TechSpec?spec=5296)

 

 

 Sends appointment information to external systems. Users can trigger messages for new, rescheduled, updated, no showed, and canceled appointments. To send surgical case schedules, the Outgoing Surgical Case Scheduling interface is required.
 

 

 [Current integrations include ](#)
 

 - 3M

 - 4S Informational Systems

 - abeo

 - ABRIDGE AI INC

 - AccuMed

 - Ace

 - Acuo Technologies

 - Agfa

 - ALEDADE, INC.

 - Allscripts

 - Ambra Health

 - Ambry Genetics

 - American Well

 - AMERISOURCE BERGEN

 - AMGA

 - Amkai

 - Apache

 - APPLIED RESEARCH WORKS INC.

 - Arakis

 - Arkansas - Public Health Agencies

 - Artera

 - Artera

 - ATHENAHEALTH, INC.

 - Atlas

 - AuditData

 - Avizia

 - Axel Health

 - Axians

 - BabySentry

 - BCB Medical

 - BD

 - Betrace

 - Biocoustics Instruments

 - Blue Shield of California

 - Bottomline

 - BREG

 - Cardiac Science

 - Cardinal Health WaveMark

 - CAREDX INC.

 - CareLogistics

 - CAREMESSAGE

 - Carestream Dental

 - Carevive

 - Casechek

 - Cedaron

 - CellCura

 - Cerner

 - CIPHERHEALTH, INC.

 - Cisco

 - Clinical Computer Systems, Inc.

 - Clinisys

 - CognisantMD

 - Comercer

 - COMMURE

 - Compumedics

 - Consensus Medical Systems

 - Covisint Corporation

 - CPS

 - CRITEX

 - Cybernius Medical Ltd.

 - DELIVERHEALTH

 - Dentrix

 - DEXCARE, INC.

 - DMDC

 - DOCASAP, INC.

 - DRDOCTOR

 - D-Scope Systems

 - Eceptionist

 - eClinicalWorks

 - Eclipsys

 - EDCi

 - EDCO

 - EHEALTH TECHNOLOGIES

 - Elekta

 - ELLKAY, LLC.

 - ELSEVIER INC.

 - Emageon

 - Embla

 - ENDOSOFT LLC

 - Ensemble Health Partners

 - Envera Health

 - Envision

 - Eon

 - ePreop

 - EXPERIAN HEALTH, INC.

 - Falcon

 - Federatie van Nederlandse Audiologische Centra

 - FinThrive

 - Fuel Medical

 - Fujifilm

 - Fujifilm Sonosite

 - Gastro Health

 - GE

 - GENESIS

 - GENEVA HEALTH SOLUTIONS

 - GeniusDoc

 - GETWELLNETWORK, INC.

 - GOHEALTH URGENT CARE

 - Graphnet

 - GUARDIAN RESEARCH NETWORK, INC.

 - Haemonetics

 - HEALOGICS, INC.

 - Health Outcomes Sciences

 - Healthcare Control Systems

 - Healthcare Systems & Technologies

 - Healthgrades

 - Healthloop

 - Highmark

 - Hologic

 - HUMANA

 - Hyland

 - IBM

 - ICLOPS

 - Idox Health

 - ifa systems

 - iGuana

 - Illinois Bone and Joint Institute

 - INDEHEALTH

 - Indiana - Public Health Agencies

 - Infinite Leap

 - Infor Global Solutions

 - InteGreat

 - IntelliGuard

 - InterSystems

 - IQMax

 - Johns Hopkins HealthCare LLC

 - Karl Storz

 - Keane

 - Kodak

 - KYRUUS, INC.

 - Laborie Medical Technologies

 - LEANTAAS, INC.

 - Lexmark Enterprise Software

 - Life Systems International

 - LM Software

 - LUMEDX

 - Lumin Medical LLC

 - M*Modal

 - MagView

 - Matrix Orthopedics

 - McKesson

 - MDnetwork

 - MDTECH

 - MedAptus

 - MEDEANALYTICS

 - Medical Brain

 - MEDICAL INFORMATICS CORP.

 - Medicom Health

 - Mediconsult

 - Medify

 - MediServe

 - Meditech

 - MedPlus

 - MEDTRAK, INC.

 - Medtronic

 - Mellowood Medical

 - MGC Diagnostics

 - Mobile Aspects

 - Modernizing Medicine

 - Mount Sinai Health Partners

 - MULESOFT, INC.

 - MyHealth First Network

 - myOnsite Healthcare

 - MYTONOMY INC.

 - National Cancer Institute

 - Natus

 - Navina

 - NET HEALTH SYSTEMS, INC.

 - Netcall

 - Netpoint Group

 - Nexa

 - NextGate Solutions

 - NextGen

 - NHN

 - Nihon Kohden

 - North American Partners in Anesthesia

 - Northwell Health

 - NovaRad

 - Novari Health

 - NUANCE COMMUNICATIONS INC.

 - Nuclear Medicine Information Systems LLC

 - O&M Solutions

 - OBJECTIVEHEALTH

 - Odeza

 - Olympus Endoworks

 - Omnicell

 - OpenText

 - Optima

 - Optimal Solutions

 - Optum

 - Orion Health

 - Owl

 - OzeScribe

 - PALANTIR

 - PathView Systems

 - PATIENT RESOURCE LLC

 - PATIENTEXP

 - PATIENTIQ

 - PatientPrompt

 - Penn Medicine

 - PenRad

 - Pentax

 - Philips

 - pMDsoft, Inc.

 - Press Ganey

 - Priority Consult

 - ProVation Medical

 - PROVIDERFLOW

 - Provox

 - Q-Centrix

 - Qmatic

 - QSI

 - QuadraMed

 - Recondo

 - REDOX

 - Rehab Documentation Company, Inc.

 - RELATIENT

 - RestorixHealth

 - RVC

 - SALESFORCE

 - SanaNet

 - SAP

 - SCC Soft Computer

 - SCI

 - ScottCare

 - SCRIBEAMERICA

 - ServiceHub

 - Shields Health Care Group

 - Siemens

 - Singapore Ministry of Health Holdings

 - SIS

 - SleepEx

 - SoftLink International

 - Softmedex

 - Solventum

 - Somnoware

 - SONIFI Solutions

 - Spheris 

 - SPINSCI TECHNOLOGIES, LLC

 - St. George's Genomics Service

 - Steeper Group

 - Stericycle Communication Solutions

 - STERIS Corporation

 - Stryker

 - SWIFT MEDICAL, INC.

 - Sybase

 - SYFT

 - SYMPLR

 - Synedra

 - Tecsys

 - TELADOC, INC.

 - TeleResults

 - The Advisory Board

 - TheraDoc

 - Thynk Health

 - TIBCO

 - Tonic Solutions Inc.

 - TransChart

 - TransUnion

 - Tridiuum

 - TSG Integrations

 - Twistle

 - Universal Research Solutions, LLC

 - UTECH

 - Varian Medical Systems

 - VAXCARE

 - Velos

 - Versus

 - Via Oncology

 - Vignette

 - VISAGE IMAGING, INC.

 - VisionTree

 - VISUS

 - VOLPARA HEALTH, INC.

 - Waseel

 - Waystar

 - WellSky

 - WOLTERS KLUWER

 - Zeiss

 - Zorgdoc

 - Zorgi

 - Zotec Partners

 - ZULAFLY, INC.

 

 

 

### 
 Coding - Incoming Query and Response
 [read the spec](/Tech/TechSpec?spec=5377)

 

 

 The incoming coding interface supports workflows in which coders are working entirely in your system. Coders in your system send messages to providers using Epic asking for more information to support their documentation (CDI or Coding Query). Responses are sent in return.
 

 

 [Current integrations include ](#)
 

 - 3M

 - NUANCE COMMUNICATIONS INC.

 - Optum

 - The Claro Group

 

 

 

### 
 Incoming Surgical Case Tracking
 [read the spec](/Tech/TechSpec?spec=5318)

 

 

 Receives surgical case event information in real time to populate the event and the event timestamp in a surgical case log.
 

 

 [Current integrations include ](#)
 

 - Amazon

 - TELETRACKING

 

 

 

### 
 Outgoing Medication Stock Transfer Request and Response
 [read the spec](/Tech/TechSpec?spec=5251)

 

 

 Initiates a fill in a dispensing system-such as robotic arm or carousel-to assist in sending medications from the pharmacy to a hospital floor. This interface also receives acknowledgments from the dispensing system, which updates stock counts in Willow Inventory Management accordingly. For example, if a user requests five bottles of a certain medicine, but only four exist in stock, the interface updates the stock count being sent to the floor to four. Note that the purpose of messages sent by the interface is to request stock for a hospital floor. For that reason, the messages aren't patient-specific.
 

 

 [Current integrations include ](#)
 

 - ARX

 - Astraia

 - BD

 - Omnicell

 - Swisslog

 

 

 

### 
 Outgoing Surgical Case Scheduling
 [read the spec](/Tech/TechSpec?spec=5208)

 

 

 Sends case scheduling information to external systems. Messages are sent for new, rescheduled, updated, and canceled cases.
 

 

 [Current integrations include ](#)
 

 - 3M

 - abeo

 - ABOUT HEALTHCARE, INC.

 - AccuMed

 - Aesculap

 - Aexis Medical

 - Agfa

 - ALERTWATCH, LLC (FKA ALERTWATCH, INC.)

 - American Association of Orthopaedic Executives

 - ANDOR HEALTH

 - Apollo

 - ARC Healthcare Technologies

 - Artera

 - Artera

 - Arthrex

 - Ascendco Health

 - AssistIQ

 - Axians

 - BCB Medical

 - BD

 - Bender

 - Betrace

 - Biotronik

 - Brainlab

 - BREG

 - CAPS Pharmacy

 - Cardinal Health WaveMark

 - CareLogistics

 - CareMedic

 - Casechek

 - Cedaron

 - Censis

 - Cisco

 - Clinisys

 - CODAMETRIX

 - Consensus Medical Systems

 - Copernicare

 - CORI

 - CRITEX

 - EDCi

 - EDCO

 - Elekta

 - ELSEVIER INC.

 - Emageon

 - ENDOSOFT LLC

 - Ensemble Health Partners

 - Envision

 - ePreop

 - ETIOMETRY, INC.

 - EVIDENCECARE, LLC

 - EXPERIAN HEALTH, INC.

 - Fleischhacker

 - FORCE THERAPEUTICS

 - Fujifilm

 - GE

 - GENESIS

 - Getinge

 - GETWELLNETWORK, INC.

 - Giles Scientific, Inc.

 - Global Healthcare Exchange

 - Graphnet

 - HCI Solutions

 - Healthcare Control Systems

 - Healthcare Systems & Technologies

 - Healthloop

 - HealthNautica

 - HID GLOBAL CORPORATION

 - Hillrom

 - Hyland

 - iMDsoft

 - Infor Global Solutions

 - INGENIOUS MED

 - IntelliGuard

 - Inter

 - INTUITIVE SURGICAL

 - Inventory Optimization Solutions (IOS)

 - InVivoLink

 - ION Solutions

 - IQMax

 - Karl Storz

 - Konica Minolta

 - LaussenLabs

 - LEANTAAS, INC.

 - LiveData

 - LPiT Solutions

 - LUMEDX

 - LUMEON INC.

 - M*Modal

 - Materials Management Microsystems

 - McKesson

 - MD-Staff

 - Medical Brain

 - MEDICAL INFORMATICS CORP.

 - Medisys Innovation

 - MEDTRAK, INC.

 - Medtronic

 - Memorial Hermann

 - Merge Healthcare

 - Mobile Aspects

 - Modernizing Medicine

 - Morrisey

 - MYTONOMY INC.

 - National Health Service

 - NEW COMPLIANCE

 - NewCura

 - North American Partners in Anesthesia

 - NUANCE COMMUNICATIONS INC.

 - O&M Solutions

 - Odeza

 - Olympus America

 - Olympus Endoworks

 - Olympus Medical Systems

 - Omnicell

 - Ontario Ministry of Health

 - OpenTempo

 - Optum

 - ORACLE

 - Orpheus

 - Ortech

 - OSG

 - PAR Excellence

 - PATIENTEXP

 - PATIENTIQ

 - Pentax

 - Philips

 - Post Acute Analytics

 - PowerHealth

 - PREMIER, INC.

 - ProSolv CardioVascular

 - Prospitalia

 - ProVation Medical

 - ReadySet Surgical

 - Recondo

 - REDOX

 - RELATIENT

 - RelayOne

 - RVC

 - SALESFORCE

 - SAP

 - Schwarzer Cardiotek

 - Sectra

 - Siemens

 - SIS

 - Softmedex

 - SONIFI Solutions

 - Stericycle Communication Solutions

 - STERIS Corporation

 - Stryker

 - Surgery Exchange

 - Surgical Safety Technologies

 - SYMPLR

 - Talis Clinical

 - Taylor Healthcare

 - Tecsys

 - TELETRACKING

 - The Advisory Board

 - TheraDoc

 - TORQ INTERFACE, INC.

 - TouchPoint Medical

 - TransUnion

 - TSG Integrations

 - Uniform Data Systems

 - Universal Research Solutions, LLC

 - Varian Medical Systems

 - vChart

 - VISAGE IMAGING, INC.

 - VISUS

 - Vivify Health

 - VueMed

 - Waseel

 - Waystar

 - Wilhelm

 - WOLTERS KLUWER

 - XSOLIS

 

 

 

### 
 Outgoing OCIO Medication Orders from EpicCare Ambulatory
 [read the spec](/Tech/TechSpec?spec=5247)

 

 

 Sends outpatient and discharge medication orders to a pharmacy information system. This interface supports a subset of HL7 version 2.4 according to the specifications defined in the Clinical System Medication Management Interface Specification version 10.1 published by the Office of Chief Information (OCIO) of Victoria in Australia.
 

 

 [Current integrations include ](#)
 

 - Pharmhos

 

 

 

### 
 Incoming Medication Inventory Management
 [read the spec](/Tech/TechSpec?spec=5353)

 

 

 Updates medication stocks in Willow Inventory, Epic's medication inventory management system, with changes for an externally managed inventory location.
 

 

 [Current integrations include ](#)
 

 - SAP

 

 

 

### 
 Outgoing Medication Inventory Depletion
 [read the spec](/Tech/TechSpec?spec=5255)

 

 

 Communicates changes in medication stock in Willow Inventory medication inventory management for an external inventory location.
 

 

 [Current integrations include ](#)
 

 - SAP

 

 

 

### 
 Incoming Surgical Resource Data
 [read the spec](/Tech/TechSpec?spec=staged%2FIncoming%20Surgical%20Instrument%20Data%20Interface%20Technical%20Specification.pdf)

 

 

 Used to automate synchronization of surgical instrument records, implant groups, or trays from an external system.
 

 

 [Current integrations include ](#)
 

 - Aesculap

 - Afas

 - Ascendco Health

 - B. Braun

 - Censis

 - Getinge

 - Materials Management Microsystems

 - McKesson

 - ORACLE

 - PREMIER, INC.

 - STERIS Corporation

 - Workday

 

 

 

### 
 Incoming Infusion Documentation
 [read the spec](/Tech/TechSpec?spec=5363)

 

 

 Receives discrete measurements from an infusion pump gateway associated with the administration of an infusion order. This is an advanced interface with a particular set of prerequisites for successful implementation.
 

 

 [Current integrations include ](#)
 

 - B. Braun

 - Baxter

 - BD

 - Capsule Technologies

 - Fresenius Medical Care

 - ICU Medical

 - NantHealth

 

 

 

### 
 Incoming Alerts from Alert Manager and Alert Reporting from Patient Care Devices
 [read the spec](/Tech/TechSpec?spec=9755)

 

 

 This collection of interfaces receives alert messages to send push notifications to end users. Upon receiving, reading, or responding to an alert, response messages are sent back to the alert manager. They can also store technical and physiological alert data from patient care devices such as physiological monitors and infusion pumps.
 

 

 [Current integrations include ](#)
 

 - Ascom

 - Capsule Technologies

 - CareLogistics

 - GlobeStar

 - Hillrom

 - Masimo

 - Philips

 - Spok

 - Stryker

 - TigerConnect

 

 

 

### 
 Incoming Medication Administration Notification
 [read the spec](/Tech/TechSpec?spec=5355)

 

 

 Files administration information to a medication order created and acted on in an external system. The read-only orders appear on the MAR for reference.
 

 

 [Current integrations include ](#)
 

 - Merge Healthcare

 - Quantum Secure

 

 

 

### 
 Incoming Prescriptions from Legacy Pharmacy to Willow Ambulatory
 [read the spec](/Tech/TechSpec?spec=5350)

 

 

 Receives medication orders from legacy pharmacy systems and files the medications orders to Willow Ambulatory Pharmacy. This interface is used only for conversions.
 

 

### 
 Incoming Ancillary Results
 [read the spec](/Tech/TechSpec?spec=5387)

 

 

 Receives test results from a laboratory, cardiology, or similar information system These results include general lab, microbiology, pathology, and blood bank results, results with a narrative/impression, and hyperlinks to results that are stored elsewhere. These results can include LIS data, RIS data, pacemaker data, ECG records, and hemodynamic data. The interface can accept incoming order messages that request order numbers, replace procedures, or cancel existing orders. This HL7v2 interface is specific to a clinical order and uses TCP/IP to exchange messages.
 

 

 [Current integrations include ](#)
 

 - Cardinal Health 

 - Abbott Diagnostics CELL-DYN, Abbott Diagnostics PXP Glucose Meter, Abbott Diagnostics PrecisionWeb

 - Agfa HeartStation, Agfa Heartlab Encompass, Agfa ICIS, Agfa IMPAX PACS, Agfa IMPAX RIS, Agfa TalkStation

 - Alere Informatics AVL Blood Gas Analyzer, Alere Informatics RALS-Plus, Alere Wellbeing, Alere epoc Blood Analysis System

 - Alverno Lab

 - Ameripath Anatomic Pathology

 - AMICAS Vision Series RIS

 - ARUP Reference Lab

 - AS Software AS-ObGyn

 - Aspyra CyberLAB II (CCA)

 - Atlas Ion, Atlas LabWorks

 - Bio-Reference Laboratories, Inc

 - BRIT

 - C/NET Solutions CNExT

 - Calloway Labs

 - Cardea Technology BoneStation

 - CardioNet MCOT

 - CareFusion Pulmonary System, CareFusion Transfusion Verification

 - Carestream Vue PACS

 - Cerner Classic Lab, Cerner MARS, Cerner Millenium Micro, Cerner Millennium Anatomic Pathology, Cerner Millennium Blood Bank, Cerner Millennium FirstNet, Cerner Millennium PathNet, Cerner Millennium PharmNet, Cerner Millennium PowerChart Office, Cerner Millennium PowerChart/PowerOrders/CareNet, Cerner Millennium ProFile, Cerner Millennium RadNet, Cerner Millennium SurgiNet, Cerner PharmNet, Cerner QuadRIS, Cerner RadPlus, Cerner Scheduling Management

 - Change Healthcare

 - ClinLab LIS

 - Commissure RadWhere

 - CompuGroup Medical LabDAQ

 - Computer Trust Corporation WinSURGE

 - Consensus Medical Systems VascuBase, Consensus Medical Systems VascuPro

 - Continuum Health Partners Continuum Clinical Laboratories

 - CoPath, CoPathPlus

 - Cortex Medical Management Systems Cortex Pathology

 - CPSI System

 - Diagnostic Lab Services, Inc. Reference Lab

 - Dianon Uropathology

 - Digisonics DigiNet Pro, Digisonics DigiView, Digisonics OB-View

 - Direct Connect Optima/Sentara

 - Dolbey Fusion Text

 - DR Systems Systems Dominator, DR Systems Unity RIS/CVIS/PACS

 - Draeger Innovian Anesthesia

 - DVI VoiceWave Transcribe

 - Dynamic Imaging IntegradWeb

 - Eclipsys eLink

 - Elekta DermPath, Elekta IntelliLab, Elekta PowerPath Anatomic Pathology

 - Emageon CardioIMS, Emageon EchoIMS, Emageon Enterprise Visual Medical System, Emageon Vericis (Camtronics)

 - Embla 

 - EMMI Solutions

 - EndoSoft LLC

 - Epiphany Cardio Server ECG Management System

 - eScription

 - Extract Systems LabDE

 - Fort Wayne Medical Laboratory Reference Lab

 - Fujifilm Synapse PACS

 - G2 Speech

 - GE CardioLab, GE Catalyst MUSE, GE Centricity EMR, GE Centricity PACS, GE Centricity RIS-IC, GE EchoPAC, GE Image Vault, GE Mac-Lab, GE MAC2000 Resting ECG, GE ViewPoint

 - General Medical Laboratories Reference Lab

 - Genzyme Corporation Genzyme Genetic Testing

 - GetWellNetwork Education Library

 - gMed gGastro+

 - Haemonetics SafeTrace Tx

 - HealthBridge Information Exchange

 - HealthCare Clinical Laboratories Lab

 - HealthLand Inpatient EHR

 - Heart Imaging Technologies WebPAX

 - HMI HealthMedia

 - HMS Monitor

 - Hologic Discovery

 - Hyland Software OnBase

 - Iatric Systems Iatrics Engine

 - InStar Systems

 - Instrumentation Laboratory GemWeb

 - Intelligent Business Solutions CardioPulse

 - InterSystems Ensemble

 - ITxM Blood Bank

 - J&S Medical Associates LabTrak

 - Keane InSight

 - Kodak DirectView

 - LabCorp Reference Lab

 - LabSoft Inc. LabNet

 - Lanier Scanning System

 - LifeWatch LifeWatch Connect

 - LUMEDX Apollo Advance, LUMEDX CardioDoc

 - M*Modal Cquence Medical Transcription, M*Modal DocQment Enterprise Platform, M*Modal SpeechQ

 - MagView Mammography Results

 - Mammography Reporting System MRS

 - Mayo Clinic - LSI

 - McKesson Horizon CPACS, McKesson Horizon Cardiovascular Information System, McKesson Horizon Clinicals, McKesson Horizon Lab, McKesson Horizon Medical Imaging, McKesson Horizon Radiology, McKesson Horizon Surgical Manager, McKesson McKesson Radiology Manager, McKesson Paragon, McKesson Series, McKesson Star

 - MEDCOM Information Systems MEDCOM Lab Manager

 - Medgraphics BreezeSuite

 - Medical Genetics Information System Medgis

 - Medicity Novo Grid

 - Medicus Medlynx

 - MediServe MediLinks

 - Meditech C/S Anatomic Pathology, Meditech C/S Blood Bank, Meditech C/S Enterprise Medical Record, Meditech C/S Lab, Meditech MAGIC Lab, Meditech MAGIC Radiology

 - Mediware HCLL, Mediware Hemocare/Lifeline

 - MedMined Hospital Infection Management

 - Mednet Services

 - Medstreaming Cardiovascular Medical Office, Medstreaming Medical Office

 - Medtronic Paceart

 - Merge Cardio, Merge Eye Care PACS, Merge LIS, Merge PACS, Merge eMed FUSION Matrix, Merge eMed RISLogic, Merge iConnect

 - Metropolitan Medical Laboratories Reference Lab

 - Microsoft Amalga

 - MIPS Glims

 - Monogram

 - Morgan Scientific ComPAS Freedom

 - Mortara

 - Mountain Star Clinical Laboratories Reference Lab

 - Multidata MultiTech

 - Natus XLTEK NeuroMax

 - NDCHealth TechRx

 - ndd Medical Technologies

 - Net Health Systems WoundExpert

 - Netsoft, Inc. IntelliPath

 - NextGen EMR

 - Nihon Kohden NeuroWorkbench, Nihon Kohden Polysmith Sleep

 - Northern Software eLab.Sys

 - NovoPath

 - nSpire Raptor, nSpire nSight

 - Nuance Dictaphone Enterprise Express, Nuance Dictaphone Enterprise Workstation, Nuance Dictaphone PowerScribe Workstation, Nuance Dictaphone ichart, Nuance EXText (Dictaphone), Nuance EXVoice (Dictaphone), Nuance Powerscribe 360 Critical Results, Nuance Powerscribe 360 Reporting, Nuance eScription / Dragon Medical 360 - eScription

 - Nuclear Medicine Information Systems LLC

 - O&M Solutions QSight

 - Olympus Endoworks

 - Orchard Harvest LIS

 - Palga U-DPS

 - Pangaea Information Technologies Guardian

 - Pathology Associates Medical Laboratories Reference Lab

 - Pathology, Inc. Reference Pathology Lab

 - PathView Systems Progeny Anatomic Pathology

 - PenRad MIS

 - Pentax Bronchoscopes, Pentax EndoPro, Pentax GI Endoscopes

 - Perceptive Software ImageNow

 - Philips Calysto Hemodynamics, Philips Labosys, Philips Tracemaster NT, Philips Tracemaster Vue, Philips Xcelera Cath Lab Management, Philips Xcelera Echo Lab Management, Philips Xper, Philips iSite

 - Picis

 - Primordial

 - ProSolv CardioVascular

 - ProVation Medical ProValent, ProVation Medical ProVation MD

 - Psyche WindoPath

 - QuadraMed Affinity

 - Quest Diagnostics Reference Lab

 - Radiometer Radiance

 - RadNet Imaging Services

 - Regional Medical Laboratory Reference Lab

 - SCC SoftA/R, SCC SoftBank, SCC SoftLab, SCC SoftPath

 - Schuyler House SchuyLab

 - Scientific Software Solutions PedCath

 - ScImage PICOMEnterprise

 - ScottCare TeleRehab VersaCare

 - Siemens Apollo Cardea, Siemens Axiom Sensis, Siemens Invision RCO and ICO, Siemens KinetDx, Siemens Lifetime Clinical Record (LCR), Siemens Novius Lab, Siemens Novius Radiology, Siemens OPENLink (Siemens), Siemens Radiology, Siemens RapidComm, Siemens syngo Dynamics, Siemens syngo Imaging, Siemens syngo Workflow

 - Skylight CareNavigator

 - SoftLink International CVI, SoftLink International Imagine

 - SoftMed ChartScript

 - Solstas Lab Partners

 - Spheris eChart

 - Summit Imaging EndoProse

 - Sunquest Blood Bank, Sunquest CoPathPlus, Sunquest Lab, Sunquest PowerPath Anatomic Pathology, Sunquest Radiology

 - Swearingen Software

 - SweetSpot Diabetes Care

 - Sybase e-Biz Impact

 - SystemLink HistoTrac

 - Tacoma Rdiology Associates TRA

 - TELCOR QML

 - Teramedica Evercore

 - Transaction Data Systems

 - Transcend BayScribe

 - Transolutions Transcription Services

 - United Clinical Laboratories Reference Lab

 - USA RMS

 - UTECH EndoSoft

 - VantageMed

 - Varian Medical Systems ARIA

 - Veenstra Instruments IBC-606

 - Via Oncology Pathways

 - Viasys Healthcare Neurocare, Viasys Healthcare Respiratory Diagnostics, Viasys Healthcare Vmax Encore

 - Viracor-IBT Laboratories Reference Lab

 - Virtual Radiologic Radiology

 - Vision Chips Observer

 - Vision4Health Molis

 - VISUS JiveX

 - WebMedX Outsourced Transcription Services

 

 

 

### 
 Discrete Genomic Results
 [read the spec](/Tech/TechSpec?spec=7986)

 

 

 Discrete genomic results file to Epic via the [Incoming Ancillary Results interface](#IncomingAncillaryResults). To include discrete genomic data as a part of the test's result, specifically formatted OBX segments must be included on the result (ORU^R01) message. These OBX segments follow the representation for discrete genomic data published in the HL7 Version 2.5.1 Implementation Guide: Lab Results Interface (LRI), Release 1 and the supported data elements are outlined in the specification document. 
 

 

### 
 Incoming Ancillary Results - Imaging
 [read the spec](/Tech/TechSpec?spec=5390)

 

 

 Epic's radiology and cardiology software receives results from a imaging, cardiology, or transcription system for use in Epic. These results include results with a narrative/impression, and image availability or hyperlinks to results that are stored elsewhere, such as a PACS. This HL7v2 interface is specific to a clinical order and uses TCP/IP to exchange messages.
 

 

 [Current integrations include ](#)
 

 - Cardinal Health 

 - Abbott Diagnostics CELL-DYN, Abbott Diagnostics PXP Glucose Meter, Abbott Diagnostics PrecisionWeb

 - Agfa HeartStation, Agfa Heartlab Encompass, Agfa ICIS, Agfa IMPAX PACS, Agfa IMPAX RIS, Agfa TalkStation

 - Alere Informatics AVL Blood Gas Analyzer, Alere Informatics RALS-Plus, Alere Wellbeing, Alere epoc Blood Analysis System

 - Alverno Lab

 - Ameripath Anatomic Pathology

 - AMICAS Vision Series RIS

 - ARUP Reference Lab

 - AS Software AS-ObGyn

 - Aspyra CyberLAB II (CCA)

 - Atlas Ion, Atlas LabWorks

 - Bio-Reference Laboratories, Inc

 - BRIT

 - C/NET Solutions CNExT

 - Calloway Labs

 - Cardea Technology BoneStation

 - CardioNet MCOT

 - CareFusion Pulmonary System, CareFusion Transfusion Verification

 - Carestream Vue PACS

 - Cerner Classic Lab, Cerner MARS, Cerner Millenium Micro, Cerner Millennium Anatomic Pathology, Cerner Millennium Blood Bank, Cerner Millennium FirstNet, Cerner Millennium PathNet, Cerner Millennium PharmNet, Cerner Millennium PowerChart Office, Cerner Millennium PowerChart/PowerOrders/CareNet, Cerner Millennium ProFile, Cerner Millennium RadNet, Cerner Millennium SurgiNet, Cerner PharmNet, Cerner QuadRIS, Cerner RadPlus, Cerner Scheduling Management

 - Change Healthcare

 - ClinLab LIS

 - Commissure RadWhere

 - CompuGroup Medical LabDAQ

 - Computer Trust Corporation WinSURGE

 - Consensus Medical Systems VascuBase, Consensus Medical Systems VascuPro

 - Continuum Health Partners Continuum Clinical Laboratories

 - CoPath, CoPathPlus

 - Cortex Medical Management Systems Cortex Pathology

 - CPSI System

 - Diagnostic Lab Services, Inc. Reference Lab

 - Dianon Uropathology

 - Digisonics DigiNet Pro, Digisonics DigiView, Digisonics OB-View

 - Direct Connect Optima/Sentara

 - Dolbey Fusion Text

 - DR Systems Systems Dominator, DR Systems Unity RIS/CVIS/PACS

 - Draeger Innovian Anesthesia

 - DVI VoiceWave Transcribe

 - Dynamic Imaging IntegradWeb

 - Eclipsys eLink

 - Elekta DermPath, Elekta IntelliLab, Elekta PowerPath Anatomic Pathology

 - Emageon CardioIMS, Emageon EchoIMS, Emageon Enterprise Visual Medical System, Emageon Vericis (Camtronics)

 - Embla 

 - EMMI Solutions

 - Epiphany Cardio Server ECG Management System

 - eScription

 - Extract Systems LabDE

 - Fort Wayne Medical Laboratory Reference Lab

 - Fujifilm Synapse PACS

 - G2 Speech

 - GE CardioLab, GE Catalyst MUSE, GE Centricity EMR, GE Centricity PACS, GE Centricity RIS-IC, GE EchoPAC, GE Image Vault, GE Mac-Lab, GE MAC2000 Resting ECG, GE ViewPoint

 - General Medical Laboratories Reference Lab

 - Genzyme Corporation Genzyme Genetic Testing

 - GetWellNetwork Education Library

 - gMed gGastro+

 - Haemonetics SafeTrace Tx

 - HealthBridge Information Exchange

 - HealthCare Clinical Laboratories Lab

 - HealthLand Inpatient EHR

 - Heart Imaging Technologies WebPAX

 - HMI HealthMedia

 - HMS Monitor

 - Hologic Discovery

 - Hyland Software OnBase

 - Iatric Systems Iatrics Engine

 - InStar Systems

 - Instrumentation Laboratory GemWeb

 - Intelligent Business Solutions CardioPulse

 - InterSystems Ensemble

 - ITxM Blood Bank

 - J&S Medical Associates LabTrak

 - Keane InSight

 - Kodak DirectView

 - LabCorp Reference Lab

 - LabSoft Inc. LabNet

 - Lanier Scanning System

 - LifeWatch LifeWatch Connect

 - LUMEDX Apollo Advance, LUMEDX CardioDoc

 - M*Modal Cquence Medical Transcription, M*Modal DocQment Enterprise Platform, M*Modal SpeechQ

 - MagView Mammography Results

 - Mammography Reporting System MRS

 - Mayo Clinic - LSI

 - McKesson Horizon CPACS, McKesson Horizon Cardiovascular Information System, McKesson Horizon Clinicals, McKesson Horizon Lab, McKesson Horizon Medical Imaging, McKesson Horizon Radiology, McKesson Horizon Surgical Manager, McKesson McKesson Radiology Manager, McKesson Paragon, McKesson Series, McKesson Star

 - MEDCOM Information Systems MEDCOM Lab Manager

 - Medgraphics BreezeSuite

 - Medical Genetics Information System Medgis

 - Medicity Novo Grid

 - Medicus Medlynx

 - MediServe MediLinks

 - Meditech C/S Anatomic Pathology, Meditech C/S Blood Bank, Meditech C/S Enterprise Medical Record, Meditech C/S Lab, Meditech MAGIC Lab, Meditech MAGIC Radiology

 - Mediware HCLL, Mediware Hemocare/Lifeline

 - MedMined Hospital Infection Management

 - Mednet Services

 - Medstreaming Cardiovascular Medical Office, Medstreaming Medical Office

 - Medtronic Paceart

 - Merge Cardio, Merge Eye Care PACS, Merge LIS, Merge PACS, Merge eMed FUSION Matrix, Merge eMed RISLogic, Merge iConnect

 - Metropolitan Medical Laboratories Reference Lab

 - Microsoft Amalga

 - MIPS Glims

 - Monogram

 - Morgan Scientific ComPAS Freedom

 - Mortara

 - Mountain Star Clinical Laboratories Reference Lab

 - Multidata MultiTech

 - Natus XLTEK NeuroMax

 - NDCHealth TechRx

 - ndd Medical Technologies

 - Net Health Systems WoundExpert

 - Netsoft, Inc. IntelliPath

 - NextGen EMR

 - Nihon Kohden NeuroWorkbench, Nihon Kohden Polysmith Sleep

 - Northern Software eLab.Sys

 - NovoPath

 - nSpire Raptor, nSpire nSight

 - Nuance Dictaphone Enterprise Express, Nuance Dictaphone Enterprise Workstation, Nuance Dictaphone PowerScribe Workstation, Nuance Dictaphone ichart, Nuance EXText (Dictaphone), Nuance EXVoice (Dictaphone), Nuance Powerscribe 360 Critical Results, Nuance Powerscribe 360 Reporting, Nuance eScription / Dragon Medical 360 - eScription

 - Nuclear Medicine Information Systems LLC

 - O&M Solutions QSight

 - Olympus Endoworks

 - Orchard Harvest LIS

 - Palga U-DPS

 - Pangaea Information Technologies Guardian

 - Pathology Associates Medical Laboratories Reference Lab

 - Pathology, Inc. Reference Pathology Lab

 - PathView Systems Progeny Anatomic Pathology

 - PenRad MIS

 - Pentax Bronchoscopes, Pentax EndoPro, Pentax GI Endoscopes

 - Perceptive Software ImageNow

 - Philips Calysto Hemodynamics, Philips Labosys, Philips Tracemaster NT, Philips Tracemaster Vue, Philips Xcelera Cath Lab Management, Philips Xcelera Echo Lab Management, Philips Xper, Philips iSite

 - Picis

 - Primordial

 - ProSolv CardioVascular

 - ProVation Medical ProValent, ProVation Medical ProVation MD

 - Psyche WindoPath

 - QuadraMed Affinity

 - Quest Diagnostics Reference Lab

 - Radiometer Radiance

 - RadNet Imaging Services

 - Regional Medical Laboratory Reference Lab

 - SCC SoftA/R, SCC SoftBank, SCC SoftLab, SCC SoftPath

 - Schuyler House SchuyLab

 - Scientific Software Solutions PedCath

 - ScImage PICOMEnterprise

 - ScottCare TeleRehab VersaCare

 - Siemens Apollo Cardea, Siemens Axiom Sensis, Siemens Invision RCO and ICO, Siemens KinetDx, Siemens Lifetime Clinical Record (LCR), Siemens Novius Lab, Siemens Novius Radiology, Siemens OPENLink (Siemens), Siemens Radiology, Siemens RapidComm, Siemens syngo Dynamics, Siemens syngo Imaging, Siemens syngo Workflow

 - Skylight CareNavigator

 - SoftLink International CVI, SoftLink International Imagine

 - SoftMed ChartScript

 - Solstas Lab Partners

 - Spheris eChart

 - Summit Imaging EndoProse

 - Sunquest Blood Bank, Sunquest CoPathPlus, Sunquest Lab, Sunquest PowerPath Anatomic Pathology, Sunquest Radiology

 - Swearingen Software

 - SweetSpot Diabetes Care

 - Sybase e-Biz Impact

 - SystemLink HistoTrac

 - Tacoma Rdiology Associates TRA

 - TELCOR QML

 - Teramedica Evercore

 - Transaction Data Systems

 - Transcend BayScribe

 - Transolutions Transcription Services

 - United Clinical Laboratories Reference Lab

 - USA RMS

 - UTECH EndoSoft

 - VantageMed

 - Varian Medical Systems ARIA

 - Veenstra Instruments IBC-606

 - Via Oncology Pathways

 - Viasys Healthcare Neurocare, Viasys Healthcare Respiratory Diagnostics, Viasys Healthcare Vmax Encore

 - Viracor-IBT Laboratories Reference Lab

 - Virtual Radiologic Radiology

 - Vision Chips Observer

 - Vision4Health Molis

 - VISUS JiveX

 - WebMedX Outsourced Transcription Services

 

 

 

### 
 Digital Pathology
 [read the spec](/Tech/TechSpec?spec=5420)

 

 

 The integration between Beaker, Epic's lab software, and an image-management system for the digital pathology workflow utilizes the Outgoing Lab Instrument Orders and the Incoming Lab Instrument Results interfaces. Beaker sends patient, case, and slide information and receives image availability notifications to enable whole slide imaging workflows.
 

 

### 
 Incoming Transcriptions
 [read the spec](/Tech/TechSpec?spec=5316)

 

 

 In this scenario, an external system has findings in a text or image format. These findings are either observations from a given contact with a patient (such as a visit or a hospitalization) or observations specific to a clinical order. Traditionally, this interface was used to match dictations with their eventual transcription (hence the name), but it can be used for a broader range of clinical findings. The EHR receives and files documents from a transcription system, scanned documents from an external document management system, or notes generated in another clinical system. This interface is often used for clinical findings that don't neatly fit into more specific data elements. Notes created or updated by the transcription interface can trigger deficiency updates.
 

 

 [Current integrations include ](#)
 

 - 3M

 - abeo

 - Accutype Medical Services

 - Acusis

 - Advanced ICU Care

 - Agfa

 - Allscripts

 - American Well

 - Amphion Medical

 - ARUP

 - AS Software

 - Athena Health

 - Axolotl

 - Becton Dickinson

 - Bottomline

 - Breitner

 - Bright.md

 - Bronx Regional Health Information Organization

 - CardioCom

 - CBAY

 - Cerner

 - CGI

 - Collective Medical Technologies

 - Conduent

 - CoPath

 - Corepoint Health

 - CORI

 - Crescendo Systems Corporation

 - Cybernius Medical Ltd.

 - Delaware Health Information Network

 - Dentrix

 - Dolbey

 - DR Systems

 - Easy Software

 - ECIN

 - eClinicalWorks

 - Eclipsys

 - eHealth Technologies

 - Elekta

 - EMC2

 - EMDAT

 - emsCharts

 - EndoSoft

 - ESO Solutions

 - Flatiron

 - Fresenius Medical Care

 - Fysicon

 - GE

 - HalfPenny

 - Healogics

 - HealthBridge

 - Heartland Information Services

 - Hypertype

 - IBM

 - ifa systems

 - iGuana

 - iMDsoft

 - iMedX

 - InterSystems

 - Isoprime

 - KnowledgeLake

 - Krames

 - Kryptiq

 - Lanier

 - LVM Systems

 - M*Modal

 - Mammography Reporting System

 - McKesson

 - MDLIVE

 - MDnetwork

 - Medical Data Systems

 - Medical Measurement Systems

 - Medicity

 - MediServe

 - Meditech

 - MedPlus

 - Med-Scribe

 - MedWrite Transcription

 - Merge

 - MGC Diagnostics

 - Microsoft

 - Morrisey

 - Nebraska Health Information Initiative

 - Net Health Systems

 - NextGen

 - Nihon Kohden

 - NovoPath

 - NowPow

 - nSpire

 - nThrive

 - Nuance Communications

 - Ohio Health Information Partnership

 - Olympus Endoworks

 - Optum

 - Orion Health

 - Ortech

 - OTTR Chronic Char Solutions

 - OzeScribe

 - PatientPing

 - PDHI

 - Pediatrix

 - Pentax

 - Philips

 - Picis

 - Polaris Health

 - ProType

 - ProVation Medical

 - Puritan Bennett

 - QuadraMed

 - Quest Diagnostics

 - Relay Health

 - Renesan Software

 - Rosch Visionary Systems

 - RVC

 - Salesforce.com

 - Scan One

 - SCC

 - ScottCare

 - Siemens

 - SoftMed

 - Softmedex

 - SoftScript, Inc.

 - SolCom

 - Spheris

 - Stb Zorg

 - Streamline Health

 - Summit Imaging

 - Sunquest

 - SystemLink

 - TeleHealth Services

 - TeleResults

 - The IPC Group

 - Transcend

 - TransDyne

 - UAMS

 - UTECH

 - Varian Medical Systems

 - vChart

 - Velos

 - Via Oncology

 - Vignette

 - virtuwell

 - Visicu

 - Vision Chips

 - Vynca

 - Vyne Medical

 - WebMedX

 - Wellsoft

 - Winscribe

 - Zipnosis

 - Zoll

 

 

 

### 
 Incoming Scanned Document Link
 [read the spec](/Tech/TechSpec?spec=5323)

 

 

 Receives and files scan pointers from an external document management system. This interface can also receive base64 encoded documents and store them to an Epic server. This interface does not file textual data intended for use in Radiant or Cupid; those documents must be processed by the Incoming Ancillary Results and Orders interface set up as an Incoming Ancillary Results and Orders - Imaging interface. Messages must be in HL7 MDM format. Documents processed by this interface can satisfy deficiencies in the Health Information Module. 
 

 

 [Current integrations include ](#)
 

 - 3M

 - Allscripts

 - Alpha Systems

 - Ambra Health

 - Ameripath

 - Amkai

 - ARUP

 - Athena Health

 - Bard Medical

 - Bernoulli

 - Biocoustics Instruments

 - Bright.md

 - Cardea Technology

 - Cardiac Science

 - CardioNet

 - Carevive

 - CBAY

 - Cedaron

 - Cerner

 - CGI

 - Citra Health Solutions

 - ClickView

 - Collective Medical Technologies

 - Conduent

 - Counsyl

 - Dentrix

 - Digisonics

 - Dolbey

 - DR Systems

 - Easy Software

 - EDCO

 - eHealth Technologies

 - Elekta

 - Elsevier

 - EMC2

 - emsCharts

 - EndoSoft

 - Epiphany

 - ePreop

 - ESO Solutions

 - Excel Medical

 - Extract Systems

 - FOTO Inc.

 - Fresenius Medical Care

 - Fuel Medical

 - Fujifilm

 - GE

 - Gene42

 - Genzyme Corporation

 - Healogics

 - HealthCare Clinical Laboratories

 - Healthloop

 - Hyland Software

 - IBM

 - iGuana

 - iMDsoft

 - IntelliDose

 - Intrascripts

 - INVIA Solutions

 - KnowledgeLake

 - LabCorp

 - Lanier

 - Life Systems International

 - LUMEDX

 - LVM Systems

 - McKesson

 - MDnetwork

 - MDRevolution

 - MEDHOST

 - Meditech

 - MedPlus

 - Medstreaming

 - Medtronic

 - Merge

 - MGC Diagnostics

 - Microsoft

 - Modernizing Medicine

 - Monarch Medical Technologies

 - Mortara

 - MSF&W

 - naviHealth

 - Net Health Systems

 - nThrive

 - Nuance Communications

 - Olympus Endoworks

 - PACSGear

 - Philips

 - ProVation Medical

 - QuadraMed

 - Quest Diagnostics

 - Redox

 - Rehab Documentation Company, Inc.

 - RVC

 - Scan One

 - Scientific Software Solutions

 - ScottCare

 - Siemens

 - SOC Telemed

 - SoftMed

 - SolCom

 - SourceCorp

 - Spectrum Medical

 - St. Jude's

 - Streamline Health

 - Stryker

 - Sunquest

 - Synedra

 - SystemLink

 - Taylor Healthcare

 - TriZetto Provider Solutions, a Cognizant Company

 - TSI

 - Uniform Data Systems

 - Urotex

 - USA

 - UTECH

 - Varian Medical Systems

 - Viasys Healthcare

 - Vignette

 - Vyne Medical

 - XSOLIS

 - Xtract Solutions

 

 

 

### 
 Smoking Cessation Integration
 [read the spec](/Tech/TechSpec?spec=5206)

 

 

 This is a group of three interfaces that together can be used to integrate with quit line vendors to communicate an order for cessation counseling, and receive in response the followup documented by the quit line and any medications, such as nicotine gum, given to the patient as part of the protocol. 
 

 

 [Current integrations include ](#)
 

 - California State Quit Line

 - National Jewish Health

 - Optum

 

 

 

### 
 Electronic Fetal Monitoring

 

 

 Epic integrates electronic fetal monitoring systems more tightly with inpatient workflows in the Epic EHR. The interfaces control establishing a shared identity with the EFM system, transmitting monitor vitals information from the fetal monitor to Epic, and associated documentation done in Epic with the fetal strip.
 

 

 [Current integrations include ](#)
 

 - CCSI OBIX

 - GE Centricity Perinatal

 - Hill-Rom NaviCare WatchChild

 - PeriGen

 - Philips OB TraceVue

 

 

 

### 
 Event Notifications via Direct
 [read the spec](/Tech/TechSpec?spec=5237)

 

 

 Epic sends CMS Event Notifications that conform to DirectTrust’s [Event Notifications via the Direct Standard™](https://directtrust.org/standards/event-notifications-via-direct) implementation guide. The goal of these notifications is to improve care coordination across healthcare settings, reduce readmissions, and improve transitions. The provided specification contains details regarding the HL7v2 attachments.
 

 

### 
 Coding - Bidirectional
 [read the spec](/Tech/TechSpec?spec=5430)

 

 

 The bidirectional interface is used to integrate with encoders and computer-assisted coding systems to exchange information for Hospital Coding workflows. Epic offers front-end integrations through web services as well as back-end integration methods. Separately, the outgoing interface can be used to send the final coded information to downstream systems such as care management products. 
 

 

 [Current integrations include ](#)
 

 - 3M 360 Encompass, 3M APCFinder/DRGFinder, 3M ARMS, 3M CDI System, 3M ClinTrac, 3M CodeFinder, 3M Coding & Reimbursement, 3M HDM, 3M HRMS

 - Dolbey Fusion CAC

 - M*Modal Fluency for Coding

 - Nuance Clintegrity 360 (Quantim) Facility Coding, Nuance Clintegrity 360 (Quantim) CAC

 - Optum Web.Strat, Optum Enterprise Computer-Assisted Coding

 - PLATOCODE Computer Assisted Coding

 - TruCode

 - Xerox MIDAS+

 

 

 

### 
 Electronic Laboratory Reporting

 

 

 This [Outgoing Results and Orders interface](../Interface/HL7v2#OutgoingResultsandOrders) sends results in the ELR format. ELR format results follow the HL7 version 2.5.1 Implementation Guide: Electronic Laboratory Reporting to Public Health, Release 1. This format is often used to notify public health agencies of tests which must be reported for disease tracking, and meet Meaningful Use (MU) or Promoting Interoperability (PI) measures in the U.S.
 

 

### 
 NAACCR Pathology Reporting
 [read the spec](/Tech/TechSpec?spec=5214)

 

 

 This [Outgoing Results and Orders Interface](../Interface/HL7v2#OutgoingResultsandOrders) sends messages for pathology reports that contain electronic cancer checklists. These messages conform to the North American Association of Central Cancer Registries (NAACCR) Standards for Cancer Registries Volume V rules for constructing HL7 messages for CAP electronic cancer checklist synoptic reporting.
 

 

### 
 Incoming Vaccination Administration
 [read the spec](/Tech/TechSpec?spec=5315)

 

 

 Receives unsolicited vaccination administration updates from either an immunization registry or an external clinical system that is not a registry. If integrating with a registry that supports the query interface, the query is the preferred integration.
 

 

 [Current integrations include ](#)
 

 - Axion Health ReadySet Occupational Health

 - CAIR (California)

 - CaraFlow

 - CHIRP (Indiana)

 - Eclipsys Sunrise Clinical Manager

 - PureSafety Occupational Health Manager

 - WIR (Wisconsin)

 

 

 

### 
 Outgoing Vaccination Query
 [read the spec](/Tech/TechSpec?spec=5201)

 

 

 Initiates a query to and receive a response from an immunization registry system. Each query requests data for a given patient. Generally, registries provide historical immunization data. Some registries additionally supply immunization recommendation data. The incoming portion of the interface does not directly update immunizations in the chart; the provider sees the response from the registry and decides what should be added to the patient record. HL7 2.5.1 specification conforms to the [Center for Disease Control HL7 2.5.1 Implementation Guide for Immunization Messaging](https://www.cdc.gov/vaccines/programs/iis/technical-guidance/downloads/hl7guide-1-5-2014-11.pdf).
 

 

 [Current integrations include ](#)
 

 - ALERT (Oregon)

 - CHIRP (Indiana)

 - CIIS (Colorado)

 - GRITS (Georgia)

 - ImmPact2 (Maine)

 - ImmPRINT (Alabama)

 - INC (Arkansas)

 - KSIR (Kansas)

 - LINKS (Louisiana)

 - MIIC (Minnesota)

 - NDIIS (North Dakota)

 - NESIIS (Nebraska)

 - PA-SIIS (Pennsylvania)

 - SDIR (San Diego)

 - ShowMeVax (Missouri)

 - WIR (Wisconsin)

 

 

 

### 
 Outgoing Vaccination Administration
 [read the spec](/Tech/TechSpec?spec=5204)

 

 

 Sends information about vaccination administrations to either an immunization registry or a clinical system or receiving system that is not a registry. An incoming response interface receives and files the response/acknowledgement returned from an immunization registry. The specification conforms to HTI-1 regulations, using the Center for Disease Control Implementation Guide for Immunization Messaging. 
 

 

 [Current integrations include ](#)
 

 - ImmTrac (Texas)

 - ALERT (Oregon)

 - ASIIS (Arizona)

 - CAIR (California)

 - CareEvolution HIEBus

 - CHILD (Washington)

 - CHIRP (Indiana)

 - CIIS (Colorado)

 - CIR (New York City)

 - dbMotion dbMotion Solution

 - DC Immunization Registry (Washington DC)

 - DIR (Delaware)

 - Eclipsys Sunrise Clinical Manager

 - Florida SHOTS (Florida)

 - GRITS (Georgia)

 - HIR (Hawaii)

 - I-CARE (Illinois)

 - ICLOPS Focus

 - ImmPRINT (Alabama)

 - ImmuNet (Maryland)

 - IMPACT SIIS (Ohio)

 - INC (Arkansas)

 - IRIS (Idaho)

 - IRIS (Iowa)

 - Kentucky Immunization Registry

 - KIDS Plus IIS (Philadelphia, PA)

 - Kryptiq CareManager

 - KSIR (Kansas)

 - LINKS (Louisiana)

 - MCIR (Michigan)

 - MIIC (Minnesota)

 - MIIS (Massachusetts)

 - MIR (Mississippi)

 - NDIIS (North Dakota)

 - NESIIS (Nebraska)

 - NJIIS (New Jersey)

 - NMSIIS (New Mexico)

 - NYSIIS (New York)

 - OSIIS (Oklahoma)

 - PA-SIIS (Pennsylvania)

 - SDIR (San Diego)

 - ShowMeVax (Missouri)

 - SIIS (South Carolina)

 - TOTS (Illinois)

 - USIIS (Utah)

 - VacTrAK (Alaska)

 - VIIS (Virginia)

 - WIR (Wisconsin)

 - WVSIIS (West Virginia)

 - WyIR (Wyoming)

 

 

 

### 
 Incoming Patient Administration from Population Register
 [read the spec](/Tech/TechSpec?spec=5341)

 

 

 The Finnish Population Information System (formerly known as the National Population Register or VRK), is a computerized national register that contains demographic information about Finnish citizens and foreign citizens residing in Finland. The population register sends data to this interface in a batch. 
 

 

### 
 Incoming Referral Notification
 [read the spec](/Tech/TechSpec?spec=5326)

 

 

 The recommended workflow, for a full closed loop referral is a 360 Exchange Closed Loop integration. [360X Closed Loop Referral](../Clinical/EHRtoEHR). This HL7v2 interface receives referral information from an external system, and is only able to create, update, and cancel a request for a referral in the receiving Epic system. 
 

 

### 
 Outgoing Referral Notification
 [read the spec](/Tech/TechSpec?spec=5216)

 

 

 The recommended workflow, for a full closed loop referral is a 360 Exchange Closed Loop integration. [360X Closed Loop Referrals](../Clinical/EHRtoEHR) This HL7v2 interface only sends new or updated request for referral information.