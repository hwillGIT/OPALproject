# open.epic :: Design Overview

> Source: https://open.epic.com/DesignOverview

---

- 

 

 

 

 
# 
 Design Overview
 

 

 

 

 Epic supports a wide variety of data exchange technologies. This guide
 provides an overview of design considerations and the different ways to
 plan your connection to organizations using Epic.
 

 
## 
 Discover Recommended Connection Practices
 

 

 Before designing your connection to Epic from scratch, explore our
 [Playbooks](/Playbooks) —
 proven data-sharing approaches built through collaboration between Epic
 staff and customers for common use cases. Each Playbook highlights
 supported standards, key design considerations, and real-world tips to
 help you get started. Building on open standards and community experience,
 these recommended practices help you ship safer, more reliable connections
 faster, so you can focus on delivering value to patients and providers
 instead of reinventing common connection logic.
 

 

 For example, over 500 patient-authorized health apps have connected to the
 Epic community in 2025. Our
 [Patient-Facing Consumer Health Apps Playbook](https://fhir.epic.com/Documentation?docId=patient_facing_apps)
 highlights how apps can use OAuth2.0 and modern FHIR APIs to help
 individuals access their health information. As networks have evolved,
 we've updated our recommended practice to include
 **TEFCA Individual Access Services (IAS)**,
 a national framework for secure, patient-authorized data exchange. TEFCA IAS
 can expand your app's reach, enabling individuals to retrieve records from
 multiple systems (including beyond Epic) through a single, trusted
 connection. It's a major step toward a more connected and patient-driven
 healthcare ecosystem.
 

 

 Playbooks give you a clear starting point where a path is already proven.
 When you're charting new territory, keep reading to design your connection.
 

 
## 
 What Should I Consider When Designing My Data Exchange?
 

 

 Due to the vast breadth of standards and types of APIs and interfaces a
 developer may wish to use, there are many factors to consider when
 determining the best way for you to exchange data with Epic. The sections
 below cover the most common considerations when designing a connection,
 while the
 [Case Studies section](#CaseStudies)
 toward the end of this document provides examples for applying
 these considerations to some sample scenarios.
 

 

 
 
 
 
 
 

 
### 
 Types of Data to Exchange
 

 

 Before you begin designing your connection, you must first understand what
 data you plan to exchange with Epic. Start by defining the discrete types
 of data your app will work with, and define a scope for the level of detail
 required within that data set. For example, you may need to exchange
 medication information. You should then more specifically define data
 elements you need within that data type, such as dosage information, RxNorm
 codes, etc.
 

 
### 
 Direction of Data Exchange
 

 

 After you have defined the data you need to exchange, determine the
 direction of that exchange. For example, transferring data
 from Epic to clinical registries may only need to read data from Epic.
 Meanwhile, a connection that results lab orders will need to write data
 back to Epic. Make sure you understand which data types need to be read out
 of Epic and which need to be written into Epic.
 

 

 When writing data to Epic, additional caution should be taken to ensure
 that the data written is accurate, complete, and documented on the correct
 patient. Improper use of these technologies may result in patient safety
 and data integrity concerns.
 

 
### 
 Workflows Using Data Exchange
 

 

 Next, determine when and how this data exchange should occur. Does data
 exchange occur based on a specific event, such as a clinician placing an
 order or a patient being discharged? Does data exchange occur on a
 schedule, such as a nightly data extract? Does data exchange occur when a
 user decides to launch your app? Some methods of data exchange might only be
 applicable in specific workflows or when specific events occur. Before
 determining your appropriate data exchange method, you must first define
 the workflows in which you plan to exchange data with Epic.
 

 
### 
 Data Exchange Method
 

 

 Epic recommends using industry standards for data exchange whenever
 possible. The most appropriate standard for your use case may vary. For
 example, NCPDP standards may be the most appropriate method to exchange of
 pharmaceutical data, while Digital Imaging and Communications (DICOM)
 standards may be the most appropriate method to exchange medical images.
 

 

 Once a data set, direction of data exchange, and workflows in which that
 exchange should occur are defined, you need to determine which
 standards or specific technologies are the most applicable.
 

 

 You can find information about the standards-based interfaces, APIs, and
 other data exchange methods that Epic currently supports by browsing the
 [API and Interface specifications](/TechnicalSpecifications)
 pages of open.epic.
 

 

 Here is a high-level overview of common use cases for
 various data sharing technologies:
 

 

 

 
 | 
 | 
 Recency | 
 Volume | 
 Direction | 
 Standards | 
 Trigger | 
 |

 
 
 | 
 HL7 Interfaces | 
 Real-time | 
 High | 
 Push | 
 ✔️ | 
 Event-driven | 
 |

 | 
 RESTful FHIR | 
 Real-time | 
 Low | 
 Push/Pull | 
 ✔️ | 
 On-demand | 
 |

 | 
 HL7 CDA | 
 Varies | 
 Medium | 
 Push/Pull | 
 ✔️ | 
 Varies | 
 |

 | 
 SMART Apps | 
 Real-time | 
 Low | 
 Bidirectional | 
 ✔️ | 
 On-demand | 
 |

 | 
 CDS Hooks | 
 Real-time | 
 Low | 
 Bidirectional | 
 ✔️ | 
 Event-driven | 
 |

 | 
 FHIRCast | 
 Real-time | 
 Low | 
 Bidirectional | 
 ✔️ | 
 Contextual | 
 |

 | 
 Bulk FHIR | 
 Delayed | 
 Moderate | 
 Pull | 
 ✔️ | 
 Batch | 
 |

 | 
 Reporting Tools | 
 Delayed | 
 High | 
 Push/Pull | 
 ❌ | 
 Batch | 
 |

 | 
 Other Web Services | 
 Real-time | 
 Low | 
 Varies | 
 ❌ | 
 Varies | 
 |

 
 

 

 

 In some cases, industry standards may not fully meet your needs.
 Epic has developed Epic-specific data exchange methods that extend the capabilities of industry standards for some use cases.
 For example, some Epic-specific web services are described on the [Web Services page](../Interface/WebServices) of open.epic.
 Other options may be available through our [Vendor Services](../EpicSupport) offering.

 

 
### 
 Security Mechanisms
 

 

 Due to the sensitive nature of healthcare data, data exchange technologies
 generally require various forms of authentication, authorization, and
 security. Some connections may use an SSO solution, such as SMART on FHIR,
 for authentication using the OAuth 2.0 framework for authorization while
 others rely on security mechanisms like client certificates or TCP/IP
 connections. Consider what authentication mechanisms are supported by the
 data exchange methods you have selected for your use case. Applications with some form
 of user interface generally require an authentication mechanism to
 authenticate the specific user gaining access to that data, while
 system-to-system connections are less likely to require user-based
 authentication.
 

 

 OAuth 2.0 is the preferred method of security for apps in which Epic users
 interact with data. TCP/IP connections and TLS/SSL certificates are common
 security mechanisms for system-to-system connections.
 

 
### 
 Where Do I Go from Here?
 

 

 Now that we've gone through the basics of which technologies to use for your data exchange
 with Epic, you can focus on turning those recommendations into a working connection.
 

 

 Check out our [step-by-step developer guide](/DeveloperResources) for
 next steps in creating a connection to a customer environment.
 

 

 For a brief overview of how to work with an Epic Community Member
 to develop your product's connection to Epic, see our
 [Strategies to Effectively Collaborate](https://fhir.epic.com/Documentation?docId=eofcollaborate)
 page.
 

 
## 
 Case Studies
 

 

 Now that we've talked about the process, you may be wondering how to apply
 that logic to your own proposed method of data exchange. This section
 provides some example scenarios for how you might apply this document's logic
 to your own decision-making process.
 

 
### 
 Case Study A: Scheduling
 

 

 *This example was last reviewed on December 15, 2022.*
 

 

 In this scenario, your organization works with patients who would like to
 schedule appointments at Epic clinics and facilities. You'd like to be able
 to view a patient's upcoming appointments, schedule new appointments, and
 cancel existing appointments.
 

 
#### 
 Types of Data to Exchange
 

 

 Your organization is only interested in basic patient information and
 appointment related data. This can help you determine potentially
 applicable technologies. Now we can look at the different data exchange
 technologies that support your desired use.
 

 

 
 FHIR APIs
 

 
 [Appointment $find](https://fhir.epic.com/Specifications?api=840)
 

 - 
 [Appointment $book](https://fhir.epic.com/Specifications?api=839)
 

 - 
 [Schedule.Read](https://fhir.epic.com/Specifications?api=500)
 

 - 
 [Slot.Read](https://fhir.epic.com/Specifications?api=862)
 

 - 
 [Appointment.Read](https://fhir.epic.com/Specifications?api=466)
 

 

 

 - 
 HL7v2 Interfaces

 

 
 [Outgoing Appointment Scheduling](../Interface/HL7v2#OutgoingAppointmentScheduling)
 

 - 
 [Incoming Appointment Scheduling](../Interface/HL7v2#IncomingAppointmentScheduling)
 

 

 
 - 
 Additional API technologies

 

 
 If you have use cases that do not seem to be covered with the technologies above, contact Vendor Services to determine if there are additional technologies available that fit your use case.
 

 

 
 

 

 In this step, you'll also want to consider individual data elements that
 your connection relies on. For appointments this may be information about
 the patient, provider, visit type, department, date and time. Some data
 exchange technologies may only support certain data fields or only provide
 limited details about the field. Making a comprehensive list of all data
 elements your application requires can help you determine whether or
 not a specific data exchange technology meets your needs.
 

 
#### 
 Direction of Data Exchange
 

 

 For this connection, your organization would like to read a patient's
 current appointments from Epic, and write new appointments, cancellations,
 and reschedules into Epic. Consequently, the direction of data exchange varies.
 In this step, you may also want to consider whether this reading
 and writing of data is initiated by your system or by Epic.
 

 

 For retrieving a patient's upcoming appointments, you have to decide if you
 want to retrieve a schedule from Epic, or be notified of schedule changes
 so that you can create your own schedule. A related question is: do you
 want to store upcoming appointments? Or do you want to retrieve upcoming
 appointments only when a patient asks? If you want to create the schedule,
 and only be notified of changes to the schedule, HL7v2 interfaces are a
 good choice for proactive notifications. If you want to retrieve a complete
 picture, or appointments only when a patient asks, then querying data
 through APIs allows for this flexibility. You look at the FHIR APIs and
 don't see an appointment.search option to retrieve an upcoming appointment
 for which you don't know the FHIR ID. You contact Vendor Services, who investigates whether
 there are additional APIs that can retrieve upcoming appointment
 information for a patient.
 

 

 You are looking to schedule and cancel appointments in Epic.
 However, you may need to query information from Epic first.
 APIs allow for querying of existing information like available slots
 and existing appointments if they aren't stored in your system. You see
 that appointment $find may be helpful for this use.
 

 
#### 
 Workflows Using Data Exchange
 

 

 Patients will interact with your web page
 to manage their appointments. You are most interested in allowing patients
 to view upcoming appointments and cancel appointments that are no longer
 needed. Your app provides a convenient way for patients new to an
 organization to schedule appointments. With the patient as the user, and
 desiring the ability to search for available slots, you would like to use
 APIs. Looking closer into Appointment $find you see that it is intended for
 a non-patient user and requires the customer to do significant build. You
 also do not see an API to cancel appointments, so you contact Vendor Services
 to help investigate whether additional APIs are available.
 

 
#### 
 Security Method
 

 

 Different APIs and interfaces have different security capabilities. In this
 scenario your app is controlled by the patient but any API calls or HL7
 messages are secured on the backend.
 

 

 A patient using your website may not have an Epic patient portal (MyChart)
 account, so they may not have any Epic credentials to facilitate single
 sign-on with your website. With APIs, you will support an OAuth 2.0 Client
 Credentials flow or basic authentication with a generic user for your app.
 This grants you an access token that can be used to authorize
 subsequent API calls.
 

 

 For HL7 you use a TCP/IP connection rather than HL7v2 over HTTPS. Data
 transferred with HL7v2 won't rely on authentication, but rather relies
 on other security mechanisms to secure your data exchange.
 

 
#### 
 Data Exchange Method
 

 

 Now that you've analyzed the above sections, we can pull that information
 together.
 

 

 You want to store your own schedule of appointments so you can send
 appointment reminders whether or not a patient logs into your portal. You
 opt to receive HL7v2 messages for appointment booking, cancellation,
 modification and for no shows so you can store this data in your own
 database. For scheduling new appointments, you decide to use additional
 API technologies available through Vendor Services. When a patient decides to book an
 appointment, you don't know what slots are available to book, so you decide
 to use APIs to query for appointment availability. Then, to book the
 appointment for the patient you decide to use APIs because the data fields
 returned by the availability API and required by the scheduling API match.
 You also decide to cancel appointments through APIs.
 

 
### 
 Case Study B: Reference Labs
 

 

 *This example was last reviewed on December 5, 2022.*
 

 

 In this scenario, your organization results labs for hospitals, some of
 which use Epic, and you'd like to be able to send lab orders and results
 back and forth between the two systems. How will you design your connection?
 

 
#### 
 Types of Data to Exchange
 

 

 The main groups of data types your organization is interested in are lab
 orders and lab results. This can help you limit down potential
 technologies. Now you can look at the different data exchange technologies
 that support these mechanisms:
 

 

 - 
 FHIR APIs
 

 
 [ServiceRequest (Order Procedure)](https://fhir.epic.com/Specifications?api=1054) for lab orders
 

 - 
 [Observation (Labs)](https://fhir.epic.com/Specifications?api=999) for lab results
 

 - 
 [DiagnosticReport](https://fhir.epic.com/Specifications?api=989) for lab results
 

 

 

 - 
 HL7v2 Interfaces
 

 
 [Outgoing Ancillary Orders interface](../Interface/HL7v2#OutgoingAncillaryOrders) for lab orders
 

 - 
 [Incoming Ancillary Results interface](../Interface/HL7v2#IncomingAncillaryResults) for lab results
 

 

 

 - 
 Additional APIs
 

 
 Lab APIs which may be available through Vendor Services
 

 

 

 

 

 In this step, you'll also want to consider individual data elements that
 you need. For labs, this may be information about the
 specimen, how it was collected, when it was received, etc. Say your lab
 also supports microbiology labs, where your application also needs to
 record sensitivity and isolate information. Some data exchange technologies
 only support certain data fields, so making a comprehensive list of all
 data elements your connection requires can help you determine whether
 or not a specific data exchange technology meets your needs.
 

 
#### 
 Direction of Data Exchange
 

 

 For this connection, your organization would like to read lab orders from
 Epic and write lab results into Epic. This means that the direction of data
 exchange varies depending on the type of data you're exchanging. In this
 step, you may also want to consider whether this reading and writing of
 data is initiated by your system or by Epic.
 

 

 Looking at the lab ordering step of the workflow, you aren't sure when a
 lab order will be placed in Epic. Rather than continually querying Epic for
 lab orders, you would prefer that Epic send you the lab order each time one
 of these orders is placed. In that case, you want Epic to push this lab
 order data into your system. HL7v2 interfaces are great for this type of
 proactive messaging so you'll want to keep that in mind in your design.
 

 

 Looking at the lab resultng step of the workflow, you do know when a
 lab is resulted in your system, so you should control when you send lab
 results back to Epic. This means that you'll push lab result back into Epic
 from your system. Many different technologies exchange lab results.
 However, you're looking to write this data, not read it. You see that
 Observation (Labs) does not support a Create interaction that would allow
 you to create this lab result in Epic. You contact Vendor Services, who informs
 you that there are no additional APIs that would allow you to write lab
 results back to Epic either. You do note that the HL7v2 Incoming Ancillary
 Results would allow you to write this data into Epic.
 

 
#### 
 Workflows Using Data Exchange
 

 

 This section is simple: you'd like to share data for
 lab ordering and resulting workflows. You're most
 interested in ordering workflow after the order has been signed and the
 resulting workflow before the lab has been resulted in Epic. Your app
 supplements these workflows by automating the delivery of orders and the
 receipt of lab results. This could replace an old workflow such as sending
 orders and results manually by fax.
 

 
#### 
 Data Exchange Method
 

 

 Now that you have analyzed the above sections, you can pull that
 information together.
 

 

 For your app connection, it makes the most sense to use the Outgoing Ancillary
 Orders and Incoming Ancillary Results HL7v2 interfaces.
 

 
#### 
 Security Method
 

 

 Now that you've generally determined the data exchange technologies needed
 for your app, you'll also want to think about what, if any, authentication
 method is needed. Since this app is entirely system-to-system using HL7v2
 interfaces and you use a TCP/IP connection rather than HL7v2 over HTTPS,
 your connection won't rely on authentication, but rather relies on
 other security mechanisms to secure your data exchange.