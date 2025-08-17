# 17363358 - Old Toolbox

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 220 bytes                  |
| Total Events     | 3                          |
| References Count | 10                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [22](#event-22)       | 0x0001       |     41 |              7 |
| [23](#event-23)       | 0x002A       |    108 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CE2      |        7394 |
|       1 | 0x1CE3      |        7395 |
|       2 | 0x1CE4      |        7396 |
|       3 | 0x0000      |           0 |
|       4 | 0x1CE6      |        7398 |
|       5 | 0x1CE7      |        7399 |
|       6 | 0x1CE8      |        7400 |
|       7 | 0x0018      |          24 |
|       8 | 0x18FA      |        6394 |
|       9 | 0x1CE5      |        7397 |

## String References

- **6394**: Obtained key item: 3.
- **7394**: You see tools and boxes lying around. They look very old.
- **7395**: You see an old iron box.
- **7396**: Examine the iron box? [Yes./No.]
- **7397**: You decide to leave it alone.
- **7398**: You look inside the box. You see several toolboxes, still filled with tools.
- **7399**: You find one with a name engraved on the cover. The name reads, "Vigilant Owl."
- **7400**: Take the toolbox with you? [Yes./No.]

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

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    53 F0 FF FF 7F F0 FF  FF 7F 72 65 73 30 53 F0   S........res0S.
0010: FF FF 7F F0 FF FF 7F 72  65 73 32 4A F0 FF FF 7F  .......res2J....
0020: 9E F1 08 01 48 00 80 23  21 00                    ....H..#!.      
```

#### Opcodes

```
  0: 0x0001 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [LocalPlayer, LocalPlayer]
  1: 0x000E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res2" with entities [LocalPlayer, LocalPlayer]
  2: 0x001B [0x4A] LocalPlayer looks at Old Toolbox (ID: 17363358/0x0108F19E)
  3: 0x0024 [0x48] [System] [7394*]:
    → "You see tools and boxes lying around. They look very old."
  4: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0028 [0x21] END_EVENT
  6: 0x0029 [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x002A    |
| Data Size    | 108 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                53 F0 FF FF 7F F0            S.....
0030: FF FF 7F 72 65 73 30 53  F0 FF FF 7F F0 FF FF 7F  ...res0S........
0040: 72 65 73 32 4A F0 FF FF  7F 9E F1 08 01 48 01 80  res2J........H..
0050: 23 24 02 80 03 80 03 80  25 02 00 10 03 80 00 90  #$......%.......
0060: 00 48 04 80 23 48 05 80  23 24 06 80 03 80 03 80  .H..#H..#$......
0070: 25 02 00 10 03 80 00 89  00 43 00 43 01 03 02 10  %........C.C....
0080: 07 80 48 08 80 23 01 8D  00 48 09 80 23 01 94 00  ..H..#...H..#...
0090: 48 09 80 23 21 00                                 H..#!.          
```

#### Opcodes

```
  0: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [LocalPlayer, LocalPlayer]
  1: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res2" with entities [LocalPlayer, LocalPlayer]
  2: 0x0044 [0x4A] LocalPlayer looks at Old Toolbox (ID: 17363358/0x0108F19E)
  3: 0x004D [0x48] [System] [7395*]:
    → "You see an old iron box."
  4: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0051 [0x24] CREATE_DIALOG(message_id=7396*, default_option=0*, option_flags=0*)
    → "Examine the iron box? [Yes./No.]"
  6: 0x0058 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0059 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0090
  8: 0x0061 [0x48] [System] [7398*]:
    → "You look inside the box. You see several toolboxes, still filled with tools."
  9: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0065 [0x48] [System] [7399*]:
    → "You find one with a name engraved on the cover. The name reads, "Vigilant Owl.""
 11: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0069 [0x24] CREATE_DIALOG(message_id=7400*, default_option=0*, option_flags=0*)
    → "Take the toolbox with you? [Yes./No.]"
 13: 0x0070 [0x25] WAIT_DIALOG_SELECT()
 14: 0x0071 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0089
 15: 0x0079 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 16: 0x007B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 17: 0x007D [0x03] Work_Zone[2] = 24*
 18: 0x0082 [0x48] [System] [6394*]:
    → "Obtained key item: 3."
 19: 0x0085 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0086 [0x01] GOTO 0x008D
 21: 0x0089 [0x48] [System] [7397*]:
    → "You decide to leave it alone."
 22: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_008D:
 23: 0x008D [0x01] GOTO 0x0094
 24: 0x0090 [0x48] [System] [7397*]:
    → "You decide to leave it alone."
 25: 0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0094:
 26: 0x0094 [0x21] END_EVENT
 27: 0x0095 [0x00] END_REQSTACK()
```
