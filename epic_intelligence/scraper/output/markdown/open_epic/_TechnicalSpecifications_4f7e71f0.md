# open.epic :: Technical Specifications

> Source: https://open.epic.com/TechnicalSpecifications

---

- 

 

 

 
# 
 Data Sharing Specifications
 

 

 

 Explore hundreds of standards-based specifications to interoperate with Epic customers.
 

 

 

 

 
 

 

 
## 
 Interfaces
 

 

 Each month more than 45 billion messages are sent between Epic and non-Epic systems.
 Across the Epic community, we have over 60,000 active interfaces with more than 2,000 vendors.
 We offer interfaces that are compliant with international standards and can support
 interfaces that are either real-time or batch, one-way or bidirectional, or point-to-point or mediated by an interface engine.
 

 

 
 To get started with event-driven interfaces, check out our [Interfaces tutorial](https://fhir.epic.com/Documentation?docId=interfaces).
 

 - 
 To learn more about each standard and any requirements that the standards body may have to use their interfaces, visit the standards body's website.
 

 - 
 Explore and download documentation about Epic's interface implementation by standard:
 [HL7](/Interface/HL7v2),
 [ASC X12](/Interface/X12),
 [NCPDP](/Interface/NCPDP),
 [DICOM](/Interface/DICOM), and
 [other standards](/Interface/Other), or find our specifications by category:
 

 

 

 [
 
 Ancillary
 ](/Ancillary)
 [
 
 Clinical
 ](/Clinical)
 [
 
 Financial
 ](/Financial)
 [
 
 Registration
 ](/Identity)
 [
 
 Country-Specific
 ](/CountrySpecific)
 [
 
 Operations
 ](/Operational)
 [
 
 Public Health
 ](/PublicHealth)
 [
 
 Scheduling
 ](/Scheduling)
 

 

 

 

 

 [](/Interface/FHIR)
 

 

 
## 
 FHIR
 

 

 Epic is a strong supporter of HL7® FHIR® (Fast Healthcare Interoperability Resources) as the future of REST-based interoperability. In addition to participating in the standards development process with HL7, Epic is also a member of the Argonaut Project and the Da Vinci Project, each aimed at accelerating the adoption of FHIR.
 

 

 Epic software includes support for a range of DSTU2, STU3, and R4 read, search, and write resources and we are continuing to add support for new resources to keep up to date as new FHIR and USCDI versions are released and adopted by the industry.
 

 
### 
 If you're just getting started with FHIR:
 

 

 - 
 Check out a [summary of our FHIR capabilities](/Interface/FHIR)
 or dive right into the [API specifications](https://fhir.epic.com/Specifications) through our FHIR developer toolbox.
 

 - 
 Review our [OAuth2 tutorial](https://fhir.epic.com/Documentation?docId=oauth2tutorial) and
 [step-by-step OAuth2 specification](https://fhir.epic.com/Documentation/Index?docId=oauth2)
 to learn how to authorize your app for making FHIR API calls.
 

 - 
 See an example of using FHIR API calls to retrieve patient clinical data in our
 [FHIR Tutorial](https://fhir.epic.com/Documentation?docId=fhir), and find more details on
 [using Search parameters](https://fhir.epic.com/Documentation?docId=searchparameters)
 in your FHIR queries, and get tips
 [on using ID Types with FHIR APIs](https://fhir.epic.com/Documentation?docId=epicidtypes).
 

 

 
### 
 When you're creating a new app and registering the client ID with Epic:
 

 

 - 
 If you're building a patient-facing app,
 [review your options for distributing your client ID](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps)
 to customers.
 

 - 
 Review our recommendations on setting the
 [App Default FHIR Version](https://fhir.epic.com/Documentation?docId=appfhirversion).
 

 

 
### 
 Advanced FHIR use cases:
 

 

 - 
 For guidance on using FHIR Bulk Data for population-level exports, see our
 [FHIR Bulk Data documentation](https://fhir.epic.com/Documentation?docId=fhir_bulk_data).
 

 - 
 For details on supporting cross-border interoperability, see our
 [International Patient Summary (IPS) documentation](https://fhir.epic.com/Documentation?docId=internationalpatientsummary).
 

 

 

 

 

 

 
 

 

 
## 
 Additional Industry-Standard and Public APIs
 

 

 In addition to FHIR, Epic provides robust support for emerging
 **industry-standard APIs**. Here
 are some examples that allow deep connectivity into our software's workflows:
 

 

 - 
 See our
 [SMART on FHIR launch guide](https://fhir.epic.com/Documentation?docId=oauth2&section=EmbeddedOauth2Launch)
 for details on app launch workflows, context passing, and OAuth2.0 security flows.
 

 - 
 Epic software also includes support for CDS Hooks
 ([specification](/interface/FHIR#CDSHooks),
 [tutorial](https://fhir.epic.com/Documentation?docId=cds-hooks)),
 which enables apps and services to provide real-time clinical decision support within the
 clinician's workflow.
 

 - 
 We support a range of client connections with our
 [Hyperdrive](/Hyperdrive) client, including
 [FHIRcast](/Hyperdrive#FHIRcast),
 an HL7 standard for synchronizing context across multiple applications, allowing
 EHRs, imaging systems, and third-party apps to stay aligned on the same patient and
 workflow.
 

 - 
 Connect using
 [other industry standards](/Interface/Other)
 such as the Bluetooth© Generic Health Sensor Device Integration with MyChart.
 

 

 

 Over the years, Epic has worked with industry standards bodies to create CDS Hooks and
 FHIRcast standards and we continue to participate in the ongoing standards evolution in these
 areas.
 

 

 Epic also offers a set of
 [web services](/Interface/WebServices)
 and other
 **public APIs**
 that extend functionality beyond standards-based
 exchange, providing additional data sharing opportunities for vendors and health systems.
 Examples include:
 

 

 - 
 [Speech-to-Text APIs](/Hyperdrive#SpeechRecognition)
 enable real-time or asynchronous transcription to streamline clinical documentation and
 improve provider efficiency.
 

 - 
 [Credit Card Device and Payment Gateway APIs](/Interface/WebServices#CreditCardandBankAccountIntegration)
 support secure payment workflows by connecting external credit card devices and payment
 gateways with Epic's billing and financial systems.
 

 - 
 [Wait Times APIs](/Interface/WebServices#WaitTimeAPIs)
 share appointment and service wait time data externally, helping patients and partners
 access up-to-date scheduling information.
 

 

 

 Check out the
 [**full list of industry-standard and Epic public APIs here**](/Home/oeAPIList).
 

 

 

 

 

 
 

 

 
## 
 Epic Private APIs
 

 

 Epic prioritizes the use of industry-standard APIs to promote data exchange and consistency
 across healthcare systems. Epic has developed Epic Private Technologies to extend functionality
 and address specific needs for
 certain cases where no appropriate industry standard exists.
 Private APIs are available to developers in our
 Vendor Services program.
 

 

 

 

 

 
 

 

 
## 
 Exports
 

 

 Epic software gives users the ability to export electronic health information in multiple
 electronic formats depending on the use case. Exports can be formatted to be human-readable or
 computable (machine-readable). Exports that are formatted to be computable can be provided in
 industry standard formats (suitable for most scenarios where information will be exchanged with
 other systems) or Epic-native formats (suitable when all available information is needed).
 

 

 A few examples of available electronic formats include:
 

 

 - 
 Human-readable documents, such as PDFs, for subsets of clinical electronic health information.
 

 - 
 [FHIR-formatted files](/Interface/FHIR#BulkDataAccess)
 for a subset of electronic health information in FHIR.
 

 - 
 [C-CDA-formatted XML documents](/Clinical/EHRtoEHR#ClinicalDocumentArchitecture(CDA)) for subsets of electronic health information that can be expressed in C-CDA templates.
 

 - 
 [EHI Tables](/EHITables) for all Epic electronic health information, in a computable, tab-separated value (TSV) file format native to Epic.
 

 

 
### 
 SQL Exports from Relational Reporting Databases
 

 

 - 
 **Kit** is a collection of views and stored procedures for access
 to clinical, operational, and financial data models from an Epic community member's
 data warehouse. The Kit data model has been optimized for performance,
 ease of reporting, and collaboration between organizations. Kit APIs are designed to
 give app developers a way to write standard queries that are compatible out of the box
 with any Epic community member's data warehouse. Kit APIs are available to developers in
 Vendor Services.
 

 - 
 **Clarity** is a relational database that contains the data you'll find in
 Kit and more. Without the standardization and other benefits provided by Kit,
 developers querying Clarity may need to create more complex queries and customize
 queries to each Epic community member. Developers can license use of the Clarity data
 model through Vendor Services.
 

 

 

 

 

 

 
 

 

 
## 
 External Health Records
 

 

 Epic provides seamless interoperability solutions to ensure healthcare providers can access the
 right patient information at the right time, helping clinicians deliver safer and more
 coordinated treatment. Epic customers participate in national data exchange frameworks using
 [widely adopted standards](/Clinical/EHRtoEHR)
 such as
 [C-CDA](/Clinical/EHRtoEHR#ClinicalDocumentArchitecture(CDA))
 and
 [IPS](https://fhir.epic.com/Documentation?docId=internationalpatientsummary),
 exchanging hundreds of millions of records per month.
 

 

 Check out
 [our tutorial](https://fhir.epic.com/Documentation?docId=external_health_records_for_patient_treatment)
 to learn more about treatment-based exchange patient records between providers through nationwide networks such as Carequality and TEFCA.
 

 
 

 

 

 

 
 

 

 
## 
 Couldn't find it?
 

 

 Trying to connect with Epic and didn't find what you were looking for? Use
 [Technology Guidance](/Contact#DataSharingGuidance)
 form to tell us more about what you're seeking.