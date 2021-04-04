# Code Analysis
 Dependency and call tree analysis.
This project provides generators for Cypher code for import into Neo4J from call tree and package dependencies.
These generators rely on several tools to provide their ingoing data.
Static calltrees of Java code can be created with java-callgraph, which can be found here: https://github.com/gousiosg/java-callgraph.
Dependencies of Java packages can be determined using JDepend, which can be found here: https://github.com/clarkware/jdepend.
Python dependencies are determined using the compiler and AST (Abstract Syntax Tree) with a tool provided in this project.

## Generating Cypher for a Java call tree
Create the call tree using java-callgraph and save it into a file, e.g., calltree-in.txt.
Run `java_call_tree calltree-in.txt > calltree-cypher.txt`.
`calltree-cypher.txt`contains two Cypher statements, one to insert all classes into a Neo4j database, and another to insert the call relations on method level.
You can just copy each statement and paste it into the Neo4j browser.
The database schema looks like this:
```
(:Class)-[:uses]->(:Class)
(:Method)-[:calls]->(:Method)
```
 
