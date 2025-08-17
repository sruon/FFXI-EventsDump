# 17764446 - An Polaali

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 560 bytes                |
| Total Events     | 23                       |
| References Count | 8                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     22 |              3 |
| [65535.6](#event-655356)   | 0x0053       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0061       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0071       |     20 |              3 |
| [65535.9](#event-655359)   | 0x0085       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0095       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00A3       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00B3       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00C1       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00D1       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00DF       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00EF       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00FD       |     16 |              2 |
| [65535.18](#event-6553518) | 0x010D       |     14 |              2 |
| [65535.19](#event-6553519) | 0x011B       |      9 |              3 |
| [44](#event-44)            | 0x0124       |     36 |             11 |
| [404](#event-404)          | 0x0148       |     36 |             11 |
| [407](#event-407)          | 0x016C       |     54 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x0034      |          52 |
|       2 | 0x0035      |          53 |
|       3 | 0x001E      |          30 |
|       4 | 0x1D88      |        7560 |
|       5 | 0x2128      |        8488 |
|       6 | 0x212D      |        8493 |
|       7 | 0x212E      |        8494 |

## String References

- **7560**: My name is An Polaali. I've parrrtnered up here with An Shanaa 'cause we are the best.
- **8488**: Woowee...! We overhearrrd you! Seems our boss has a darrring side to her after all!t
- **8493**: So it was just anotherrr Mithra who has a similarrr name to our boss, Hae Jakkya, who borrowed the saucy romance novel... Well, that was a letdown!
- **8494**: What a borrring outcome.

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               66                 f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 32 00     ..........tlk2. 
```

#### Opcodes

```
  0: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 32 00           ........tlk2.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         81 00 F8               ...
0040: FF FF 7F 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 68  ...f..........th
0050: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x003D [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0043 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=50*
  2: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31     S........thk1
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0053 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   f..........thk2
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0061 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=50*
  1: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 81 01   S........thk2..
0080: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0071 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x007E [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                66 01 80  F8 FF FF 7F F8 FF FF 7F       f..........
0090: 64 69 73 30 00                                    dis0.           
```

#### Opcodes

```
  0: 0x0085 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=52*
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                53 F8 FF  FF 7F F8 FF FF 7F 64 69       S........di
00A0: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0095 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          66 01 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     f..........tl
00B0: 63 30 00                                          c0.             
```

#### Opcodes

```
  0: 0x00A3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=52*
  1: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          53 F8 FF FF 7F  F8 FF FF 7F 74 6C 63 30     S........tlc0
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc0" with entities [EventEntity, EventEntity]
  1: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    66 01 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 63 31   f..........tlc1
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00C1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=52*
  1: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 63 31 00      S........tlc1. 
```

#### Opcodes

```
  0: 0x00D1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
  1: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               66                 f
00E0: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 31 00     ..........tlb1. 
```

#### Opcodes

```
  0: 0x00DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
  1: 0x00EE [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EF   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               53                 S
00F0: F8 FF FF 7F F8 FF FF 7F  74 6C 62 31 00           ........tlb1.   
```

#### Opcodes

```
  0: 0x00EF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  1: 0x00FC [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         66 02 80               f..
0100: F8 FF FF 7F F8 FF FF 7F  74 6C 62 32 00           ........tlb2.   
```

#### Opcodes

```
  0: 0x00FD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
  1: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         53 F8 FF               S..
0110: FF 7F F8 FF FF 7F 74 6C  62 32 00                 ......tlb2.     
```

#### Opcodes

```
  0: 0x010D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb2" with entities [EventEntity, EventEntity]
  1: 0x011A [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                   5E 69 64 6C 30             ^idl0
0120: 1C 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x011B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0120 [0x1C] WAIT(30* ticks)
  2: 0x0123 [0x00] END_REQSTACK()
```

### Event 44

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0124   |
| Data Size    | 36 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:             1E F0 FF FF  7F 6F 70 29 08 5E 10 0F      .....op).^..
0130: 01 0F 1D 04 80 23 29 08  5E 10 0F 01 11 29 08 5E  .....#).^....).^
0140: 10 0F 01 12 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0124 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0129 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x012A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x012B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x0F)
  4: 0x0132 [0x1D] PRINT_EVENT_MESSAGE(message_id=7560*)
    → "My name is An Polaali. I've parrrtnered up here with An Shanaa 'cause we are the best."
  5: 0x0135 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0136 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x11)
  7: 0x013D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x12)
  8: 0x0144 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0146 [0x21] END_EVENT
 10: 0x0147 [0x00] END_REQSTACK()
```

### Event 404

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0148   |
| Data Size    | 36 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                          1E F0 FF FF 7F 6F 70 29          .....op)
0150: 08 5E 10 0F 01 0F 1D 05  80 23 29 08 5E 10 0F 01  .^.......#).^...
0160: 11 29 08 5E 10 0F 01 12  20 00 21 00              .).^.... .!.    
```

#### Opcodes

```
  0: 0x0148 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x014D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x014E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x014F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x0F)
  4: 0x0156 [0x1D] PRINT_EVENT_MESSAGE(message_id=8488*)
    → "Woowee...! We overhearrrd you! Seems our boss has a darrring side to her after all!t"
  5: 0x0159 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x015A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x11)
  7: 0x0161 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x12)
  8: 0x0168 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x016A [0x21] END_EVENT
 10: 0x016B [0x00] END_REQSTACK()
```

### Event 407

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016C   |
| Data Size    | 54 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                      1E F0 FF FF              ....
0170: 7F 6F 70 29 08 5E 10 0F  01 09 1D 06 80 23 29 08  .op).^.......#).
0180: 5E 10 0F 01 0A 29 08 5E  10 0F 01 0B 1D 07 80 23  ^....).^.......#
0190: 29 08 5E 10 0F 01 0D 29  08 5E 10 0F 01 0E 20 00  ).^....).^.... .
01A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x016C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0171 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0172 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0173 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x09)
  4: 0x017A [0x1D] PRINT_EVENT_MESSAGE(message_id=8493*)
    → "So it was just anotherrr Mithra who has a similarrr name to our boss, Hae Jakkya, who borrowed the saucy romance novel... Well, that was a letdown!"
  5: 0x017D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x017E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x0A)
  7: 0x0185 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x0B)
  8: 0x018C [0x1D] PRINT_EVENT_MESSAGE(message_id=8494*)
    → "What a borrring outcome."
  9: 0x018F [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0190 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x0D)
 11: 0x0197 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=An Polaali (ID: 17764446/0x010F105E), tag_num=0x0E)
 12: 0x019E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x01A0 [0x21] END_EVENT
 14: 0x01A1 [0x00] END_REQSTACK()
```
