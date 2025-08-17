# 17797183 - Laughing Bison

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 120 bytes        |
| Total Events     | 2                |
| References Count | 7                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [333](#event-333)     | 0x0001       |     66 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0090      |         144 |
|       1 | 0x003C      |          60 |
|       2 | 0x0000      |           0 |
|       3 | 0x1C64      |        7268 |
|       4 | 0x1C63      |        7267 |
|       5 | 0x1C66      |        7270 |
|       6 | 0x1C65      |        7269 |

## String References

- **7267**: The ship bound for Selbina will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time).
- **7268**: The ship bound for Selbina is now [arriving/departing].
- **7269**: The ship bound for Al Zahbi will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time).
- **7270**: The ship bound for Al Zahbi is now [arriving/departing].

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 333

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 66 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 04 10 02 10 15 04  10 00 80 15 02 10 01 80   ...............
0010: 02 05 10 02 80 00 2E 00  02 02 10 02 80 00 27 00  ..............'.
0020: 1D 03 80 23 01 2B 00 1D  04 80 23 01 41 00 02 02  ...#.+....#.A...
0030: 10 02 80 00 3D 00 1D 05  80 23 01 41 00 1D 06 80  ....=....#.A....
0040: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[4] = Work_Zone[2]
  1: 0x0006 [0x15] Work_Zone[4] /= 144*
  2: 0x000B [0x15] Work_Zone[2] /= 60*
  3: 0x0010 [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x002E
  4: 0x0018 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0027
  5: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7268*)
    → "The ship bound for Selbina is now [arriving/departing]."
  6: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0024 [0x01] GOTO 0x002B
  8: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=7267*)
    → "The ship bound for Selbina will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time)."
  9: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_002B:
 10: 0x002B [0x01] GOTO 0x0041
 11: 0x002E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x003D
 12: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=7270*)
    → "The ship bound for Al Zahbi is now [arriving/departing]."
 13: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003A [0x01] GOTO 0x0041
 15: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=7269*)
    → "The ship bound for Al Zahbi will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time)."
 16: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0041:
 17: 0x0041 [0x21] END_EVENT
 18: 0x0042 [0x00] END_REQSTACK()
```
