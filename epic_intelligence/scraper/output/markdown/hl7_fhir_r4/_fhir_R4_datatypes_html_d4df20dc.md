# Datatypes - FHIR v4.0.1Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeActual value attribute of the data typeActual value attribute of the data typeActual value attribute of the data typeActual value attribute of the data typeActual value attribute of the data typeActual value attribute of the data typeActual value attribute of the data typeActual value attribute of the data typeActual value attribute of the data typeActual value attribute of the data typeExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe value of the measured amount. The value includes an implicit precision in the presentation of the valueHow the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value (this element modifies the meaning of other elements)How the Quantity should be understood and represented. (Strength=Required)A human-readable form of the unitThe identification of the system that provides the coded form of the unitA computer processable form of the unit in some unit representation systemIdentifies the type of the data in the attachment and allows a method to be chosen to interpret or render the data. Includes mime type parameters such as charset where appropriateThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)The human language of the content. The value can be any valid value according to BCP 47A human language. (Strength=Preferred)The actual data of the attachment - a sequence of bytes, base64 encodedA location where the data can be accessedThe number of bytes of data that make up this attachment (before base64 encoding, if that is done)The calculated hash of the data using SHA-1. Represented using base64A label or set of text to display in place of the dataThe date that the attachment was first createdThe low limit. The boundary is inclusiveThe high limit. The boundary is inclusiveThe start of the period. The boundary is inclusiveThe end of the period. If the end of the period is missing, it means no end was known or planned at the time the instance was created. The start may be in the past, and the end date in the future, which means that period is expected/planned to end at that timeThe value of the numeratorThe value of the denominatorA reference to a code defined by a terminology systemA human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the userThe identification of the code system that defines the meaning of the symbol in the codeThe version of the code system which was used when choosing this code. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchangedA symbol in syntax defined by the system. The symbol may be a predefined code or an expression in a syntax defined by the coding system (e.g. post-coordination)A representation of the meaning of the code in the system, following the rules of the systemIndicates that this coding was chosen by a user directly - e.g. off a pick list of available items (codes or displays)The individual responsible for making the annotationIndicates when this particular annotation was madeThe text of the annotation in markdown formatNumerical value (with implicit precision)ISO 4217 Currency CodeA code indicating the currency, taken from ISO 4217. (Strength=Required)Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe purpose of this identifier (this element modifies the meaning of other elements)Identifies the purpose for this identifier, if known . (Strength=Required)A coded type for the identifier that can be used to determine which identifier to use for a specific purposeA coded type for an identifier that can be used to determine which identifier to use for a specific purpose. (Strength=Extensible)Establishes the namespace for the value - that is, a URL that describes a set values that are uniqueThe portion of the identifier typically relevant to the user and which is unique within the context of the systemTime period during which identifier is/was valid for useOrganization that issued/manages the identifierIdentifies the purpose for this name (this element modifies the meaning of other elements)The use of a human name. (Strength=Required)Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific partsThe part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his fatherGiven namePart of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the namePart of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the nameIndicates the period of time when this name was valid for the named personThe purpose of this address (this element modifies the meaning of other elements)The use of an address. (Strength=Required)Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are bothThe type of an address (physical / postal). (Strength=Required)Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific partsThis component contains the house number, apartment number, street name, street direction,  P.O. Box number, delivery hints, and similar address informationThe name of the city, town, suburb, village or other community or delivery centerThe name of the administrative area (county)Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes)A postal code designating a region defined by the postal serviceCountry - a nation as commonly understood or generally acceptedTime period when address was/is in useTelecommunications form for contact point - what communications system is required to make use of the contactTelecommunications form for contact point. (Strength=Required)The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address)Identifies the purpose for the contact point (this element modifies the meaning of other elements)Use of contact point. (Strength=Required)Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank valuesTime period when the contact point was/is in useIdentifies specific times when the event occursA code for the timing schedule (or just text in code.text). Some codes such as BID are ubiquitous, but many institutions define their own additional codes. If a code is provided, the code is understood to be a complete statement of whatever is specified in the structured timing data, and either the code or the data may be used to interpret the Timing, with the exception that .repeat.bounds still applies over the code (and is not contained in the code)Code for a known / defined timing pattern. (Strength=Preferred)Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing scheduleA total count of the desired number of repetitions across the duration of the entire timing specification. If countMax is present, this element indicates the lower bound of the allowed range of count valuesIf present, indicates that the count is a range - so to perform the action between [count] and [countMax] timesHow long this thing happens for when it happens. If durationMax is present, this element indicates the lower bound of the allowed range of the durationIf present, indicates that the duration is a range - so to perform the action between [duration] and [durationMax] time lengthThe units of time for the duration, in UCUM unitsA unit of time (units from UCUM). (Strength=Required)The number of times to repeat the action within the specified period. If frequencyMax is present, this element indicates the lower bound of the allowed range of the frequencyIf present, indicates that the frequency is a range - so to repeat between [frequency] and [frequencyMax] times within the period or period rangeIndicates the duration of time over which repetitions are to occur; e.g. to express "3 times per day", 3 would be the frequency and "1 day" would be the period. If periodMax is present, this element indicates the lower bound of the allowed range of the period lengthIf present, indicates that the period is a range from [period] to [periodMax], allowing expressing concepts such as "do this once every 3-5 daysThe units of time for the period in UCUM unitsA unit of time (units from UCUM). (Strength=Required)If one or more days of week is provided, then the action happens only on the specified day(s) (Strength=Required)Specified time of day for action to take placeAn approximate time period during the day, potentially linked to an event of daily living that indicates when the action should occurReal world event relating to the schedule. (Strength=Required)The number of minutes from the event. If the event code does not indicate whether the minutes is before or after the event, then the offset is assumed to be after the eventAn indication of the reason that the entity signed this document. This may be explicitly included as part of the signature information and can be used when determining accountability for various actions concerning the documentAn indication of the reason that an entity signed the object. (Strength=Preferred)When the digital signature was signedA reference to an application-usable description of the identity that signed  (e.g. the signature used their private key)A reference to an application-usable description of the identity that is represented by the signatureA mime type that indicates the technical format of the target resources signed by the signatureThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)A mime type that indicates the technical format of the signature. Important mime types are application/signature+xml for X ML DigSig, application/jose for JWS, and image/* for a graphical image of a signature, etcThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)The base64 encoding of the Signature content. When signature is not recorded electronically this element would be emptyThe base quantity that a measured value of zero represents. In addition, this provides the units of the entire measurement seriesThe length of time between sampling times, measured in millisecondsA correction factor that is applied to the sampled data points before they are added to the originThe lower limit of detection of the measured points. This is needed if any of the data points have the value "L" (lower than detection limit)The upper limit of detection of the measured points. This is needed if any of the data points have the value "U" (higher than detection limit)The number of sample points at each time point. If this value is greater than one, then the dimensions will be interlaced - all the sample points for a point in time will be recorded at onceA series of data points which are decimal values separated by a single space (character u20). The special values "E" (error), "L" (below detection limit) and "U" (above detection limit) can also be used in place of a decimal valueMay be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself) (this element modifies the meaning of other elements)A set of rules that describe when the event is scheduledExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeIdentifies the type of the data in the attachment and allows a method to be chosen to interpret or render the data. Includes mime type parameters such as charset where appropriateThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)The human language of the content. The value can be any valid value according to BCP 47A human language. (Strength=Preferred)The actual data of the attachment - a sequence of bytes, base64 encodedA location where the data can be accessedThe number of bytes of data that make up this attachment (before base64 encoding, if that is done)The calculated hash of the data using SHA-1. Represented using base64A label or set of text to display in place of the dataThe date that the attachment was first createdExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeIdentifies the type of the data in the attachment and allows a method to be chosen to interpret or render the data. Includes mime type parameters such as charset where appropriateThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)The human language of the content. The value can be any valid value according to BCP 47A human language. (Strength=Preferred)The actual data of the attachment - a sequence of bytes, base64 encodedA location where the data can be accessedThe number of bytes of data that make up this attachment (before base64 encoding, if that is done)The calculated hash of the data using SHA-1. Represented using base64A label or set of text to display in place of the dataThe date that the attachment was first createdExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe identification of the code system that defines the meaning of the symbol in the codeThe version of the code system which was used when choosing this code. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchangedA symbol in syntax defined by the system. The symbol may be a predefined code or an expression in a syntax defined by the coding system (e.g. post-coordination)A representation of the meaning of the code in the system, following the rules of the systemIndicates that this coding was chosen by a user directly - e.g. off a pick list of available items (codes or displays)Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe identification of the code system that defines the meaning of the symbol in the codeThe version of the code system which was used when choosing this code. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchangedA symbol in syntax defined by the system. The symbol may be a predefined code or an expression in a syntax defined by the coding system (e.g. post-coordination)A representation of the meaning of the code in the system, following the rules of the systemIndicates that this coding was chosen by a user directly - e.g. off a pick list of available items (codes or displays)Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeA reference to a code defined by a terminology systemA human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the userExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeA reference to a code defined by a terminology systemA human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the userExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe value of the measured amount. The value includes an implicit precision in the presentation of the valueHow the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value (this element modifies the meaning of other elements)How the Quantity should be understood and represented. (Strength=Required)A human-readable form of the unitThe identification of the system that provides the coded form of the unitA computer processable form of the unit in some unit representation systemExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe value of the measured amount. The value includes an implicit precision in the presentation of the valueHow the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value (this element modifies the meaning of other elements)How the Quantity should be understood and represented. (Strength=Required)A human-readable form of the unitThe identification of the system that provides the coded form of the unitA computer processable form of the unit in some unit representation systemExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeNumerical value (with implicit precision)ISO 4217 Currency CodeA code indicating the currency, taken from ISO 4217. (Strength=Required)Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeNumerical value (with implicit precision)ISO 4217 Currency CodeA code indicating the currency, taken from ISO 4217. (Strength=Required)Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe low limit. The boundary is inclusiveThe high limit. The boundary is inclusiveExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe low limit. The boundary is inclusiveThe high limit. The boundary is inclusiveExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe value of the numeratorThe value of the denominatorExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe value of the numeratorThe value of the denominatorExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe start of the period. The boundary is inclusiveThe end of the period. If the end of the period is missing, it means no end was known or planned at the time the instance was created. The start may be in the past, and the end date in the future, which means that period is expected/planned to end at that timeExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe start of the period. The boundary is inclusiveThe end of the period. If the end of the period is missing, it means no end was known or planned at the time the instance was created. The start may be in the past, and the end date in the future, which means that period is expected/planned to end at that timeExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe base quantity that a measured value of zero represents. In addition, this provides the units of the entire measurement seriesThe length of time between sampling times, measured in millisecondsA correction factor that is applied to the sampled data points before they are added to the originThe lower limit of detection of the measured points. This is needed if any of the data points have the value "L" (lower than detection limit)The upper limit of detection of the measured points. This is needed if any of the data points have the value "U" (higher than detection limit)The number of sample points at each time point. If this value is greater than one, then the dimensions will be interlaced - all the sample points for a point in time will be recorded at onceA series of data points which are decimal values separated by a single space (character u20). The special values "E" (error), "L" (below detection limit) and "U" (above detection limit) can also be used in place of a decimal valueExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe base quantity that a measured value of zero represents. In addition, this provides the units of the entire measurement seriesThe length of time between sampling times, measured in millisecondsA correction factor that is applied to the sampled data points before they are added to the originThe lower limit of detection of the measured points. This is needed if any of the data points have the value "L" (lower than detection limit)The upper limit of detection of the measured points. This is needed if any of the data points have the value "U" (higher than detection limit)The number of sample points at each time point. If this value is greater than one, then the dimensions will be interlaced - all the sample points for a point in time will be recorded at onceA series of data points which are decimal values separated by a single space (character u20). The special values "E" (error), "L" (below detection limit) and "U" (above detection limit) can also be used in place of a decimal valueExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe purpose of this identifier (this element modifies the meaning of other elements)Identifies the purpose for this identifier, if known . (Strength=Required)A coded type for the identifier that can be used to determine which identifier to use for a specific purposeA coded type for an identifier that can be used to determine which identifier to use for a specific purpose. (Strength=Extensible)Establishes the namespace for the value - that is, a URL that describes a set values that are uniqueThe portion of the identifier typically relevant to the user and which is unique within the context of the systemTime period during which identifier is/was valid for useOrganization that issued/manages the identifierExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe purpose of this identifier (this element modifies the meaning of other elements)Identifies the purpose for this identifier, if known . (Strength=Required)A coded type for the identifier that can be used to determine which identifier to use for a specific purposeA coded type for an identifier that can be used to determine which identifier to use for a specific purpose. (Strength=Extensible)Establishes the namespace for the value - that is, a URL that describes a set values that are uniqueThe portion of the identifier typically relevant to the user and which is unique within the context of the systemTime period during which identifier is/was valid for useOrganization that issued/manages the identifierExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeIdentifies the purpose for this name (this element modifies the meaning of other elements)The use of a human name. (Strength=Required)Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific partsThe part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his fatherGiven namePart of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the namePart of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the nameIndicates the period of time when this name was valid for the named personExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeIdentifies the purpose for this name (this element modifies the meaning of other elements)The use of a human name. (Strength=Required)Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific partsThe part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his fatherGiven namePart of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the namePart of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the nameIndicates the period of time when this name was valid for the named personExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe purpose of this address (this element modifies the meaning of other elements)The use of an address. (Strength=Required)Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are bothThe type of an address (physical / postal). (Strength=Required)Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific partsThis component contains the house number, apartment number, street name, street direction,  P.O. Box number, delivery hints, and similar address informationThe name of the city, town, suburb, village or other community or delivery centerThe name of the administrative area (county)Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes)A postal code designating a region defined by the postal serviceCountry - a nation as commonly understood or generally acceptedTime period when address was/is in useExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe purpose of this address (this element modifies the meaning of other elements)The use of an address. (Strength=Required)Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are bothThe type of an address (physical / postal). (Strength=Required)Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific partsThis component contains the house number, apartment number, street name, street direction,  P.O. Box number, delivery hints, and similar address informationThe name of the city, town, suburb, village or other community or delivery centerThe name of the administrative area (county)Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes)A postal code designating a region defined by the postal serviceCountry - a nation as commonly understood or generally acceptedTime period when address was/is in useExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeTelecommunications form for contact point - what communications system is required to make use of the contactTelecommunications form for contact point. (Strength=Required)The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address)Identifies the purpose for the contact point (this element modifies the meaning of other elements)Use of contact point. (Strength=Required)Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank valuesTime period when the contact point was/is in useExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeTelecommunications form for contact point - what communications system is required to make use of the contactTelecommunications form for contact point. (Strength=Required)The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address)Identifies the purpose for the contact point (this element modifies the meaning of other elements)Use of contact point. (Strength=Required)Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank valuesTime period when the contact point was/is in useExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeModifier Extensions - as described for some elements: additional information that is not part of the basic definition of the resource / type that modifies the interpretation of the containing elementIdentifies specific times when the event occursA code for the timing schedule (or just text in code.text). Some codes such as BID are ubiquitous, but many institutions define their own additional codes. If a code is provided, the code is understood to be a complete statement of whatever is specified in the structured timing data, and either the code or the data may be used to interpret the Timing, with the exception that .repeat.bounds still applies over the code (and is not contained in the code)Code for a known / defined timing pattern. (Strength=Preferred)Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing scheduleA total count of the desired number of repetitions across the duration of the entire timing specification. If countMax is present, this element indicates the lower bound of the allowed range of count valuesIf present, indicates that the count is a range - so to perform the action between [count] and [countMax] timesHow long this thing happens for when it happens. If durationMax is present, this element indicates the lower bound of the allowed range of the durationIf present, indicates that the duration is a range - so to perform the action between [duration] and [durationMax] time lengthThe units of time for the duration, in UCUM unitsA unit of time (units from UCUM). (Strength=Required)The number of times to repeat the action within the specified period. If frequencyMax is present, this element indicates the lower bound of the allowed range of the frequencyIf present, indicates that the frequency is a range - so to repeat between [frequency] and [frequencyMax] times within the period or period rangeIndicates the duration of time over which repetitions are to occur; e.g. to express "3 times per day", 3 would be the frequency and "1 day" would be the period. If periodMax is present, this element indicates the lower bound of the allowed range of the period lengthIf present, indicates that the period is a range from [period] to [periodMax], allowing expressing concepts such as "do this once every 3-5 daysThe units of time for the period in UCUM unitsA unit of time (units from UCUM). (Strength=Required)If one or more days of week is provided, then the action happens only on the specified day(s) (Strength=Required)Specified time of day for action to take placeAn approximate time period during the day, potentially linked to an event of daily living that indicates when the action should occurReal world event relating to the schedule. (Strength=Required)The number of minutes from the event. If the event code does not indicate whether the minutes is before or after the event, then the offset is assumed to be after the eventMay be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself) (this element modifies the meaning of other elements)A set of rules that describe when the event is scheduledExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeModifier Extensions - as described for some elements: additional information that is not part of the basic definition of the resource / type that modifies the interpretation of the containing elementIdentifies specific times when the event occursA code for the timing schedule (or just text in code.text). Some codes such as BID are ubiquitous, but many institutions define their own additional codes. If a code is provided, the code is understood to be a complete statement of whatever is specified in the structured timing data, and either the code or the data may be used to interpret the Timing, with the exception that .repeat.bounds still applies over the code (and is not contained in the code)Code for a known / defined timing pattern. (Strength=Preferred)Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing scheduleA total count of the desired number of repetitions across the duration of the entire timing specification. If countMax is present, this element indicates the lower bound of the allowed range of count valuesIf present, indicates that the count is a range - so to perform the action between [count] and [countMax] timesHow long this thing happens for when it happens. If durationMax is present, this element indicates the lower bound of the allowed range of the durationIf present, indicates that the duration is a range - so to perform the action between [duration] and [durationMax] time lengthThe units of time for the duration, in UCUM unitsA unit of time (units from UCUM). (Strength=Required)The number of times to repeat the action within the specified period. If frequencyMax is present, this element indicates the lower bound of the allowed range of the frequencyIf present, indicates that the frequency is a range - so to repeat between [frequency] and [frequencyMax] times within the period or period rangeIndicates the duration of time over which repetitions are to occur; e.g. to express "3 times per day", 3 would be the frequency and "1 day" would be the period. If periodMax is present, this element indicates the lower bound of the allowed range of the period lengthIf present, indicates that the period is a range from [period] to [periodMax], allowing expressing concepts such as "do this once every 3-5 daysThe units of time for the period in UCUM unitsA unit of time (units from UCUM). (Strength=Required)If one or more days of week is provided, then the action happens only on the specified day(s) (Strength=Required)Specified time of day for action to take placeAn approximate time period during the day, potentially linked to an event of daily living that indicates when the action should occurReal world event relating to the schedule. (Strength=Required)The number of minutes from the event. If the event code does not indicate whether the minutes is before or after the event, then the offset is assumed to be after the eventMay be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself) (this element modifies the meaning of other elements)A set of rules that describe when the event is scheduledExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeAn indication of the reason that the entity signed this document. This may be explicitly included as part of the signature information and can be used when determining accountability for various actions concerning the documentAn indication of the reason that an entity signed the object. (Strength=Preferred)When the digital signature was signedA reference to an application-usable description of the identity that signed  (e.g. the signature used their private key)A reference to an application-usable description of the identity that is represented by the signatureA mime type that indicates the technical format of the target resources signed by the signatureThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)A mime type that indicates the technical format of the signature. Important mime types are application/signature+xml for X ML DigSig, application/jose for JWS, and image/* for a graphical image of a signature, etcThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)The base64 encoding of the Signature content. When signature is not recorded electronically this element would be emptyExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeAn indication of the reason that the entity signed this document. This may be explicitly included as part of the signature information and can be used when determining accountability for various actions concerning the documentAn indication of the reason that an entity signed the object. (Strength=Preferred)When the digital signature was signedA reference to an application-usable description of the identity that signed  (e.g. the signature used their private key)A reference to an application-usable description of the identity that is represented by the signatureA mime type that indicates the technical format of the target resources signed by the signatureThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)A mime type that indicates the technical format of the signature. Important mime types are application/signature+xml for X ML DigSig, application/jose for JWS, and image/* for a graphical image of a signature, etcThe mime type of an attachment. Any valid mime type is allowed. (Strength=Required)The base64 encoding of the Signature content. When signature is not recorded electronically this element would be emptyExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe individual responsible for making the annotationIndicates when this particular annotation was madeThe text of the annotation in markdown formatExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeThe individual responsible for making the annotationIndicates when this particular annotation was madeThe text of the annotation in markdown formatExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeSource of the definition for the extension code - a logical name or a URLValue of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list)The status of the narrative - whether it's entirely generated (from just the defined data or the extensions too), or whether a human authored it and it may contain additional dataThe status of a resource narrative. (Strength=Required)The actual narrative content, a stripped down version of XHTMLA reference to a location at which the other resource is found. The reference may be a relative reference, in which case it is relative to the service base URL, or an absolute URL that resolves to the location where the resource is found. The reference may be version specific or not. If the reference is not to a FHIR RESTful server, then it should be assumed to be version specific. Internal fragment references (start with '#') refer to contained resourcesThe expected type of the target of the reference. If both Reference.type and Reference.reference are populated and Reference.reference is a FHIR URL, both SHALL be consistent.

The type is the Canonical URL of Resource Definition that is the type this reference refers to. References are URLs that are relative to http://hl7.org/fhir/StructureDefinition/ e.g. "Patient" is a reference to http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are only allowed for logical models (and can only be used in references in logical models, not resources)Aa resource (or, for logical models, the URI of the logical model). (Strength=Extensible)An identifier for the target resource. This is used when there is no way to reference the other resource directly, either because the entity it represents is not available through a FHIR server, or because there is no way for the author of the resource to convert a known identifier to an actual location. There is no requirement that a Reference.identifier point to something that is actually exposed as a FHIR instance, but it SHALL point to a business concept that would be expected to be exposed as a FHIR instance, and that instance would need to be of a FHIR resource type allowed by the referencePlain text narrative that identifies the resource in addition to the resource reference

> Source: https://hl7.org/fhir/R4/datatypes.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/datatypes.html) [R4B](http://hl7.org/fhir/R4B/datatypes.html) **R4** [R3](http://hl7.org/fhir/STU3/datatypes.html) [R2](http://hl7.org/fhir/DSTU2/datatypes.html)
 

 

# 2.24.0 Data Types [
](datatypes.html#2.24.0)

| [FHIR Infrastructure ](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Maturity Level](versions.html#maturity): Normative | [Standards Status](versions.html#std-process): [Partially Normative](versions.html#std-process) | |

 | 
 
 
 | 
 
 This page has been approved as part of an [ANSI ](https://www.ansi.org/) standard.
 See the [Infrastructure](ansi-infrastructure.html) Package for further details.
 | 
 |

The FHIR specification defines a set of data types that are used for the 
resource elements. There are four categories of data types:

 - Simple / primitive types, which are single elements with a primitive value ([below](#primitive))

 - General-purpose complex types, which are re-usable clusters of elements ([below](#complex))

 - Metadata types: A set of types for use with metadata resources 

 - Special purpose data types - defined elsewhere in the specification for specific usages

This page describes the general-purpose data types (categories 1 and 2). 

 

**Data Types Summary**. 

Legend: see [Standards Status Colors](versions.html#std-process)

 
**Primitive Types**** 
 
 
 
 
 
 
 [Element](element.html#Element)- [instant](#instant)[time](#time)[date](#date)[dateTime](#dateTime)[decimal](#decimal)[boolean](#boolean)[integer](#integer)[string](#string)[uri](#uri)[base64Binary](#base64Binary)[code](#code)[id](#id)[oid](#oid)[unsignedInt](#unsignedInt)[positiveInt](#positiveInt)[markdown](#markdown)[url](#url)[canonical](#canonical)[uuid](#uuid)

 
General-Purpose Data types**** 
 
 
 
 
 
 
 [Element](element.html#Element)[Identifier](#Identifier)[HumanName](#HumanName)[Address](#Address)[ContactPoint](#ContactPoint)[Timing](#Timing)[Quantity](#Quantity)[SimpleQuantity](#SimpleQuantity)[Attachment](#Attachment)[Range](#Range)[Period](#Period)[Ratio](#Ratio)[CodeableConcept](#CodeableConcept)[Coding](#Coding)[SampledData](#SampledData)[Age](#Age)[Distance](#Distance)[Duration](#Duration)[Count](#Count)[Money](#Money)[MoneyQuantity](#MoneyQuantity)[Annotation](#Annotation)[Signature](#Signature)[BackboneElement](backboneelement.html#BackboneElement)

 
Metadata Types**** 
 
 
 
 
 
 
 [Element](element.html#Element)[ContactDetail](metadatatypes.html#ContactDetail)[Contributor](metadatatypes.html#Contributor)[DataRequirement](metadatatypes.html#DataRequirement)[ParameterDefinition](metadatatypes.html#ParameterDefinition)[RelatedArtifact](metadatatypes.html#RelatedArtifact)[TriggerDefinition](metadatatypes.html#TriggerDefinition)[UsageContext](metadatatypes.html#UsageContext)[Expression](metadatatypes.html#Expression)

 
Special Purpose Data types**** 
 
 
 
 
 
 
 [Element](element.html#Element)[Reference](references.html#Reference)[Narrative](narrative.html#Narrative)[Extension](extensibility.html#Extension)[Meta](resource.html#Meta)[ElementDefinition](elementdefinition.html#ElementDefinition)[Dosage](dosage.html#Dosage)[BackboneElement](backboneelement.html#BackboneElement)[xhtml](narrative.html#xhtml)

A [limited set](extensibility.html#list) of these data types may 
appear in extensions. All data types (including primitives) may have
extensions, but only the following data types may include [Modifier Extensions](extensibility.html#modifier):

 [Timing](datatypes.html#timing)

 - [Dosage](dosage.html#Dosage)

 - [ElementDefinition](elementdefinition.html#ElementDefinition)

## 2.24.0.1 Primitive Types [
](datatypes.html#primitive)

 
 
 
 
 
 
 
 [Element](element.html#Element)- [Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeextension](extensibility.html) : [Extension](extensibility.html) 0..*[instant](#instant)Actual value attribute of the data typevalue : [xs:dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) 0..1[time](#time)Actual value attribute of the data typevalue : [xs:time](http://www.w3.org/TR/xmlschema-2/#time) 0..1[date](#date)Actual value attribute of the data typevalue : [xs:gYear](http://www.w3.org/TR/xmlschema-2/#gYear)|[xs:gYearMonth](http://www.w3.org/TR/xmlschema-2/#gYearMonth)|[xs:date](http://www.w3.org/TR/xmlschema-2/#date) 0..1[dateTime](#dateTime)Actual value attribute of the data typevalue : [xs:gYear](http://www.w3.org/TR/xmlschema-2/#gYear)|[xs:gYearMonth](http://www.w3.org/TR/xmlschema-2/#gYearMonth)|[xs:date](http://www.w3.org/TR/xmlschema-2/#date)|[xs:dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) 0..1[decimal](#decimal)Actual value attribute of the data typevalue : [xs:decimal](http://www.w3.org/TR/xmlschema-2/#decimal)|[xs:double](http://www.w3.org/TR/xmlschema-2/#double) 0..1[boolean](#boolean)Actual value attribute of the data typevalue : [xs:boolean](http://www.w3.org/TR/xmlschema-2/#boolean) 0..1[integer](#integer)Actual value attribute of the data typevalue : [xs:int](http://www.w3.org/TR/xmlschema-2/#int) 0..1[string](#string)Actual value attribute of the data typevalue : [xs:string](http://www.w3.org/TR/xmlschema-2/#string) 0..1[uri](#uri)Actual value attribute of the data typevalue : [xs:anyURI](http://www.w3.org/TR/xmlschema-2/#anyURI) 0..1[base64Binary](#base64Binary)Actual value attribute of the data typevalue : [xs:base64Binary](http://www.w3.org/TR/xmlschema-2/#base64Binary) 0..1[code](#code)[id](#id)[oid](#oid)[unsignedInt](#unsignedInt)[positiveInt](#positiveInt)[markdown](#markdown)[url](#url)[canonical](#canonical)[uuid](#uuid)

The following table describes the primitive types that are used in this specification. Primitive types are those with only a value, and no additional elements as children (though, like
all types, they have [extensions](extensibility.html)). See also the [Examples](datatypes-examples.html#primitives).

 | 
 Primitive Types** | 
 |

 | 
 FHIR Name | 
 Value Domain | 
 XML Representation | 
 JSON representation | 
 |

 | 
 boolean | 
 true | false | 
 xs:boolean, except that **0 and 1 are not valid values** | 
 JSON boolean (true or false) | 
 |

 | 
 | 
 Regex: `true|false` | 
 |

 
 | 
 integer | 
 A signed integer in the range −2,147,483,648..2,147,483,647 (32-bit; for larger values, use decimal) | 
 xs:int, except that **leading 0 digits are not allowed** | 
 JSON number (with no decimal point) | 
 |

 | 
 | 
 Regex: `[0]|[-+]?[1-9][0-9]*` | 
 |

 | 
 string | 
 A sequence of Unicode characters | 
 xs:string | 
 JSON String | 
 |

 | 
 | 
 Note that strings SHALL NOT exceed 1MB (1024*1024 characters) in size. Strings SHOULD not contain Unicode character points below 32, except for u0009 (horizontal tab), u0010 (carriage return) and u0013 (line feed).
 Leading and Trailing whitespace is allowed, but SHOULD be [removed when using the XML format](xml.html#whitespace).
 Note: This means that a string that consists only of whitespace could be trimmed to nothing, which would be treated as an invalid element value. Therefore strings SHOULD always contain non-whitespace content | 
 |

 | 
 | 
 This data type can be [bound](terminologies.html#string) to a [ValueSet](valueset.html) | 
 |

 | 
 | 
 Regex: `[ \r\n\t\S]+` (see notes below) | 
 |

 | 
 decimal | 
 Rational numbers that have a decimal representation. See below about the precision of the number | 
 union of xs:decimal and xs:double (see below for limitations) | 
 A JSON number (see below for limitations) | 
 |

 | 
 | 
 Regex: `-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?` | 
 |

 | 
 uri | 
 A Uniform Resource Identifier Reference ([RFC 3986 ](http://tools.ietf.org/html/rfc3986)). Note: URIs are case sensitive. For UUID (urn:uuid:53fefa32-fcbb-4ff8-8a92-55ee120877b7) use all lowercase | 
 xs:anyURI | 
 A JSON string - a URI | 
 |

 | 
 | 
 Regex: `\S*` (This regex is very permissive, but URIs must be valid. Implementers are welcome to use more specific regex statements for a URI in specific contexts) | 
 |

 | 
 | 
 URIs can be absolute or relative, and may have an optional fragment identifier**
 This data type can be [bound](terminologies.html#string) to a [ValueSet](valueset.html) | 
 |

 | 
 url | 
 A Uniform Resource Locator ([RFC 1738 ](http://tools.ietf.org/html/rfc1738)). Note URLs are accessed directly using the specified protocol. Common URL protocols are `http{s}:`, `ftp:`, `mailto:` and `mllp:`, though many others are defined | 
 xs:anyURI | 
 A JSON string - a URL | 
 |

 | 
 canonical | 
 A URI that refers to a [resource by its canonical URL](references.html#canonical) ([resources with a `url` property](references.html#canonical-list)). The `canonical` type differs from a `uri` in that it has special meaning in this specification, 
 and in that it may have a version appended, separated by a vertical bar (|). Note that the type `canonical` is not used for the actual canonical URLs that are the target
 of these references, but for the URIs that refer to them, and may have the version suffix in them. Like other URIs, elements of type `canonical` may also have #fragment references | 
 xs:anyURI | 
 A JSON string - a canonical URL | 
 |

 | 
 base64Binary | 
 A stream of bytes, base64 encoded ([RFC 4648 ](http://tools.ietf.org/html/rfc4648)) | 
 xs:base64Binary | 
 A JSON string - base64 content | 
 |

 | 
 | 
 Regex: `(\s*([0-9a-zA-Z\+\=]){4}\s*)+` | 
 |

 | 
 | 
 There is no specified upper limit to the size of a binary, but systems will have to impose some implementation based limit to the size they support. This should be clearly documented, though there is no computable for this at this time | 
 |

 | 
 instant | 
 An instant in time in the format YYYY-MM-DDThh:mm:ss.sss+zz:zz (e.g. 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z). The time SHALL specified at least to the second and SHALL include a time zone. 
 Note: This is intended for when precisely observed times are required (typically system logs etc.), and not human-reported times - for those, use date or dateTime (which can be as precise as `instant`, but is not required to be). `instant` is a more constrained dateTime | 
 xs:dateTime | 
 A JSON string - an xs:dateTime | 
 |

 | 
 | 
 Note: This type is for system times, not human times (see date and dateTime below). | 
 |

 | 
 | 
 Regex: `([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))` | 
 |

 | 
 date | 
 A date, or partial date (e.g. just year or year + month) as used in human communication. The format is YYYY, YYYY-MM, or YYYY-MM-DD, e.g. 2018, 1973-06, or 1905-08-23. There SHALL be no time zone**. Dates SHALL be valid dates | 
 union of xs:date, xs:gYearMonth, xs:gYear | 
 A JSON string - a union of xs:date, xs:gYearMonth, xs:gYear | 
 |

 | 
 | 
 Regex: `([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?` | 
 |

 | 
 dateTime | 
 A date, date-time or partial date (e.g. just year or year + month) as used in human communication. The format is YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDThh:mm:ss+zz:zz, e.g. 2018, 1973-06, 1905-08-23, 2015-02-07T13:28:17-05:00 or 2017-01-01T00:00:00.000Z.
 If hours and minutes are specified, a time zone SHALL be populated. Seconds must be provided due to schema type constraints but may be zero-filled and may be ignored at receiver discretion. Dates SHALL be valid dates. **The time "24:00" is not allowed**. Leap Seconds are allowed - see below | 
 union of xs:dateTime, xs:date, xs:gYearMonth, xs:gYear | 
 A JSON string - a union of xs:dateTime, xs:date, xs:gYearMonth, xs:gYear | 
 |

 | 
 | 
 Regex: `([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?` | 
 |

 | 
 time | 
 A time during the day, in the format hh:mm:ss. There is no date specified. Seconds must be provided due to schema type constraints but may be zero-filled and may be ignored at receiver discretion. 
 **The time "24:00" SHALL NOT be used. A time zone SHALL NOT be present**. Times can be converted to a [Duration](#Duration) since midnight. | 
 xs:time | 
 A JSON string - an xs:time | 
 |

 | 
 | 
 Regex: `([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?` | 
 |

 | 
 code | 
 Indicates that the value is taken from a set of controlled strings defined elsewhere (see [Using codes](terminologies.html) 
 for further discussion). Technically, a code is restricted to a string which has at least one character and no leading or trailing 
 whitespace, and where there is no whitespace other than single spaces in the contents | 
 xs:token | 
 JSON string | 
 |

 | 
 | 
 Regex: `[^\s]+(\s[^\s]+)*`**
 This data type can be [bound](terminologies.html#string) to a [ValueSet](valueset.html) | 
 |

 | 
 oid | 
 An OID represented as a URI ([RFC 3001 ](http://www.ietf.org/rfc/rfc3001.txt)); e.g. urn:oid:1.2.3.4.5 | 
 xs:anyURI | 
 JSON string - uri | 
 |

 | 
 | 
 Regex: `urn:oid:[0-2](\.(0|[1-9][0-9]*))+` | 
 |

 | 
 id | 
 Any combination of upper- or lower-case ASCII letters ('A'..'Z', and 'a'..'z', numerals ('0'..'9'), '-' and '.', with a length limit of 64 characters. (This might be an integer, an un-prefixed OID, UUID or any other identifier pattern that meets these constraints.) | 
 xs:string | 
 JSON string | 
 |

 | 
 | 
 Regex: `[A-Za-z0-9\-\.]{1,64}` | 
 |

 | 
 markdown | 
 A FHIR `string` (see above) that may contain markdown syntax for optional processing by a markdown presentation engine, in the GFM extension of CommonMark format (see below) | 
 xs:string | 
 JSON string | 
 |

 | 
 | 
 Regex: `\s*(\S|\s)*` (can't put size limit in the regex - too large) | 
 |

 | 
 unsignedInt | 
 Any non-negative integer in the range 0..2,147,483,647 | 
 xs:nonNegativeInteger | 
 JSON number | 
 |

 | 
 | 
 Regex: `[0]|([1-9][0-9]*)` | 
 |

 | 
 positiveInt | 
 Any positive integer in the range 1..2,147,483,647 | 
 xs:positiveInteger | 
 JSON number | 
 |

 | 
 | 
 Regex: `+?[1-9][0-9]*` | 
 |

 | 
 uuid | 
 A UUID (aka GUID) represented as a URI ([RFC 4122 ](http://www.ietf.org/rfc/rfc4122.txt)); e.g. urn:uuid:c757873d-ec9a-4326-a141-556f43239520 | 
 xs:anyURI | 
 JSON string - uri | 
 |

Notes:

 For all the types, the XML, JSON and Turtle representations of the primitive values are the same except for different escaping in XML and JSON

 - For decimal values, the XML special values `INF`, `-INF` and `NaN` are not allowed, and JSON is restricted to the [precision limits documented in XML schema for xs:double and xs:decimal ](https://www.w3.org/TR/xmlschema-2/)

 - The precision of the decimal value has significance:
 

 e.g. 0.010 is regarded as different to 0.01, and the original precision should be preserved

 - Implementations SHALL handle decimal values in ways that preserve and respect the precision of the value as represented for presentation purposes

 - Implementations are not required to perform calculations with these numbers differently, though they may choose to do so (i.e. preserve significance)

 - See implementation comments for [XML](xml.html#schema-gen), [JSON](json.html#decimal) and [RDF](rdf.html#decimal)

 - In object code, implementations that might meet this constraint are GMP implementations or equivalents to Java BigDecimal that implement arbitrary precision, or a combination of a (64 bit) floating point value with a precision field

 - Note that large and/or highly precise values are extremely rare in medicine. One element where highly precise decimals may be encountered is the [Location](location.html) coordinates. Irrespective of this, the limits documented in XML Schema apply

 

 
 - Boolean values can also be represented using coded values (such as [HL7 v2 Table 0136](v2/0136/index.html)). See [Observation](observation.html#valuex) for one such use

 - Issues with the specified regexes: 
 

 The regexes are provided to assist with tooling, but are informative, not normative**. There are several issues with the regexes

 - The string regex has problems with unicode - specifically, it might or might not allow unicode whitespace to some degree depending on unicode support in the regex engine being used. 
 The regexes `[\r\n\t\x{0020}-\x{FFFF}]*` or `[\r\n\t\u0020-\uFFFF]*` are better expressions of the constraints on string, but poorly supported (see [Regex Tutorial ](https://www.regular-expressions.info/unicode.html) for details).
 The `string` regex also applies to `markdown` as well. The regex does not enforce the length limit

 - The unicode issues also apply to the regex for `code`

 - The regexes should be qualified with start of string and end of string anchors based on the regex implementation used (e.g. caret '^' and dollar-sign '$' for JavaScript, POSIX, XML and XPath; '\A' and '\Z' for .NET, Java, Python and others; please verify these definitions with the regex implementation used).
 
 - The regexes may allow a broader set of values than are actually valid (e.g. leap years) so additional validation is always needed

 

 
 - Leap second are allowed in the datetime, instant and time types. Note, though, that many systems and libraries do not support leap seconds. Applications reading times SHOULD accept and handle leap seconds gracefully, and applications producing them MAY choose to avoid encoding leap seconds

 - About the id datatype:
 

 Ids are case sensitive. UUIDs SHALL be sent using lowercase letters

 - The ID type includes identifiers consistent with [ISO 18232 ](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=38610), but also includes other identifier formats as well, and is not case insensitive like ISO 18232.

 - In a typical FHIR URL, like `http://example.com/fhir/Patient/1234`, the last part "1234" (highlighted in red) is the part that is an id datatype

 - A full UUID is a `uri`, not an `id`. UUIDs in URIs SHALL also be represented in lowercase (urn:uuid:59bf0ef4-e89c-4628-9b51-12ae3fdbe22b)

 

 
 - About the `uri`, `url` and `canonical` datatypes:
 

 They all contain URIs, but differ in how applications resolve the reference

 - Although the `url` and `canonical` are specializations of `uri`, they are never substituted for each other

 - They are all case sensitive for comparison purposes. Applications SHOULD not create URIs that only differ by case

 - A general URI may be either a URL or a canonical URL or some other kind of URI

 

 
 - About the markdown datatype:
 

 This specification requires and uses the [GFM (Github Flavored Markdown) ](https://github.github.com/gfm/) extensions on [CommonMark ](http://spec.commonmark.org/0.28/) format

 - Note that GFM prohibits Raw HTML

 - Systems are not required to have markdown support, so the content of a string should be readable without markdown processing, per markdown philosophy

 - Markdown content SHALL NOT contain Unicode character points below 32, except for u0009 (horizontal tab), u0010 (carriage return) and u0013 (line feed)

 - Markdown is a `string`, and subject to the same rules (e.g. length limit)

 - Converting an element that has the type `string` to `markdown` in a later version of this FHIR specification 
 is not considered a breaking change (neither is adding `markdown` as a choice to an optional element that already has a choice of data types)

 

 

### 2.24.0.1.1 Representations in XML, JSON, and Turtle [
](datatypes.html#representations)

All elements using these primitive types may have one or more of a value as described above, an internal identity (e.g. xml:id), and extensions.
For an example, take an element of name "count" and type "integer".

**XML**

The value is represented in XML as an attribute named "value":

```
data
```

 

 

 

 

 

 
**JSON Template**

 

 
```
system
```

 

 

 

 

 

 
**JSON Template**

 

 
```
CodeableConcept
```

 
 
 Note that these concepts may be cross mapped using the [ConceptMap](conceptmap.html) resource *instead of * or *in addition to* being represented as translations directly in the in `CodeableConcept`.

 
 
**Using Text in CodeableConcept**

The `text`
is the representation of the concept as entered or chosen by the user, and which most closely
represents the intended meaning of the user or concept. Very often the `text`
is the same as a `display` of one of the codings. One or more of the codings
may be flagged as the user selected code - the code or concept that the user actually selected directly.
Note that in all but a few cases, only one of the codings may be flagged as the `coding.userSelected = true` 
- the code or concept that the user actually selected directly. If more than one code is marked as user selected, 
this means the user explicitly chose multiple codes. When none of the `coding` elements is 
marked as user selected, the text (if present) is the preferred source of meaning.

 
A free text only representation of the concept without any `coding` elements is permitted if there is no appropriate code and only free text is available (and not prohibited by the implementation). For example, using text only, the `Observation.valueCodeableConcept` element would be:

 
```
value
```

 

 

 

 

 

 
**JSON Template**

 

 
```
value
```

 

 

 

 

 

 
**JSON Template**

 

 
```
unit
```

 

 

 

 

 

 
**JSON Template**

 

 
```
start
```

 

 - [Structure](#tabs-SampledData-struc)

 - [UML](#tabs-SampledData-uml)

 - [XML](#tabs-SampledData-xml)

 - [JSON](#tabs-SampledData-json)

 - [Turtle](#tabs-SampledData-ttl)

 - [R3 Diff](#tabs-SampledData-diff)

 - [All](#tabs-SampledData-all)

 

 

 

 
**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [SampledData](datatypes-definitions.html#SampledData) | [TU](versions.html#std-process) | | [Element](element.html) | A series of measurements taken by a device**Elements defined in Ancestors: [id](element.html#Element), [extension](element.html#Element) | |

| [origin](datatypes-definitions.html#SampledData.origin) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Zero value and units | |

| [period](datatypes-definitions.html#SampledData.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [decimal](datatypes.html#decimal) | Number of milliseconds between samples | |

| [factor](datatypes-definitions.html#SampledData.factor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [decimal](datatypes.html#decimal) | Multiply data by this before adding to origin | |

| [lowerLimit](datatypes-definitions.html#SampledData.lowerLimit) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [decimal](datatypes.html#decimal) | Lower limit of detection | |

| [upperLimit](datatypes-definitions.html#SampledData.upperLimit) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [decimal](datatypes.html#decimal) | Upper limit of detection | |

| [dimensions](datatypes-definitions.html#SampledData.dimensions) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [positiveInt](datatypes.html#positiveInt) | Number of sample points at each time point | |

| [data](datatypes-definitions.html#SampledData.data) | | 0..1 | [string](datatypes.html#string) | Decimal values with spaces, or "E" | "U" | "L" | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

 

 

 
UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 [Element](element.html#Element)- [Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeextension](extensibility.html) : [Extension](extensibility.html) 0..*[SampledData](#SampledData)[The base quantity that a measured value of zero represents. In addition, this provides the units of the entire measurement seriesorigin](datatypes-definitions.html#SampledData.origin) : [Quantity](#Quantity)([SimpleQuantity](#SimpleQuantity)) [1..1][The length of time between sampling times, measured in millisecondsperiod](datatypes-definitions.html#SampledData.period) : [decimal](#decimal) [1..1][A correction factor that is applied to the sampled data points before they are added to the originfactor](datatypes-definitions.html#SampledData.factor) : [decimal](#decimal) [0..1][The lower limit of detection of the measured points. This is needed if any of the data points have the value "L" (lower than detection limit)lowerLimit](datatypes-definitions.html#SampledData.lowerLimit) : [decimal](#decimal) [0..1][The upper limit of detection of the measured points. This is needed if any of the data points have the value "U" (higher than detection limit)upperLimit](datatypes-definitions.html#SampledData.upperLimit) : [decimal](#decimal) [0..1][The number of sample points at each time point. If this value is greater than one, then the dimensions will be interlaced - all the sample points for a point in time will be recorded at oncedimensions](datatypes-definitions.html#SampledData.dimensions) : [positiveInt](#positiveInt) [1..1][A series of data points which are decimal values separated by a single space (character u20). The special values "E" (error), "L" (below detection limit) and "U" (above detection limit) can also be used in place of a decimal valuedata](datatypes-definitions.html#SampledData.data) : [string](#string) [0..1]

 

 

 

 

 

 **XML Template**

 

 
```
value
```

 

 

 

 

 

 
**JSON Template**

 

 
```
HumanName
```

 

 

 

 

 

 
**JSON Template**

 

 
```
system
```

 

 

 

 

 

 
**JSON Template**

 

 
```
Timing.code.text
```

Note, though, that some systems include timing details in 
something like 'Dosage instructions' which is wider than just Timing; those systems do not use the 
Timing data type. Other systems use a set of 'common' codes - including, but usually not limited to, 
widely understood acronyms such as "BID". If a `Timing.code` is
provided, the code is understood to be a complete statement of whatever is specified in the structured timing
data (except for `Timing.repeat.bounds`, which applies to the code), and either the code or the
data may be used to interpret the `Timing`. A structured timing specification SHOULD be provided whenever
possible, unless the code is BID, TID, QID, AM or PM, which have a ubiquitous meaning.

This table shows the relationship between the [codes provided as
part of the base specification](valueset-timing-abbreviation.html), and the structured data portions of the Timing type:

 | **description** | **duration** | **durationUnit** | **frequency** | **frequencyMax** | **period** | **periodUnit** | **periodMax** | **when** | **bounds[x]** | |

 | QOD | | | 1 | | 2 | d | | | | |

 | QD | | | 1 | | 1 | d | | | | |

 | BID | | | 2 | | 1 | d | | | | |

 | TID | | | 3 | | 1 | d | | | | |

 | QID | | | 4 | | 1 | d | | | | |

 | Q4H | | | 1 | | 4 | h | | | | |

 | Q6H | | | 1 | | 6 | h | | | | |

 | AM | | | 1 | | 1 | d | | MORN | | |

 | PM | | | 1 | | 1 | d | | AFT or EVE | | |

These codes SHALL be understood as having the formal meanings documented in this table. Note that BID, etc. are defined as 'at institutionally specified times'.
For example, an institution may choose that BID is "always at 7am and 6pm". If it is inappropriate for this choice to be made, the code BID
should not be used. Instead, a distinct organization-specific code should be used in place of the HL7-defined BID code and/or a structured
representation should be used (in this case, `timeOfDay`).

**Constraints**

 
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **tim-1** | [Rule](conformance-rules.html#rule) | Timing.repeat | if there's a duration, there needs to be duration units | duration.empty() or durationUnit.exists() | |
| **tim-2** | [Rule](conformance-rules.html#rule) | Timing.repeat | if there's a period, there needs to be period units | period.empty() or periodUnit.exists() | |
| **tim-4** | [Rule](conformance-rules.html#rule) | Timing.repeat | duration SHALL be a non-negative value | duration.exists() implies duration >= 0 | |
| **tim-5** | [Rule](conformance-rules.html#rule) | Timing.repeat | period SHALL be a non-negative value | period.exists() implies period >= 0 | |
| **tim-6** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's a periodMax, there must be a period | periodMax.empty() or period.exists() | |
| **tim-7** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's a durationMax, there must be a duration | durationMax.empty() or duration.exists() | |
| **tim-8** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's a countMax, there must be a count | countMax.empty() or count.exists() | |
| **tim-9** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's an offset, there must be a when (and not C, CM, CD, CV) | offset.empty() or (when.exists() and ((when in ('C' | 'CM' | 'CD' | 'CV')).not())) | |
| **tim-10** | [Rule](conformance-rules.html#rule) | Timing.repeat | If there's a timeOfDay, there cannot be a when, or vice versa | timeOfDay.empty() or when.empty() | |

Note that these constraints still allow for nonsensical timing specifications such as "Once per day at 2:00 and 4:00" or "every 3 days on Friday".
Implementers must take care to ensure that their configuration and data collection designs do not lead to these non-interpretable timing specifications.
The elements `dayOfWeek`, `timeOfDay`, and `when` are particularly likely to be at issue here.

**Terminology Bindings**

 | Path | Definition | Type | Reference | |

 | Timing.repeat.durationUnit**Timing.repeat.periodUnit | A unit of time (units from UCUM). | [Required](terminologies.html#required) | [UnitsOfTime](valueset-units-of-time.html) | |

 | Timing.repeat.dayOfWeek | | [Required](terminologies.html#required) | [DaysOfWeek](valueset-days-of-week.html) | |

 | Timing.repeat.when | Real world event relating to the schedule. | [Required](terminologies.html#required) | [EventTiming](valueset-event-timing.html) | |

 | Timing.code | Code for a known / defined timing pattern. | [Preferred](terminologies.html#preferred) | [TimingAbbreviation](valueset-timing-abbreviation.html) | |

 

Timing is used in the following places: [Dosage](dosage.html#Dosage), [TriggerDefinition](metadatatypes.html#TriggerDefinition), [ActivityDefinition](activitydefinition.html#activitydefinition), [CarePlan](careplan.html#careplan), [ChargeItem](chargeitem.html#chargeitem), [Contract](contract.html#contract), [DeviceMetric](devicemetric.html#devicemetric), [DeviceRequest](devicerequest.html#devicerequest), [DeviceUseStatement](deviceusestatement.html#deviceusestatement), [EvidenceVariable](evidencevariable.html#evidencevariable), [NutritionOrder](nutritionorder.html#nutritionorder), [Observation](observation.html#observation), [PlanDefinition](plandefinition.html#plandefinition), [RequestGroup](requestgroup.html#requestgroup), [ResearchElementDefinition](researchelementdefinition.html#researchelementdefinition), [ServiceRequest](servicerequest.html#servicerequest), [SupplyDelivery](supplydelivery.html#supplydelivery), [SupplyRequest](supplyrequest.html#supplyrequest) and [VerificationResult](verificationresult.html#verificationresult)

## 2.24.0.17 
Signature
 [
](datatypes.html#signature)

Normative Candidate Note: This DataType is not normative - it is still undergoing Trial Use while more experience is gathered.

See also [Examples](datatypes-examples.html#Signature), [Detailed Descriptions](datatypes-definitions.html#Signature), [Mappings](datatypes-mappings.html#Signature), [Profiles & Extensions](datatypes-extras.html#Signature) and [R2 Conversions](datatypes-version-maps.html#Signature).

A Signature holds an electronic representation of a signature and its supporting context in a FHIR accessible form.
The signature may either be a cryptographic type (XML DigSig or a JWS), which is able to provide non-repudiation proof, or
it may be a graphical image that represents a signature or a signature process.

 

 [Structure](#tabs-Signature-struc)

 - [UML](#tabs-Signature-uml)

 - [XML](#tabs-Signature-xml)

 - [JSON](#tabs-Signature-json)

 - [Turtle](#tabs-Signature-ttl)

 - [R3 Diff](#tabs-Signature-diff)

 - [All](#tabs-Signature-all)

 

 

 

 
Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Signature](datatypes-definitions.html#Signature) | [TU](versions.html#std-process) | | [Element](element.html) | A Signature - XML DigSig, JWS, Graphical image of signature, etc.**Elements defined in Ancestors: [id](element.html#Element), [extension](element.html#Element) | |

| [type](datatypes-definitions.html#Signature.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..* | [Coding](datatypes.html#Coding) | Indication of the reason the entity signed the object(s)
[Signature Type Codes](valueset-signature-type.html) ([Preferred](terminologies.html#preferred))
 | |

| [when](datatypes-definitions.html#Signature.when) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [instant](datatypes.html#instant) | When the signature was created | |

| [who](datatypes-definitions.html#Signature.who) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [Device](device.html) | [Organization](organization.html)) | Who signed | |

| [onBehalfOf](datatypes-definitions.html#Signature.onBehalfOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [Device](device.html) | [Organization](organization.html)) | The party represented | |

| [targetFormat](datatypes-definitions.html#Signature.targetFormat) | | 0..1 | [code](datatypes.html#code) | The technical format of the signed resources
[MimeType](valueset-mimetypes.html) ([Required](terminologies.html#required)) | |

| [sigFormat](datatypes-definitions.html#Signature.sigFormat) | | 0..1 | [code](datatypes.html#code) | The technical format of the signature
[MimeType](valueset-mimetypes.html) ([Required](terminologies.html#required)) | |

| [data](datatypes-definitions.html#Signature.data) | | 0..1 | [base64Binary](datatypes.html#base64Binary) | The actual signature content (XML DigSig. JWS, picture, etc.) | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

 

 

 
UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 [Element](element.html#Element)- [Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeextension](extensibility.html) : [Extension](extensibility.html) 0..*[Signature](#Signature)[An indication of the reason that the entity signed this document. This may be explicitly included as part of the signature information and can be used when determining accountability for various actions concerning the documenttype](datatypes-definitions.html#Signature.type) : [Coding](#Coding) [1..*] « [An indication of the reason that an entity signed the object. (Strength=Preferred)SignatureTypeCodes](valueset-signature-type.html)? »[When the digital signature was signedwhen](datatypes-definitions.html#Signature.when) : [instant](#instant) [1..1][A reference to an application-usable description of the identity that signed (e.g. the signature used their private key)who](datatypes-definitions.html#Signature.who) : [Reference](references.html#Reference) [1..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)| [Patient](patient.html#Patient)|[Device](device.html#Device)|[Organization](organization.html#Organization) »[A reference to an application-usable description of the identity that is represented by the signatureonBehalfOf](datatypes-definitions.html#Signature.onBehalfOf) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[Organization](organization.html#Organization) »[A mime type that indicates the technical format of the target resources signed by the signaturetargetFormat](datatypes-definitions.html#Signature.targetFormat) : [code](#code) [0..1] « [The mime type of an attachment. Any valid mime type is allowed. (Strength=Required)Mime Types](valueset-mimetypes.html)! »[A mime type that indicates the technical format of the signature. Important mime types are application/signature+xml for X ML DigSig, application/jose for JWS, and image/* for a graphical image of a signature, etcsigFormat](datatypes-definitions.html#Signature.sigFormat) : [code](#code) [0..1] « [The mime type of an attachment. Any valid mime type is allowed. (Strength=Required)Mime Types](valueset-mimetypes.html)! »[The base64 encoding of the Signature content. When signature is not recorded electronically this element would be emptydata](datatypes-definitions.html#Signature.data) : [base64Binary](#base64Binary) [0..1]

 

 

 

 

 

 **XML Template**

 

 
```
Signature.type
```

 

 

 

 

 

 
**JSON Template**

 

 
```
{[](json.html)
 // from Element: [extension](extensibility.html)
 // author[x]: Individual responsible for the annotation. One of these 2:
 "[authorReference](datatypes-definitions.html#Annotation.authorReference)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) },
 "[authorString](datatypes-definitions.html#Annotation.authorString)" : "<[string](datatypes.html#string)>",
 "[time](datatypes-definitions.html#Annotation.time)" : "<[dateTime](datatypes.html#dateTime)>", // [When the annotation was made](terminologies.html#unbound)
 "[text](datatypes-definitions.html#Annotation.text)" : "<[markdown](datatypes.html#markdown)>" // **R!** [The annotation - text content (as markdown)](terminologies.html#unbound)
}

```

 

 

 

 

 

 
**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: [Element.extension](extensibility.html)
 # [Annotation.author[x]](datatypes-definitions.html#Annotation.author[x]) : 0..1 Individual responsible for the annotation. One of these 2
 fhir:[Annotation.authorReference](datatypes-definitions.html#Annotation.authorReference) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]
 fhir:[Annotation.authorString](datatypes-definitions.html#Annotation.authorString) [ [string](datatypes.html#string) ]
 fhir:[Annotation.time](datatypes-definitions.html#Annotation.time) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the annotation was made
 fhir:[Annotation.text](datatypes-definitions.html#Annotation.text) [ [markdown](datatypes.html#markdown) ]; # 1..1 The annotation - text content (as markdown)
]

```

 

 

 

 

 

 
**Changes since Release 3**

 

 

 | 
 
 [Annotation](datatypes.html#Annotation)
 | 
 | 
 |

 | 
 Annotation.text | 
 
 

 Type changed from string to markdown

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 

 

 

 

 
 
**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Annotation](datatypes-definitions.html#Annotation) | [N](versions.html#std-process) | | [Element](element.html) | Text node with attribution**Elements defined in Ancestors: [id](element.html#Element), [extension](element.html#Element) | |

| [author[x]](datatypes-definitions.html#Annotation.author_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Individual responsible for the annotation | |

| authorReference | | | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | | |

| authorString | | | [string](datatypes.html#string) | | |

| [time](datatypes-definitions.html#Annotation.time) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When the annotation was made | |

| [text](datatypes-definitions.html#Annotation.text) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [markdown](datatypes.html#markdown) | The annotation - text content (as markdown) | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

 
 
UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 [Element](element.html#Element)- [Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeextension](extensibility.html) : [Extension](extensibility.html) 0..*[Annotation](#Annotation)[The individual responsible for making the annotationauthor[x]](datatypes-definitions.html#Annotation.author_x_) : [Type](formats.html#umlchoice) [0..1] « [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[Patient](patient.html#Patient)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization))|[string](#string) »[Indicates when this particular annotation was madetime](datatypes-definitions.html#Annotation.time) : [dateTime](#dateTime) [0..1][The text of the annotation in markdown formattext](datatypes-definitions.html#Annotation.text) : [markdown](#markdown) [1..1]

 

 

 

 
 **XML Template**

 

 
```
<[**[name]**](datatypes-definitions.html#Annotation) xmlns="http://hl7.org/fhir">
 <!-- from Element: [extension](extensibility.html) -->
 <[**author[x]**](datatypes-definitions.html#Annotation.author[x])><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization))|
 [string](datatypes.html#string) [Individual responsible for the annotation](terminologies.html#unbound) --></author[x]>
 <[**time**](datatypes-definitions.html#Annotation.time) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When the annotation was made](terminologies.html#unbound) -->
 <[**text**](datatypes-definitions.html#Annotation.text) value="[[markdown](datatypes.html#markdown)]"/><!-- **1..1** [The annotation - text content (as markdown)](terminologies.html#unbound) -->
</[name]>

```

 

 

 

 
 
**JSON Template**

 

 
```
{[](json.html)
 // from Element: [extension](extensibility.html)
 // author[x]: Individual responsible for the annotation. One of these 2:
 "[authorReference](datatypes-definitions.html#Annotation.authorReference)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) },
 "[authorString](datatypes-definitions.html#Annotation.authorString)" : "<[string](datatypes.html#string)>",
 "[time](datatypes-definitions.html#Annotation.time)" : "<[dateTime](datatypes.html#dateTime)>", // [When the annotation was made](terminologies.html#unbound)
 "[text](datatypes-definitions.html#Annotation.text)" : "<[markdown](datatypes.html#markdown)>" // **R!** [The annotation - text content (as markdown)](terminologies.html#unbound)
}

```

 

 

 

 
 
**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: [Element.extension](extensibility.html)
 # [Annotation.author[x]](datatypes-definitions.html#Annotation.author[x]) : 0..1 Individual responsible for the annotation. One of these 2
 fhir:[Annotation.authorReference](datatypes-definitions.html#Annotation.authorReference) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]
 fhir:[Annotation.authorString](datatypes-definitions.html#Annotation.authorString) [ [string](datatypes.html#string) ]
 fhir:[Annotation.time](datatypes-definitions.html#Annotation.time) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the annotation was made
 fhir:[Annotation.text](datatypes-definitions.html#Annotation.text) [ [markdown](datatypes.html#markdown) ]; # 1..1 The annotation - text content (as markdown)
]

```

 

 

 

 
 
**Changes since Release 3**

 

 

 | 
 
 [Annotation](datatypes.html#Annotation)
 | 
 | 
 |

 | 
 Annotation.text | 
 
 

 Type changed from string to markdown

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 

 

Systems that do not have structured annotations simply communicate a single annotation with no author or time.

This element may need to be included in narrative because of the potential for modifying information.

Annotations **SHOULD NOT** be used to communicate "modifying" information that could be computable
(this is a SHOULD because enforcing user behavior is nearly impossible).

 

Annotation is used in the following places: [AllergyIntolerance](allergyintolerance.html#allergyintolerance), [CarePlan](careplan.html#careplan), [CareTeam](careteam.html#careteam), [ChargeItem](chargeitem.html#chargeitem), [ClinicalImpression](clinicalimpression.html#clinicalimpression), [Communication](communication.html#communication), [CommunicationRequest](communicationrequest.html#communicationrequest), [Condition](condition.html#condition), [Contract](contract.html#contract), [Device](device.html#device), [DeviceDefinition](devicedefinition.html#devicedefinition), [DeviceRequest](devicerequest.html#devicerequest), [DeviceUseStatement](deviceusestatement.html#deviceusestatement), [EffectEvidenceSynthesis](effectevidencesynthesis.html#effectevidencesynthesis), [Evidence](evidence.html#evidence), [EvidenceVariable](evidencevariable.html#evidencevariable), [FamilyMemberHistory](familymemberhistory.html#familymemberhistory), [Goal](goal.html#goal), [GuidanceResponse](guidanceresponse.html#guidanceresponse), [ImagingStudy](imagingstudy.html#imagingstudy), [Immunization](immunization.html#immunization), [Invoice](invoice.html#invoice), [List](list.html#list), [Media](media.html#media), [MedicationAdministration](medicationadministration.html#medicationadministration), [MedicationDispense](medicationdispense.html#medicationdispense), [MedicationRequest](medicationrequest.html#medicationrequest), [MedicationStatement](medicationstatement.html#medicationstatement), [NutritionOrder](nutritionorder.html#nutritionorder), [Observation](observation.html#observation), [Procedure](procedure.html#procedure), [RequestGroup](requestgroup.html#requestgroup), [ResearchStudy](researchstudy.html#researchstudy), [RiskAssessment](riskassessment.html#riskassessment), [RiskEvidenceSynthesis](riskevidencesynthesis.html#riskevidencesynthesis), [ServiceRequest](servicerequest.html#servicerequest), [Specimen](specimen.html#specimen), [Task](task.html#task) and [VisionPrescription](visionprescription.html#visionprescription)

## 2.24.0.19 Open Type Element [
](datatypes.html#open)

Some elements do not have a specified type. The type is represented by the wildcard symbol "*". In these cases, the element type may be one of the following:

 
 
**Primitive Types**

- [base64Binary](datatypes.html#base64Binary)

- [boolean](datatypes.html#boolean)

- [canonical](datatypes.html#canonical)

- [code](datatypes.html#code)

- [date](datatypes.html#date)

- [dateTime](datatypes.html#dateTime)

- [decimal](datatypes.html#decimal)

- [id](datatypes.html#id)

- [instant](datatypes.html#instant)

- [integer](datatypes.html#integer)

- [markdown](datatypes.html#markdown)

- [oid](datatypes.html#oid)

- [positiveInt](datatypes.html#positiveInt)

- [string](datatypes.html#string)

- [time](datatypes.html#time)

- [unsignedInt](datatypes.html#unsignedInt)

- [uri](datatypes.html#uri)

- [url](datatypes.html#url)

- [uuid](datatypes.html#uuid)

**Data Types**

- [Address](datatypes.html#Address)

- [Age](datatypes.html#Age)

- [Annotation](datatypes.html#Annotation)

- [Attachment](datatypes.html#Attachment)

- [CodeableConcept](datatypes.html#CodeableConcept)

- [Coding](datatypes.html#Coding)

- [ContactPoint](datatypes.html#ContactPoint)

- [Count](datatypes.html#Count)

- [Distance](datatypes.html#Distance)

- [Duration](datatypes.html#Duration)

- [HumanName](datatypes.html#HumanName)

- [Identifier](datatypes.html#Identifier)

- [Money](datatypes.html#Money)

- [Period](datatypes.html#Period)

- [Quantity](datatypes.html#Quantity)

- [Range](datatypes.html#Range)

- [Ratio](datatypes.html#Ratio)

- [Reference](references.html#Reference)

- [SampledData](datatypes.html#SampledData)

- [Signature](datatypes.html#Signature)

- [Timing](datatypes.html#Timing)

**MetaDataTypes**

- [ContactDetail](metadatatypes.html#ContactDetail)

- [Contributor](metadatatypes.html#Contributor)

- [DataRequirement](metadatatypes.html#DataRequirement)

- [Expression](metadatatypes.html#Expression)

- [ParameterDefinition](metadatatypes.html#ParameterDefinition)

- [RelatedArtifact](metadatatypes.html#RelatedArtifact)

- [TriggerDefinition](metadatatypes.html#TriggerDefinition)

- [UsageContext](metadatatypes.html#UsageContext)

**Special Types**

- [Dosage](dosage.html#Dosage)

- [Meta](resource.html#Meta)

The element name ends with "[x]", and this is replaced with the Title cased name of the data type.

Open references are used in the following places: [Parameters](parameters.html#parameters), [StructureMap](structuremap.html#structuremap) and [Task](task.html#task)

## 2.24.0.20 Other Types [
](datatypes.html#other)

The following types are defined as part of the data types, but are documented elsewhere in the specification:

 
 
 
 
 
 
 
 [Element](element.html#Element)- [Extensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeextension](extensibility.html) : [Extension](extensibility.html) 0..*[Extension](extensibility.html#Extension)[Source of the definition for the extension code - a logical name or a URLurl](extensibility-definitions.html#Extension.url) : [uri](#uri) [1..1][Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list)value[x]](extensibility-definitions.html#Extension.value_x_) : [*](datatypes.html#open) [0..1][Narrative](narrative.html#Narrative)[The status of the narrative - whether it's entirely generated (from just the defined data or the extensions too), or whether a human authored it and it may contain additional datastatus](narrative-definitions.html#Narrative.status) : [code](#code) [1..1] « [The status of a resource narrative. (Strength=Required)NarrativeStatus](valueset-narrative-status.html)! »[The actual narrative content, a stripped down version of XHTMLdiv](narrative-definitions.html#Narrative.div) : [xhtml](narrative.html#xhtml) [1..1][Reference](references.html#Reference)[A reference to a location at which the other resource is found. The reference may be a relative reference, in which case it is relative to the service base URL, or an absolute URL that resolves to the location where the resource is found. The reference may be version specific or not. If the reference is not to a FHIR RESTful server, then it should be assumed to be version specific. Internal fragment references (start with '#') refer to contained resourcesreference](references-definitions.html#Reference.reference) : [string](#string) [0..1][The expected type of the target of the reference. If both Reference.type and Reference.reference are populated and Reference.reference is a FHIR URL, both SHALL be consistent.

The type is the Canonical URL of Resource Definition that is the type this reference refers to. References are URLs that are relative to http://hl7.org/fhir/StructureDefinition/ e.g. "Patient" is a reference to http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are only allowed for logical models (and can only be used in references in logical models, not resources)type](references-definitions.html#Reference.type) : [uri](#uri) [0..1] « [Aa resource (or, for logical models, the URI of the logical model). (Strength=Extensible)ResourceType](valueset-resource-types.html)+ »[An identifier for the target resource. This is used when there is no way to reference the other resource directly, either because the entity it represents is not available through a FHIR server, or because there is no way for the author of the resource to convert a known identifier to an actual location. There is no requirement that a Reference.identifier point to something that is actually exposed as a FHIR instance, but it SHALL point to a business concept that would be expected to be exposed as a FHIR instance, and that instance would need to be of a FHIR resource type allowed by the referenceidentifier](references-definitions.html#Reference.identifier) : [Identifier](#Identifier) [0..1][Plain text narrative that identifies the resource in addition to the resource referencedisplay](references-definitions.html#Reference.display) : [string](#string) [0..1]

 **[Resource](resource.html#metadata)** - the conceptual base class for all resources

 - **[Reference](references.html#Reference)** - for references from one resource to another

 - **[Extension](extensibility.html)** - used to convey additional data in a resource

 - **[Narrative](narrative.html#Narrative)** - conveys a human-readable representation of the content of a resource