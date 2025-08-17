# 17478358 - Rodeupansat

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Crawlers' Nest [S] (ID: 171) |
| Block Size       | 416 bytes                    |
| Total Events     | 6                            |
| References Count | 19                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [106](#event-106)     | 0x0001       |     27 |             13 |
| [107](#event-107)     | 0x001C       |     75 |             23 |
| [108](#event-108)     | 0x0067       |     15 |              7 |
| [109](#event-109)     | 0x0076       |    153 |             25 |
| [110](#event-110)     | 0x010F       |     28 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E11      |        7697 |
|       1 | 0x1E12      |        7698 |
|       2 | 0x1E13      |        7699 |
|       3 | 0x1E14      |        7700 |
|       4 | 0x1E15      |        7701 |
|       5 | 0x0014      |          20 |
|       6 | 0x1E16      |        7702 |
|       7 | 0x03C8      |         968 |
|       8 | 0x1E17      |        7703 |
|       9 | 0x1E18      |        7704 |
|      10 | 0x1E19      |        7705 |
|      11 | 0x1E1A      |        7706 |
|      12 | 0x1E1B      |        7707 |
|      13 | 0x1E1C      |        7708 |
|      14 | 0x1E1D      |        7709 |
|      15 | 0x1E1E      |        7710 |
|      16 | 0x00C9      |         201 |
|      17 | 0x0000      |           0 |
|      18 | 0x1E1F      |        7711 |

## String References

- **7697**: Greetings. I am Rodeupansat, a friar from the San d'Orian Cathedral.
- **7698**: As a servant of the Goddess, my duty is to purify the evil that torments our fair land. I have devoted myself to the strengthening of seals that ward off the ever-growing presence of evil.
- **7699**: Currently, I am working on a seal that will cleanse Vunkerl Inlet of a foul creature of darkness that has been menacing there of late.
- **7700**: It is imperative that these vile beings, known in the Near East as "djinn," are banished once and for all.
- **7701**: I must hurry and complete the seal lest evil overwhelm the land...
- **7702**: You are a soldier of the Allied Forces, are you not? Please lend me your ears and listen to my plea.
- **7703**: If you happen to travel to Vunkerl Inlet, could you please take this $3 with you?
- **7704**: I am informed that the presence of evil is most prominent in the southwest region of Vunkerl Inlet. The seal's effect will be greatest if it is attached to the tower that stands there.
- **7705**: May the Goddess guide you.
- **7706**: You have attached the $3 to the tower? You have my gratitude! Did the seal produce the desired effect?
- **7707**: Is that so... What could possibly have gone wrong?
- **7708**: This is most discouraging... I created the seal based on the legendary artifact that was said to have warded off evil in the Gusgen Mines in days of yore.
- **7709**: But I shan't give up! I shall not rest until I have created a powerful seal that will keep the children of Altana safe from harm.
- **7710**: Please accept this small token of my gratitude.
- **7711**: Let us work together for the sake of all that is good in this world. May Paradise open its gates to you.

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

### Event 106

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 27 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 1D 02   ........#...#..
0010: 80 23 1D 03 80 23 1D 04  80 23 21 00              .#...#...#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7697*)
    → "Greetings. I am Rodeupansat, a friar from the San d'Orian Cathedral."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7698*)
    → "As a servant of the Goddess, my duty is to purify the evil that torments our fair land. I have devoted myself to the strengthening of seals that ward off the ever-growing presence of evil."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=7699*)
    → "Currently, I am working on a seal that will cleanse Vunkerl Inlet of a foul creature of darkness that has been menacing there of late."
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=7700*)
    → "It is imperative that these vile beings, known in the Near East as "djinn," are banished once and for all."
  8: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "I must hurry and complete the seal lest evil overwhelm the land..."
 10: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x001A [0x21] END_EVENT
 12: 0x001B [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 75 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      42 1E F0 FF              B...
0020: FF 7F 1D 00 80 23 1D 01  80 23 1D 02 80 23 1D 03  .....#...#...#..
0030: 80 23 5B 05 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#[..........tlk
0040: 30 1D 06 80 23 03 02 10  07 80 1D 08 80 23 1D 09  0...#........#..
0050: 80 23 5B 05 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#[..........tlk
0060: 31 1D 0A 80 23 21 00                              1...#!.         
```

#### Opcodes

```
  0: 0x001C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x001D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7697*)
    → "Greetings. I am Rodeupansat, a friar from the San d'Orian Cathedral."
  3: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=7698*)
    → "As a servant of the Goddess, my duty is to purify the evil that torments our fair land. I have devoted myself to the strengthening of seals that ward off the ever-growing presence of evil."
  5: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=7699*)
    → "Currently, I am working on a seal that will cleanse Vunkerl Inlet of a foul creature of darkness that has been menacing there of late."
  7: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7700*)
    → "It is imperative that these vile beings, known in the Near East as "djinn," are banished once and for all."
  9: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0032 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 11: 0x0041 [0x1D] PRINT_EVENT_MESSAGE(message_id=7702*)
    → "You are a soldier of the Allied Forces, are you not? Please lend me your ears and listen to my plea."
 12: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0045 [0x03] Work_Zone[2] = 968*
 14: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=7703*)
    → "If you happen to travel to Vunkerl Inlet, could you please take this $3 with you?"
 15: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=7704*)
    → "I am informed that the presence of evil is most prominent in the southwest region of Vunkerl Inlet. The seal's effect will be greatest if it is attached to the tower that stands there."
 17: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0052 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 19: 0x0061 [0x1D] PRINT_EVENT_MESSAGE(message_id=7705*)
    → "May the Goddess guide you."
 20: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0065 [0x21] END_EVENT
 22: 0x0066 [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      1E  F0 FF FF 7F 1D 09 80 23         ........#
0070: 1D 0A 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0067 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x006C [0x1D] PRINT_EVENT_MESSAGE(message_id=7704*)
    → "I am informed that the presence of evil is most prominent in the southwest region of Vunkerl Inlet. The seal's effect will be greatest if it is attached to the tower that stands there."
  2: 0x006F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=7705*)
    → "May the Goddess guide you."
  4: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0074 [0x21] END_EVENT
  6: 0x0075 [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0076    |
| Data Size    | 153 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   42 1E  F0 FF FF 7F 03 02 10 07        B.........
0080: 80 6F 70 5B 05 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .op[..........tl
0090: 6B 30 1D 0B 80 23 5B 05  80 F8 FF FF 7F F8 FF FF  k0...#[.........
00A0: 7F 74 6C 6B 31 1D 0C 80  23 1D 0D 80 23 5B 05 80  .tlk1...#...#[..
00B0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 0E 80 23  ........tlk0...#
00C0: 5B 05 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 53  [..........tlk1S
00D0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 5B 05 80 F8  ........tlk1[...
00E0: FF FF 7F F8 FF FF 7F 70  61 73 30 1D 0F 80 23 53  .......pas0...#S
00F0: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 45 10 80 F8  ........pas0E...
0100: FF FF 7F F8 FF FF 7F 71  73 74 63 11 80 21 00     .......qstc..!. 
```

#### Opcodes

```
  0: 0x0076 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0077 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x007C [0x03] Work_Zone[2] = 968*
  3: 0x0081 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0082 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0083 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  6: 0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=7706*)
    → "You have attached the $3 to the tower? You have my gratitude! Did the seal produce the desired effect?"
  7: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0096 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  9: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7707*)
    → "Is that so... What could possibly have gone wrong?"
 10: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00A9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7708*)
    → "This is most discouraging... I created the seal based on the legendary artifact that was said to have warded off evil in the Gusgen Mines in days of yore."
 12: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00AD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 14: 0x00BC [0x1D] PRINT_EVENT_MESSAGE(message_id=7709*)
    → "But I shan't give up! I shall not rest until I have created a powerful seal that will keep the children of Altana safe from harm."
 15: 0x00BF [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00C0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 17: 0x00CF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 18: 0x00DC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 19: 0x00EB [0x1D] PRINT_EVENT_MESSAGE(message_id=7710*)
    → "Please accept this small token of my gratitude."
 20: 0x00EE [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00EF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 22: 0x00FC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 23: 0x010D [0x21] END_EVENT
 24: 0x010E [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               1E                 .
0110: F0 FF FF 7F 6F 70 5B 05  80 F8 FF FF 7F F8 FF FF  ....op[.........
0120: 7F 69 6E 6F 30 1D 12 80  23 21 00                 .ino0...#!.     
```

#### Opcodes

```
  0: 0x010F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0114 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0115 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0116 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0125 [0x1D] PRINT_EVENT_MESSAGE(message_id=7711*)
    → "Let us work together for the sake of all that is good in this world. May Paradise open its gates to you."
  5: 0x0128 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0129 [0x21] END_EVENT
  7: 0x012A [0x00] END_REQSTACK()
```
