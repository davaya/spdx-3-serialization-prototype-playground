# SPDX v2.3 Example to Logical Examples

```commandline
  "SPDXID": "SPDXRef-DOCUMENT",
  "spdxVersion": "SPDX-2.3",
  "creationInfo": {
    "comment": "This package has been shipped in source and binary form.\nThe binaries were created with gcc 4.5.1 and expect to link to\ncompatible system run time libraries.",
    "created": "2010-01-29T18:30:22Z",
    "creators": ["Jane Doe", "ExampleCodeInspect", "LicenseFind-1.0"],
    "licenseListVersion": "3.17"
  },
  "name": "SPDX-Tools-v2.0",
  "dataLicense": "CC0-1.0",
  "comment": "This document was created using SPDX 2.0 using licenses from the web site.",
  "documentDescribes": ["SPDXRef-File", "SPDXRef-Package"],
  "documentNamespace": "http://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301",
```


| 2.3 Values                                       | Logical Examples                                               |                                        Notes                                         |
|--------------------------------------------------|----------------------------------------------------------------|:------------------------------------------------------------------------------------:|
| --- **Agents** ---                               | --- **Agents** ---                                             |                                                                                      |
|                                                  | [Agent1](ex/agent.md)                                          |                                                                                      |
| Person: Jane Doe ()                              | [Person1](ex/person1.md) with minimal CreationInfo             |                                                                                      |
|                                                  | [Person2](ex/person2.md) with full CreationInfo                |                                                                                      |
|                                                  | [Person3](ex/person3.md) with no CreationInfo???               |                                                                                      |
| Organization: ExampleCodeInspect ()              | [Organization1](ex/organization1.md)                           |                                                                                      |
| Tool: LicenseFind-1.0                            | [Tool1](ex/tool1.md) not an Agent                              |                                                                                      |
| --- **Annotations** ---                          | --- **Annotations** ---                                        |                                                                                      |
| 2010-01-29T18:30:22Z, Jane Doe ()                | [Annotation1](ex/annotation1.md)                               |                                                                                      |
| 2010-02-10T00:00:00Z, Joe Reviewer               | Annotation2                                                    |                                                                                      |
| 2011-03-13T00:00:00Z, Suzanne Reviewer           | Annotation3                                                    |                                                                                      |
| 2011-01-29T18:30:22Z, Package Commenter (glibc)  | Annotation4                                                    |                                                                                      |
| 2011-01-29T18:30:22Z, File Commenter (foo.c)     | Annotation5                                                    |                                                                                      |
| --- **Artifacts** ---                            | --- **Artifacts** ---                                          |                                                                                      |
| fromDoap-1, Apache Commons Lang                  | [Package1](ex/package1.md)                                     |                                                                                      |
|                                                  | [Package2](ex/package2.md) with ExternalIdentifier             |                                                                                      |
| glibc - refs: [cpe:2.3, acmecorp]                | [Package3](ex/package3.md) with ExternalReference              | hasFiles (Bag! 14) [Specification(5), CommonsLangSrc(4), JenaLib(3), DoapSource (2)] |
| fromDoap-0, Jena                                 | Package4                                                       |                                                                                      |
| Saxon                                            | Package5                                                       |                                                                                      |
| DoapSource                                       | [File1](ex/file1.md)                                           |                                                                                      |
| CommonsLangSrs                                   | [File2](ex/file2.md)                                           |                                                                                      |
| Specification (myspec.pdf)                       | File3                                                          |                                                                                      |
| File (foo.c)                                     | File4                                                          |                                                                                      |
| from Linux kernel                                | [Snippet1](ex/snippet1.md)                                     |                                                                                      |
|                                                  |                                                                |                                                                                      |
| --- **Relationships** ---                        | --- **Relationships** ---                                      |                                                                                      |
|                                                  | [Relationship1](ex/relationship1.md) Pkg1, File1, File2        |                                                                                      |
|                                                  | [Relationship2](ex/relationship2.md) with time properties      |                                                                                      |
| DOCUMENT CONTAINS Package                        |                                                                |                                                                                      |
| DOCUMENT COPY_OF spdx-tool-1.2:ToolsElement      |                                                                |                                                                                      |
| Package DYNAMIC_LINK Saxon                       |                                                                |                                                                                      |
| CommonsLangSrc GENERATED_FROM NOASSERTION        |                                                                |                                                                                      |
| JenaLib CONTAINS Package                         |                                                                |                                                                                      |
| Specification SPECIFICATION_FOR fromDoap-0       |                                                                |                                                                                      |
| File GENERATED_FROM fromDoap-0                   |                                                                |                                                                                      |
|                                                  | [LifecycleScopeRelationship1](ex/lcsrelationship1.md)          |                                                                                      |
|                                                  | [AssessmentRelationship1](ex/assessmentrelationship1.md)       |                                                                                      |
|                                                  | [SoftwareDependencyRelationship1](ex/swdeprelationshpi.md)     |                                                                                      |
| --- **Collections** ---                          | --- **Collections** ---                                        |                                                                                      |
|                                                  | [Bom2](ex/bom1.md)                                             |                                                                                      |
|                                                  | [Sbom1](ex/sbom1.md) with two Files                            |                                                                                      |
|                                                  | [Sbom2](ex/sbom2.md) with Pkg1, File1, File2, Rel1             |                                                                                      |                           |                      |                      |                             |                                        |     [o](json2/examples/sbom1.json)      |                          |          |      |      |                          |
|                                                  | [Bundle1](ex/bundle1.md)                                       |                                                                                      |
|                                                  | [Bundle2](ex/bundle2.md) of Person1, Person2                   |                                                                                      |
| --- **SpdxDocuments** ---                        | --- **SpdxDocuments** ---                                      |                                                                                      |
|                                                  | [SpdxDocument1](ex/spdxdocument1.md) with two Files            |                                                                                      |
|                                                  | [SpdxDocument2](ex/spdxdocument2.md) with two Sboms            |                                                                                      |
|                                                  | [SpdxDocument3](ex/spdxdocument3.md) with NamespaceMap         |                                                                                      |
|                                                  | [SpdxDocument4](ex/spdxdocument4.md) with ExternalMap          |                                                                                      |
| DOCUMENT (SPDX-Tools-v2.0, 2011-01-29T18:30:22Z) | [SpdxDocument5](ex/spdxdocument5.md) v2.3 example              |                                                                                      |
| externalDocumentId: DocumentRef-spdx-tool-1.2    |                                                                |                   SpdxDocument is a document, internal or external                   |
| --- **Licensing** ---                            | --- **Licensing** ---                                          |                                                                                      |
|                                                  | [License1](ex/license1.md) single artifact                     |                                                                                      |
|                                                  | [CustomLicense1](ex/customlicense1.md) single artifact         |                                                                                      |
|                                                  | [LicenseExpression1](ex/licenseexpression1.md) single artifact |                                                                                      |
|                                                  | [LicenseExpression2](ex/licenseexpression2.md) single artifact |                                                                                      |
|                                                  | [LicenseExpression3](ex/licenseexpression3.md) two artifacts   |                                                                                      |
| licenseId: LicenseRef-1                          |                                                                |                                                                                      |
| licenseId: LicenseRef-2                          |                                                                |                                                                                      |
| licenseId: LicenseRef-4                          |                                                                |                                                                                      |
| name: Beer-Ware License (Version 42)             |                                                                |                                                                                      |
| name: CyberNeko License                          |                                                                |                                                                                      |
|                                                  | --- **Security** ---                                           |                                                                                      |
|                                                  |                                                                |                                                                                      |
|                                                  | --- **Build** ---                                              |                                                                                      |
|                                                              