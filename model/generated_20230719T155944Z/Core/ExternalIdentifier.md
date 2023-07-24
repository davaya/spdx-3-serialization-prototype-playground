## [ExternalIdentifier](https://github.com/spdx/spdx-3-model/blob/main/model/Core/Classes/ExternalIdentifier.md)
Model: [fa68f94](https://github.com/spdx/spdx-3-model/commit/fa68f942ae1a0d0e8f05df6526f147cbe64183ed) 2023-07-19T15:59:44Z
```
class ExternalIdentifier():
    externalIdentifierType: ExternalIdentifierType = None # 
    identifier: String = None                          # * 
    comment: String = None                             # * optional 
    identifierLocator: String = None                   # * optional Set[1..*]
    issuingAuthority: String = None                    # * optional 
```