# 17801279 - Pahya Lolohoiv

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 460 bytes        |
| Total Events     | 22               |
| References Count | 7                |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |      9 |              3 |
| [65535.3](#event-655353)   | 0x001A       |     22 |              3 |
| [65535.4](#event-655354)   | 0x0030       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003E       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004E       |     20 |              3 |
| [65535.7](#event-655357)   | 0x0062       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0072       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0080       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0090       |     14 |              2 |
| [65535.11](#event-6553511) | 0x009E       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00AE       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00BC       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00CC       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00DA       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00EA       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00F8       |      9 |              3 |
| [75](#event-75)            | 0x0101       |     33 |             12 |
| [172](#event-172)          | 0x0122       |     33 |             12 |
| [191](#event-191)          | 0x0143       |      1 |              1 |
| [193](#event-193)          | 0x0144       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x0034      |          52 |
|       3 | 0x2737      |       10039 |
|       4 | 0x2738      |       10040 |
|       5 | 0x286D      |       10349 |
|       6 | 0x286E      |       10350 |

## String References

- **10039**: Nothing in this world is crrreated good or evil. However, evil can arrrise when something exists in a place where it did not originally belong.
- **10040**: To rrreturn these things to the place where they belong, we must often rrreceive help from the hand of nature. This is also true when currring disease and healing wounds.
- **10349**: Nothing in this world is crrreated good or evil. However, evil can arrrise when something exists in a place where it did not originally belong.
- **10350**: Even now, I can smell something on you that does not belong... Something very, verrry, evil...

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
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
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
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
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                81 00 F8 FF FF 7F            ......
0020: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 31 00  f..........thk1.
```

#### Opcodes

```
  0: 0x001A [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=50*
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 00        S........thk1.  
```

#### Opcodes

```
  0: 0x0030 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            66 00                f.
0040: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 00        .........thk2.  
```

#### Opcodes

```
  0: 0x003E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=50*
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            53 F8                S.
0050: FF FF 7F F8 FF FF 7F 74  68 6B 32 81 01 F8 FF FF  .......thk2.....
0060: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x004E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x005B [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       66 02 80 F8 FF FF  7F F8 FF FF 7F 64 69 73    f..........dis
0070: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0062 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=52*
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       53 F8 FF FF 7F F8  FF FF 7F 64 69 73 30 00    S........dis0.
```

#### Opcodes

```
  0: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 66 02 80 F8 FF FF 7F F8  FF FF 7F 74 6C 63 30 00  f..........tlc0.
```

#### Opcodes

```
  0: 0x0080 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=52*
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 63 30 00        S........tlc0.  
```

#### Opcodes

```
  0: 0x0090 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc0" with entities [EventEntity, EventEntity]
  1: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            66 02                f.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 63 31 00        .........tlc1.  
```

#### Opcodes

```
  0: 0x009E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=52*
  1: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            53 F8                S.
00B0: FF FF 7F F8 FF FF 7F 74  6C 63 31 00              .......tlc1.    
```

#### Opcodes

```
  0: 0x00AE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
  1: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      66 02 80 F8              f...
00C0: FF FF 7F F8 FF FF 7F 70  6F 69 30 00              .......poi0.    
```

#### Opcodes

```
  0: 0x00BC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=52*
  1: 0x00CB [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CC   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                      53 F8 FF FF              S...
00D0: 7F F8 FF FF 7F 70 6F 69  30 00                    .....poi0.      
```

#### Opcodes

```
  0: 0x00CC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x00D9 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DA   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                66 00 80 F8 FF FF            f.....
00E0: 7F F8 FF FF 7F 70 61 73  30 00                    .....pas0.      
```

#### Opcodes

```
  0: 0x00DA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=50*
  1: 0x00E9 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EA   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                53 F8 FF FF 7F F8            S.....
00F0: FF FF 7F 70 61 73 30 00                           ...pas0.        
```

#### Opcodes

```
  0: 0x00EA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x00F7 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F8  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                          5E 69 64 6C 30 1C 01 80          ^idl0...
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F8 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00FD [0x1C] WAIT(30* ticks)
  2: 0x0100 [0x00] END_REQSTACK()
```

### Event 75

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    1E F0 FF FF 7F 6F 70  29 08 3F A0 0F 01 01 1D   .....op).?.....
0110: 03 80 23 1D 04 80 23 29  08 3F A0 0F 01 02 20 00  ..#...#).?.... .
0120: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0101 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0106 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0107 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0108 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pahya Lolohoiv (ID: 17801279/0x010FA03F), tag_num=0x01)
  4: 0x010F [0x1D] PRINT_EVENT_MESSAGE(message_id=10039*)
    → "Nothing in this world is crrreated good or evil. However, evil can arrrise when something exists in a place where it did not originally belong."
  5: 0x0112 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0113 [0x1D] PRINT_EVENT_MESSAGE(message_id=10040*)
    → "To rrreturn these things to the place where they belong, we must often rrreceive help from the hand of nature. This is also true when currring disease and healing wounds."
  7: 0x0116 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0117 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pahya Lolohoiv (ID: 17801279/0x010FA03F), tag_num=0x02)
  9: 0x011E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0120 [0x21] END_EVENT
 11: 0x0121 [0x00] END_REQSTACK()
```

### Event 172

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0122   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:       1E F0 FF FF 7F 6F  70 29 08 3F A0 0F 01 01    .....op).?....
0130: 1D 05 80 23 1D 06 80 23  29 08 3F A0 0F 01 02 20  ...#...#).?.... 
0140: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0122 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0127 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0128 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0129 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pahya Lolohoiv (ID: 17801279/0x010FA03F), tag_num=0x01)
  4: 0x0130 [0x1D] PRINT_EVENT_MESSAGE(message_id=10349*)
    → "Nothing in this world is crrreated good or evil. However, evil can arrrise when something exists in a place where it did not originally belong."
  5: 0x0133 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0134 [0x1D] PRINT_EVENT_MESSAGE(message_id=10350*)
    → "Even now, I can smell something on you that does not belong... Something very, verrry, evil..."
  7: 0x0137 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0138 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pahya Lolohoiv (ID: 17801279/0x010FA03F), tag_num=0x02)
  9: 0x013F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0141 [0x21] END_EVENT
 11: 0x0142 [0x00] END_REQSTACK()
```

### Event 191

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0143  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:          00                                          .            
```

#### Opcodes

```
  0: 0x0143 [0x00] END_REQSTACK()
```

### Event 193

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0144  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:             00                                        .           
```

#### Opcodes

```
  0: 0x0144 [0x00] END_REQSTACK()
```
