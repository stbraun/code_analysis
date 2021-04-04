# Code Analysis
 Dependency and call tree analysis.
This project provides generators for Cypher code for import into Neo4J from call tree and package dependencies.
These generators rely on several tools to provide their ingoing data.
Static calltrees of Java code can be created with java-callgraph, which can be found here: [java_callgraph on GitHub](https://github.com/gousiosg/java-callgraph).
Dependencies of Java packages can be determined using JDepend, which can be found here: [JDepend on GitHub](https://github.com/clarkware/jdepend).
Python dependencies are determined using the compiler and AST (Abstract Syntax Tree) with a tool provided in this project.

## Generating Cypher for a Java call tree
Create the call tree using java-callgraph and save it into a file, e.g., `java_call_tree_input.txt`.
Run 

```
java_call_tree java_call_tree_input.txt > calltree-cypher.txt
```

`calltree-cypher.txt`contains two Cypher statements, one to insert all classes into a Neo4j database, and another to insert the call relations on method level.
You can just copy each statement and paste it into the Neo4j browser.

The database schema looks like this:

```
(:Class)-[:uses]->(:Class)
(:Method)-[:calls]->(:Method)
```
 
## Generating Cypher code for Java dependencies
Create dependencies using JDepend and save it in a file, e.g., `java_depend.txt`.

Run following command:

```
java_dependencies java_depend.txt > java_depend.cypher
```

Now you can copy the Cypher statements stored in `java_depend.cypher` and paste it into the Neo4j browser.

The database schema looks like this:

```
(:Package)-[:depends_on]->(:Package)
```

To check for cycles you may run the query:

```
MATCH (p:Package)-[r1:depends_on]->(q:Package)-[r2:depends_on]->(p:Package)
RETURN p, q, r1, r2
```

It helps to switch off the default setting, which shows all relations, in the browser settings.

## Generating Cypher code for Python dependencies

Determination of dependencies and generation of Cypher code are done in one step in this case:

```
python_dependencies <path to your package> > python-deps.cypher
```

The tool compiles the code and walks the AST looking for import statements. Then it generates Cypher code modelling the relationships between the packages.

The database schema looks like this:

```
(:Package)-[:contains]->(:Module) 
(:Module)-[:uses]->(:Module)
```

