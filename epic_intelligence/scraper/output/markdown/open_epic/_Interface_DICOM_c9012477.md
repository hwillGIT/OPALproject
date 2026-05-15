# open.epic :: Explore By Interface Type

> Source: https://open.epic.com/Interface/DICOM

---

# 
 By Interface Type

 

 

 
 

 

 
 

 
 

 
 
 

## DICOM

 
Standards developed by Digital Imaging and Communications are used internationally for communicating medical images and related information. You can learn more from [DICOM](http://medical.nema.org). 

### 
 Imaging Integration
 [read the spec](/Tech/TechSpec?spec=5152)

 

 

 Epic has APIs available for PACS integration that include single sign-on, patient context synchronization, study context synchronization, and real-time measurement exchange. These APIs have been implemented to varying degrees across PACS and CPACS vendors. Check out our [DICOM conformance statement](../Tech/TechSpec?spec=staged/Epic DICOM Conformance Statement.pdf) as well. We additionally have an [encryption utility](../Tech/TechSpec?spec=Epic.EncryptionValidator.exe&specType=tools) for use with our XML integration (identical to URL encryption).
 

 

 [Current integrations include ](#)
 

 - Agfa

 - Ambra Health

 - BRIT

 - Change Healthcare

 - Client Outlook

 - Compressus

 - Digisonics

 - Fujifilm

 - GE

 - Heart Imaging Technologies

 - Hermes Medical Solutions

 - Hologic

 - Hyland

 - INFINITT NORTH AMERICA

 - Intelerad

 - LUMEDX

 - Medstreaming

 - Merge Healthcare

 - Mortara

 - PaxeraHealth

 - Philips

 - ScImage

 - Sectra

 - Siemens

 - Vidistar

 - VISAGE IMAGING, INC.

 - VISUS

 - Vital Images

 

 

 

### 
 MWL (Modality Work List)
 [read the spec](/Tech/TechSpec?spec=5409)

 

 

 This DICOM interface enables a piece of imaging equipment to obtain details of patients and scheduled examinations electronically, avoiding the need to type such information multiple times. 
 

 

### 
 MPPS (Modality Performed Procedure Step)
 [read the spec](/Tech/TechSpec?spec=5409)

 

 

 This DICOM interface provides a mechanism for modalities to send the procedure start and procedure complete notification. 
 

 

### 
 SR (Structured Reporting)
 [read the spec](/Tech/TechSpec?spec=5409)

 

 

 This DICOM interface provides a mechanism for modalities to send structured information from the performed exam to Epic. Each modality or exam can send different measurements. 
 

 

### 
 SC (Secondary Capture)
 [read the spec](/Tech/TechSpec?spec=5409)

 

 

 This DICOM interface provides a mechanism for modalities or a PACS to forward a copy of the DICOM SC images flagged by the technologist to Epic. We can process this message and file the image to be used when reviewing the patient's chart. 
 

 

### 
 WADO (Web Access to DICOM Objects) Import of Key Objects
 [read the spec](/Tech/TechSpec?spec=5409)

 

 

 This DICOM interface pulls key objects from the PACS via WADO to support streamlined workflows throughout the EHR. 
 

 

 [Current integrations include ](#)
 

 - Acuo

 - Dell