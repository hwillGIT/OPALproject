# Artifacts Summary - SMART App Launch v2.2.0

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/artifacts.html

---

SMART App Launch, published by HL7 International / FHIR Infrastructure. This guide is not an authorized publication; it is the continuous build for version 2.2.0 built by the FHIR (HL7® FHIR® Standard) CI Build. This version is based on the current content of [https://github.com/HL7/smart-app-launch/](https://github.com/HL7/smart-app-launch/) and changes regularly. See the [Directory of published versions](http://hl7.org/fhir/smart-app-launch/history.html)

 
## Artifacts Summary

 
 
 
 

 
Contents:

 

 - 
 [User Access Brands](#1)
 

 - 
 [User Access Brand Examples](#2)
 

 - 
 [SMART App State](#3)
 

 - 
 [SMART Launch Tasks](#4)
 

 

 
This page provides a list of the FHIR artifacts defined as part of this implementation guide.

 
 
### User Access Brands 

 
Helping patients find and connect to the right API endpoints, by enabling publication of branding information for API providers, portals, and endpoints.

For an overview, see [User Access Brands](brands.html).

 
 
 | 
 
 [User Access Brands Bundle Profile](StructureDefinition-user-access-brands-bundle.html)
 | 
 

FHIR Bundle of Organizations and Endpoints that is hosted at a stable, publicly available location

 | 
 |

 | 
 
 [User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html)
 | 
 

Profile on Organization to convey a User Access Brand

 | 
 |

 | 
 
 [User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html)
 | 
 

Profile on Endpoint associated with a User Access Brand

 | 
 |

 | 
 
 [User Access Category Value Set](ValueSet-user-access-category.html)
 | 
 

Categorizes a UserAccessBrand into high-level taxonomy

 | 
 |

 
 

 
 
### User Access Brand Examples 

 
The following examples demonstrate use of User Access Brands. See [example-brands](./example-brands.html) for a guided tour.

 
 
 | 
 
 [Lab with Locations Nationwide](Bundle-example1.html)
 | 
 |

 | 
 
 [Regional Health System With Independently Branded Affiliates](Bundle-example2.html)
 | 
 |

 | 
 
 [Different EHRs for different sub-populations displayed in a unified card](Bundle-example3.html)
 | 
 |

 | 
 
 [Two co-equal brands](Bundle-example4.html)
 | 
 |

 
 

 
 
### SMART App State 

 
Helping apps persist state to an EHR.

 
 
 | 
 
 [SMART App State](StructureDefinition-smart-app-state-basic.html)
 | 
 

SMART App State profile on Basic resource

 | 
 |

 | 
 
 [App State Server CapabilityStatement](CapabilityStatement-smart-app-state-server.html)
 | 
 

Required capabilities for App State Server

 | 
 |

 | 
 
 [Example App State](Basic-app-state.html)
 | 
 

Example App State

 | 
 |

 
 

 
 
### SMART Launch Tasks 

 
Helping EHRs manage deferred or proposed app launches.

For an overview, see [Task profile for requesting SMART launch](task-launch.html).

 
 
 | 
 
 [TaskEhrLaunch](StructureDefinition-task-ehr-launch.html)
 | 
 

Defines a Task that indicates the user should launch an application using the SMART on FHIR EHR launch.

 | 
 |

 | 
 
 [TaskStandaloneLaunch](StructureDefinition-task-standalone-launch.html)
 | 
 

Defines a Task that indicates the user should launch an application as a standalone application.

 | 
 |

 | 
 
 [SMART on FHIR terminology.](CodeSystem-smart-codes.html)
 | 
 

Codes used in profiles related to SMART on FHIR.

 | 
 |

 | 
 
 [Codes for tasks to application launches](ValueSet-smart-launch-info.html)
 | 
 

Defines codes for Tasks that request launch of SMART applications.

 | 
 |

 | 
 
 [Launch Types for tasks to application launches](ValueSet-smart-launch-types.html)
 | 
 

Defines Launch Type codes for Tasks that request launch of SMART applications.

 | 
 |

 | 
 
 [Example Task for Standalone Launch](Task-task-for-standalone-launch.html)
 | 
 

Example Task for Standalone Launch

 | 
 |

 | 
 
 [Example Task for EHR Launch](Task-task-for-ehr-launch.html)
 | 
 

Example Task for EHR Launch

 | 
 |