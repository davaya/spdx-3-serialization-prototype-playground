# Logical Model and the SPDX v2.3 Examples

The spdx-spec v2.3 [examples](https://github.com/spdx/spdx-spec/tree/development/v2.3.1/examples) directory says:

> All of the examples in this directory are for *the same SPDX document*.

(emphasis added), and includes examples in several formats:
* JSON
* RDF
* Spreadsheet
* Tag
* XML
* YAML

Since examples in different formats cannot be directly compared, SPDX v3 is based on a
[logical model](https://github.com/spdx/spdx-3-model/tree/main/model) that provides the mechanism
for determining what is meant by "the same SPDX document":
if processing each of the examples results in the identical set of logical values,
then they represent the same information.

* SPDX document - a set of one or more logical values that are serialized into a "unit of transmission" -
a file or payload
* Collection - a set of one or more logical values that are included in a logical group, such as the members
of a BOM or SBOM.

A single document can include parts of one collection (as shown in the v2.3 examples), parts of multiple
collections, or logical values that are members of no collections.
