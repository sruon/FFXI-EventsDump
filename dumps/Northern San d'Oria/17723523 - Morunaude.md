# 17723523 - Morunaude

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 600 bytes                     |
| Total Events     | 24                            |
| References Count | 10                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |      9 |              3 |
| [65535.3](#event-655353)   | 0x001A       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002A       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0038       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0048       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0056       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0066       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0074       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0084       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0092       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00A2       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00B0       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00C0       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00CE       |      9 |              3 |
| [634](#event-634)          | 0x00D7       |     29 |             10 |
| [635](#event-635)          | 0x00F4       |     32 |              9 |
| [65535.16](#event-6553516) | 0x0114       |     23 |              7 |
| [65535.17](#event-6553517) | 0x012B       |     19 |              5 |
| [65535.18](#event-6553518) | 0x013E       |     37 |              9 |
| [636](#event-636)          | 0x0163       |     37 |             14 |
| [978](#event-978)          | 0x0188       |     26 |              8 |
| [979](#event-979)          | 0x01A2       |     27 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1C1C      |        7196 |
|       2 | 0x1C1D      |        7197 |
|       3 | 0x1C1E      |        7198 |
|       4 | 0x1C1F      |        7199 |
|       5 | 0x1C20      |        7200 |
|       6 | 0x1C21      |        7201 |
|       7 | 0x1C22      |        7202 |
|       8 | 0x1C23      |        7203 |
|       9 | 0x1C24      |        7204 |

## String References

- **7196**: Our furniture is built to last!
- **7197**: Say, that $3 you've got there...
- **7198**: What did you say? It was in the $2 you purchased...from us?
- **7199**: Might I have a look? Wait, this $3 looks familiar.
- **7200**: Yes, as I thought! This is the mark of the royal family. This is a teacup of noble lineage!
- **7201**: You must return it to its rightful owner, wherever he or she might be.
- **7202**: That $2 you found was crafted of old. I would love to hear the history behind it.
- **7203**: Few pieces of such age and quality remain.
- **7204**: Shame on Calovour! Hawking such a treasure as if it were junk!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 00  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                66 00 80 F8 FF FF            f.....
0020: 7F F8 FF FF 7F 74 68 6B  31 00                    .....thk1.      
```

#### Opcodes

```
  0: 0x001A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                53 F8 FF FF 7F F8            S.....
0030: FF FF 7F 74 68 6B 31 00                           ...thk1.        
```

#### Opcodes

```
  0: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          66 00 80 F8 FF FF 7F F8          f.......
0040: FF FF 7F 74 68 6B 32 00                           ...thk2.        
```

#### Opcodes

```
  0: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          53 F8 FF FF 7F F8 FF FF          S.......
0050: 7F 74 68 6B 32 00                                 .thk2.          
```

#### Opcodes

```
  0: 0x0048 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   66 00  80 F8 FF FF 7F F8 FF FF        f.........
0060: 7F 70 61 73 30 00                                 .pas0.          
```

#### Opcodes

```
  0: 0x0056 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   53 F8  FF FF 7F F8 FF FF 7F 70        S........p
0070: 61 73 30 00                                       as0.            
```

#### Opcodes

```
  0: 0x0066 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             66 00 80 F8  FF FF 7F F8 FF FF 7F 70      f..........p
0080: 6F 69 30 00                                       oi0.            
```

#### Opcodes

```
  0: 0x0074 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             53 F8 FF FF  7F F8 FF FF 7F 70 6F 69      S........poi
0090: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0084 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       66 00 80 F8 FF FF  7F F8 FF FF 7F 70 6F 69    f..........poi
00A0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0092 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=30*
  1: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       53 F8 FF FF 7F F8  FF FF 7F 70 6F 69 31 00    S........poi1.
```

#### Opcodes

```
  0: 0x00A2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  1: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 66 00 80 F8 FF FF 7F F8  FF FF 7F 77 65 62 30 00  f..........web0.
```

#### Opcodes

```
  0: 0x00B0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "web0" with entities [EventEntity, EventEntity], work=30*
  1: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 53 F8 FF FF 7F F8 FF FF  7F 77 65 62 30 00        S........web0.  
```

#### Opcodes

```
  0: 0x00C0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "web0" with entities [EventEntity, EventEntity]
  1: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CE  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            5E 69                ^i
00D0: 64 6C 30 1C 00 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x00CE [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00D3 [0x1C] WAIT(30* ticks)
  2: 0x00D6 [0x00] END_REQSTACK()
```

### Event 634

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D7   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
00E0: 83 70 0E 01 01 1D 01 80  23 29 08 83 70 0E 01 02  .p......#)..p...
00F0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x00D7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00DC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00DD [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00DE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x01)
  4: 0x00E5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7196*)
    → "Our furniture is built to last!"
  5: 0x00E8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00E9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x02)
  7: 0x00F0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00F2 [0x21] END_EVENT
  9: 0x00F3 [0x00] END_REQSTACK()
```

### Event 635

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F4   |
| Data Size    | 32 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             1E F0 FF FF  7F 6F 70 29 0B 83 70 0E      .....op)..p.
0100: 01 12 29 0B 83 70 0E 01  13 29 0B 83 70 0E 01 14  ..)..p...)..p...
0110: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x00F4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00F9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00FA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00FB [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x12)
  4: 0x0102 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x13)
  5: 0x0109 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x14)
  6: 0x0110 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x0112 [0x21] END_EVENT
  8: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             29 08 83 70  0E 01 01 1D 02 80 23 1D      )..p......#.
0120: 03 80 23 29 08 83 70 0E  01 02 00                 ..#)..p....     
```

#### Opcodes

```
  0: 0x0114 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x01)
  1: 0x011B [0x1D] PRINT_EVENT_MESSAGE(message_id=7197*)
    → "Say, that $3 you've got there..."
  2: 0x011E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x011F [0x1D] PRINT_EVENT_MESSAGE(message_id=7198*)
    → "What did you say? It was in the $2 you purchased...from us?"
  4: 0x0122 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0123 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x02)
  6: 0x012A [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012B   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   29 08 83 70 0E             )..p.
0130: 01 01 1D 04 80 23 29 08  83 70 0E 01 02 00        .....#)..p....  
```

#### Opcodes

```
  0: 0x012B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x01)
  1: 0x0132 [0x1D] PRINT_EVENT_MESSAGE(message_id=7199*)
    → "Might I have a look? Wait, this $3 looks familiar."
  2: 0x0135 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0136 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x02)
  4: 0x013D [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            29 08                ).
0140: 83 70 0E 01 03 29 08 83  70 0E 01 04 29 08 83 70  .p...)..p...)..p
0150: 0E 01 05 1D 05 80 23 29  08 83 70 0E 01 06 1D 06  ......#)..p.....
0160: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x013E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x03)
  1: 0x0145 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x04)
  2: 0x014C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x05)
  3: 0x0153 [0x1D] PRINT_EVENT_MESSAGE(message_id=7200*)
    → "Yes, as I thought! This is the mark of the royal family. This is a teacup of noble lineage!"
  4: 0x0156 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0157 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x06)
  6: 0x015E [0x1D] PRINT_EVENT_MESSAGE(message_id=7201*)
    → "You must return it to its rightful owner, wherever he or she might be."
  7: 0x0161 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0162 [0x00] END_REQSTACK()
```

### Event 636

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0163   |
| Data Size    | 37 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:          1E F0 FF FF 7F  6F 70 29 08 83 70 0E 01     .....op)..p..
0170: 01 1D 07 80 23 1D 08 80  23 1D 09 80 23 29 08 83  ....#...#...#)..
0180: 70 0E 01 02 20 00 21 00                           p... .!.        
```

#### Opcodes

```
  0: 0x0163 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0168 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0169 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x016A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x01)
  4: 0x0171 [0x1D] PRINT_EVENT_MESSAGE(message_id=7202*)
    → "That $2 you found was crafted of old. I would love to hear the history behind it."
  5: 0x0174 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0175 [0x1D] PRINT_EVENT_MESSAGE(message_id=7203*)
    → "Few pieces of such age and quality remain."
  7: 0x0178 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0179 [0x1D] PRINT_EVENT_MESSAGE(message_id=7204*)
    → "Shame on Calovour! Hawking such a treasure as if it were junk!"
  9: 0x017C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x017D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Morunaude (ID: 17723523/0x010E7083), tag_num=0x02)
 11: 0x0184 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0186 [0x21] END_EVENT
 13: 0x0187 [0x00] END_REQSTACK()
```

### Event 978

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0188   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                          4A F8 FF FF 7F F0 FF FF          J.......
0190: 7F 4A F0 FF FF 7F F8 FF  FF 7F 6F 70 1D 05 10 23  .J........op...#
01A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0188 [0x4A] EventEntity looks at LocalPlayer
  1: 0x0191 [0x4A] LocalPlayer looks at EventEntity
  2: 0x019A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x019B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x019C [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  5: 0x019F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01A0 [0x21] END_EVENT
  7: 0x01A1 [0x00] END_REQSTACK()
```

### Event 979

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A2   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:       42 4A F8 FF FF 7F  F0 FF FF 7F 4A F0 FF FF    BJ........J...
01B0: 7F F8 FF FF 7F 6F 70 1D  05 10 23 21 00           .....op...#!.   
```

#### Opcodes

```
  0: 0x01A2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01A3 [0x4A] EventEntity looks at LocalPlayer
  2: 0x01AC [0x4A] LocalPlayer looks at EventEntity
  3: 0x01B5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01B6 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x01B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  6: 0x01BA [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01BB [0x21] END_EVENT
  8: 0x01BC [0x00] END_REQSTACK()
```
