# BiologicallyDerivedProduct - FHIR v4.0.1This records identifiers associated with this biologically derived product instance that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation)Broad category of this productBiologically Derived Product Category. (Strength=Required)A code that identifies the kind of this biologically derived product (SNOMED Ctcode)Whether the product is currently availableBiologically Derived Product Status. (Strength=Required)Procedure request to obtain this biologically derived productNumber of discrete units within this productParent product (if any)Healthcare professional who is performing the collectionThe patient or entity, such as a hospital or vendor in the case of a processed/manipulated/manufactured product, providing the productTime of product collectionDescription of of processingProcesing codeBiologically Derived Product Procedure. (Strength=Example)Substance added during processingTime of processingDescription of manipulationTime of manipulationDescription of storageStorage temperatureTemperature scale usedBiologicallyDerived Product Storage Scale. (Strength=Required)Storage timeperiodHow this product was collectedAny processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem CellsAny manipulation of product post-collection that is intended to alter the product.  For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusionProduct storageThis records identifiers associated with this biologically derived product instance that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation)Broad category of this productBiologically Derived Product Category. (Strength=Required)A code that identifies the kind of this biologically derived product (SNOMED Ctcode)Whether the product is currently availableBiologically Derived Product Status. (Strength=Required)Procedure request to obtain this biologically derived productNumber of discrete units within this productParent product (if any)Healthcare professional who is performing the collectionThe patient or entity, such as a hospital or vendor in the case of a processed/manipulated/manufactured product, providing the productTime of product collectionDescription of of processingProcesing codeBiologically Derived Product Procedure. (Strength=Example)Substance added during processingTime of processingDescription of manipulationTime of manipulationDescription of storageStorage temperatureTemperature scale usedBiologicallyDerived Product Storage Scale. (Strength=Required)Storage timeperiodHow this product was collectedAny processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem CellsAny manipulation of product post-collection that is intended to alter the product.  For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusionProduct storage

> Source: https://hl7.org/fhir/R4/biologicallyderivedproduct.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/biologicallyderivedproduct.html) [R4B](http://hl7.org/fhir/R4B/biologicallyderivedproduct.html) **R4**
 

# 10.11 Resource BiologicallyDerivedProduct - Content [
](biologicallyderivedproduct.html#10.11)

| [Orders and Observations ](http://www.hl7.org/Special/committees/orders/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 0 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): Not linked to any defined compartments | |

A material substance originating from a biological entity intended to be transplanted or infused
into another (possibly the same) biological entity.

 
 
## 10.11.1 Scope and Usage [
](biologicallyderivedproduct.html#bnc)

**Trial-Use Note:**

**Note that this content is preliminary has not undergone proper review by the appropriate Workgroups.**

 

A material substance originating from a biological entity intended to be transplanted or infused into another (possibly the same) biological entity.

 

Examples include:

 

 - hematopoietic stem cells (bone marrow, peripheral blood, or cord blood extraction)

 - blood (whole, extracted cells, plasma, etc.)

 - organs

 - tissues (porcine valves, skin, bovine cardiac tissue, etc.)

 - manipulated cells (e.g. CAR T-cells)

 

 

The workflow using this resource (e.g., request, administration) should be discussed and implemented in a consistent way as other similar resources are handled (e.g., device, medication)

 

## 10.11.2 Boundaries and Relationships [
](biologicallyderivedproduct.html#10.11.2)

This resource relates to these other resource:

 - ProcedureRequest (for collection)

 - Patient ("receiver" and "source")

 - Practitioner (who collected product)

 - Substance (product processing)

 - DiagnosticReport (containing HLA-typing)

 - BiologicallyDerivedProduct ("parent" product for multi-day collections)

 - Procedure (one for collection and one for transplantation, will need to add BiologicallyDerivedProduct to the "usedReference")

 

This resource is referenced by itself

## 10.11.3 
Resource Content
 [
](biologicallyderivedproduct.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [BiologicallyDerivedProduct](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A material substance originating from a biological entity**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External ids for this item
 | |

| [productCategory](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory) | | 0..1 | [code](datatypes.html#code) | organ | tissue | fluid | cells | biologicalAgent
[BiologicallyDerivedProductCategory](valueset-product-category.html) ([Required](terminologies.html#required)) | |

| [productCode](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | What this biologically derived product is | |

| [status](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status) | | 0..1 | [code](datatypes.html#code) | available | unavailable
[BiologicallyDerivedProductStatus](valueset-product-status.html) ([Required](terminologies.html#required)) | |

| [request](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request) | | 0..* | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | Procedure request
 | |

| [quantity](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity) | | 0..1 | [integer](datatypes.html#integer) | The amount of this biologically derived product | |

| [parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent) | | 0..* | [Reference](references.html#Reference)([BiologicallyDerivedProduct](biologicallyderivedproduct.html)) | BiologicallyDerivedProduct parent
 | |

| [collection](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection) | | 0..1 | [BackboneElement](backboneelement.html) | How this product was collected | |

| [collector](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Individual performing collection | |

| [source](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source) | | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Organization](organization.html)) | Who is product from | |

| [collected[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collected_x_) | | 0..1 | | Time of product collection | |

| collectedDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| collectedPeriod | | | [Period](datatypes.html#Period) | | |

| [processing](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing) | | 0..* | [BackboneElement](backboneelement.html) | Any processing of the product during collection
 | |

| [description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description) | | 0..1 | [string](datatypes.html#string) | Description of of processing | |

| [procedure](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Procesing code
[Procedure Codes (SNOMED CT)](valueset-procedure-code.html) ([Example](terminologies.html#example)) | |

| [additive](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive) | | 0..1 | [Reference](references.html#Reference)([Substance](substance.html)) | Substance added during processing | |

| [time[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.time_x_) | | 0..1 | | Time of processing | |

| timeDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| timePeriod | | | [Period](datatypes.html#Period) | | |

| [manipulation](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation) | | 0..1 | [BackboneElement](backboneelement.html) | Any manipulation of product post-collection | |

| [description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description) | | 0..1 | [string](datatypes.html#string) | Description of manipulation | |

| [time[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.time_x_) | | 0..1 | | Time of manipulation | |

| timeDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| timePeriod | | | [Period](datatypes.html#Period) | | |

| [storage](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage) | | 0..* | [BackboneElement](backboneelement.html) | Product storage
 | |

| [description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description) | | 0..1 | [string](datatypes.html#string) | Description of storage | |

| [temperature](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature) | | 0..1 | [decimal](datatypes.html#decimal) | Storage temperature | |

| [scale](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale) | | 0..1 | [code](datatypes.html#code) | farenheit | celsius | kelvin
[BiologicallyDerivedProductStorageScale](valueset-product-storage-scale.html) ([Required](terminologies.html#required)) | |

| [duration](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration) | | 0..1 | [Period](datatypes.html#Period) | Storage timeperiod | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 BiologicallyDerivedProduct ([DomainResource](domainresource.html))[This records identifiers associated with this biologically derived product instance that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation)identifier](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Broad category of this productproductCategory](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory) : [code](datatypes.html#code) [0..1] « [Biologically Derived Product Category. (Strength=Required)BiologicallyDerivedProductCat...](valueset-product-category.html)! »[A code that identifies the kind of this biologically derived product (SNOMED Ctcode)productCode](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][Whether the product is currently availablestatus](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status) : [code](datatypes.html#code) [0..1] « [Biologically Derived Product Status. (Strength=Required)BiologicallyDerivedProductSta...](valueset-product-status.html)! »[Procedure request to obtain this biologically derived productrequest](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request) : [Reference](references.html#Reference) [0..*] « [ServiceRequest](servicerequest.html#ServiceRequest) »[Number of discrete units within this productquantity](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity) : [integer](datatypes.html#integer) [0..1][Parent product (if any)parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent) : [Reference](references.html#Reference) [0..*] « [BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct) »Collection[Healthcare professional who is performing the collectioncollector](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[The patient or entity, such as a hospital or vendor in the case of a processed/manipulated/manufactured product, providing the productsource](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Organization](organization.html#Organization) »[Time of product collectioncollected[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collected_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »Processing[Description of of processingdescription](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description) : [string](datatypes.html#string) [0..1][Procesing codeprocedure](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Biologically Derived Product Procedure. (Strength=Example)ProcedureCodes(SNOMEDCT)](valueset-procedure-code.html)?? »[Substance added during processingadditive](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive) : [Reference](references.html#Reference) [0..1] « [Substance](substance.html#Substance) »[Time of processingtime[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.time_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »Manipulation[Description of manipulationdescription](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description) : [string](datatypes.html#string) [0..1][Time of manipulationtime[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.time_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »Storage[Description of storagedescription](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description) : [string](datatypes.html#string) [0..1][Storage temperaturetemperature](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature) : [decimal](datatypes.html#decimal) [0..1][Temperature scale usedscale](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale) : [code](datatypes.html#code) [0..1] « [BiologicallyDerived Product Storage Scale. (Strength=Required)BiologicallyDerivedProductSto...](valueset-product-storage-scale.html)! »[Storage timeperiodduration](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration) : [Period](datatypes.html#Period) [0..1]
[How this product was collectedcollection](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection)[0..1][Any processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem Cellsprocessing](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing)[0..*][Any manipulation of product post-collection that is intended to alter the product. For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusionmanipulation](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation)[0..1][Product storagestorage](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage)[0..*]
 

 

 

**XML Template**

 

 
```
<[**BiologicallyDerivedProduct**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External ids for this item](terminologies.html#unbound) --></identifier>
 <[**productCategory**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory) value="[[code](datatypes.html#code)]"/><!-- **0..1** [organ | tissue | fluid | cells | biologicalAgent](valueset-product-category.html) -->
 <[**productCode**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [What this biologically derived product is](terminologies.html#unbound) --></productCode>
 <[**status**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status) value="[[code](datatypes.html#code)]"/><!-- **0..1** [available | unavailable](valueset-product-status.html) -->
 <[**request**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request)><!-- **0..*** [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) [Procedure request](terminologies.html#unbound) --></request>
 <[**quantity**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity) value="[[integer](datatypes.html#integer)]"/><!-- **0..1** [The amount of this biologically derived product](terminologies.html#unbound) -->
 <[**parent**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent)><!-- **0..*** [Reference](references.html#Reference)([BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct)) [BiologicallyDerivedProduct parent](terminologies.html#unbound) --></parent>
 <[**collection**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection)> <!-- **0..1** How this product was collected -->
 <[**collector**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) [Individual performing collection](terminologies.html#unbound) --></collector>
 <[**source**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Organization](organization.html#Organization)) [Who is product from](terminologies.html#unbound) --></source>
 <[**collected[x]**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collected[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [Time of product collection](terminologies.html#unbound) --></collected[x]>
 </collection>
 <[**processing**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing)> <!-- **0..*** Any processing of the product during collection -->
 <[**description**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Description of of processing](terminologies.html#unbound) -->
 <[**procedure**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Procesing code](valueset-procedure-code.html) --></procedure>
 <[**additive**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive)><!-- **0..1** [Reference](references.html#Reference)([Substance](substance.html#Substance)) [Substance added during processing](terminologies.html#unbound) --></additive>
 <[**time[x]**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.time[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [Time of processing](terminologies.html#unbound) --></time[x]>
 </processing>
 <[**manipulation**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation)> <!-- **0..1** Any manipulation of product post-collection -->
 <[**description**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Description of manipulation](terminologies.html#unbound) -->
 <[**time[x]**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.time[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [Time of manipulation](terminologies.html#unbound) --></time[x]>
 </manipulation>
 <[**storage**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage)> <!-- **0..*** Product storage -->
 <[**description**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Description of storage](terminologies.html#unbound) -->
 <[**temperature**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Storage temperature](terminologies.html#unbound) -->
 <[**scale**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale) value="[[code](datatypes.html#code)]"/><!-- **0..1** [farenheit | celsius | kelvin](valueset-product-storage-scale.html) -->
 <[**duration**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration)><!-- **0..1** [Period](datatypes.html#Period) [Storage timeperiod](terminologies.html#unbound) --></duration>
 </storage>
</BiologicallyDerivedProduct>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**BiologicallyDerivedProduct**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External ids for this item](terminologies.html#unbound)
 "[productCategory](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory)" : "<[code](datatypes.html#code)>", // [organ | tissue | fluid | cells | biologicalAgent](valueset-product-category.html)
 "[productCode](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [What this biologically derived product is](terminologies.html#unbound)
 "[status](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status)" : "<[code](datatypes.html#code)>", // [available | unavailable](valueset-product-status.html)
 "[request](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request)" : [{ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) }], // [Procedure request](terminologies.html#unbound)
 "[quantity](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity)" : <[integer](datatypes.html#integer)>, // [The amount of this biologically derived product](terminologies.html#unbound)
 "[parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent)" : [{ [Reference](references.html#Reference)([BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct)) }], // [BiologicallyDerivedProduct parent](terminologies.html#unbound)
 "[collection](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection)" : { // [How this product was collected](terminologies.html#unbound)
 "[collector](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [Individual performing collection](terminologies.html#unbound)
 "[source](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Organization](organization.html#Organization)) }, // [Who is product from](terminologies.html#unbound)
 // collected[x]: Time of product collection. One of these 2:
 "[collectedDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collectedDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[collectedPeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collectedPeriod)" : { [Period](datatypes.html#Period) }
 },
 "[processing](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing)" : [{ // [Any processing of the product during collection](terminologies.html#unbound)
 "[description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description)" : "<[string](datatypes.html#string)>", // [Description of of processing](terminologies.html#unbound)
 "[procedure](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Procesing code](valueset-procedure-code.html)
 "[additive](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive)" : { [Reference](references.html#Reference)([Substance](substance.html#Substance)) }, // [Substance added during processing](terminologies.html#unbound)
 // time[x]: Time of processing. One of these 2:
 "[timeDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.timeDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[timePeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.timePeriod)" : { [Period](datatypes.html#Period) }
 }],
 "[manipulation](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation)" : { // [Any manipulation of product post-collection](terminologies.html#unbound)
 "[description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description)" : "<[string](datatypes.html#string)>", // [Description of manipulation](terminologies.html#unbound)
 // time[x]: Time of manipulation. One of these 2:
 "[timeDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.timeDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[timePeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.timePeriod)" : { [Period](datatypes.html#Period) }
 },
 "[storage](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage)" : [{ // [Product storage](terminologies.html#unbound)
 "[description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description)" : "<[string](datatypes.html#string)>", // [Description of storage](terminologies.html#unbound)
 "[temperature](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature)" : <[decimal](datatypes.html#decimal)>, // [Storage temperature](terminologies.html#unbound)
 "[scale](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale)" : "<[code](datatypes.html#code)>", // [farenheit | celsius | kelvin](valueset-product-storage-scale.html)
 "[duration](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration)" : { [Period](datatypes.html#Period) } // [Storage timeperiod](terminologies.html#unbound)
 }]
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**BiologicallyDerivedProduct**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[BiologicallyDerivedProduct.identifier](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External ids for this item
 fhir:[BiologicallyDerivedProduct.productCategory](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory) [ [code](datatypes.html#code) ]; # 0..1 organ | tissue | fluid | cells | biologicalAgent
 fhir:[BiologicallyDerivedProduct.productCode](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 What this biologically derived product is
 fhir:[BiologicallyDerivedProduct.status](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status) [ [code](datatypes.html#code) ]; # 0..1 available | unavailable
 fhir:[BiologicallyDerivedProduct.request](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request) [ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) ], ... ; # 0..* Procedure request
 fhir:[BiologicallyDerivedProduct.quantity](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity) [ [integer](datatypes.html#integer) ]; # 0..1 The amount of this biologically derived product
 fhir:[BiologicallyDerivedProduct.parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent) [ [Reference](references.html#Reference)([BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct)) ], ... ; # 0..* BiologicallyDerivedProduct parent
 fhir:[BiologicallyDerivedProduct.collection](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection) [ # 0..1 How this product was collected
 fhir:[BiologicallyDerivedProduct.collection.collector](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 Individual performing collection
 fhir:[BiologicallyDerivedProduct.collection.source](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Organization](organization.html#Organization)) ]; # 0..1 Who is product from
 # [BiologicallyDerivedProduct.collection.collected[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collected[x]) : 0..1 Time of product collection. One of these 2
 fhir:[BiologicallyDerivedProduct.collection.collectedDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collectedDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[BiologicallyDerivedProduct.collection.collectedPeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collectedPeriod) [ [Period](datatypes.html#Period) ]
 ];
 fhir:[BiologicallyDerivedProduct.processing](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing) [ # 0..* Any processing of the product during collection
 fhir:[BiologicallyDerivedProduct.processing.description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description) [ [string](datatypes.html#string) ]; # 0..1 Description of of processing
 fhir:[BiologicallyDerivedProduct.processing.procedure](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Procesing code
 fhir:[BiologicallyDerivedProduct.processing.additive](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive) [ [Reference](references.html#Reference)([Substance](substance.html#Substance)) ]; # 0..1 Substance added during processing
 # [BiologicallyDerivedProduct.processing.time[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.time[x]) : 0..1 Time of processing. One of these 2
 fhir:[BiologicallyDerivedProduct.processing.timeDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.timeDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[BiologicallyDerivedProduct.processing.timePeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.timePeriod) [ [Period](datatypes.html#Period) ]
 ], ...;
 fhir:[BiologicallyDerivedProduct.manipulation](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation) [ # 0..1 Any manipulation of product post-collection
 fhir:[BiologicallyDerivedProduct.manipulation.description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description) [ [string](datatypes.html#string) ]; # 0..1 Description of manipulation
 # [BiologicallyDerivedProduct.manipulation.time[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.time[x]) : 0..1 Time of manipulation. One of these 2
 fhir:[BiologicallyDerivedProduct.manipulation.timeDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.timeDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[BiologicallyDerivedProduct.manipulation.timePeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.timePeriod) [ [Period](datatypes.html#Period) ]
 ];
 fhir:[BiologicallyDerivedProduct.storage](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage) [ # 0..* Product storage
 fhir:[BiologicallyDerivedProduct.storage.description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description) [ [string](datatypes.html#string) ]; # 0..1 Description of storage
 fhir:[BiologicallyDerivedProduct.storage.temperature](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature) [ [decimal](datatypes.html#decimal) ]; # 0..1 Storage temperature
 fhir:[BiologicallyDerivedProduct.storage.scale](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale) [ [code](datatypes.html#code) ]; # 0..1 farenheit | celsius | kelvin
 fhir:[BiologicallyDerivedProduct.storage.duration](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration) [ [Period](datatypes.html#Period) ]; # 0..1 Storage timeperiod
 ], ...;
]

```

 

 

 

**Changes since R3**

 

 
This resource did not exist in Release 2

 

 This analysis is available as [XML](biologicallyderivedproduct.diff.xml) or [JSON](biologicallyderivedproduct.diff.json).
 

 
 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [BiologicallyDerivedProduct](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A material substance originating from a biological entity**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External ids for this item
 | |

| [productCategory](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory) | | 0..1 | [code](datatypes.html#code) | organ | tissue | fluid | cells | biologicalAgent
[BiologicallyDerivedProductCategory](valueset-product-category.html) ([Required](terminologies.html#required)) | |

| [productCode](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | What this biologically derived product is | |

| [status](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status) | | 0..1 | [code](datatypes.html#code) | available | unavailable
[BiologicallyDerivedProductStatus](valueset-product-status.html) ([Required](terminologies.html#required)) | |

| [request](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request) | | 0..* | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | Procedure request
 | |

| [quantity](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity) | | 0..1 | [integer](datatypes.html#integer) | The amount of this biologically derived product | |

| [parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent) | | 0..* | [Reference](references.html#Reference)([BiologicallyDerivedProduct](biologicallyderivedproduct.html)) | BiologicallyDerivedProduct parent
 | |

| [collection](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection) | | 0..1 | [BackboneElement](backboneelement.html) | How this product was collected | |

| [collector](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Individual performing collection | |

| [source](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source) | | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Organization](organization.html)) | Who is product from | |

| [collected[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collected_x_) | | 0..1 | | Time of product collection | |

| collectedDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| collectedPeriod | | | [Period](datatypes.html#Period) | | |

| [processing](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing) | | 0..* | [BackboneElement](backboneelement.html) | Any processing of the product during collection
 | |

| [description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description) | | 0..1 | [string](datatypes.html#string) | Description of of processing | |

| [procedure](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Procesing code
[Procedure Codes (SNOMED CT)](valueset-procedure-code.html) ([Example](terminologies.html#example)) | |

| [additive](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive) | | 0..1 | [Reference](references.html#Reference)([Substance](substance.html)) | Substance added during processing | |

| [time[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.time_x_) | | 0..1 | | Time of processing | |

| timeDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| timePeriod | | | [Period](datatypes.html#Period) | | |

| [manipulation](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation) | | 0..1 | [BackboneElement](backboneelement.html) | Any manipulation of product post-collection | |

| [description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description) | | 0..1 | [string](datatypes.html#string) | Description of manipulation | |

| [time[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.time_x_) | | 0..1 | | Time of manipulation | |

| timeDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| timePeriod | | | [Period](datatypes.html#Period) | | |

| [storage](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage) | | 0..* | [BackboneElement](backboneelement.html) | Product storage
 | |

| [description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description) | | 0..1 | [string](datatypes.html#string) | Description of storage | |

| [temperature](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature) | | 0..1 | [decimal](datatypes.html#decimal) | Storage temperature | |

| [scale](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale) | | 0..1 | [code](datatypes.html#code) | farenheit | celsius | kelvin
[BiologicallyDerivedProductStorageScale](valueset-product-storage-scale.html) ([Required](terminologies.html#required)) | |

| [duration](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration) | | 0..1 | [Period](datatypes.html#Period) | Storage timeperiod | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 BiologicallyDerivedProduct ([DomainResource](domainresource.html))[This records identifiers associated with this biologically derived product instance that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation)identifier](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Broad category of this productproductCategory](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory) : [code](datatypes.html#code) [0..1] « [Biologically Derived Product Category. (Strength=Required)BiologicallyDerivedProductCat...](valueset-product-category.html)! »[A code that identifies the kind of this biologically derived product (SNOMED Ctcode)productCode](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][Whether the product is currently availablestatus](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status) : [code](datatypes.html#code) [0..1] « [Biologically Derived Product Status. (Strength=Required)BiologicallyDerivedProductSta...](valueset-product-status.html)! »[Procedure request to obtain this biologically derived productrequest](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request) : [Reference](references.html#Reference) [0..*] « [ServiceRequest](servicerequest.html#ServiceRequest) »[Number of discrete units within this productquantity](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity) : [integer](datatypes.html#integer) [0..1][Parent product (if any)parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent) : [Reference](references.html#Reference) [0..*] « [BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct) »Collection[Healthcare professional who is performing the collectioncollector](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[The patient or entity, such as a hospital or vendor in the case of a processed/manipulated/manufactured product, providing the productsource](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Organization](organization.html#Organization) »[Time of product collectioncollected[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collected_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »Processing[Description of of processingdescription](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description) : [string](datatypes.html#string) [0..1][Procesing codeprocedure](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Biologically Derived Product Procedure. (Strength=Example)ProcedureCodes(SNOMEDCT)](valueset-procedure-code.html)?? »[Substance added during processingadditive](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive) : [Reference](references.html#Reference) [0..1] « [Substance](substance.html#Substance) »[Time of processingtime[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.time_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »Manipulation[Description of manipulationdescription](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description) : [string](datatypes.html#string) [0..1][Time of manipulationtime[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.time_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »Storage[Description of storagedescription](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description) : [string](datatypes.html#string) [0..1][Storage temperaturetemperature](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature) : [decimal](datatypes.html#decimal) [0..1][Temperature scale usedscale](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale) : [code](datatypes.html#code) [0..1] « [BiologicallyDerived Product Storage Scale. (Strength=Required)BiologicallyDerivedProductSto...](valueset-product-storage-scale.html)! »[Storage timeperiodduration](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration) : [Period](datatypes.html#Period) [0..1]
[How this product was collectedcollection](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection)[0..1][Any processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem Cellsprocessing](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing)[0..*][Any manipulation of product post-collection that is intended to alter the product. For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusionmanipulation](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation)[0..1][Product storagestorage](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage)[0..*]
 

**XML Template**

 

 
```
<[**BiologicallyDerivedProduct**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External ids for this item](terminologies.html#unbound) --></identifier>
 <[**productCategory**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory) value="[[code](datatypes.html#code)]"/><!-- **0..1** [organ | tissue | fluid | cells | biologicalAgent](valueset-product-category.html) -->
 <[**productCode**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [What this biologically derived product is](terminologies.html#unbound) --></productCode>
 <[**status**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status) value="[[code](datatypes.html#code)]"/><!-- **0..1** [available | unavailable](valueset-product-status.html) -->
 <[**request**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request)><!-- **0..*** [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) [Procedure request](terminologies.html#unbound) --></request>
 <[**quantity**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity) value="[[integer](datatypes.html#integer)]"/><!-- **0..1** [The amount of this biologically derived product](terminologies.html#unbound) -->
 <[**parent**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent)><!-- **0..*** [Reference](references.html#Reference)([BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct)) [BiologicallyDerivedProduct parent](terminologies.html#unbound) --></parent>
 <[**collection**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection)> <!-- **0..1** How this product was collected -->
 <[**collector**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) [Individual performing collection](terminologies.html#unbound) --></collector>
 <[**source**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Organization](organization.html#Organization)) [Who is product from](terminologies.html#unbound) --></source>
 <[**collected[x]**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collected[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [Time of product collection](terminologies.html#unbound) --></collected[x]>
 </collection>
 <[**processing**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing)> <!-- **0..*** Any processing of the product during collection -->
 <[**description**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Description of of processing](terminologies.html#unbound) -->
 <[**procedure**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Procesing code](valueset-procedure-code.html) --></procedure>
 <[**additive**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive)><!-- **0..1** [Reference](references.html#Reference)([Substance](substance.html#Substance)) [Substance added during processing](terminologies.html#unbound) --></additive>
 <[**time[x]**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.time[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [Time of processing](terminologies.html#unbound) --></time[x]>
 </processing>
 <[**manipulation**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation)> <!-- **0..1** Any manipulation of product post-collection -->
 <[**description**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Description of manipulation](terminologies.html#unbound) -->
 <[**time[x]**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.time[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [Time of manipulation](terminologies.html#unbound) --></time[x]>
 </manipulation>
 <[**storage**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage)> <!-- **0..*** Product storage -->
 <[**description**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Description of storage](terminologies.html#unbound) -->
 <[**temperature**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Storage temperature](terminologies.html#unbound) -->
 <[**scale**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale) value="[[code](datatypes.html#code)]"/><!-- **0..1** [farenheit | celsius | kelvin](valueset-product-storage-scale.html) -->
 <[**duration**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration)><!-- **0..1** [Period](datatypes.html#Period) [Storage timeperiod](terminologies.html#unbound) --></duration>
 </storage>
</BiologicallyDerivedProduct>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**BiologicallyDerivedProduct**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External ids for this item](terminologies.html#unbound)
 "[productCategory](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory)" : "<[code](datatypes.html#code)>", // [organ | tissue | fluid | cells | biologicalAgent](valueset-product-category.html)
 "[productCode](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [What this biologically derived product is](terminologies.html#unbound)
 "[status](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status)" : "<[code](datatypes.html#code)>", // [available | unavailable](valueset-product-status.html)
 "[request](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request)" : [{ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) }], // [Procedure request](terminologies.html#unbound)
 "[quantity](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity)" : <[integer](datatypes.html#integer)>, // [The amount of this biologically derived product](terminologies.html#unbound)
 "[parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent)" : [{ [Reference](references.html#Reference)([BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct)) }], // [BiologicallyDerivedProduct parent](terminologies.html#unbound)
 "[collection](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection)" : { // [How this product was collected](terminologies.html#unbound)
 "[collector](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [Individual performing collection](terminologies.html#unbound)
 "[source](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Organization](organization.html#Organization)) }, // [Who is product from](terminologies.html#unbound)
 // collected[x]: Time of product collection. One of these 2:
 "[collectedDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collectedDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[collectedPeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collectedPeriod)" : { [Period](datatypes.html#Period) }
 },
 "[processing](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing)" : [{ // [Any processing of the product during collection](terminologies.html#unbound)
 "[description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description)" : "<[string](datatypes.html#string)>", // [Description of of processing](terminologies.html#unbound)
 "[procedure](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Procesing code](valueset-procedure-code.html)
 "[additive](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive)" : { [Reference](references.html#Reference)([Substance](substance.html#Substance)) }, // [Substance added during processing](terminologies.html#unbound)
 // time[x]: Time of processing. One of these 2:
 "[timeDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.timeDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[timePeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.timePeriod)" : { [Period](datatypes.html#Period) }
 }],
 "[manipulation](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation)" : { // [Any manipulation of product post-collection](terminologies.html#unbound)
 "[description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description)" : "<[string](datatypes.html#string)>", // [Description of manipulation](terminologies.html#unbound)
 // time[x]: Time of manipulation. One of these 2:
 "[timeDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.timeDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[timePeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.timePeriod)" : { [Period](datatypes.html#Period) }
 },
 "[storage](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage)" : [{ // [Product storage](terminologies.html#unbound)
 "[description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description)" : "<[string](datatypes.html#string)>", // [Description of storage](terminologies.html#unbound)
 "[temperature](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature)" : <[decimal](datatypes.html#decimal)>, // [Storage temperature](terminologies.html#unbound)
 "[scale](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale)" : "<[code](datatypes.html#code)>", // [farenheit | celsius | kelvin](valueset-product-storage-scale.html)
 "[duration](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration)" : { [Period](datatypes.html#Period) } // [Storage timeperiod](terminologies.html#unbound)
 }]
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**BiologicallyDerivedProduct**](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[BiologicallyDerivedProduct.identifier](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External ids for this item
 fhir:[BiologicallyDerivedProduct.productCategory](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCategory) [ [code](datatypes.html#code) ]; # 0..1 organ | tissue | fluid | cells | biologicalAgent
 fhir:[BiologicallyDerivedProduct.productCode](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.productCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 What this biologically derived product is
 fhir:[BiologicallyDerivedProduct.status](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.status) [ [code](datatypes.html#code) ]; # 0..1 available | unavailable
 fhir:[BiologicallyDerivedProduct.request](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.request) [ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) ], ... ; # 0..* Procedure request
 fhir:[BiologicallyDerivedProduct.quantity](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.quantity) [ [integer](datatypes.html#integer) ]; # 0..1 The amount of this biologically derived product
 fhir:[BiologicallyDerivedProduct.parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent) [ [Reference](references.html#Reference)([BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct)) ], ... ; # 0..* BiologicallyDerivedProduct parent
 fhir:[BiologicallyDerivedProduct.collection](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection) [ # 0..1 How this product was collected
 fhir:[BiologicallyDerivedProduct.collection.collector](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collector) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 Individual performing collection
 fhir:[BiologicallyDerivedProduct.collection.source](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.source) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Organization](organization.html#Organization)) ]; # 0..1 Who is product from
 # [BiologicallyDerivedProduct.collection.collected[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collected[x]) : 0..1 Time of product collection. One of these 2
 fhir:[BiologicallyDerivedProduct.collection.collectedDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collectedDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[BiologicallyDerivedProduct.collection.collectedPeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.collection.collectedPeriod) [ [Period](datatypes.html#Period) ]
 ];
 fhir:[BiologicallyDerivedProduct.processing](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing) [ # 0..* Any processing of the product during collection
 fhir:[BiologicallyDerivedProduct.processing.description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.description) [ [string](datatypes.html#string) ]; # 0..1 Description of of processing
 fhir:[BiologicallyDerivedProduct.processing.procedure](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.procedure) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Procesing code
 fhir:[BiologicallyDerivedProduct.processing.additive](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.additive) [ [Reference](references.html#Reference)([Substance](substance.html#Substance)) ]; # 0..1 Substance added during processing
 # [BiologicallyDerivedProduct.processing.time[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.time[x]) : 0..1 Time of processing. One of these 2
 fhir:[BiologicallyDerivedProduct.processing.timeDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.timeDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[BiologicallyDerivedProduct.processing.timePeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.processing.timePeriod) [ [Period](datatypes.html#Period) ]
 ], ...;
 fhir:[BiologicallyDerivedProduct.manipulation](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation) [ # 0..1 Any manipulation of product post-collection
 fhir:[BiologicallyDerivedProduct.manipulation.description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.description) [ [string](datatypes.html#string) ]; # 0..1 Description of manipulation
 # [BiologicallyDerivedProduct.manipulation.time[x]](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.time[x]) : 0..1 Time of manipulation. One of these 2
 fhir:[BiologicallyDerivedProduct.manipulation.timeDateTime](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.timeDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[BiologicallyDerivedProduct.manipulation.timePeriod](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.manipulation.timePeriod) [ [Period](datatypes.html#Period) ]
 ];
 fhir:[BiologicallyDerivedProduct.storage](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage) [ # 0..* Product storage
 fhir:[BiologicallyDerivedProduct.storage.description](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.description) [ [string](datatypes.html#string) ]; # 0..1 Description of storage
 fhir:[BiologicallyDerivedProduct.storage.temperature](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.temperature) [ [decimal](datatypes.html#decimal) ]; # 0..1 Storage temperature
 fhir:[BiologicallyDerivedProduct.storage.scale](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.scale) [ [code](datatypes.html#code) ]; # 0..1 farenheit | celsius | kelvin
 fhir:[BiologicallyDerivedProduct.storage.duration](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.storage.duration) [ [Period](datatypes.html#Period) ]; # 0..1 Storage timeperiod
 ], ...;
]

```

 

**Changes since Release 3**

 

 
This resource did not exist in Release 2

 

 This analysis is available as [XML](biologicallyderivedproduct.diff.xml) or [JSON](biologicallyderivedproduct.diff.json).
 

 
 

 

 

See the [Profiles & Extensions](biologicallyderivedproduct-profiles.html) and the alternate definitions:
Master Definition [XML](biologicallyderivedproduct.profile.xml.html) + [JSON](biologicallyderivedproduct.profile.json.html),
[XML](xml.html) [Schema](biologicallyderivedproduct.xsd)/[Schematron](biologicallyderivedproduct.sch) + [JSON](json.html) 
[Schema](biologicallyderivedproduct.schema.json.html), [ShEx](biologicallyderivedproduct.shex.html) (for [Turtle](rdf.html)) + [see the extensions](biologicallyderivedproduct-profiles.html) & the [dependency analysis](biologicallyderivedproduct-dependencies.html)

### 10.11.3.1 
Terminology Bindings
 [
](biologicallyderivedproduct.html#tx)

 | Path | Definition | Type | Reference | |

 | BiologicallyDerivedProduct.productCategory | Biologically Derived Product Category. | [Required](terminologies.html#required) | [BiologicallyDerivedProductCategory](valueset-product-category.html) | |

 | BiologicallyDerivedProduct.productCode | Biologically Derived Product Code. | Unknown | No details provided yet | |

 | BiologicallyDerivedProduct.status | Biologically Derived Product Status. | [Required](terminologies.html#required) | [BiologicallyDerivedProductStatus](valueset-product-status.html) | |

 | BiologicallyDerivedProduct.processing.procedure | Biologically Derived Product Procedure. | [Example](terminologies.html#example) | [ProcedureCodes(SNOMEDCT)](valueset-procedure-code.html) | |

 | BiologicallyDerivedProduct.storage.scale | BiologicallyDerived Product Storage Scale. | [Required](terminologies.html#required) | [BiologicallyDerivedProductStorageScale](valueset-product-storage-scale.html) | |