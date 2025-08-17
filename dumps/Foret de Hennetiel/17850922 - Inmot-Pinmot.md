# 17850922 - Inmot-Pinmot

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Foret de Hennetiel (ID: 262) |
| Block Size       | 324 bytes                    |
| Total Events     | 6                            |
| References Count | 13                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2520](#event-2520)   | 0x0001       |     56 |             16 |
| [2521](#event-2521)   | 0x0039       |     44 |             10 |
| [2522](#event-2522)   | 0x0065       |     73 |             17 |
| [2525](#event-2525)   | 0x00AE       |     44 |             10 |
| [2524](#event-2524)   | 0x00DA       |     11 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0022      |          34 |
|       1 | 0x1D53      |        7507 |
|       2 | 0x1D54      |        7508 |
|       3 | 0x1D55      |        7509 |
|       4 | 0x1D56      |        7510 |
|       5 | 0x1D57      |        7511 |
|       6 | 0x1D58      |        7512 |
|       7 | 0x1D59      |        7513 |
|       8 | 0x1D5A      |        7514 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0000      |           0 |
|      11 | 0x1D5B      |        7515 |
|      12 | 0x1D5C      |        7516 |

## String References

- **7507**: Excuse me! On your way here, did you come across any unsully-wullied land?
- **7508**: These areas are keptaru clean by mystical forces known as "ergon loci."
- **7509**: If you find one, can you collectaru a bunch of sand from the area? I'm conducting advanced research into the loci's origin-worigin and effects.
- **7510**: I've heard that ergon loci have the power to cleansy-weanse poison and other detrimentarus from the surrounding land. You should recognize one at first sight. Does that help?
- **7511**: You found it! You really found it! This is fantastic-wastic! It's both pure and clean. My experimentations can now continue!
- **7512**: You see, we don't know much about these loci, except that there are pristine locations in other areas of Eastern Ulbuka-wuka, too.
- **7513**: The one thing the loci have in common is their ability to sanctify surrounding lands, like a force of energy-wenergy welling up from the ground. You must have feltaru something when you crossed the beaches.
- **7514**: But for now, back to work! If all goes according to plan, this may be the secretaru to cleansing the whole river!
- **7515**: [Defiled/Pure white] sand stretches out before you.
- **7516**: An aura of tranquility embraces the land and soothes your heart.

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

### Event 2520

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 56 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F   B.....opf......
0010: F8 FF FF 7F 74 6C 62 30  1D 01 80 23 1D 02 80 23  ....tlb0...#...#
0020: 1D 03 80 23 1D 04 80 23  66 00 80 F8 FF FF 7F F8  ...#...#f.......
0030: FF FF 7F 74 6C 62 31 21  00                       ...tlb1!.       
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=34*
  5: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7507*)
    → "Excuse me! On your way here, did you come across any unsully-wullied land?"
  6: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=7508*)
    → "These areas are keptaru clean by mystical forces known as "ergon loci.""
  8: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7509*)
    → "If you find one, can you collectaru a bunch of sand from the area? I'm conducting advanced research into the loci's origin-worigin and effects."
 10: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7510*)
    → "I've heard that ergon loci have the power to cleansy-weanse poison and other detrimentarus from the surrounding land. You should recognize one at first sight. Does that help?"
 12: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=34*
 14: 0x0037 [0x21] END_EVENT
 15: 0x0038 [0x00] END_REQSTACK()
```

### Event 2521

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             42 1E F0 FF FF 7F 6F           B.....o
0040: 70 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 62 30  pf..........tlb0
0050: 1D 04 80 23 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
0060: 6C 62 31 21 00                                    lb1!.           
```

#### Opcodes

```
  0: 0x0039 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x003A [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0040 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0041 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=34*
  5: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=7510*)
    → "I've heard that ergon loci have the power to cleansy-weanse poison and other detrimentarus from the surrounding land. You should recognize one at first sight. Does that help?"
  6: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0054 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=34*
  8: 0x0063 [0x21] END_EVENT
  9: 0x0064 [0x00] END_REQSTACK()
```

### Event 2522

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 73 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                42 1E F0  FF FF 7F 6F 70 66 00 80       B.....opf..
0070: F8 FF FF 7F F8 FF FF 7F  74 6C 62 30 1D 05 80 23  ........tlb0...#
0080: 1D 06 80 23 1D 07 80 23  1D 08 80 23 66 00 80 F8  ...#...#...#f...
0090: FF FF 7F F8 FF FF 7F 74  6C 62 31 45 09 80 F0 FF  .......tlb1E....
00A0: FF 7F F0 FF FF 7F 71 73  74 63 0A 80 21 00        ......qstc..!.  
```

#### Opcodes

```
  0: 0x0065 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0066 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x006C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x006D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=34*
  5: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=7511*)
    → "You found it! You really found it! This is fantastic-wastic! It's both pure and clean. My experimentations can now continue!"
  6: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=7512*)
    → "You see, we don't know much about these loci, except that there are pristine locations in other areas of Eastern Ulbuka-wuka, too."
  8: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=7513*)
    → "The one thing the loci have in common is their ability to sanctify surrounding lands, like a force of energy-wenergy welling up from the ground. You must have feltaru something when you crossed the beaches."
 10: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7514*)
    → "But for now, back to work! If all goes according to plan, this may be the secretaru to cleansing the whole river!"
 12: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x008C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=34*
 14: 0x009B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 15: 0x00AC [0x21] END_EVENT
 16: 0x00AD [0x00] END_REQSTACK()
```

### Event 2525

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            42 1E                B.
00B0: F0 FF FF 7F 6F 70 66 00  80 F8 FF FF 7F F8 FF FF  ....opf.........
00C0: 7F 74 6C 62 30 1D 08 80  23 66 00 80 F8 FF FF 7F  .tlb0...#f......
00D0: F8 FF FF 7F 74 6C 62 31  21 00                    ....tlb1!.      
```

#### Opcodes

```
  0: 0x00AE [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00AF [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00B4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00B5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00B6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=34*
  5: 0x00C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7514*)
    → "But for now, back to work! If all goes according to plan, this may be the secretaru to cleansing the whole river!"
  6: 0x00C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00C9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=34*
  8: 0x00D8 [0x21] END_EVENT
  9: 0x00D9 [0x00] END_REQSTACK()
```

### Event 2524

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DA   |
| Data Size    | 11 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                42 48 0B 80 23 48            BH..#H
00E0: 0C 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x00DA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00DB [0x48] [System] [7515*]:
    → "[Defiled/Pure white] sand stretches out before you."
  2: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00DF [0x48] [System] [7516*]:
    → "An aura of tranquility embraces the land and soothes your heart."
  4: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00E3 [0x21] END_EVENT
  6: 0x00E4 [0x00] END_REQSTACK()
```
