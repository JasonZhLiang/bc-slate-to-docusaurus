---
title: "Global Entity File Formats"
date: "2017-10-10"
---

brainCloud supports the importing and exporting of Global Entities via JSON files. This is useful for:

- backing up global entity data
- migrating entities from app to app
- easy integration with external tools

There are three different JSON file formats supported. There are pros and cons to each of them:

- _Raw JSON Object format_ - highly recommended for backups and data migration. Not as clean for use with external tools.
- _Simplified JSON Object format_ - very good for integration with external tools.
- _Simplified JSON Line format_ - useful for integration with external tools that support JSON line format. Limited to a single entity-type per file.

Each of the file formats is described in more detail below.

* * *

### Raw JSON Object Format

Below is a raw JSON object file. Note that:

- EntityTypes are enclosed in JSON arrays - and thus multiple entityTypes are supported.
- brainCloud meta-data is preserved
    - entityId
    - entityIndexedId
    - timeToLive
    - expiresAt
    - createdAt
    - updatedAt
    - version
    - acl
    - ownerId ← only if the appId of the record matches the currently selected gameId

_Note that although the example below only shows a single entity type, "hero", the file structure does allow multiple types of entities to be present in a single file._

{
  "hero" : \[ 
    {
      "entityIndexedId" : "superman",
      "timeToLive" : null,
      "createdAt" : 1506914746453,
      "data" : {
        "name" : "Superman",
        "alignment" : "Lawful Good",
        "cape" : true,
        "sex" : "m",
        "secretIdentity" : {
          "firstName" : "Clark",
          "lastName" : "Kent"
        },
        "attributes" : {
          "intelligence" : 90,
          "strength" : 300,
          "charisma" : 95
        },
        "powers" : \[ "flight", "xray vision", "heat vision", "super strength", "invulnerable" \],
        "skills" : \[ "combat" \],
        "equipment" : \[ "glasses" \]
      },
      "entityType" : "hero",
      "appId" : "22436",
      "entityId" : "2642b324-0c86-4779-817a-832c30884c81",
      "acl" : {
        "other" : 1
      },
      "ownerId" : null,
      "version" : 1,
      "expiresAt" : 9223372036854775807,
      "updatedAt" : 1506914746453
    }, {
      "entityIndexedId" : "batman",
      "timeToLive" : null,
      "createdAt" : 1506914673444,
      "data" : {
        "name" : "Batman",
        "alignment" : "Neutral Good",
        "cape" : true,
        "sex" : "m",
        "secretIdentity" : {
          "firstName" : "Bruce",
          "lastName" : "Wayne"
        },
        "attributes" : {
          "intelligence" : 99,
          "strength" : 95,
          "charisma" : 90
        },
        "powers" : \[ \],
        "skills" : \[ "martial arts", "combat", "detective", "stealth", "tactics" \],
        "equipment" : \[ "grapple gun", "batarangs", "utility belt" \]
      },
      "entityType" : "hero",
      "appId" : "22436",
      "entityId" : "9e73c19a-f82e-4385-8bce-320c249b2c9b",
      "acl" : {
        "other" : 1
      },
      "ownerId" : null,
      "version" : 1,
      "expiresAt" : 9223372036854775807,
      "updatedAt" : 1506914673444
    }, {
      "entityIndexedId" : "wonder woman",
      "timeToLive" : null,
      "createdAt" : 1506914835429,
      "data" : {
        "name" : "Wonder Woman",
        "alignment" : "Neutral Good",
        "cape" : false,
        "sex" : "f",
        "secretIdentity" : {
          "firstName" : "Diana",
          "lastName" : "Prince"
        },
        "attributes" : {
          "intelligence" : 90,
          "strength" : 250,
          "charisma" : 92
        },
        "powers" : \[ "flight", "super strength", "invulnerability" \],
        "skills" : \[ "combat" \],
        "equipment" : \[ "lasso", "sword", "shield" \]
      },
      "entityType" : "hero",
      "appId" : "22436",
      "entityId" : "dce12974-d76d-4922-b011-ec596ec14d47",
      "acl" : {
        "other" : 1
      },
      "ownerId" : null,
      "version" : 1,
      "expiresAt" : 9223372036854775807,
      "updatedAt" : 1506914835429
    } 
  \]
}

* * *

### Simplified JSON Object Format

Simplified JSON is very readable, and suitable for round-trip importing and exporting with tools like Google Sheets.

It minimizes the structure and overheads that brainCloud imposes - though that comes with limitations (record-level ACL, ownership, and entityIds are not preserved).

File format specifics:

- EntityTypes are enclosed in JSON arrays - and thus multiple entityTypes are supported. ← Same as RAW
- brainCloud meta-data is NOT preserved, other than **`entityIndexedId`** (encoded as `_eiid`) and **`entityType`** (represented by the enclosing array)
- The lack of a "data" section makes the object easier to view and understand

_NOTE - \_eiid is not unique - it is simply a lookup index. This is one of the reasons that we delete all entities of a type before importing - so that each import doesn't create more and more entities!_

{
  "hero" : \[ 
    {
      "name" : "Superman",
      "alignment" : "Lawful Good",
      "cape" : true,
      "sex" : "m",
      "secretIdentity" : {
        "firstName" : "Clark",
        "lastName" : "Kent"
      },
      "attributes" : {
        "intelligence" : 90,
        "strength" : 300,
        "charisma" : 95
      },
      "powers" : \[ "flight", "xray vision", "heat vision", "super strength", "invulnerable" \],
      "skills" : \[ "combat" \],
      "equipment" : \[ "glasses" \],
      "\_eiid" : "superman"
    }, {
      "name" : "Batman",
      "alignment" : "Neutral Good",
      "cape" : true,
      "sex" : "m",
      "secretIdentity" : {
        "firstName" : "Bruce",
        "lastName" : "Wayne"
      },
      "attributes" : {
        "intelligence" : 99,
        "strength" : 95,
        "charisma" : 90
      },
      "powers" : \[ \],
      "skills" : \[ "martial arts", "combat", "detective", "stealth", "tactics"\],
      "equipment" : \[ "grapple gun", "batarangs", "utility belt" \],
      "\_eiid" : "batman"
    }, {
      "name" : "Wonder Woman",
      "alignment" : "Neutral Good",
      "cape" : false,
      "sex" : "f",
      "secretIdentity" : {
        "firstName" : "Diana",
        "lastName" : "Prince"
      },
      "attributes" : {
        "intelligence" : 90,
        "strength" : 250,
        "charisma" : 92
      },
      "powers" : \[ "flight", "super strength", "invulnerability" \],
      "skills" : \[ "combat" \],
      "equipment" : \[ "lasso", "sword", "shield" \],
      "\_eiid" : "wonder woman"
    } 
  \]
}

* * *

### Simplified JSON Lines Format

JSON Lines files are a bit simpler in structure that JSON object files - in that they don't require the enclosing object array structure.

Basically each line of the file is considered a separate JSON object.

Because of this, JSON Lines files can only support a single _entityType_ per file.

Note that we are using a simpler example for better readability. Also note that the file below contains just 3 lines (it looks like more due to word-wrapping - notice the line numbers).

{"name":"Superman","alignment":"Lawful Good","cape":true,"sex":"m","secretIdentity":{"firstName":"Clark","lastName":"Kent"},"\_eiid":"superman"}
{"name":"Batman","alignment":"Neutral Good","cape":true,"sex":"m","secretIdentity":{"firstName":"Bruce","lastName":"Wayne"},,"\_eiid":"batman"}
{"name":"Wonder Woman","alignment":"Neutral Good","cape":false,"sex":"f","secretIdentity":{"firstName":"Diana","lastName":"Prince"},"\_eiid":"wonder woman"}
